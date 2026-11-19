#!/bin/bash
# deploy.sh — کامیت و پوش همه‌ی تغییرات به گیت‌هاب
# استفاده: bash .build/deploy.sh "پیام کامیت"
set -e
cd /home/user
MSG="${1:-به‌روزرسانی پروژه}"
T="${GITHUB_TOKEN:?GITHUB_TOKEN تنظیم نشده}"
git remote set-url origin "https://x-access-token:$T@github.com/sinaaminzadeh-byte/remotion-fa.git" 2>/dev/null || \
  git remote add origin "https://x-access-token:$T@github.com/sinaaminzadeh-byte/remotion-fa.git"
git add -A
git -c user.name="Sina Aminzadeh" -c user.email="sinaaminzadeh@gmail.com" commit -q -m "$MSG" || echo "(تغییری برای کامیت نبود)"
git push -q origin main
echo "✅ پوش شد: $MSG"
