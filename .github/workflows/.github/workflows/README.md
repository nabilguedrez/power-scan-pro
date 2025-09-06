# PowerScan Pro

نسخة احترافية من التطبيق مع اسم وأيقونة مخصصة.

## 🚀 البناء التلقائي (GitHub Releases)
- عند كل push، GitHub يبني APK جديد ويضيفه في قسم Releases.

### التحميل
1. افتح المستودع على GitHub.
2. اذهب إلى تبويب **Releases**.
3. حمل آخر ملف APK.

---

## 📌 التخصيص
- اسم التطبيق: **PowerScan Pro**
- Package name: **com.powerscan.app.powerscanpro**
- أيقونة: `icon.png` (يمكنك استبدالها بأيقونة خاصة بك).

---

## 📌 البناء المحلي (اختياري)

### على ويندوز (EXE)
```bash
pip install kivy pyinstaller
pyinstaller --onefile main.py
```

### على لينكس (APK)
```bash
pip install buildozer
buildozer init
buildozer -v android debug
```
