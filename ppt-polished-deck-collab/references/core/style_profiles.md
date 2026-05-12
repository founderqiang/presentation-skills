# Style Profiles

**这份文档的定位。** 本文定义 `ppt-polished-deck-collab` 的任务分流和风格 profile。profile 用来帮助 agent 做路线选择，不是给用户展示的内部字段。与用户沟通时应使用通俗问题。

## 通俗确认

**优先问人的问题。**
- 这份 PPT 是发出去让别人自己看懂，还是主要配合你现场讲？
- 有没有必须沿用的模板、旧 PPT 或品牌素材？
- 更像清晰商业汇报、技术说明、研究材料，还是更有设计感的发布会 / 分享型演示？
- 后续是否还会频繁改数据、改图表或改结构？

**内部再映射到 profile。** 用户不需要听到 `source_context`、`delivery_context`、`visual_profile` 这些字段名。

## Source Context

**`template_locked`。** 用户提供了必须沿用的正式模板。必须先做 template audit，再围绕模板页族、母版元素和真实字号系统规划页面。

**`template_guided`。** 用户给了参考 PPT 或风格样张，但不要求继承母版结构。可以提取视觉纪律，再走 branded rebuild 或空白页直生。

**`content_migration`。** 用户给的是旧 PPT 或材料包，主要任务是迁移内容、重写叙事或重新设计页面。先分清内容事实和旧设计遗留。

**`brand_assets_only`。** 用户只给了 logo、颜色、字体或品牌手册。先锁品牌边界，再选择沟通任务和视觉路线。

**`no_template`。** 没有模板、品牌素材或旧 PPT。使用 skill 默认合同，包括中文 typography / table policy。

## Delivery Context

**`self-contained_reading_deck`。** 无人讲解也能流传。页面需要完整判断、上下文、图表注释、单位、来源、风险边界和必要解释文本。

**`speaker-led_stage_deck`。** 有人讲的演示材料。页面应低密度、强节奏、强记忆点，正文少，视觉锚点和翻页呼吸更重要。

**`hybrid_review_deck`。** 现场讲完后还会被转发。关键页可以偏演示，证据页、附录页和复杂说明页需要更自解释。

**`reference_or_appendix_deck`。** 查阅型材料。允许高密度表格、定义、样本、假设和方法说明，视觉目标是检索稳定。

## Communication Profile

**`business_report`。** 商业汇报、管理层同步、经营复盘和客户汇报。典型页面包括管理层摘要、进展 / 风险 / next step、KPI 图表、对比矩阵、路线图和附录表格。

**`technical_explainer`。** 技术方案、架构说明、Agent / dataflow / system design 解释。典型页面包括 layered architecture、process flow、dependency map、机制图和技术取舍矩阵。

**`research_review`。** 研究汇报、财报点评、实验结果和方法说明。典型页面包括 chart spotlight、方法页、误差分析、来源注、限制说明和附录。

**`keynote_story`。** 发布会、分享、私享会和设计感叙事。典型页面包括 hero statement、big number、quote、image hero、duo compare 和章节幕封。

## Visual Profile

**`corporate_clear`。** 商业汇报默认风格。允许多形状、多图表、多注释和矩阵，视觉目标是清晰、稳定、克制。避免把页面做成海报。

**`editorial_ink`。** 电子杂志 / 电子墨水方向。适合观点表达、人文叙事、行业观察和带图片的讲述型材料。重点是图文叙事、hero / non-hero 节奏、照片作为证据和情绪锚点、克制色彩、引用页和大字报页。

**`swiss_modernist`。** Swiss Style 方向。适合科技产品、方法论、数据大字报、工程和设计领域分享。重点是 12/16 列网格、单一 accent、直角、发丝线、低字重、版式登记、图片槽位和标题不居中。

**`product_launch`。** 产品发布、路演和 demo day。它通常混合强 hero 页、产品图、路线图、证据页和商业汇报式数据页。

## Density Profile

**`dense_reference`。** 自解释材料、附录、研报和查阅页。要求完整标题、注释、来源、单位和上下文。

**`balanced_brief`。** 大多数商业汇报和技术说明。它在清晰结论和足够证据之间平衡。

**`low_density_stage`。** 有人讲的舞台演示。减少正文，把信息压力转给讲者、讲稿或备注。

## Editability Profile

**`fully_editable`。** 优先使用原生文本、形状、表格、Office chart 和真绑定 connector。

**`chart_editable`。** 对图表数据保持可编辑，允许部分视觉资产图片化。

**`mixed_assets`。** 允许 Python figure、图片化研究图、生成配图和截图再设计，但关键文字和业务对象仍尽量可编辑。

**`snapshot_allowed`。** 只在明确需要视觉冲击且后续编辑要求低时使用，不能作为默认路线。

## 常见组合

| 需求 | 推荐组合 |
| --- | --- |
| 发给管理层自己看 | `self-contained_reading_deck + business_report + corporate_clear + dense_reference + fully_editable` |
| 会议现场汇报，之后会转发 | `hybrid_review_deck + business_report + corporate_clear + balanced_brief + chart_editable` |
| 技术方案说明 | `hybrid_review_deck + technical_explainer + corporate_clear + balanced_brief + fully_editable` |
| 研究 / 财报点评 | `self-contained_reading_deck + research_review + corporate_clear + dense_reference + mixed_assets` |
| 发布会 / 分享 | `speaker-led_stage_deck + keynote_story + editorial_ink/product_launch + low_density_stage + mixed_assets` |
| 瑞士风方法论演示 | `speaker-led_stage_deck + keynote_story + swiss_modernist + low_density_stage + mixed_assets` |

## 设计底线

**Profile 不能覆盖正确性。** 数据、来源、单位、图表可读性、表格语义和 connector 真实性仍然优先。

**风格强不等于信息弱。** 强设计感 deck 也可以有证据页，但证据页应使用对应的低密度表达或进入附录。

**商业汇报不等于难看。** 商业汇报的审美目标是稳定、清楚、可追责、可复用。

**模板优先级最高。** 只要存在 `template_locked`，先继承模板系统，再在模板页族内映射 profile。
