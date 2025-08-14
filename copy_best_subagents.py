#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
复制最佳subagent文件脚本
根据分析结果，将最佳版本的subagent文件复制到对应的分类目录中
"""

import os
import shutil
import re
from pathlib import Path
from collections import defaultdict
import yaml

def extract_frontmatter(content):
    """提取文件的frontmatter信息"""
    if content.startswith('---'):
        try:
            end_idx = content.find('---', 3)
            if end_idx != -1:
                frontmatter = content[3:end_idx].strip()
                return yaml.safe_load(frontmatter)
        except:
            pass
    return {}

def analyze_file(file_path):
    """分析单个文件的信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter = extract_frontmatter(content)
        
        return {
            'path': str(file_path),
            'name': frontmatter.get('name', Path(file_path).stem),
            'description': frontmatter.get('description', ''),
            'category': frontmatter.get('category', ''),
            'tools': frontmatter.get('tools', []),
            'content_length': len(content),
            'line_count': content.count('\n') + 1,
            'has_examples': 'example' in content.lower() or 'usage' in content.lower(),
            'has_checklist': 'checklist' in content.lower() or '- [' in content,
            'has_mcp_tools': 'mcp' in content.lower(),
            'frontmatter': frontmatter,
            'content': content
        }
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

def quality_score(file_info):
    """计算文件质量评分"""
    score = 0
    score += file_info['content_length'] * 0.1  # 内容长度
    score += file_info['line_count'] * 2  # 行数
    score += len(file_info['description']) * 0.5  # 描述长度
    score += len(file_info.get('tools', [])) * 10  # 工具数量
    score += 50 if file_info['has_examples'] else 0  # 有示例
    score += 30 if file_info['has_checklist'] else 0  # 有检查清单
    score += 20 if file_info['has_mcp_tools'] else 0  # 有MCP工具
    return score

def determine_category(file_info):
    """根据文件信息确定分类目录"""
    category = file_info.get('category', '').lower()
    name = file_info.get('name', '').lower()
    description = file_info.get('description', '').lower()
    
    # 分类映射规则
    if any(keyword in category + name + description for keyword in ['frontend', 'react', 'vue', 'angular', 'ui', 'component']):
        return '01-core-development'
    elif any(keyword in category + name + description for keyword in ['backend', 'api', 'server', 'database', 'microservice']):
        return '01-core-development'
    elif any(keyword in category + name + description for keyword in ['python', 'javascript', 'java', 'go', 'rust', 'php', 'ruby']):
        return '02-language-specialists'
    elif any(keyword in category + name + description for keyword in ['devops', 'docker', 'kubernetes', 'cloud', 'aws', 'azure', 'infrastructure']):
        return '03-infrastructure'
    elif any(keyword in category + name + description for keyword in ['test', 'security', 'quality', 'audit', 'review']):
        return '04-quality-security'
    elif any(keyword in category + name + description for keyword in ['ai', 'ml', 'data', 'machine learning', 'nlp', 'llm']):
        return '05-data-ai'
    elif any(keyword in category + name + description for keyword in ['cli', 'tool', 'automation', 'workflow', 'productivity']):
        return '06-developer-experience'
    elif any(keyword in category + name + description for keyword in ['business', 'product', 'manager', 'sales', 'customer']):
        return '08-business-product'
    elif any(keyword in category + name + description for keyword in ['research', 'analysis', 'academic']):
        return '10-research-analysis'
    elif any(keyword in category + name + description for keyword in ['orchestration', 'meta', 'agent', 'coordinator']):
        return '09-meta-orchestration'
    else:
        return '07-specialized-domains'

def main():
    base_dir = Path('/Users/xiaole/Workspaces/xiaole/claude-subagents-chinese')
    
    # 定义三个源目录
    directories = {
        'collection': base_dir / 'claude-code-subagents-collection-main' / 'subagents',
        'sub-agents': base_dir / 'claude-code-sub-agents-main',
        'awesome': base_dir / 'awesome-claude-code-subagents-main' / 'categories'
    }
    
    all_files = {}
    duplicates = defaultdict(list)
    
    # 收集所有文件
    for source, directory in directories.items():
        if directory.exists():
            for md_file in directory.rglob('*.md'):
                if md_file.name != 'README.md':
                    file_info = analyze_file(md_file)
                    if file_info:
                        file_info['source'] = source
                        all_files[str(md_file)] = file_info
                        duplicates[file_info['name']].append(file_info)
    
    print(f"总共找到 {len(all_files)} 个subagent文件")
    print(f"其中 {len([k for k, v in duplicates.items() if len(v) > 1])} 个有重复")
    
    # 确定最佳文件
    best_files = {}
    for name, files in duplicates.items():
        if len(files) > 1:
            best_file = max(files, key=quality_score)
            best_files[name] = best_file
            print(f"重复文件 {name}: 选择 {best_file['source']} 版本 (评分: {quality_score(best_file):.1f})")
        else:
            best_files[name] = files[0]
    
    # 创建目标目录并复制文件
    target_base = base_dir / 'subagents'
    
    # 统计每个分类的文件数量
    category_counts = defaultdict(int)
    
    for name, file_info in best_files.items():
        category = determine_category(file_info)
        category_counts[category] += 1
        
        target_dir = target_base / category
        target_dir.mkdir(parents=True, exist_ok=True)
        
        source_path = Path(file_info['path'])
        target_path = target_dir / f"{name}.md"
        
        try:
            shutil.copy2(source_path, target_path)
            print(f"复制: {name}.md -> {category}/")
        except Exception as e:
            print(f"复制失败 {name}.md: {e}")
    
    print("\n=== 分类统计 ===")
    for category, count in sorted(category_counts.items()):
        print(f"{category}: {count} 个文件")
    
    print(f"\n总计复制了 {sum(category_counts.values())} 个subagent文件")
    
    # 生成文件清单
    print("\n=== 生成文件清单 ===")
    manifest = {}
    for category in sorted(category_counts.keys()):
        manifest[category] = []
        category_dir = target_base / category
        if category_dir.exists():
            for md_file in sorted(category_dir.glob('*.md')):
                file_info = analyze_file(md_file)
                if file_info:
                    manifest[category].append({
                        'name': file_info['name'],
                        'description': file_info['description'][:100] + '...' if len(file_info['description']) > 100 else file_info['description'],
                        'tools': file_info.get('tools', [])
                    })
    
    # 保存清单到文件
    import json
    with open(base_dir / 'subagents_manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print("文件清单已保存到 subagents_manifest.json")

if __name__ == '__main__':
    main()