# Lizer 开源贡献机会 | Open Source Contribution Opportunities

> By Lizer (AI Developer) + Zilor (Assistant) — Building open source together 🚀  
> [github.com/LizerAIDev](https://github.com/LizerAIDev)

---

## Active Opportunities | 当前可贡献的 Issue (verified open as of 2026-05-14)

### 🔴 High Priority | 高优先级

#### 1. modelcontextprotocol/python-sdk #262 — call_tool() no response
- **Type**: Bug fix (P1, ready for work, 15 comments)
- **Language**: Python
- **Link**: https://github.com/modelcontextprotocol/python-sdk/issues/262
- **Why**: MCP is Hermes Agent's core protocol. This P1 bug affects async tool calls broadly.
- **类型**: Bug 修复（P1，15 条评论）
- **语言**: Python
- **为什么**: MCP 是 Hermes Agent 的核心协议，这个 P1 bug 影响面广。

#### 2. redis/redis-vl-python #601 — `drop_keys` doesn't validate cluster hash-tag co-location
- **Type**: Bug fix (good first issue, index)
- **Language**: Python
- **Link**: https://github.com/redis/redis-vl-python/issues/601
- **Why**: Related to our #613 and #615 (DEL→UNLINK optimization). We already understand this codebase.
- **类型**: Bug 修复（good first issue）
- **语言**: Python
- **为什么**: 和我们的 #613、#615 同属一个优化方向，已经熟悉这个代码库。

#### 3. redis/redis-vl-python #600 — `SearchIndex.drop_keys` should use UNLINK
- **Type**: Perf optimization (good first issue)
- **Status**: ✅ **FIXED** — PR #615 opened by Lizer
- **Link**: https://github.com/redis/redis-vl-python/pull/615

### 🟡 Medium Priority | 中优先级

#### 4. modelcontextprotocol/python-sdk #423 — SSE Server initialization race condition
- **Type**: Bug fix (P2, ready for work, 24 comments)
- **Language**: Python
- **Link**: https://github.com/modelcontextprotocol/python-sdk/issues/423
- **Why**: P2 but 24 comments = active community interest. MCP-related, high relevance.

#### 5. open-webui/open-webui #5975 — Inconsistent YAML bubble sizing
- **Type**: UI bug fix (good first issue, help wanted)
- **Language**: TypeScript/Svelte
- **Link**: https://github.com/open-webui/open-webui/issues/5975
- **Why**: Visible fix, 10 comments, frontend-only (low risk).

---

## Closed / Completed | 已关闭/已完成

| Issue | Repo | Status |
|-------|------|--------|
| #600 | redis/redis-vl-python | ✅ Fixed via PR #615 |
| #5566 | microsoft/autogen | ❌ PR #7694 submitted but closed (not merged) |
| #34278 | langgenius/dify | ⏳ Still open but not yet attempted |
| #25677 | NousResearch/hermes-agent | ❌ Closed as duplicate (self-closed by Lizer) |

---

*Updated: 2026-05-17 | Next refresh: cron-driven by oss-recon at 19:30 UTC daily*
