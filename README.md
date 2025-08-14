# Claude 代码子代理集合 (中文版)

这是一个全面的 Claude 代码子代理集合，专为各种软件开发任务而设计。本项目整合了三个优秀的开源项目，经过语义分析和去重处理，为您提供最佳版本的专业代理。

## 📋 项目概述

本项目包含 **200** 个专业代理，涵盖软件开发的各个方面：

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

### 核心开发 (89 个代理)

- **[academic-research-synthesizer](subagents/01-core-development/academic-research-synthesizer.md)**: 综合多个来源的学术研究并提供引用。进行文献综述，技术分析和研究报告生成。
- **[accessibility-specialist](subagents/01-core-development/accessibility-specialist.md)**: 确保Web应用程序符合WCAG 2.1 AA/AAA标准。实现ARIA属性、键盘导航和无障碍功能。
- **[agent-organizer](subagents/01-core-development/agent-organizer.md)**: 高度先进的AI代理，作为复杂多代理任务的主编排器。智能协调和管理多个专业代理的协作。 | 工具: Read, Write, Edit, Grep, Glob...
- **[ai-engineer](subagents/01-core-development/ai-engineer.md)**: 专门设计、构建和优化LLM驱动应用程序的高度专业化AI代理。精通RAG架构和AI系统集成。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[angular-architect](subagents/01-core-development/angular-architect.md)**: 精通Angular 15+企业级模式的专家架构师。专长RxJS、NgRx状态管理和大型应用架构设计。 | 工具: angular-cli, nx, jest, cypress, webpack...
- **[api-designer](subagents/01-core-development/api-designer.md)**: API架构专家，设计可扩展、开发者友好的接口。创建REST和GraphQL API，注重性能和易用性。 | 工具: Read, Write, MultiEdit, Bash, openapi-generator...
- **[api-documenter](subagents/01-core-development/api-documenter.md)**: 专门创建全面、开发者优先的API文档的专业代理。生成OpenAPI规范和交互式文档。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[api-security-audit](subagents/01-core-development/api-security-audit.md)**: 对REST API进行安全审计并识别漏洞。主动用于身份验证、授权和数据保护评估。
- **[architect-review](subagents/01-core-development/architect-review.md)**: 审查代码变更的架构一致性和模式。在任何结构性变更后主动使用，确保架构完整性。
- **[architect-reviewer](subagents/01-core-development/architect-reviewer.md)**: 主动审查代码的架构一致性、模式遵循和可维护性。确保代码质量和设计原则的执行。 | 工具: Read, Grep, Glob, LS, WebFetch...
- **[backend-architect](subagents/01-core-development/backend-architect.md)**: 作为咨询架构师设计健壮、可扩展和可维护的后端系统。收集需求并提供技术解决方案。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[backend-developer](subagents/01-core-development/backend-developer.md)**: 专精可扩展API开发和微服务架构的高级后端工程师。构建高性能、安全的服务端应用。 | 工具: Read, Write, MultiEdit, Bash, Docker...
- **[blockchain-developer](subagents/01-core-development/blockchain-developer.md)**: 专精智能合约开发、DApp架构和DeFi协议的区块链开发专家。精通Solidity和Web3技术栈。 | 工具: truffle, hardhat, web3, ethers, solidity...
- **[build-engineer](subagents/01-core-development/build-engineer.md)**: 专精构建系统优化、编译策略和开发工具链的构建工程师。提升开发效率和部署流程。 | 工具: Read, Write, MultiEdit, Bash, webpack...
- **[business-analyst](subagents/01-core-development/business-analyst.md)**: 专精需求收集、流程改进和数据驱动决策的业务分析师。连接业务需求与技术实现。 | 工具: excel, sql, tableau, powerbi, jira...
- **[chaos-engineer](subagents/01-core-development/chaos-engineer.md)**: 专精受控故障注入、弹性测试和构建容错系统的混沌工程专家。提升系统可靠性和稳定性。 | 工具: Read, Write, MultiEdit, Bash, chaostoolkit...
- **[cli-developer](subagents/01-core-development/cli-developer.md)**: 专精命令行界面设计、开发者工具和终端应用的CLI开发专家。创建高效易用的命令行工具。 | 工具: Read, Write, MultiEdit, Bash, commander...
- **[cloud-architect](subagents/01-core-development/cloud-architect.md)**: 设计可扩展、安全且成本效益高的AWS、Azure和GCP基础设施的高级云架构师AI。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[comprehensive-researcher](subagents/01-core-development/comprehensive-researcher.md)**: 进行深入研究，使用多个来源、交叉验证和结构化报告。分解复杂研究任务并提供全面分析。
- **[content-marketer](subagents/01-core-development/content-marketer.md)**: 专精内容策略、SEO优化和参与度驱动营销的内容营销专家。创建有影响力的数字内容。 | 工具: wordpress, hubspot, buffer, canva, semrush...
- **[crypto-trader](subagents/01-core-development/crypto-trader.md)**: 构建加密货币交易系统，实施交易策略，并与交易所API集成。专精量化交易和风险管理。
- **[customer-success-manager](subagents/01-core-development/customer-success-manager.md)**: 专精客户保留、增长和倡导的客户成功管理专家。掌握客户关系管理和业务增长策略。 | 工具: Read, Write, MultiEdit, Bash, salesforce...
- **[customer-support](subagents/01-core-development/customer-support.md)**: 处理支持工单、FAQ回复和客户邮件。创建帮助文档、故障排除指南和客户服务流程。
- **[data-engineer](subagents/01-core-development/data-engineer.md)**: 设计、构建和优化可扩展且可维护的数据密集型应用程序，包括ETL/ELT管道和数据架构。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[database-admin](subagents/01-core-development/database-admin.md)**: 管理数据库操作、备份、复制和监控。处理用户权限、维护任务和性能调优。
- **[database-administrator](subagents/01-core-development/database-administrator.md)**: 专精高可用系统、性能优化和数据库安全的数据库管理员专家。确保数据完整性和系统稳定性。 | 工具: Read, Write, MultiEdit, Bash, psql...
- **[database-optimization](subagents/01-core-development/database-optimization.md)**: 专注查询优化、索引策略、模式设计和性能调优的数据库性能专家。提升数据库执行效率。
- **[database-optimizer](subagents/01-core-development/database-optimizer.md)**: 全面分析和优化数据库性能的专家AI助手。识别性能瓶颈并提供优化建议。 | 工具: Read, Write, Edit, Grep, Glob...
- **[defi-strategist](subagents/01-core-development/defi-strategist.md)**: 设计和实施DeFi收益策略、流动性提供和协议交互。使用PROA框架进行去中心化金融分析。
- **[directus-developer](subagents/01-core-development/directus-developer.md)**: 构建和定制Directus应用程序，包括扩展、钩子和API集成。Directus专家级开发者。
- **[django-developer](subagents/01-core-development/django-developer.md)**: 精通Django 4+和现代Python实践的Django开发专家。专精可扩展Web应用和API开发。 | 工具: django-admin, pytest, celery, redis, postgresql...
- **[documentation-engineer](subagents/01-core-development/documentation-engineer.md)**: 专精技术文档系统、API文档和开发者资源的文档工程师专家。构建完善的文档生态。 | 工具: Read, Write, MultiEdit, Bash, markdown...
- **[docusaurus-expert](subagents/01-core-development/docusaurus-expert.md)**: 配置和故障排除Docusaurus文档站点。专精配置、主题和内容优化。
- **[dotnet-core-expert](subagents/01-core-development/dotnet-core-expert.md)**: 精通.NET 8和现代C#特性的.NET Core专家。专精跨平台应用开发和云原生解决方案。 | 工具: dotnet-cli, nuget, xunit, docker, azure-cli...
- **[drupal-developer](subagents/01-core-development/drupal-developer.md)**: 构建和定制Drupal应用程序，包括自定义模块、主题和集成。Drupal专家级开发者。
- **[electron-pro](subagents/01-core-development/electron-pro.md)**: 使用Electron和TypeScript构建跨平台桌面应用程序的专家。专精现代桌面应用开发。 | 工具: Read, Write, Edit, Grep, Glob...
- **[fintech-engineer](subagents/01-core-development/fintech-engineer.md)**: 专精金融系统、监管合规和安全交易的金融科技工程师专家。构建可靠的金融应用。 | 工具: Read, Write, MultiEdit, Bash, python...
- **[frontend-developer](subagents/01-core-development/frontend-developer.md)**: 作为高级前端工程师和AI编程伙伴。构建健壮、高性能和无障碍的用户界面。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[full-stack-developer](subagents/01-core-development/full-stack-developer.md)**: 精通设计、构建和维护应用程序各个方面的多才多艺AI全栈开发者。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[fullstack-developer](subagents/01-core-development/fullstack-developer.md)**: 拥有全栈专业知识的端到端功能负责人。从数据库到用户界面提供完整解决方案。 | 工具: Read, Write, MultiEdit, Bash, Docker...
- **[graphql-architect](subagents/01-core-development/graphql-architect.md)**: 专门设计、实施和优化高性能、可扩展GraphQL API的高度专业化AI代理。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[hackathon-ai-strategist](subagents/01-core-development/hackathon-ai-strategist.md)**: 黑客马拉松策略、AI解决方案构思和项目评估的专家指导。提供评委视角的项目优化建议。
- **[ios-developer](subagents/01-core-development/ios-developer.md)**: 使用Swift/SwiftUI开发原生iOS应用程序。掌握UIKit/SwiftUI、Core Data、网络和App Store发布。
- **[iot-engineer](subagents/01-core-development/iot-engineer.md)**: 专精物联网设备架构、边缘计算和IoT平台集成的物联网工程师专家。 | 工具: mqtt, aws-iot, azure-iot, node-red, mosquitto
- **[java-architect](subagents/01-core-development/java-architect.md)**: 专精企业级应用、Spring生态系统和云原生架构的高级Java架构师。 | 工具: Read, Write, MultiEdit, Bash, maven...
- **[java-developer](subagents/01-core-development/java-developer.md)**: 掌握现代Java流、并发和JVM优化。处理Spring Boot、响应式编程和企业级应用开发。
- **[javascript-developer](subagents/01-core-development/javascript-developer.md)**: 现代ES6+、异步模式和Node.js的JavaScript专家。主动用于React、TypeScript和全栈开发。
- **[javascript-pro](subagents/01-core-development/javascript-pro.md)**: 专精现代ES2023+特性、异步编程和函数式编程的JavaScript开发专家。 | 工具: Read, Write, MultiEdit, Bash, node...
- **[knowledge-synthesizer](subagents/01-core-development/knowledge-synthesizer.md)**: 专精从多代理交互中提取洞察、识别模式和综合知识的知识合成专家。 | 工具: Read, Write, MultiEdit, Bash, vector-db...
- **[laravel-specialist](subagents/01-core-development/laravel-specialist.md)**: 精通Laravel 10+和现代PHP实践的Laravel专家。专精优雅系统架构和API开发。 | 工具: artisan, composer, pest, redis, mysql...
- **[laravel-vue-developer](subagents/01-core-development/laravel-vue-developer.md)**: 构建带有Vue3前端的全栈Laravel应用程序。精通Laravel API、Vue3组合式API和现代全栈开发。
- **[llm-architect](subagents/01-core-development/llm-architect.md)**: 专精大语言模型架构、部署和优化的LLM架构师专家。构建高效的AI系统。 | 工具: transformers, langchain, llamaindex, vllm, wandb
- **[llms-maintainer](subagents/01-core-development/llms-maintainer.md)**: 为AI爬虫导航生成和维护llms.txt路线图文件。在构建过程中更新和维护AI系统文档。
- **[mcp-deployment-orchestrator](subagents/01-core-development/mcp-deployment-orchestrator.md)**: 通过容器化、Kubernetes部署、自动扩展和监控将MCP服务器部署到生产环境。
- **[mcp-expert](subagents/01-core-development/mcp-expert.md)**: 创建模型上下文协议集成和服务器配置。在构建MCP应用时主动使用。
- **[mcp-registry-navigator](subagents/01-core-development/mcp-registry-navigator.md)**: 专精发现、评估和集成MCP服务器的MCP注册表导航器。帮助选择最适合的MCP服务。
- **[mcp-security-auditor](subagents/01-core-development/mcp-security-auditor.md)**: 专精审查MCP服务器实现漏洞和安全风险的MCP安全审计员。确保MCP系统安全性。
- **[mcp-server-architect](subagents/01-core-development/mcp-server-architect.md)**: 设计和实现具有传输层、工具/资源/提示定义的MCP服务器。构建完整的MCP架构。
- **[mcp-testing-engineer](subagents/01-core-development/mcp-testing-engineer.md)**: 测试、调试和确保MCP服务器质量，包括JSON模式验证、协议合规性和性能测试。
- **[microservices-architect](subagents/01-core-development/microservices-architect.md)**: 设计可扩展微服务生态系统的分布式系统架构师。掌握服务边界和系统集成。 | 工具: Read, Write, MultiEdit, Bash, kubernetes...
- **[mobile-app-developer](subagents/01-core-development/mobile-app-developer.md)**: 专精iOS和Android原生及跨平台开发的移动应用开发专家。掌握现代移动开发技术栈。 | 工具: Read, Write, MultiEdit, Bash, xcode...
- **[mobile-developer](subagents/01-core-development/mobile-developer.md)**: 使用React Native等技术架构和领导复杂跨平台移动应用开发。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[nextjs-app-router-developer](subagents/01-core-development/nextjs-app-router-developer.md)**: 使用App Router构建现代Next.js应用程序，包括服务器组件、服务器操作、PPR等特性。
- **[nextjs-developer](subagents/01-core-development/nextjs-developer.md)**: 精通Next.js 14+、App Router和全栈特性的Next.js开发专家。专精现代React开发。 | 工具: next, vercel, turbo, prisma, playwright...
- **[nextjs-pro](subagents/01-core-development/nextjs-pro.md)**: 专精构建高性能、可扩展和SEO友好Web应用的Next.js开发专家。 | 工具: Read, Write, Edit, Grep, Glob...
- **[platform-engineer](subagents/01-core-development/platform-engineer.md)**: 专精内部开发者平台、自助服务基础设施和开发者体验的平台工程师专家。 | 工具: Read, Write, MultiEdit, Bash, kubectl...
- **[postgres-pro](subagents/01-core-development/postgres-pro.md)**: 精通数据库管理、性能优化和高可用性的PostgreSQL专家。掌握企业级数据库解决方案。 | 工具: psql, pg_dump, pgbench, pg_stat_statements, pgbadger
- **[postgresql-pglite-pro](subagents/01-core-development/postgresql-pglite-pro.md)**: PostgreSQL和Pglite专家，专精健壮的数据库架构、性能调优和轻量级数据库解决方案。 | 工具: Read, Write, Edit, Grep, Glob...
- **[rails-expert](subagents/01-core-development/rails-expert.md)**: 精通Rails 7+和现代约定的Rails专家。专精约定优于配置和快速Web开发。 | 工具: rails, rspec, sidekiq, redis, postgresql...
- **[react-performance-optimization](subagents/01-core-development/react-performance-optimization.md)**: 专注识别、分析和解决React性能问题的React性能优化专家。提升应用响应速度和用户体验。
- **[react-pro](subagents/01-core-development/react-pro.md)**: 专精创建现代、高性能和可扩展Web应用程序的React开发专家。掌握React生态系统。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[react-specialist](subagents/01-core-development/react-specialist.md)**: 精通React 18+、现代模式和生态系统的React专家。专精性能优化和组件设计。 | 工具: vite, webpack, jest, cypress, storybook...
- **[research-brief-generator](subagents/01-core-development/research-brief-generator.md)**: 将用户研究查询转换为结构化、可操作的研究简报，包含具体问题和方法论。
- **[research-coordinator](subagents/01-core-development/research-coordinator.md)**: 战略性规划和协调跨多个专家的复杂研究任务。主动用于大型研究项目管理。
- **[spring-boot-engineer](subagents/01-core-development/spring-boot-engineer.md)**: 精通Spring Boot 3+和云原生模式的Spring Boot工程师专家。专精微服务架构。 | 工具: maven, gradle, spring-cli, docker, kubernetes...
- **[sql-expert](subagents/01-core-development/sql-expert.md)**: 编写复杂SQL查询和优化数据库性能。主动用于查询优化和数据库设计。
- **[sql-pro](subagents/01-core-development/sql-pro.md)**: 专精复杂查询优化、数据库设计和性能调优的SQL开发专家。掌握高级数据库技术。 | 工具: Read, Write, MultiEdit, Bash, psql...
- **[sre-engineer](subagents/01-core-development/sre-engineer.md)**: 通过SLO、自动化和监控平衡功能速度与系统稳定性的站点可靠性工程师专家。 | 工具: Read, Write, MultiEdit, Bash, prometheus...
- **[swift-expert](subagents/01-core-development/swift-expert.md)**: 专精Swift 5.9+、async/await、SwiftUI和面向协议编程的Swift开发专家。 | 工具: Read, Write, MultiEdit, Bash, swift...
- **[technical-researcher](subagents/01-core-development/technical-researcher.md)**: 分析代码仓库、技术文档和实现细节。主动用于技术调研和架构分析。
- **[technical-writer](subagents/01-core-development/technical-writer.md)**: 专精清晰、准确文档和内容创作的技术写作专家。掌握多种文档工具和格式。 | 工具: markdown, asciidoc, confluence, gitbook, mkdocs
- **[test-automator](subagents/01-core-development/test-automator.md)**: 负责设计、实施和维护全面测试自动化框架的测试自动化专家。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[tooling-engineer](subagents/01-core-development/tooling-engineer.md)**: 专精开发者工具创建、CLI开发和生产力增强的工具工程师专家。 | 工具: node, python, go, rust, webpack...
- **[ui-designer](subagents/01-core-development/ui-designer.md)**: 专注创建视觉吸引力、直观且用户友好界面的创意UI设计师AI。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[ui-ux-designer](subagents/01-core-development/ui-ux-designer.md)**: 运用现代设计原则、无障碍标准和设计系统设计用户界面和体验。
- **[url-link-extractor](subagents/01-core-development/url-link-extractor.md)**: 查找、提取和编目网站代码库中的所有URL和链接。包括内部链接、外部链接和资源引用。
- **[vue-expert](subagents/01-core-development/vue-expert.md)**: 精通Vue 3、组合式API和生态系统的Vue专家。专精响应式系统和组件架构。 | 工具: vite, vue-cli, vitest, cypress, vue-devtools...
- **[wordpress-developer](subagents/01-core-development/wordpress-developer.md)**: 构建专业WordPress解决方案，包括自定义主题、插件和高级功能。WordPress专家级开发者。
- **[workflow-orchestrator](subagents/01-core-development/workflow-orchestrator.md)**: 专精复杂流程设计、状态机实现和业务流程自动化的工作流编排专家。 | 工具: Read, Write, workflow-engine, state-machine, bpmn

### 语言专家 (20 个代理)

- **[cpp-engineer](subagents/02-language-specialists/cpp-engineer.md)**: 编写具有现代特性、RAII、智能指针和STL算法的惯用C++代码。处理模板和内存管理。
- **[data-analyst](subagents/02-language-specialists/data-analyst.md)**: 专精商业智能、数据可视化和统计分析的数据分析专家。 | 工具: Read, Write, MultiEdit, Bash, sql...
- **[golang-expert](subagents/02-language-specialists/golang-expert.md)**: 编写具有goroutines、channels和interfaces的惯用Go代码。优化并发性，实现高性能系统。
- **[golang-pro](subagents/02-language-specialists/golang-pro.md)**: 架构、编写和重构健壮、并发、高性能Go应用程序的Go专家。 | 工具: Read, Write, Edit, Grep, Glob...
- **[incident-responder](subagents/02-language-specialists/incident-responder.md)**: 经验丰富的事件指挥官，负责领导关键生产事件的响应处理。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[network-engineer](subagents/02-language-specialists/network-engineer.md)**: 专精云和混合网络架构、安全和性能优化的网络工程师专家。 | 工具: Read, Write, MultiEdit, Bash, tcpdump...
- **[php-developer](subagents/02-language-specialists/php-developer.md)**: 编写具有设计模式、SOLID原则和现代最佳实践的惯用PHP代码。实现企业级解决方案。
- **[php-pro](subagents/02-language-specialists/php-pro.md)**: 专精现代PHP 8.3+、强类型、异步编程和企业架构的PHP开发专家。 | 工具: Read, Write, MultiEdit, Bash, php...
- **[product-manager](subagents/02-language-specialists/product-manager.md)**: 战略性和以客户为中心的AI产品经理，负责定义产品愿景、策略和路线图。 | 工具: Read, Write, Edit, Grep, Glob...
- **[python-expert](subagents/02-language-specialists/python-expert.md)**: 编写具有装饰器、生成器和async/await等高级特性的惯用Python代码。优化性能和可读性。
- **[python-pro](subagents/02-language-specialists/python-pro.md)**: 专精编写清洁、高性能和惯用代码的Python开发专家。利用现代Python特性和最佳实践。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[quant-analyst](subagents/02-language-specialists/quant-analyst.md)**: 专精金融建模、算法交易和风险分析的量化分析专家。 | 工具: python, numpy, pandas, quantlib, zipline...
- **[report-generator](subagents/02-language-specialists/report-generator.md)**: 专精将综合研究发现转化为结构化、可操作报告的报告生成器专家。
- **[ruby-expert](subagents/02-language-specialists/ruby-expert.md)**: 遵循最佳实践和设计模式编写惯用Ruby代码。实现SOLID原则和元编程技术。
- **[rust-engineer](subagents/02-language-specialists/rust-engineer.md)**: 专精系统编程、内存安全和零成本抽象的Rust开发专家。 | 工具: Read, Write, MultiEdit, Bash, cargo...
- **[rust-expert](subagents/02-language-specialists/rust-expert.md)**: 编写具有所有权、生命周期和类型安全的惯用Rust代码。实现并发系统和高性能应用。
- **[security-engineer](subagents/02-language-specialists/security-engineer.md)**: 专精DevSecOps、云安全和合规框架的基础设施安全工程师专家。 | 工具: Read, Write, MultiEdit, Bash, nmap...
- **[task-decomposition-expert](subagents/02-language-specialists/task-decomposition-expert.md)**: 将复杂用户目标分解为可操作任务，并识别工具、代理和工作流程的最佳组合。
- **[typescript-expert](subagents/02-language-specialists/typescript-expert.md)**: 编写具有高级类型系统特性、泛型和实用类型的类型安全TypeScript代码。实现复杂类型推断。
- **[url-context-validator](subagents/02-language-specialists/url-context-validator.md)**: 验证URL的技术功能性和上下文适当性。超越链接检查，确保内容相关性和质量。

### 基础设施与运维 (11 个代理)

- **[compliance-auditor](subagents/03-infrastructure/compliance-auditor.md)**: 专精监管框架、数据隐私法律和安全标准的合规审计专家。 | 工具: Read, Write, MultiEdit, Bash, prowler...
- **[csharp-developer](subagents/03-infrastructure/csharp-developer.md)**: 专精现代.NET开发、ASP.NET Core和云原生应用的C#开发专家。 | 工具: Read, Write, MultiEdit, Bash, dotnet...
- **[deployment-engineer](subagents/03-infrastructure/deployment-engineer.md)**: 设计和实施健壮的CI/CD管道、容器编排和云基础设施自动化的部署工程师。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[devops-engineer](subagents/03-infrastructure/devops-engineer.md)**: 通过全面自动化、监控和基础设施管理连接开发和运维的DevOps工程师专家。 | 工具: Read, Write, MultiEdit, Bash, docker...
- **[devops-incident-responder](subagents/03-infrastructure/devops-incident-responder.md)**: 专门负责领导事件响应、进行深入根因分析和实施预防措施的专业代理。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[devops-troubleshooter](subagents/03-infrastructure/devops-troubleshooter.md)**: 调试生产问题、分析日志和修复部署故障。掌握监控工具、事件管理和系统诊断。
- **[kubernetes-specialist](subagents/03-infrastructure/kubernetes-specialist.md)**: 精通容器编排、集群管理和云原生架构的Kubernetes专家。 | 工具: Read, Write, MultiEdit, Bash, kubectl...
- **[machine-learning-engineer](subagents/03-infrastructure/machine-learning-engineer.md)**: 专精生产模型部署、服务基础设施和可扩展ML系统的机器学习工程师专家。 | 工具: Read, Write, MultiEdit, Bash, tensorflow...
- **[mlops-engineer](subagents/03-infrastructure/mlops-engineer.md)**: 专精ML基础设施、平台工程和运营卓越的MLOps工程师专家。 | 工具: mlflow, kubeflow, airflow, docker, prometheus...
- **[terraform-engineer](subagents/03-infrastructure/terraform-engineer.md)**: 专精基础设施即代码、多云配置和模块化设计的Terraform工程师专家。 | 工具: Read, Write, MultiEdit, Bash, terraform...
- **[terraform-specialist](subagents/03-infrastructure/terraform-specialist.md)**: 编写Terraform模块和管理基础设施即代码。主动用于基础设施自动化和云资源管理。

### 质量与安全 (19 个代理)

- **[academic-researcher](subagents/04-quality-security/academic-researcher.md)**: 查找和分析学术资源、研究论文和学术文献。主动用于文献综述和研究支持。
- **[accessibility-tester](subagents/04-quality-security/accessibility-tester.md)**: 专精WCAG合规性、包容性设计和通用访问的无障碍测试专家。 | 工具: Read, Write, MultiEdit, Bash, axe...
- **[audio-quality-controller](subagents/04-quality-security/audio-quality-controller.md)**: 分析、增强和标准化专业级内容的音频质量。规范化音量和音频处理。
- **[code-reviewer](subagents/04-quality-security/code-reviewer.md)**: 专精代码质量、安全漏洞和跨语言最佳实践的代码审查专家。 | 工具: Read, Grep, Glob, git, eslint...
- **[code-reviewer-pro](subagents/04-quality-security/code-reviewer-pro.md)**: 进行全面代码审查的AI驱动高级工程主管。分析代码质量、安全性和架构。 | 工具: Read, Grep, Glob, Bash, LS...
- **[command-expert](subagents/04-quality-security/command-expert.md)**: 创建自动化和工具的CLI命令。主动用于设计命令行界面和脚本工具。
- **[debugger](subagents/04-quality-security/debugger.md)**: 专精错误、测试失败和异常行为的调试专家。主动用于遇到技术问题时。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[dependency-manager](subagents/04-quality-security/dependency-manager.md)**: 专精包管理、安全审计和版本冲突解决的依赖管理专家。 | 工具: npm, yarn, pip, maven, gradle...
- **[ocr-quality-assurance](subagents/04-quality-security/ocr-quality-assurance.md)**: 执行OCR校正文本最终审查和验证的OCR质量保证专家。
- **[penetration-tester](subagents/04-quality-security/penetration-tester.md)**: 专精道德黑客、漏洞评估和安全测试的渗透测试专家。 | 工具: Read, Grep, nmap, metasploit, burpsuite...
- **[qa-expert](subagents/04-quality-security/qa-expert.md)**: 设计、实施和管理全面质量保证流程的精密AI质量保证专家。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[refactoring-specialist](subagents/04-quality-security/refactoring-specialist.md)**: 掌握安全代码转换技术和设计模式应用的重构专家。 | 工具: ast-grep, semgrep, eslint, prettier, jscodeshift
- **[research-orchestrator](subagents/04-quality-security/research-orchestrator.md)**: 负责管理全面研究项目和协调多个研究代理的精英研究编排者。
- **[review-agent](subagents/04-quality-security/review-agent.md)**: 知识管理系统的专业质量保证代理。主要负责内容审查和质量控制。
- **[risk-manager](subagents/04-quality-security/risk-manager.md)**: 专精全面风险评估、缓解策略和合规管理的风险管理专家。 | 工具: python, R, matlab, excel, sas...
- **[security-auditor](subagents/04-quality-security/security-auditor.md)**: 专精识别、评估和缓解安全威胁的高级应用安全审计师和道德黑客。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[task-distributor](subagents/04-quality-security/task-distributor.md)**: 专精智能工作分配、负载均衡和队列管理的任务分发专家。 | 工具: Read, Write, task-queue, load-balancer, scheduler
- **[typescript-pro](subagents/04-quality-security/typescript-pro.md)**: 架构、编写和重构可扩展、类型安全、可维护应用的TypeScript专家。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[ux-researcher](subagents/04-quality-security/ux-researcher.md)**: 专精用户洞察、可用性测试和数据驱动设计决策的UX研究专家。 | 工具: Read, Write, MultiEdit, Bash, figma...

### 数据与AI (39 个代理)

- **[agent-expert](subagents/05-data-ai/agent-expert.md)**: 创建和优化专业的 Claude Code 代理。专精代理设计、提示工程等领域。
- **[competitive-analyst](subagents/05-data-ai/competitive-analyst.md)**: 专精竞争对手情报、战略分析和市场定位的竞争分析专家。 | 工具: Read, Write, WebSearch, WebFetch, similarweb...
- **[connection-agent](subagents/05-data-ai/connection-agent.md)**: 分析并建议知识管理系统中相关内容之间的有意义链接。识别内容关联性。
- **[context-manager](subagents/05-data-ai/context-manager.md)**: 专精信息存储、检索和跨多系统同步的上下文管理专家。 | 工具: Read, Write, redis, elasticsearch, vector-db
- **[crypto-analyst](subagents/05-data-ai/crypto-analyst.md)**: 执行加密货币市场分析、链上分析和情绪分析。主动用于加密货币投资决策。
- **[data-researcher](subagents/05-data-ai/data-researcher.md)**: 专精发现、收集和分析多样化数据源的数据研究专家。 | 工具: Read, Write, sql, python, pandas...
- **[data-scientist](subagents/05-data-ai/data-scientist.md)**: 专精高级SQL、BigQuery优化和可操作数据洞察的数据科学家专家。 | 工具: Read, Write, Edit, Grep, Glob...
- **[documentation-expert](subagents/05-data-ai/documentation-expert.md)**: 专精设计、创建和维护全面软件文档的AI文档专家。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[embedded-systems](subagents/05-data-ai/embedded-systems.md)**: 专精微控制器编程、RTOS开发和硬件集成的嵌入式系统工程师专家。 | 工具: gcc-arm, platformio, arduino, esp-idf, stm32cube
- **[episode-orchestrator](subagents/05-data-ai/episode-orchestrator.md)**: 通过按顺序协调多个专业代理来管理基于剧集的工作流程。检测完成状态。
- **[error-coordinator](subagents/05-data-ai/error-coordinator.md)**: 专精分布式错误处理、故障恢复和系统恢复的错误协调专家。 | 工具: Read, Write, MultiEdit, Bash, sentry...
- **[hyperledger-fabric-developer](subagents/05-data-ai/hyperledger-fabric-developer.md)**: 使用Hyperledger Fabric v2.5 LTS和v3.x开发企业区块链解决方案。专精链码开发。
- **[legacy-modernizer](subagents/05-data-ai/legacy-modernizer.md)**: 专精规划和执行遗留系统增量现代化的专业代理。重构和迁移专家。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[legal-advisor](subagents/05-data-ai/legal-advisor.md)**: 专精技术法律、合规和风险缓解的法律顾问专家。掌握合同管理。 | 工具: markdown, latex, docusign, contract-tools
- **[markdown-syntax-formatter](subagents/05-data-ai/markdown-syntax-formatter.md)**: 将带有视觉格式的文本转换为正确的markdown语法，修复markdown格式问题。
- **[market-research-analyst](subagents/05-data-ai/market-research-analyst.md)**: 为商业策略和投资决策进行全面的市场研究和竞争分析。
- **[metadata-agent](subagents/05-data-ai/metadata-agent.md)**: 处理前置元数据标准化和跨文件元数据添加。确保元数据一致性。
- **[ml-engineer](subagents/05-data-ai/ml-engineer.md)**: 设计、构建和管理机器学习模型在生产环境中的端到端生命周期。专精于创建可扩展、可靠和自动化的ML系统。主动用于涉及ML模型部署、监控和维护的任务。 | 工具: Read, Write, Edit, Grep, Glob...
- **[moc-agent](subagents/05-data-ai/moc-agent.md)**: 识别并生成缺失的内容地图(MOCs)，组织孤立资产。创建导航结构。
- **[multi-agent-coordinator](subagents/05-data-ai/multi-agent-coordinator.md)**: 专精复杂工作流编排、代理间通信和协作的多代理协调专家。 | 工具: Read, Write, message-queue, pubsub, workflow-engine
- **[nlp-engineer](subagents/05-data-ai/nlp-engineer.md)**: 专精自然语言处理、理解和生成的NLP工程师专家。 | 工具: Read, Write, MultiEdit, Bash, transformers...
- **[ocr-grammar-fixer](subagents/05-data-ai/ocr-grammar-fixer.md)**: OCR语法修复专家，专精清理通过OCR处理的包含识别错误的文本。
- **[payment-integration](subagents/05-data-ai/payment-integration.md)**: 专精支付网关集成、PCI合规和金融安全的支付集成专家。 | 工具: stripe, paypal, square, razorpay, braintree
- **[podcast-content-analyzer](subagents/05-data-ai/podcast-content-analyzer.md)**: 分析播客转录以识别引人入胜的片段和病毒式传播时刻。主动用于内容优化。
- **[podcast-metadata-specialist](subagents/05-data-ai/podcast-metadata-specialist.md)**: 播客元数据专家，生成全面的元数据、节目笔记、章节标记等。
- **[podcast-transcriber](subagents/05-data-ai/podcast-transcriber.md)**: 播客转录专家，专精从音频/视频文件中提取准确的转录文本。
- **[podcast-trend-scout](subagents/05-data-ai/podcast-trend-scout.md)**: 播客趋势侦察员，识别播客节目的新兴技术话题和新闻。
- **[project-supervisor-orchestrator](subagents/05-data-ai/project-supervisor-orchestrator.md)**: 项目监督编排器，管理协调多个代理的复杂多步骤工作流程。
- **[prompt-engineer](subagents/05-data-ai/prompt-engineer.md)**: 一位精通架构和优化复杂LLM交互的提示工程大师。用于设计高级AI系统，将模型性能推向极限，创建稳健、安全、可靠的代理工作流程。在各种高级提示技术、模型特定细节和道德AI设计方面具有专业知识。 | 工具: Read, Write, Edit, Grep, Glob...
- **[query-clarifier](subagents/05-data-ai/query-clarifier.md)**: 分析研究查询的清晰度并确定是否需要澄清。主动用于研究开始阶段。
- **[research-analyst](subagents/05-data-ai/research-analyst.md)**: 专精全面信息收集、综合和洞察生成的研究分析专家。 | 工具: Read, Write, WebSearch, WebFetch, Grep
- **[research-synthesizer](subagents/05-data-ai/research-synthesizer.md)**: 将多个研究来源的发现整合并综合为统一分析。用于多源研究整合。
- **[sales-automator](subagents/05-data-ai/sales-automator.md)**: 起草冷邮件、跟进邮件和提案模板。创建定价页面、案例研究和销售材料。
- **[seo-podcast-optimizer](subagents/05-data-ai/seo-podcast-optimizer.md)**: 专精技术播客的SEO顾问。专长于制作搜索优化的播客内容。
- **[tag-agent](subagents/05-data-ai/tag-agent.md)**: 为知识管理系统标准化和分层组织标签分类法。维护清晰的标签结构。
- **[text-comparison-validator](subagents/05-data-ai/text-comparison-validator.md)**: 比较从图像提取的文本与现有markdown文件以确保准确性和一致性。
- **[timestamp-precision-specialist](subagents/05-data-ai/timestamp-precision-specialist.md)**: 从音频/视频文件中提取帧精确时间戳用于播客编辑。识别精确剪切点。
- **[twitter-ai-influencer-manager](subagents/05-data-ai/twitter-ai-influencer-manager.md)**: 与Twitter上的AI思想领袖和影响者互动。发布推文、搜索内容、分析趋势。
- **[visual-analysis-ocr](subagents/05-data-ai/visual-analysis-ocr.md)**: 从PNG图像中提取和分析文本内容，同时保持原始格式和结构。

### 开发者体验 (3 个代理)

- **[dx-optimizer](subagents/06-developer-experience/dx-optimizer.md)**: 专精开发者体验(DX)优化的专业代理。主动改进工具链、环境配置和开发流程，提升开发效率和体验。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[git-workflow-manager](subagents/06-developer-experience/git-workflow-manager.md)**: 专精Git工作流管理、分支策略、自动化和团队协作的Git工作流管理专家。优化版本控制流程。 | 工具: git, github-cli, gitlab, gitflow, pre-commit
- **[social-media-clip-creator](subagents/06-developer-experience/social-media-clip-creator.md)**: 专精从长内容中创建优化社交媒体视频片段的内容创作专家。处理平台特定的视频优化需求。

### 专业领域 (9 个代理)

- **[arbitrage-bot](subagents/07-specialized-domains/arbitrage-bot.md)**: 识别并执行跨交易所和DeFi协议的加密货币套利机会。专精自动化交易策略。
- **[c-developer](subagents/07-specialized-domains/c-developer.md)**: 专精系统编程和嵌入式开发的C语言编程专家。掌握内存管理和性能优化。
- **[flutter-expert](subagents/07-specialized-domains/flutter-expert.md)**: 精通Flutter 3+和现代架构模式的Flutter专家。专精跨平台移动应用开发。 | 工具: flutter, dart, android-studio, xcode, firebase...
- **[game-developer](subagents/07-specialized-domains/game-developer.md)**: 专精游戏引擎编程、图形优化和多人游戏开发的游戏开发专家。 | 工具: unity, unreal, godot, phaser, pixi...
- **[kotlin-specialist](subagents/07-specialized-domains/kotlin-specialist.md)**: 专精协程、多平台开发和Android应用的Kotlin开发专家。 | 工具: Read, Write, MultiEdit, Bash, kotlin...
- **[performance-engineer](subagents/07-specialized-domains/performance-engineer.md)**: 定义和执行全面性能策略的高级性能工程师。专精系统性能优化和监控。 | 工具: Read, Write, Edit, MultiEdit, Grep...
- **[scrum-master](subagents/07-specialized-domains/scrum-master.md)**: 专精敏捷转型、团队促进和持续改进的Scrum Master专家。 | 工具: Read, Write, MultiEdit, Bash, jira...
- **[search-specialist](subagents/07-specialized-domains/search-specialist.md)**: 专精高级信息检索、查询优化和知识发现的搜索专家。 | 工具: Read, Write, WebSearch, Grep, elasticsearch...
- **[websocket-engineer](subagents/07-specialized-domains/websocket-engineer.md)**: 实现可扩展WebSocket架构的实时通信专家。掌握双向通信和实时数据传输。 | 工具: Read, Write, MultiEdit, Bash, socket.io...

### 业务与产品 (6 个代理)

- **[crypto-risk-manager](subagents/08-business-product/crypto-risk-manager.md)**: 专精加密货币交易和DeFi头寸风险管理系统的风险管理专家。
- **[market-researcher](subagents/08-business-product/market-researcher.md)**: 专精市场分析、消费者洞察和竞争情报的市场研究专家。 | 工具: Read, Write, WebSearch, survey-tools, analytics...
- **[project-manager](subagents/08-business-product/project-manager.md)**: 专精项目规划、执行和交付的项目管理专家。掌握资源管理和团队协调。 | 工具: jira, asana, monday, ms-project, slack...
- **[sales-engineer](subagents/08-business-product/sales-engineer.md)**: 专精技术售前、解决方案架构和概念验证的销售工程师专家。 | 工具: Read, Write, MultiEdit, Bash, salesforce...
- **[social-media-copywriter](subagents/08-business-product/social-media-copywriter.md)**: 专精播客推广的社交媒体文案专家。专长于将播客内容转化为引人入胜的社交媒体内容。
- **[ux-designer](subagents/08-business-product/ux-designer.md)**: 专注通过改善可用性和用户体验来提升用户满意度的创意UX设计师专家。 | 工具: Read, Write, Edit, MultiEdit, Grep...

### 元编程与编排 (1 个代理)

- **[cpp-pro](subagents/09-meta-orchestration/cpp-pro.md)**: 专精现代C++20/23、系统编程和高性能计算的C++开发专家。 | 工具: Read, Write, MultiEdit, Bash, g++...

### 研究与分析 (3 个代理)

- **[error-detective](subagents/10-research-analysis/error-detective.md)**: 专精复杂错误模式分析、关联性分析和根因诊断的错误侦探专家。 | 工具: Read, Grep, Glob, elasticsearch, datadog...
- **[performance-monitor](subagents/10-research-analysis/performance-monitor.md)**: 专精系统级指标收集、分析和优化建议的性能监控专家。 | 工具: Read, Write, MultiEdit, Bash, prometheus...
- **[trend-analyst](subagents/10-research-analysis/trend-analyst.md)**: 专精识别新兴模式、预测未来发展趋势和市场洞察的趋势分析专家。 | 工具: Read, Write, WebSearch, google-trends, social-listening...

## 🎯 使用指南

### 快速开始

1. **选择合适的代理**: 根据您的任务需求，从上述分类中选择最适合的代理
2. **查看代理文档**: 点击代理名称查看详细的使用说明和配置
3. **配置工具**: 根据代理要求配置相应的 MCP 工具
4. **开始使用**: 按照代理文档中的指南开始您的开发任务

### 代理选择建议

#### 根据开发阶段选择
- **项目初始化**: 从 `01-core-development` 选择 `full-stack-developer`、`frontend-developer` 或 `backend-developer`
- **代码质量保证**: 从 `04-quality-security` 选择 `code-reviewer`、`test-engineer` 或 `security-auditor`
- **性能优化**: 从 `07-specialized-domains` 选择 `performance-engineer` 或数据库相关代理
- **部署运维**: 从 `03-infrastructure` 选择 `devops-engineer`、`docker-specialist` 或云平台专家

#### 根据技术栈选择
- **前端开发**: `02-language-specialists` 中的 `react-expert`、`vue-specialist`、`angular-expert`
- **后端开发**: `02-language-specialists` 中的 `python-expert`、`nodejs-specialist`、`java-expert`
- **移动开发**: `07-specialized-domains` 中的 `flutter-expert` 或原生开发专家
- **数据科学**: `05-data-ai` 中的 `data-scientist`、`ml-engineer`、`nlp-engineer`

#### 根据业务需求选择
- **产品规划**: `08-business-product` 中的 `project-manager`、`ux-designer`
- **市场分析**: `08-business-product` 中的 `market-researcher`、`competitive-analyst`
- **内容创作**: `06-developer-experience` 中的内容相关代理
- **研究分析**: `10-research-analysis` 中的 `trend-analyst`、`research-analyst`

#### 根据项目复杂度选择
- **简单项目**: 选择单一专业代理即可
- **中等项目**: 组合 2-3 个不同分类的代理
- **复杂项目**: 使用 `09-meta-orchestration` 中的编排代理协调多个专业代理

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

本仓库内容参考了以下来源：
- [claude-code-subagents-collection-main](https://github.com/ProfSynapse/claude-code-subagents-collection)
- [claude-code-sub-agents-main](https://github.com/ProfSynapse/claude-code-sub-agents)
- [awesome-claude-code-subagents-main](https://github.com/ProfSynapse/awesome-claude-code-subagents)

