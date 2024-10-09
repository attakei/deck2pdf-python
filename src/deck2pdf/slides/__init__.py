"""Slide operator package."""

import importlib


def resolve_slide(name: str):
    return importlib.import_module(f"{__name__}.{name}")
