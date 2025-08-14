#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
子代理文件分析脚本
用于分析三个目录中的subagents文件，识别重复项并确定最佳版本
"""

import os
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
            'frontmatter': frontmatter
        }
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

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
    
    # 分析重复文件
    print("\n=== 重复文件分析 ===")
    for name, files in duplicates.items():
        if len(files) > 1:
            print(f"\n{name} ({len(files)} 个版本):")
            
            # 按质量评分排序
            def quality_score(file_info):
                score = 0
                score += file_info['content_length'] * 0.1  # 内容长度
                score += file_info['line_count'] * 2  # 行数
                score += len(file_info['description']) * 0.5  # 描述长度
                score += len(file_info.get('tools', [])) * 10  # 工具数量
                score += 50 if file_info['has_examples'] else 0  # 有示例
                score += 30 if file_info['has_checklist'] else 0  # 有检查清单
                score += 20 if file_info['has_mcp_tools'] else 0  # 有MCP工具
                return score
            
            sorted_files = sorted(files, key=quality_score, reverse=True)
            
            for i, file_info in enumerate(sorted_files):
                score = quality_score(file_info)
                status = "[最佳]" if i == 0 else "[备选]"
                print(f"  {status} {file_info['source']}: {file_info['path']}")
                print(f"    评分: {score:.1f}, 长度: {file_info['content_length']}, 行数: {file_info['line_count']}")
                print(f"    描述: {file_info['description'][:100]}...")
    
    # 生成分类映射
    print("\n=== 分类映射建议 ===")
    category_mapping = {
        'development': '01-core-development',
        'development-architecture': '01-core-development', 
        'language-specialists': '02-language-specialists',
        'infrastructure': '03-infrastructure',
        'quality-testing': '04-quality-security',
        'security': '04-quality-security',
        'data-ai': '05-data-ai',
        'developer-experience': '06-developer-experience',
        'specialized-domains': '07-specialized-domains',
        'business': '08-business-product',
        'meta-orchestration': '09-meta-orchestration',
        'research': '10-research-analysis'
    }
    
    # 统计每个分类的文件数量
    category_counts = defaultdict(int)
    for file_info in all_files.values():
        category = file_info.get('category', 'unknown')
        mapped_category = category_mapping.get(category, '07-specialized-domains')
        category_counts[mapped_category] += 1
    
    for category, count in sorted(category_counts.items()):
        print(f"{category}: {count} 个文件")
    
    # 输出最佳文件列表
    print("\n=== 最佳文件列表 ===")
    best_files = {}
    for name, files in duplicates.items():
        if len(files) > 1:
            def quality_score(file_info):
                score = 0
                score += file_info['content_length'] * 0.1
                score += file_info['line_count'] * 2
                score += len(file_info['description']) * 0.5
                score += len(file_info.get('tools', [])) * 10
                score += 50 if file_info['has_examples'] else 0
                score += 30 if file_info['has_checklist'] else 0
                score += 20 if file_info['has_mcp_tools'] else 0
                return score
            
            best_file = max(files, key=quality_score)
            best_files[name] = best_file
        else:
            best_files[name] = files[0]
    
    # 按分类输出最佳文件
    for category in sorted(category_counts.keys()):
        print(f"\n{category}:")
        for name, file_info in best_files.items():
            file_category = file_info.get('category', 'unknown')
            mapped_category = category_mapping.get(file_category, '07-specialized-domains')
            if mapped_category == category:
                print(f"  {name}: {file_info['path']}")

if __name__ == '__main__':
    main()