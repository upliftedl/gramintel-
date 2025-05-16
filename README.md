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
## 📁 Project Structure: Gramintel

```
gramintel/
├── gramintel/                 
│   ├── __init__.py            # Initializer
│   └── core.py                # CLI & API
├── setup.py                   # Setup script for installation
├── README.md                  
├── LICENSE                    # GPLv3 license
├── .gitignore                 
├── SECURITY.md               
├── CODE_OF_CONDUCT.md        
```


## 🔐 How to Get Your Instagram Session ID

1. Login at [instagram.com](https://instagram.com)
2. Open DevTools → Application → Cookies → `sessionid`
3. Copy the full value (do not encode)

---

## 💻 Usage

```bash
gramintel -u <username> -s <session_id>
```

Example:
```bash
gramintel -u natgeo -s 1234567890:abcDEFghiJKLmnopQR
```

---

## 📄 Example Output

```
Informations about      : xxxusernamexxx
Full Name               : xxxusernamesxx          | userID : 123456789
Verified                : False                   | Is business Account : False
Is private Account      : False
Follower                : xxx                     | Following : xxx
Number of posts         : x
Number of tag in posts  : x
External url            : http://example.com
IGTV posts              : x
Biography               : example biography
Public Email            : public@example.com
Public Phone            : +00 0 00 00 00 00
Obfuscated email        : me********s@examplemail.com
Obfuscated phone        : +00 0xx xxx xx 00
------------------------
Profile Picture         : https://scontent-X-X.cdninstagram.com/
```
---

## 🚨 Legal Disclaimer

This tool is intended for **educational and lawful OSINT** purposes only.  
Usage against Instagram’s Terms of Service is solely your responsibility.

---

## 📄 License

Licensed under the [GNU GPLv3](LICENSE)

---
## 👤 Author

 
[**upliftedl** ](https://github.com/upliftedl)

```
Originally based on Toutatis by @megadose, licensed under GPLv3.
```
