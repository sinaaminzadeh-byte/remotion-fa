# -*- coding: utf-8 -*-
"""ویدیوهای نمونه‌ی هر سبک — کلیپ واقعی + پوستر، جاسازی‌شده به‌صورت data-URI."""
import base64, json, os
META = json.load(open(".build/vids/meta.json"))

def _b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def clip(n):
    return "data:video/mp4;base64," + _b64(f".build/vid/clips/c{n}.mp4")

def poster(n):
    return "data:image/jpeg;base64," + _b64(f".build/vids/p{n}.jpg")

def info(n):
    return META[str(n)]

def kb(n):
    return round(os.path.getsize(f".build/vid/clips/c{n}.mp4") / 1024)
