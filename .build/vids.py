# -*- coding: utf-8 -*-
"""ویدیوهای نمونه‌ی سبک‌ها — رندر واقعی خودمان با Remotion (motion-starter)."""
import base64, json, os

# نگاشت شماره‌ی سبک کاتالوگ → شناسه‌ی کامپوزیشن رندرشده
OWN = {
    1: "BoldKinetic", 6: "GradientGlass", 9: "ClaySoft", 11: "NeoBrutalist",
    12: "Memphis90s", 15: "NeonFuturistic", 16: "PaperCollage", 17: "KraftStudio",
    24: "Voxel3D", 26: "MinimalEditorial", 27: "SwissGrid", 28: "FlatCorporate",
    29: "InfographicData",
}


def _b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def has(n):
    return int(n) in OWN


def clip(n):
    return "data:video/mp4;base64," + _b64(f".build/r13/{OWN[int(n)]}.mp4")


def poster(n):
    return "data:image/jpeg;base64," + _b64(f".build/r13/{OWN[int(n)]}.jpg")


def source(n):
    """فایل رندر کامل و عمومی برای دانلود."""
    return f"previews/{OWN[int(n)]}.mp4"
