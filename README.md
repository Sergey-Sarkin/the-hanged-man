# 💀 The Hanged Man (Виселица)
Консольная игра Виселица

# 🎯 Цель
Учебный pet-проект

# ⚙️ Функционал
- Неблокирующий ввод с клавиатуры.
- Управление клавишами (↑, ↓, →, ← навигация и enter подтверждение).
- Текстовое меню и стилизация интерфейса в терминале.

## 🗺️ Roadmap
- [x] **v1.0.0** Релиз.

# 🛠️ Стек
- **Язык:** Python 3.11+
- **Встроенные модули:** `pathlib`, `random`, `json`.
- **Сторонние модули:** `readchar` неблокирующий ввод, `pyinstaller` сборка.

# 🚀 Запуск
```bash
git clone https://github.com/Sergey-Sarkin/the-hanged-man.git
cd the-hanged-man

python -m venv .venv

# Для Windows (PowerShell / CMD)
.venv\Scripts\activate

# Для Linux / macOS
source .venv/bin/activate

python -m pip install -r requirements.txt

python app/main.py
```

# 🔧 Сборка
```bash
pyinstaller --onefile --name="The Hanged Man" --icon="data/icon.ico" --add-data "data/words.json;data" --copy-metadata readchar --copy-metadata rich app/main.py
```