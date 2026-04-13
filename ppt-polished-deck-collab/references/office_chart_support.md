# Office Chart Support

**这份文档的定位。** 本文定义 `ppt-polished-deck-collab` 中原生 Office chart 模块的使用边界、实现方式和验证要求。它服务“图表需要继续编辑”的页面，而不是所有图表页。

## 目录

- 什么时候先读它
- 什么时候优先用原生 Office chart
- 当前可用实现
- 图表选择表
- 标题与注释语言
- 验证要求

## 什么时候先读它

**当页面核心是趋势、比较、构成、排名，而且会后高概率继续改数时，先读这份文档。** 它回答“哪些图表应当保持原生可编辑，以及当前 skill 怎么稳定生成它们”。

## 什么时候优先用原生 Office chart

**数字会继续改时，优先原生 chart。** 管理层汇报、周报、经营复盘、项目节奏图这类页面，后续常会改 series、换类目、调标签，因此应尽量保持为 PowerPoint 原生图表。

**证据结构简单而稳定时，优先原生 chart。** 条形图、柱状图、折线图、堆叠图、简单组合图，只要 Office chart 足够表达，就不必先走 Python figure。

**重点是 editable，不是炫技。** 一张可继续编辑的普通条形图，通常优于一张看起来更花但会后没法改数的图片图表。

## 当前可用实现

**当前 skill 已经有可复用 helper。** `scripts/ppt_asset_helpers.py` 内的 `add_native_chart_card()` 可以直接把原生 chart 放进一个标准 panel 卡片里。

**当前依赖只需要 `python-pptx`。** 这意味着 native chart 在本 skill 中已经是 `available`，不再只是规划状态。

**当前 helper 适合这些图表。**
- `BAR_CLUSTERED`
- `COLUMN_CLUSTERED`
- `LINE`
- `BAR_STACKED`
- 其他 `python-pptx` 支持且不依赖特殊格式设置的标准 chart type

## 图表选择表

| 证据形状 | 推荐原生 chart | 为什么 |
| --- | --- | --- |
| 类别比较 | 条形图 / 柱状图 | 最稳、最易读、最易改数 |
| 时间趋势 | 折线图 | 管理层和运营页最常见 |
| 构成变化 | 堆叠柱 / 100% 堆叠 | Office 原生足够表达 |
| 小规模 before / after | 双 series 对比图 | editable 且注释简单 |
| 单页 KPI 对比 | 横向条形图 | 与结论卡片搭配自然 |

**这些场景不应优先走原生 chart。**
- 高密度热力图
- 密集散点和复杂分布图
- 排序很多、标注很密的研究图

这些更适合走 `python-figure-image` 路线。

## 标题与注释语言

**标题应先给发现，再让图表支撑。** 推荐写法如：
- “Coverage gap 集中在执行后期”
- “方案 B 在成本与速度之间最平衡”
- “Q3 的增长主要来自两条产品线”

**注释应只写图上最关键的两三处。** 不要把图例、标签和正文讲成三遍同样的话。

## 验证要求

**当前自动验证重点是 preview，不是 XML 级 chart 解析。** 原生 chart 页至少要有逐页预览图，并人工确认 chart 仍然可选中、可编辑、图例和标签没有漂移。

**推荐验证顺序。**
- 导出逐页预览图
- 在 PowerPoint 中点选 chart，确认不是图片
- 抽检一页修改数据或系列颜色，确认图仍可编辑

**当前相关脚本。**
- `scripts/ppt_asset_helpers.py`
- `scripts/export_pptx_previews.py`

**典型 build 方式。**

```python
from pptx.enum.chart import XL_CHART_TYPE
from scripts.ppt_asset_helpers import add_native_chart_card

add_native_chart_card(
    slide=slide,
    title="Weekly Coverage by Phase",
    left=0.7,
    top=1.3,
    width=6.2,
    height=3.1,
    accent_rgb=(37, 99, 235),
    categories=["Phase 1", "Phase 2", "Phase 3"],
    series_list=[("Coverage", [92, 88, 73])],
    chart_type=XL_CHART_TYPE.BAR_CLUSTERED,
)
```
