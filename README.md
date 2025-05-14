# 📌 Gramintel

> A clean, fast Instagram metadata extractor built by [upliftedl](https://github.com/upliftedl)

**Gramintel** is a command-line OSINT tool to extract public and obfuscated metadata (emails, phones, links, bios, follower stats, etc.) from Instagram profiles using a valid session ID.

---

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/github/license/upliftedl/gramintel-)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)

---

## ⚙️ Prerequisites

- Python 3.8+
- pip (Python package manager)
- Instagram session ID (from browser cookies)

---

## 📦 Installation

```bash
git clone https://github.com/upliftedl/gramintel-.git
cd gramintel-
pip install .
```

---

## 🔐 How to Get Your Instagram Session ID

1. Login at [instagram.com](https://instagram.com)
2. Open DevTools → Application → Cookies → `sessionid`
3. Copy the full value (do not encode)

---

## 💻 Usage

```bash
gramintel -u <username> -s <session_id>
gramintel -i <user_id> -s <session_id>
```

Example:
```bash
gramintel -u natgeo -s 1234567890:abcDEFghiJKLmnopQR
```

---

## 🧪 Output

- ✅ Simple terminal display
- ✅ Mobile API headers to bypass detection
- ✅ No JSON clutter

---

## 🚨 Legal Disclaimer

This tool is intended for **educational and lawful OSINT** purposes only.  
Usage against Instagram’s Terms of Service is solely your responsibility.

---

## 📄 License

Licensed under the [GNU GPLv3](LICENSE)

---

> 📦 Originally based on [Toutatis](https://github.com/megadose/toutatis) by @megadose, licensed under GPLv3.

