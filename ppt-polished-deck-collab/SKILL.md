---
name: ppt-polished-deck-collab
description: Use when collaborating with humans to produce polished, editable, high-quality PPT decks across business, technical, research, education, product, and operations themes. Supports deck planning, slide archetype selection, diagram/chart/icon asset strategy, preview export, and validation for reusable PowerPoint deliverables.
---

# PPT Polished Deck Collab

## 概览
把“讲清楚任务 + 做出高质量页面 + 交付可编辑 PPT + 给出验证证据”作为同一个任务完成。
默认服务的是 **deck 级任务**，不是单页复杂图，也不是只会套模板。

## 什么时候用

- 用户要做高质量 PPT、演示稿、汇报 deck、路演稿、研究汇报、技术方案 deck、教学或培训材料。
- 用户希望输出是 **可编辑 `pptx`**，而不是截图拼图或不可维护的导出物。
- 任务需要在流程图、架构图、图表页、证据页、管理层摘要页之间切换，并保持整套 deck 的一致性。
- 任务需要 **预览导出、结构校验、视觉复核**，而不是只生成脚本后口头说“应该可以”。

## 默认工作流

按下面顺序执行，避免把 PPT 任务退化成“边画边想”。

1. **先锁 deck 任务与工作空间**
- 明确目标读者、使用场景、页面数量级、交付时间、是否有模板/品牌约束。
- 如果用户没有现成 workspace，先按 `references/deck_workflow.md` 建立 `brief.md`、`deck_narrative.md`、`assets/`、`data/`、`build/`、`validation/`、`final/` 结构。

2. **先收敛 narrative，再做页面**
- 先写 `brief.md`，再在 `deck_narrative.md` 里收敛整套叙事、每页 intent 与页面想法，然后由脚本派生 `slide_specs.yaml`。
- 每页先定义 `reader question`、`page task`、`reading mode`、`archetype`、`asset mode`、`validation mode`。
- 页面原型、图表 / diagram / 语言选择先看 `references/design_support.md`。
- 页面级视觉底线与网格规则再看 `references/slide_design_system.md`。

3. **再选技术路线**
- 先看 `references/technical_support.md`，明确这页对应的实现模块和验证要求。
- 再看 `references/build_routes.md`，确认当前环境能走哪条具体 backend 路线。
- 不要把某一条路线写死为唯一正解。模板改写、空白页直生、品牌重建、PowerPoint 导出、LibreOffice 导出都可以是有效选项。

4. **再生成 editable PPT**
- 优先保留文本、形状、图表、connector 的可编辑性。
- 不是所有页面都需要 Mermaid，也不是所有 diagram 页都需要 connector。
- 如果页面属于复杂结构图并且后续要拖动维护，必须使用真正绑定的 connector。

5. **强制做验证与预览**
- 所有 deck 都必须导出逐页预览图。
- diagram 页按需要执行 connector 校验。
- 视觉复核顺序固定为 `fatal -> warning -> preference`。

## 资源路由

**核心文档**
- 需要统一定义 deck、slide spec、validation bundle 和文档分层时，读取 `references/principles.md`。
- 需要建立 workspace、起草 `brief.md` / `deck_narrative.md`、派生 `slide_specs`、执行主流程和确认验证证据时，读取 `references/deck_workflow.md`。
- 需要决定页面该用什么 archetype、图表、diagram、语言模式时，读取 `references/design_support.md`。
- 需要决定某类资产该用什么 SDK、脚本、验证方式时，读取 `references/technical_support.md`。

**专项文档**
- 需要统一标题区、网格、留白、视觉复核底线时，读取 `references/slide_design_system.md`。
- 需要在模板改写、空白页直生、PowerPoint / LibreOffice 预览导出、diagram connector 路线之间做选择时，读取 `references/build_routes.md`。
- 需要做系统架构图、dataflow、dependency map、Mermaid 草稿层和 connector 策略时，读取 `references/diagram_support.md`。
- 需要做原生 PowerPoint chart，并判断何时优先保持 editable chart 时，读取 `references/office_chart_support.md`。
- 需要做高 DPI Python figure、研究图、热力图和排序图时，读取 `references/python_figure_support.md`。
- 只有在页面需要额外节奏增强、导航锚点或主题 icon 资产时，才读取 `references/icon_system.md`。

## 质量标准

- 默认交付物至少包含：`brief.md`、`deck_narrative.md`、派生 `slide_specs.yaml`、可编辑 `pptx`、验证结果、逐页预览图。
- 没有预览图的 deck 不算完成。
- 需要 connector 的页面，没有结构校验结果不算完成。
- 页面风格允许多样，但弱信息、标题层级、网格稳定性和高对比文本是底线。
- 高质量是交付标准，不是题材限制。这个 skill 既可以做商业汇报，也可以做技术、研究、教育、运营等主题。

## 快速命令

```bash
# 1) 检查环境与可用路线
python scripts/check_environment.py

# 2) 导出逐页预览图
python scripts/export_pptx_previews.py \
  --pptx <path/to/deck.pptx> \
  --out-dir <path/to/ppt_preview> \
  --backend auto

# 3) 校验 diagram 页 connector
python scripts/check_pptx_connectors.py \
  --pptx <path/to/deck.pptx> \
  --slide 3 \
  --json-out <path/to/connector_report.json> \
  --min-connectors 1

# 4) 检查 workspace 关键输入是否齐全
python scripts/lint_deck_assets.py \
  --workspace-dir <path/to/deck_workspace>

# 5) 从总叙事文档派生 slide specs
python scripts/derive_slide_specs_from_narrative.py \
  --narrative <path/to/deck_narrative.md> \
  --out-yaml <path/to/build/generated/slide_specs.yaml>

# 6) 检查 diagram / chart / python figure 等模块可用性
python scripts/check_environment.py \
  --json-out <path/to/env_check.json>
```

## 额外说明

- 如果任务是“只做复杂图、重点在 connector 维护”，这个 skill 仍然适用，但应把 diagram module 当成专项路线处理，而不是让整个 deck 都退化成复杂图思维。
- 如果用户给了品牌模板或既有 `pptx`，优先考虑模板改写或 branded rebuild，不要机械重做全部页面。
- 如果环境里没有某个推荐工具，应该显式切换到备选路线并记录，而不是静默降级。
