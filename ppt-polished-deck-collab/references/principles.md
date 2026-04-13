# Principles

**这份文档的定位。** 本文定义 `ppt-polished-deck-collab` 的核心业务逻辑与开发逻辑，并给出 references 的分层地图，让后续 workflow、page design、build route 和脚本都共享同一套对象定义。

## 核心对象

**`deck` 是最小业务对象。** `deck` 是围绕单一沟通任务组织起来的一组页面。它的核心问题是“这套材料要让谁在什么场景下理解、判断、行动”，不是“我能不能先画一张图”。

**`slide_spec` 是最小页面对象。** 每一页都应先定义 `reader_question`、`page_task`、`reading_mode`、`archetype`、`asset_mode`、`validation_mode`。页面的版式与技术路线都应从这些字段推出，而不是在脚本里隐式决定。

**`validation_bundle` 是最小验收对象。** 完整交付至少包含可编辑 `pptx`、逐页预览图、结构校验结果与必要的人工复核记录。没有验证证据的 deck 不算完成。

**`workspace` 是最小协作对象。** 人类与 Codex 的长期协作应围绕稳定 workspace 展开，而不是每次生成一棵新的 run 目录。workspace 的职责是让 brief、plan、assets、build、validation 和 final 始终可追溯。

## 文档分层

**核心文档现在分成四份。** 新 skill 的默认核心文档应当是：
- `principles.md`
- `deck_workflow.md`
- `technical_support.md`
- `design_support.md`

**专项文档按需读取。** 只有在需要看更细的实现路线或视觉细则时，才读取：
- `build_routes.md`
- `diagram_support.md`
- `office_chart_support.md`
- `python_figure_support.md`
- `slide_design_system.md`
- `icon_system.md`

**这样设计的原因很直接。** `technical_support` 和 `design_support` 是 skill 级主分层，分别回答“怎么实现”和“怎么表达”；专项文档再回答更细的 backend、视觉网格和 icon 细则。

## 顶层原则

**Deck-first。** 默认从整套 deck 的任务定义出发，再决定哪些页面需要 diagram、chart、icon、table 或纯文字结构。不要让单页复杂图反向支配整套 deck 的组织方式。

**Workspace-first。** 默认先建立稳定工作空间，再往里补页面、资产与脚本。不要把计划、源资产、中间产物和最终交付混在同一层目录。

**High-quality 是标准，不是题材。** 这个 skill 服务的是高质量 PPT 交付标准，不限制题材。商业、技术、研究、教育、产品、运营等主题都应适配同一套质量体系。

**技术支持与设计支持显式分层。** `design_support` 负责决定页面如何被读懂、该用什么图表与语言，`technical_support` 负责决定这些设计如何以可编辑、可验证的方式落地。

**Editable-by-default。** 默认优先交付可编辑对象，包括文本、形状、图表和必要的 connector。截图、整页位图和不可维护导出物只能是明确受限场景下的例外。

**Validation-by-default。** 预览导出不是可选锦上添花，而是默认要求。diagram 页的结构校验、chart 页的比例与可编辑性检查、模板页的视觉回归都属于基本交付义务。

**Correct-failure。** 缺少依赖、环境不满足、模板结构不稳定、页数不匹配、connector 非真绑定时，应明确失败并暴露原因。禁止静默降级和“看起来差不多”的自我安慰。

## 页面层原则

**先定义页面任务，再谈视觉。** 一页首先要回答它是 `说服`、`解释`、`比较`、`证据` 还是 `存档`。只有任务清楚，阅读方式、信息密度和页面原型才有稳定依据。

**一页只选一个主原型。** 一页可以混合图、数、文，但不应同时承担两个主 archetype。`decision logic` 页不应偷偷兼做 dashboard，`war-room board` 也不应再塞成 appendix。

**原型比模板更重要。** archetype 是稳定的页面语法，模板只是某个视觉实例。skill 应优先沉淀 archetype，而不是堆积大量长得不一样但逻辑重复的样板页。

## 资产层原则

**资产按类型平级组织。** diagram、chart、icon、image、table 都是合法源资产。不要再让 Mermaid 冒充所有页面的默认起点。

**icon 是可选增强资产。** icon 的职责是给 section、卡片和弱语义提示增加节奏感，不是每套 deck 的必需输入，也不是信息主载体。

**图表与 diagram 都应先归类再实现。** `office-chart-native`、`python-figure-image`、`diagram-connector`、`diagram-visual` 这些类型必须在 `slide_spec.asset_mode` 中显式表达，不能在脚本里临时决定。

**技术路线按场景选择。** 空白页直生、模板改写、品牌重建、PowerPoint 预览导出、LibreOffice 预览导出都可以成立。skill 应给出选择标准，而不是写死唯一通道。

**图页是专项能力，不是默认入口。** 复杂 diagram 是 skill 的强能力之一，但它只是 deck 的某一页类型。不要让所有任务都退化成复杂图任务。

## 文档层原则

**`SKILL.md` 只保留核心工作流。** 触发条件、默认工作流、资源路由和最小命令留在 `SKILL.md`。详细规范与路线说明进入 `references/`。

**`references/` 承载真正的 requirements 与方法论。** requirements、技术路线、视觉系统、页面原型、模板和环境基线都应进入 `references/`，并由 `SKILL.md` 明确指向。

**规范文档必须能单独工作。** 一个不了解 `demo_draft` 的 agent，只看新 skill 的 `references/`，也应能理解 deck 如何规划、如何生成、如何验证。

## 交付底线

**最低交付物。** 一次完整 deck 任务至少要有 `deck_plan`、可编辑 `pptx`、逐页预览图和验证结果。

**最低可读性。** 弱信息不能抢标题区，正文与背景必须高对比，同类对象必须挂到公共网格，一页必须存在清晰的第一视觉中心。

**最低可维护性。** 后续需要迭代的节点、图表、文本和品牌元素应尽量保持可编辑。对于 connector 页面，必须能回答“拖动后是否仍然绑定”。
