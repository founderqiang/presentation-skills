#!/usr/bin/env python3
"""从 timeline.json 生成 SRT 字幕文件。

定位：
- timeline 是主键数据：segments 内含 start/end/text。
- 该脚本用于“先录无字幕母带，再后期烧录字幕”的路线。

输入：
- timeline.json（要求包含 segments，每段有 start_sec/end_sec/text）

输出：
- 标准 .srt（UTF-8）
"""

from __future__ import annotations

import argparse
import json
import unicodedata
from pathlib import Path
from typing import Any, Dict, List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="timeline.json -> SRT")
    parser.add_argument("--timeline", required=True, help="timeline.json 路径")
    parser.add_argument("--output", required=True, help="输出 .srt 路径")
    parser.add_argument(
        "--auto-wrap",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="是否启用自适应换行（默认 false）",
    )
    parser.add_argument(
        "--wrap-max-units",
        type=int,
        default=42,
        help="每行最大视觉宽度单位（CJK 字符按 2，ASCII 按 1）",
    )
    return parser.parse_args()


def to_srt_time(seconds: float) -> str:
    if seconds < 0:
        raise ValueError("时间不能为负")
    total_ms = int(round(seconds * 1000))
    hh = total_ms // 3_600_000
    total_ms %= 3_600_000
    mm = total_ms // 60_000
    total_ms %= 60_000
    ss = total_ms // 1000
    ms = total_ms % 1000
    return f"{hh:02d}:{mm:02d}:{ss:02d},{ms:03d}"


def normalize_text(value: Any) -> str:
    if not isinstance(value, str):
        raise ValueError("segment.text 必须是字符串")
    text = value.strip()
    if not text:
        raise ValueError("segment.text 不能为空")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def char_display_units(ch: str) -> int:
    if not ch:
        return 0
    if unicodedata.combining(ch):
        return 0
    if ch.isspace():
        return 1
    eaw = unicodedata.east_asian_width(ch)
    if eaw in {"F", "W", "A"}:
        return 2
    return 1


def find_last_break_idx(chars: List[str]) -> int:
    break_chars = set("，。！？；：、,.!?;:)]}）】》」』 ")
    for idx in range(len(chars) - 1, -1, -1):
        if chars[idx] in break_chars:
            return idx + 1
    return -1


def wrap_paragraph(paragraph: str, max_units: int) -> List[str]:
    if not paragraph:
        return [paragraph]
    out: List[str] = []
    buf: List[str] = []
    units = 0
    for ch in paragraph:
        buf.append(ch)
        units += char_display_units(ch)
        if units <= max_units:
            continue
        split_idx = find_last_break_idx(buf)
        if split_idx <= 0:
            split_idx = max(1, len(buf) - 1)
        line = "".join(buf[:split_idx]).strip()
        if line:
            out.append(line)
        remain = "".join(buf[split_idx:]).lstrip()
        buf = list(remain)
        units = sum(char_display_units(c) for c in buf)
    tail = "".join(buf).strip()
    if tail:
        out.append(tail)
    return out if out else [paragraph]


def auto_wrap_text(text: str, max_units: int) -> str:
    paragraphs = text.split("\n")
    wrapped: List[str] = []
    for paragraph in paragraphs:
        p = paragraph.strip()
        if not p:
            wrapped.append("")
            continue
        wrapped.extend(wrap_paragraph(p, max_units))
    return "\n".join(wrapped).strip()


def load_timeline(path: Path) -> Dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("timeline 顶层必须是对象")
    segments = payload.get("segments")
    if not isinstance(segments, list) or not segments:
        raise ValueError("timeline.segments 必须是非空数组")
    return payload


def build_entries(
    segments: List[Dict[str, Any]],
    *,
    auto_wrap: bool,
    wrap_max_units: int,
) -> List[str]:
    entries: List[str] = []
    last_end = -1.0
    for i, seg in enumerate(segments, start=1):
        if not isinstance(seg, dict):
            raise ValueError("timeline.segments 元素必须是对象")
        start = float(seg.get("start_sec", 0.0))
        end = float(seg.get("end_sec", 0.0))
        if start < 0 or end <= start:
            raise ValueError(f"segment[{i-1}] 的 start/end 非法")
        if last_end > start + 1e-6:
            raise ValueError(f"segment[{i-1}] 的 start 早于上一段 end")
        text = normalize_text(seg.get("text", ""))
        if auto_wrap:
            text = auto_wrap_text(text, wrap_max_units)
        entries.append(
            "\n".join(
                [
                    str(i),
                    f"{to_srt_time(start)} --> {to_srt_time(end)}",
                    text,
                    "",
                ]
            )
        )
        last_end = end
    return entries


def main() -> None:
    args = parse_args()
    timeline_path = Path(args.timeline)
    out_path = Path(args.output)

    timeline = load_timeline(timeline_path)
    segments = timeline["segments"]
    if args.wrap_max_units < 8:
        raise ValueError("--wrap-max-units 不能小于 8")
    entries = build_entries(
        segments,
        auto_wrap=bool(args.auto_wrap),
        wrap_max_units=int(args.wrap_max_units),
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(entries).rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"timeline": str(timeline_path), "output": str(out_path), "entries": len(entries)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
