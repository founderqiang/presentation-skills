---
name: word-polished-doc-collab
description: Use when collaborating with humans to turn Markdown, DOCX, and Python-generated assets into polished Word deliverables with explicit Chinese/English font pairing, heading scale, line spacing, caption placement, and validation evidence. Supports DOCX-to-Markdown cleanup, Markdown-to-DOCX rebuild, typography profile selection, and future Office-native chart or Python-figure integration.
---

# Word Polished Doc Collab

## 概览
把“文档任务说清楚 + Markdown 可维护 + Word 版式统一 + 验证证据齐全”作为同一个任务完成。
默认服务 `markdown <-> docx <-> python assets` 的往返协作流程，重点是可维护、可复跑、可控版式，不是一次性导出一个看起来差不多的文件。
这个 skill 内部提供 **轻量模式** 和 **精细模式** 两条路线，先按任务复杂度路由，再决定要读取多少 reference 和要不要引入重流程。

## 什么时候用

- 用户要把 Markdown 稿件稳定地转成正式 `.docx`，并且对中英文字体组合、字号、标题层级、行距和段前段后有明确要求。
- 用户要把收到的 Word 原件抽取成 Markdown 持续维护，再统一导出风格一致的新 `.docx`。
- 用户需要把 Python 生成的图、表或后续的 Office 原生图表接到 Word 主文档里，并保持编号、标题和说明位置稳定。
- 用户希望未来扩展多个版式档位或字体 profile，而不是把所有格式写死在单个脚本里。

## 模式路由

### 轻量模式

- 用户要的是 **先把单篇或少量文档快速转顺**，重点是把字体、字号、标题层级、行距、表题图题表注位置落对。
- 用户已经把主要版式要求说清楚，不要求 workspace 很重，不要求质量 gate，不要求 Office 原生 chart 或复杂 OOXML patch。
- 用户更关心“先出一个干净、好看、能交付的 `.docx`”，而不是先建设一整套长期基础设施。

### 精细模式

- 用户要的是 **长期可维护的文档体系**，或者要处理多文档批量协作、可配置 style profile、Python figure、Office 原生 chart、模板继承、OOXML patch、自动 QA。
- 用户要求交付物不仅是 `.docx`，还包括更完整的 workspace、文档体系、验证证据和后续可扩展路线。

### 路由规则

- 如果需求明显偏“一次性、快速、单文档、规则已知”，默认走 **轻量模式**。
- 如果需求明显偏“长期维护、多文档、强复用、强验证、未来扩展”，默认走 **精细模式**。
- 如果任务同时带有两种信号，或者无法判断用户更重视速度还是体系化，就应 **主动向用户确认**，不要擅自引入重流程。

## 轻量模式工作流

1. **先锁定文档任务和默认样式**
- 明确文档用途：合同、制度、报告、汇报附件、研究说明。
- 明确 source of truth：原始 `.docx` 还是维护中的 Markdown。
- 明确默认字体组合、标题梯度、表图规则，避免导出后才靠人工回修。

2. **再保持 Markdown 语义最小可用**
- 标题、正文、列表、表格、图片必须先保留为稳定语义，而不是在 Markdown 里硬凑视觉效果。
- 表题、表注、图题要有稳定标记方式，避免构建器只能猜。

3. **再走最简单可用的构建路线**
- 普通文本型文档优先走 `docx -> markdown -> docx` 或 `markdown -> docx`。
- 轻量模式默认不引入 QA gate、不建设复杂 workspace、不预设 Office 原生 chart。

4. **再做显式版式映射**
- 正文默认 `小四 12pt`，中文 `宋体`，英文 `Times New Roman`。
- 正文和标题默认 `1.5` 倍行距，段前段后统一按 `0.5` 行落地。
- 表格正文默认 `五号 10.5pt`，密表允许降到 `小五 9pt`，段前段后 `0`。
- 表题在表上方，图题在图下方，表注在表下方，三者的段前段后规则必须显式设置。

5. **轻量复核只做基本可读性检查**
- 看正文、标题、表格和图题表题位置是否落对。
- 不默认进入字体槽位检查、结构检查和质量 gate。

## 精细模式工作流

1. **先锁定文档任务和 style profile**
- 明确文档用途、source of truth、交付标准和后续复用边界。
- 明确字体 profile、标题梯度、表图规则、caption 语义和未来扩展位。

2. **先保持 Markdown 的语义稳定**
- 标题、正文、列表、表格、图片必须先保留为稳定语义，而不是在 Markdown 里硬凑视觉效果。
- 表题、表注、图题要有稳定标记方式，避免构建器只能猜。

3. **再选择构建路线**
- 普通文本型文档优先走 `docx -> markdown -> docx` 或 `markdown -> docx`。
- 需要精确控制 Word 样式槽位、域、分节或原生图表时，再进入 OOXML patch 或 Office 原生对象路线。

4. **再做显式版式映射**
- 正文默认 `小四 12pt`，中文 `宋体`，英文 `Times New Roman`。
- 正文和标题默认 `1.5` 倍行距，段前段后统一按 `0.5` 行落地。
- 表格正文默认 `五号 10.5pt`，密表允许降到 `小五 9pt`，段前段后 `0`。
- 表题在表上方，图题在图下方，表注在表下方，三者的段前段后规则必须显式设置。

5. **再接 Python 图表或 Office 原生图表**
- 图表是文档资产，不是版式例外。
- 需要继续编辑数据时优先考虑 Office 原生 chart。
- 需要高复杂度研究图时走 Python figure 路线，但字体、标题和图下注仍然受同一套文档规范约束。

6. **强制做 QA**
- 至少检查字体槽位、中英文字体、标题层级、行距、段前段后、表图标题位置、表格字号和图片裁切。
- 没有视觉复核或结构核对的 `.docx` 不算完成。

## 资源路由

### 轻量模式

- 默认先读取 `references/lightweight_mode.md`。
- 这份文档已经包含默认字体组合、标题梯度、段前段后、表题图题表注规则和最小 workspace。
- 只有当轻量模式已经不能覆盖需求时，才升级到精细模式文档。

### 精细模式

**核心文档**
- 需要统一定义对象、版式规范和 references 分层时，读取 `references/principles.md`。
- 需要执行 `docx -> markdown -> docx` 的协作流程、Markdown 语义约定和 workspace 组织时，读取 `references/doc_workflow.md`。
- 需要确定默认字体组合、字号梯度、段前段后、表题图题表注规则时，读取 `references/typography_profiles.md`。
- 需要明确实现层的技术边界、OOXML 字体槽位和失败条件时，读取 `references/technical_support.md`。

**专项文档**
- 需要在 `python-docx`、Pandoc、OOXML patch 等构建路线之间做选择时，读取 `references/build_routes.md`。
- 需要接 Office 原生图表时，读取 `references/office_chart_support.md`。
- 需要接 Python 绘图资产时，读取 `references/python_figure_support.md`。
- 需要执行交付前质量 gate 时，读取 `references/quality_gates.md`。
- 需要参考一个已落地的宿主工作区实践时，读取 `references/local_pipeline_case_study.md`。

## 质量标准

- 正文默认必须满足 `中文宋体 + 英文 Times New Roman + 小四 12pt + 1.5 倍行距 + 段前段后 0.5 行`。
- 标题字号必须随层级单调递减，不能出现二级标题比一级标题更大。
- 表格正文默认使用 `五号 10.5pt`，确有密度压力时才降到 `小五 9pt`。
- 表题必须在表上方，图题必须在图下方，表注必须在表下方。
- 没有显式设置 `ascii/hAnsi/eastAsia/cs` 字体槽位的构建结果，不应被当作“格式已锁定”。

## 典型宿主命令

如果宿主工作区已经具备类似 `doc_pipeline.py` 的实现，常见命令会是：

```bash
python scripts/doc_pipeline.py docx-to-md
python scripts/doc_pipeline.py md-to-docx
python scripts/doc_pipeline.py rebuild-all
```

## 额外说明

- 这个 skill 当前把核心价值放在 **文档体系、版式规范和路线选择** 上，不假装某一个固定脚本已经覆盖所有 Word 特性。
- 如果宿主脚本没有显式支持字体 profile、caption 语义或 Office 原生图表，不应静默宣称“已经支持”，而应先暴露能力边界。
