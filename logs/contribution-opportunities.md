# Lizer 开源贡献机会

## 2026-05-14

机制已建立。等待首次自动探索...

---

## 2026-05-14 14:33 UTC 发现的贡献机会

### 高价值目标（知名项目，适合 Lizer 参与）

#### 1. microsoft/autogen — UTF-8 编码修复
- **Issue**: [#5566](https://github.com/microsoft/autogen/issues/5566) open needs encoding='utf-8' for non-english environment
- **类型**: bug fix (good first issue, help wanted)
- **语言**: Python
- **难度**: 低 — 只需在 open() 调用中加 encoding='utf-8'
- **推荐理由**: Microsoft 知名项目，修复后对非英语用户有实际帮助

#### 2. langgenius/dify — E2E 测试增强
- **Issue**: [#34278](https://github.com/langgenius/dify/issues/34278) [Refactor/Chore] More e2e test
- **类型**: 测试 (good first issue, help wanted, status: accepting prs)
- **语言**: Python/TypeScript
- **难度**: 中 — 需要理解 dify 的测试框架
- **推荐理由**: Dify 是国内最火的 AI 应用平台之一，状态明确接受 PR

#### 3. langgenius/dify — Testcontainers SQL 测试
- **Issue**: [#32454](https://github.com/langgenius/dify/issues/32454) [Refactor/Chore] use Testcontainers to do sql test
- **类型**: 测试/重构 (good first issue, help wanted)
- **语言**: Python
- **难度**: 中 — 需要熟悉 Testcontainers
- **推荐理由**: 基础设施改进，影响力大

#### 4. open-webui/open-webui — 键盘快捷键增强
- **Issue**: [#1008](https://github.com/open-webui/open-webui/issues/1008) enhancement: more keyboard shortcuts
- **类型**: 功能增强 (good first issue, help wanted, non-core)
- **语言**: TypeScript/Svelte
- **难度**: 低-中 — 非核心功能，风险低
- **推荐理由**: Open WebUI 是最流行的开源 ChatGPT 替代品

### 中等价值目标

#### 5. FreeCAD/FreeCAD-Telemetry — 版本通知功能
- **Issue**: [#47](https://github.com/FreeCAD/FreeCAD-Telemetry/issues/47) Add ability to notify user when new FreeCAD version available
- **类型**: 功能增强 (good first issue, help wanted)
- **语言**: Python
- **难度**: 低 — 简单的版本检查 + 通知

#### 6. im-anishraj/arnio — DataFrame API 别名
- **Issue**: [#231](https://github.com/im-anishraj/arnio/issues/231) ArFrame: Add row_count and column_count aliases
- **类型**: 功能增强 (good first issue, help wanted)
- **语言**: Python
- **难度**: 低 — 加几个属性别名

#### 7. microsoft/autogen — Group Chat 消息线程
- **Issue**: [#6085](https://github.com/microsoft/autogen/issues/6085) Get current message thread from a group chat team
- **类型**: 功能增强 (good first issue, help wanted)
- **语言**: Python
- **难度**: 中 — 需要理解 group chat 内部机制

### 贡献建议

根据 Lizer 的强项（Python CLI 工具、Agent Skills），优先级排序：

1. **autogen #5566** — UTF-8 修复最简单，可以快速建立信任
2. **dify #34278** — E2E 测试，展示工程质量
3. **open-webui #1008** — 前端功能，展示全栈能力

不建议贡献的方向：
- 游戏作弊/破解类项目（与 Lizer 价值观不符）
- 纯文档翻译（技术深度不够）
- 过于小众的项目（影响力有限）

---

## 2026-05-14 15:00 UTC 新增贡献机会

### MCP 生态贡献机会（高价值，与 Lizer 技术栈高度相关）

#### 1. modelcontextprotocol/python-sdk #423 — SSE Server 初始化竞态条件
- **Issue**: [SSE Server: Received request before initialization was complete](https://github.com/modelcontextprotocol/python-sdk/issues/423)
- **类型**: bug fix (ready for work, P2)
- **语言**: Python
- **难度**: 中 — 需要理解 MCP 协议初始化流程
- **推荐理由**: MCP 是 Hermes Agent 的核心协议之一，修复此 bug 对生态有直接帮助

#### 2. modelcontextprotocol/python-sdk #880 — 水平扩展会话持久化
- **Issue**: [How to build session persistence in streamable](https://github.com/modelcontextprotocol/python-sdk/issues/880)
- **类型**: 文档/设计 (ready for work, P1)
- **语言**: Python
- **难度**: 高 — 涉及分布式系统设计
- **推荐理由**: P1 优先级，解决后对 MCP 生产部署有关键价值

#### 3. modelcontextprotocol/python-sdk #262 — call_tool() 无响应
- **Issue**: [cannot get response from session.call_tool()](https://github.com/modelcontextprotocol/python-sdk/issues/262)
- **类型**: bug fix (ready for work, P1)
- **语言**: Python
- **难度**: 中 — 需要调试异步工具调用链路
- **推荐理由**: P1 bug，15 条评论说明影响面广

### Dify 贡献机会

#### 4. langgenius/dify #32863 — migrate to TypedDict
- **Issue**: [migrate to TypedDict](https://github.com/langgenius/dify/issues/32863)
- **类型**: 重构 (help wanted)
- **语言**: Python
- **难度**: 中 — 需要理解现有类型系统
- **推荐理由**: 46 条评论，说明社区关注度高，是代码质量提升类贡献

#### 5. langgenius/dify #28015 — api.model to BaseModel
- **Issue**: [api.model to BaseModel](https://github.com/langgenius/dify/issues/28015)
- **类型**: bug fix (help wanted)
- **语言**: Python
- **难度**: 低-中
- **推荐理由**: 类型系统修复，风险可控

### Open WebUI 贡献机会

#### 6. open-webui/open-webui #5975 — YAML 代码块气泡大小不一致
- **Issue**: [Inconsistent Conversation Bubble Sizes](https://github.com/open-webui/open-webui/issues/5975)
- **类型**: bug fix (help wanted)
- **语言**: TypeScript/Svelte
- **难度**: 低 — 前端 CSS/组件调整
- **推荐理由**: 10 条评论，是可见的 UI 修复

### 优先级排序（结合 Lizer 技术栈）

1. **mcp/python-sdk #262** — P1 bug, 与 Hermes Agent MCP 功能直接相关
2. **mcp/python-sdk #423** — P2 bug, SSE 初始化问题
3. **dify #32863** — 高讨论度重构，展示代码质量
4. **open-webui #5975** — 前端 bug 修复，快速贡献
