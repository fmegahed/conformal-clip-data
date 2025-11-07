#!/usr/bin/env python
"""
Lightweight local verification for the conformal-clip-data package.

What it checks:
- Imports succeed and reports version + install path
- Dataset root and class subdirectories exist
- Each class (nominal/local/global) contains at least 1 .jpg image
- Optionally, if Pillow is installed, opens one image and prints its size

Exit code is non-zero if any required check fails.
"""
from __future__ import annotations

from pathlib import Path
import sys
import traceback


def _fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    sys.exit(1)


def main() -> int:
    print("Python:", sys.version.replace("\n", " "))
    print("Executable:", sys.executable)

    # Import package and basic metadata
    try:
        import conformal_clip_data as c  # type: ignore
    except Exception as e:
        traceback.print_exc()
        _fail("Failed to import conformal_clip_data. Is it installed in this interpreter?")

    print("Package version:", getattr(c, "__version__", "<unknown>"))
    print("Package file:", getattr(c, "__file__", "<unknown>"))

    # Resolve dataset paths
    try:
        root = c.textile_simulated_root()
        nominal = c.nominal_dir()
        local = c.local_dir()
        global_ = c.global_dir()
    except Exception:
        traceback.print_exc()
        _fail("Failed to resolve dataset paths via helper functions.")

    print("Dataset root:", root)

    # Validate paths
    if not Path(root).exists():
        _fail(f"Dataset root does not exist: {root}")

    for name, d in ("nominal", nominal), ("local", local), ("global", global_):
        if not d.exists() or not d.is_dir():
            _fail(f"Missing or not a directory: {name} -> {d}")

    # Count images
    def count_imgs(p: Path) -> int:
        return len(list(p.glob("*.jpg")))

    n_nom = count_imgs(nominal)
    n_loc = count_imgs(local)
    n_glo = count_imgs(global_)

    print(f"Counts -> nominal: {n_nom}, local: {n_loc}, global: {n_glo}")
    if n_nom < 1 or n_loc < 1 or n_glo < 1:
        _fail("One or more classes have zero images; package data may be missing.")

    # Print a few sample filenames
    def samples(p: Path, k: int = 3) -> list[str]:
        return [f.name for f in list(p.glob("*.jpg"))[:k]]

    print("Samples:", {
        "nominal": samples(nominal),
        "local": samples(local),
        "global": samples(global_),
    })

    # Optional Pillow check
    try:
        from PIL import Image  # type: ignore

        sample = next((f for f in nominal.glob("*.jpg")), None)
        if sample:
            with Image.open(sample) as im:
                print("Pillow check -> sample:", sample.name, "size:", im.size, "mode:", im.mode)
        else:
            print("Pillow check skipped: no sample found in nominal.")
    except Exception as e:
        print("Pillow not installed or failed to open image (this is optional).")

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

