# Gramintel

**Gramintel** is a CLI tool by [upliftedl](https://github.com/abhishekjohns) for extracting publicly accessible and obfuscated metadata from Instagram accounts using either a username or an ID.

## Features

- ✅ Query by **username** or **Instagram ID**
- ✅ Export results to **JSON file** (`--json`)
- ✅ Print **pretty JSON** in terminal (`--pretty`)
- ✅ Colored terminal output

## Installation

```bash
git clone https://github.com/abhishekjohns/gramintel.git
cd gramintel
python3 setup.py install
```

## Usage

```bash
gramintel -u username -s YOUR_SESSION_ID
gramintel -i instagram_id -s YOUR_SESSION_ID --json result.json
gramintel -u username -s YOUR_SESSION_ID --pretty
```

## License

Licensed under the GPLv3.