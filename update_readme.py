#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新README文件脚本
为每个subagent添加链接和功能说明
"""

import json
from pathlib import Path

def load_manifest():
    """加载subagents清单文件"""
    with open('subagents_manifest.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_category_name(category_code):
    """获取分类的中文名称"""
    category_names = {
        '01-core-development': '核心开发',
        '02-language-specialists': '语言专家',
        '03-infrastructure': '基础设施与运维',
        '04-quality-security': '质量与安全',
        '05-data-ai': '数据与AI',
        '06-developer-experience': '开发者体验',
        '07-specialized-domains': '专业领域',
        '08-business-product': '业务与产品',
        '09-meta-orchestration': '元编程与编排',
        '10-research-analysis': '研究与分析'
    }
    return category_names.get(category_code, category_code)

def generate_readme_content(manifest):
    """生成新的README内容"""
    content = '''# Claude 代码子代理集合 (中文版)

这是一个全面的 Claude 代码子代理集合，专为各种软件开发任务而设计。本项目整合了三个优秀的开源项目，经过语义分析和去重处理，为您提供最佳版本的专业代理。

## 📋 项目概述

本项目包含 **{total_count}** 个专业代理，涵盖软件开发的各个方面：

- 🔧 **核心开发**: 前端、后端、全栈开发专家
- 🌐 **语言专家**: 各种编程语言的专业代理
- ☁️ **基础设施**: DevOps、云架构、容器化专家
- 🔒 **质量安全**: 测试、代码审查、安全专家
- 🤖 **数据AI**: 机器学习、数据工程、AI专家
- 🛠️ **开发体验**: CLI工具、自动化、生产力专家
- 🎯 **专业领域**: 特定行业和技术领域专家
- 💼 **业务产品**: 产品管理、业务分析专家
- 🔄 **元编程**: 代码生成、编排、自动化专家
- 📊 **研究分析**: 学术研究、数据分析专家

## 🚀 主要特性

### 生产就绪性
- ✅ 经过实战验证的代理配置
- ✅ 详细的使用说明和最佳实践
- ✅ 完整的工具集成和依赖管理
- ✅ 持续更新和社区支持

### MCP 工具集成
- 🔌 支持 Model Context Protocol (MCP)
- 🛠️ 丰富的工具生态系统
- 🔄 无缝的工具链集成
- 📈 可扩展的架构设计

### Web UI 和 CLI 工具
- 🌐 直观的 Web 界面管理
- ⌨️ 强大的命令行工具
- 📱 响应式设计支持
- 🎨 现代化的用户体验

## 📚 可用子代理

'''
    
    total_count = sum(len(agents) for agents in manifest.values())
    content = content.format(total_count=total_count)
    
    # 为每个分类生成内容
    for category_code in sorted(manifest.keys()):
        category_name = get_category_name(category_code)
        agents = manifest[category_code]
        
        content += f"### {category_name} ({len(agents)} 个代理)\n\n"
        
        for agent in sorted(agents, key=lambda x: x['name']):
            name = agent['name']
            description = agent['description']
            tools = agent.get('tools', [])
            
            # 处理工具列表
            tools_str = ""
            if tools:
                if isinstance(tools, list):
                    tools_str = f" | 工具: {', '.join(tools[:5])}{'...' if len(tools) > 5 else ''}"
                elif isinstance(tools, str):
                    tool_list = [t.strip() for t in tools.split(',')]
                    tools_str = f" | 工具: {', '.join(tool_list[:5])}{'...' if len(tool_list) > 5 else ''}"
            
            content += f"- **[{name}](subagents/{category_code}/{name}.md)**: {description}{tools_str}\n"
        
        content += "\n"
    
    # 添加使用指南
    content += '''## 🎯 使用指南

### 快速开始

1. **选择合适的代理**: 根据您的任务需求，从上述分类中选择最适合的代理
2. **查看代理文档**: 点击代理名称查看详细的使用说明和配置
3. **配置工具**: 根据代理要求配置相应的 MCP 工具
4. **开始使用**: 按照代理文档中的指南开始您的开发任务

### 代理选择建议

- **新项目开发**: 使用 `full-stack-developer` 或 `frontend-developer` + `backend-developer`
- **代码审查**: 使用 `code-reviewer` 或 `architect-reviewer`
- **性能优化**: 使用 `performance-optimizer` 或 `database-optimizer`
- **安全审计**: 使用 `security-auditor` 或 `api-security-audit`
- **文档编写**: 使用 `technical-writer` 或 `api-documenter`

### 工具集成

大多数代理支持以下 MCP 工具：
- `Read`, `Write`, `Edit`: 文件操作
- `Grep`, `Glob`: 代码搜索
- `Bash`, `LS`: 系统操作
- `WebSearch`, `WebFetch`: 网络资源
- `context7`: 上下文管理
- `magic`: UI 组件生成
- `playwright`: 浏览器自动化

## 📋 可用命令分类

### 版本控制与 Git
- `git-expert`: Git 工作流和版本控制专家
- `git-workflow`: Git 分支策略和协作流程

### 代码分析与测试
- `code-reviewer`: 代码质量和最佳实践审查
- `test-engineer`: 测试策略和自动化测试
- `performance-optimizer`: 性能分析和优化

### 上下文加载与准备
- `context-manager`: 项目上下文和依赖管理
- `environment-setup`: 开发环境配置和初始化

### 文档与变更日志
- `technical-writer`: 技术文档编写和维护
- `api-documenter`: API 文档生成和管理
- `changelog-generator`: 变更日志自动生成

### 项目与任务管理
- `project-manager`: 项目规划和进度管理
- `task-coordinator`: 任务分解和协调
- `scrum-master`: 敏捷开发流程管理

## 🔧 安装要求

### 基础要求
- Claude AI 访问权限
- MCP (Model Context Protocol) 支持
- Node.js 18+ (用于 Web UI)
- Python 3.8+ (用于某些工具)

### 推荐工具
- VS Code 或其他支持 MCP 的编辑器
- Git 版本控制
- Docker (用于容器化开发)
- 相关编程语言运行时

## 🤝 贡献指南

我们欢迎社区贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

### 贡献类型
- 🐛 Bug 修复
- ✨ 新功能添加
- 📚 文档改进
- 🎨 代码优化
- 🔧 工具集成

## 🔍 故障排除

### 常见问题

**Q: 代理无法正常工作？**
A: 请检查 MCP 工具配置和依赖安装

**Q: 如何选择合适的代理？**
A: 根据任务类型查看分类说明，选择最匹配的代理

**Q: 代理响应速度慢？**
A: 检查网络连接和 Claude API 配额

### 获取帮助
- 📖 查看代理文档
- 💬 提交 Issue
- 🌐 访问社区论坛

## 📖 学习资源

- [Claude AI 官方文档](https://docs.anthropic.com/)
- [MCP 协议规范](https://modelcontextprotocol.io/)
- [最佳实践指南](docs/best-practices.md)
- [示例项目](examples/)

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢以下开源项目的贡献：

'''
    
    return content

def get_repo_links():
    """获取原始仓库链接"""
    repo_links = []
    
    # 读取各个子目录的 .git/config 文件
    subdirs = [
        'claude-code-subagents-collection-main',
        'claude-code-sub-agents-main', 
        'awesome-claude-code-subagents-main'
    ]
    
    for subdir in subdirs:
        git_config_path = Path(subdir) / '.git' / 'config'
        if git_config_path.exists():
            try:
                with open(git_config_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 提取 URL
                    for line in content.split('\n'):
                        if 'url =' in line:
                            url = line.split('url =')[1].strip()
                            repo_links.append(f"- [{subdir}]({url})")
                            break
            except Exception as e:
                print(f"无法读取 {git_config_path}: {e}")
    
    return repo_links

def main():
    # 加载清单
    manifest = load_manifest()
    
    # 生成README内容
    content = generate_readme_content(manifest)
    
    # 添加原始仓库链接
    repo_links = get_repo_links()
    if repo_links:
        content += "\n### 原始仓库\n\n"
        content += "\n".join(repo_links)
        content += "\n"
    
    # 写入README文件
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("README.md 已更新完成！")
    print(f"总共包含 {sum(len(agents) for agents in manifest.values())} 个代理")
    print(f"分布在 {len(manifest)} 个分类中")

if __name__ == '__main__':
    main()