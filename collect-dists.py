#!/usr/bin/env python3

import argparse
from pathlib import Path
import shutil


def store_package(
    package_path: Path,
    package_storage: Path,
):
    """
    Collect package files and store in storage path
    """

    # Create dir in package storage
    target_path = package_storage / package_path.name
    target_path.mkdir(exist_ok=True, parents=True)

    # Copy files
    dist_dir = package_path / "dist"
    for file in dist_dir.iterdir():
        shutil.copy(file, target_path / file.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("package_path", help="Path to package")
    parser.add_argument("package_storage", help="Path to package storage")
    args = parser.parse_args()
    package_path = Path(args.package_path)
    package_storage = Path(args.package_storage)
    store_package(package_path, package_storage)
