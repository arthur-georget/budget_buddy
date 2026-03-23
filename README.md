# Budget Buddy
### Bank account management app
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/release/python-3120/)

```
,--------------------------------------------------------------------------.
| OV"|OOOOOOOO> U N I T E D  S T A T E S   OF  A M E R I C A <OOOOOOOV"|OO |
| OO |OOOOOOOOOOOOmmmmOOOOOOmmmmmmmmmmmmmmmmmmOOOOOOOmmmmOOOOOOOOOOOOO |OO |
| OO_|OO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@OO_|OO |
| OOOOO@6@@@@@@@@@@@@@@@@@@@@@'"           "`@@@@@@@@@@F@81497973A@@OOOOOO |
| OO@@@@@@@@@@@@@@@@@@@@@@@@`  ,,:@@@@@@*.    `@@@@@@@@@@@@@@@@@@@@@@@@@OO |
| OOO@@@@@' _`@@@@@@@@@@@@@`  W@@@@@@@@@@@;    `@@@@@@@@@@@@@@@@6@@@@@@OOO |
| OOO@@@@' |_ `@@@@@@@@@@@'  (@@@@@;--;;--@'    `@@@@@@@@@@@@@@@@@@@@@@OOO |
| OOO@@@@. |  .@@@@@@@@@@@   (@@@@  @  \@ ;@     @@@@@@@@@@@@@@@@@@@@@@OOO |
| OOO@@@@@,  ,@@@@@@@@@@@@   (@@@@     _\ }@     @@@@@@@@'==`@@@@@@@@@@OOO |
| OOO@@@@@@@@@@@@@@@@@@@@@.    \_@;;; __ ;;     .@@@@@@@@./\,@@@@@@@@@@OOO |
| OO@@@@@F@81497973A@@@@@@@.   ,;;\_ .__/;,    .@@@@@@@@@@@@@@@@@@@@@@@@OO |
| OOOOOO@@@@@@@@@@@@@@@@@@@@@. ,;;;\  , /;;;; .@@@@@@@@@@@@@@@@@@@@@OOOOOO |
| OV"|OO@@@6@@@@@@@@@@@@@@@@@@@. Washington .@@@@@@@@@@@@@@@@@@@6@@@OV"IOO |
| OO |OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO IOO |
| OO_|OOOOOOOOOOOOOO>   O  N  E     D  O  L  L  A  R   <OOOOOOOOOOOOOO_IOO |
`--------------------------------------------------------------------------'
                                                    -Phoenix-             
```

**(La Plateforme_ team software project)**

Budget buddy is a customtkinter app to safely manage money between differents accounts.


## Setup

## Dependencies
- **python3**
- **pip**
    - **customtkinter**
    - **CTKMessagebox**
    - **bcrypt**
    - **mysql-connector-python**

# Install

## Commands

Clone the repository locally
```bash
git clone https://github.com/arthur-georget/budget_buddy
```

If you are familiar with python virtual environments you can create one and avoid global modules installation.
```bash
python -m venv .venv
```

You then need to activate the environments with the following commands
**Windows Powershell**
```bash
.venv/Scripts/Activate.ps1
```

**Linux**
```bash
.venv/Scripts/activate
```

You can then install the dependency on your python virtual environment with
```bash
pip install customtkinter CTKMessagebox bcrypt mysql-connector-python
```

Setup your MySQL database:
```bash
py init_db.py
```

## Quick Start

1. Run Budget Buddy:

   ```bash
   py main.py
   ```

2. Enjoy!

   ## Roadmap
- Enhance admin interface
- Improve program stability

   ## Authors
  - [Elyes](https://github.com/elyes-messaadia)
  - [Marius](https://github.com/marius-gavini)
  - [Arthur](https://github.com/arthur-georget)