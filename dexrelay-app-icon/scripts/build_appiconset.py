#!/usr/bin/env python3
"""Build an Xcode AppIcon.appiconset from a master 1024x1024 PNG."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


ICON_SPECS = [
    {"idiom": "iphone", "size": "20x20", "scale": "2x", "pixels": 40},
    {"idiom": "iphone", "size": "20x20", "scale": "3x", "pixels": 60},
    {"idiom": "iphone", "size": "29x29", "scale": "2x", "pixels": 58},
    {"idiom": "iphone", "size": "29x29", "scale": "3x", "pixels": 87},
    {"idiom": "iphone", "size": "40x40", "scale": "2x", "pixels": 80},
    {"idiom": "iphone", "size": "40x40", "scale": "3x", "pixels": 120},
    {"idiom": "iphone", "size": "60x60", "scale": "2x", "pixels": 120},
    {"idiom": "iphone", "size": "60x60", "scale": "3x", "pixels": 180},
    {"idiom": "ipad", "size": "20x20", "scale": "1x", "pixels": 20},
    {"idiom": "ipad", "size": "20x20", "scale": "2x", "pixels": 40},
    {"idiom": "ipad", "size": "29x29", "scale": "1x", "pixels": 29},
    {"idiom": "ipad", "size": "29x29", "scale": "2x", "pixels": 58},
    {"idiom": "ipad", "size": "40x40", "scale": "1x", "pixels": 40},
    {"idiom": "ipad", "size": "40x40", "scale": "2x", "pixels": 80},
    {"idiom": "ipad", "size": "76x76", "scale": "1x", "pixels": 76},
    {"idiom": "ipad", "size": "76x76", "scale": "2x", "pixels": 152},
    {"idiom": "ipad", "size": "83.5x83.5", "scale": "2x", "pixels": 167},
    {"idiom": "ios-marketing", "size": "1024x1024", "scale": "1x", "pixels": 1024},
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an Xcode AppIcon.appiconset from one master PNG."
    )
    parser.add_argument("source", help="Path to the master 1024x1024 PNG.")
    parser.add_argument(
        "output",
        help="Output directory for the generated AppIcon.appiconset.",
    )
    parser.add_argument(
        "--prefix",
        default="icon",
        help="Filename prefix for generated PNGs. Default: icon",
    )
    return parser.parse_args()


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stderr or result.stdout)
        raise SystemExit(result.returncode)


def ensure_source(source: Path) -> None:
    if not source.is_file():
        raise SystemExit(f"Source PNG not found: {source}")
    if source.suffix.lower() != ".png":
        raise SystemExit("Source file must be a PNG.")


def prepare_output(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for child in output.iterdir():
        if child.is_file():
            child.unlink()
        elif child.is_dir():
            shutil.rmtree(child)


def resize_png(source: Path, destination: Path, pixels: int) -> None:
    run(
        [
            "sips",
            "-s",
            "format",
            "png",
            "-z",
            str(pixels),
            str(pixels),
            str(source),
            "--out",
            str(destination),
        ]
    )


def build_contents(prefix: str) -> dict:
    images = []
    for spec in ICON_SPECS:
        pixels = spec["pixels"]
        filename = f"{prefix}-{pixels}.png"
        images.append(
            {
                "idiom": spec["idiom"],
                "size": spec["size"],
                "scale": spec["scale"],
                "filename": filename,
            }
        )
    return {"images": images, "info": {"version": 1, "author": "xcode"}}


def main() -> None:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    ensure_source(source)
    prepare_output(output)

    for spec in ICON_SPECS:
        pixels = spec["pixels"]
        destination = output / f"{args.prefix}-{pixels}.png"
        resize_png(source, destination, pixels)

    contents = build_contents(args.prefix)
    (output / "Contents.json").write_text(json.dumps(contents, indent=2) + "\n")

    print(f"Generated {len(ICON_SPECS)} icons in {output}")


if __name__ == "__main__":
    main()
