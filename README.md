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
- [x] **v1.1.0** `game/storage` на ООП.
- [ ] **v1.2.0** `game/logic` на ООП.
- [ ] **v1.3.0** `game/ui` на ООП.
- [ ] **v1.4.0** `game` на ООП.
- [ ] **v1.5.0** `utils` на ООП.
- [ ] **v1.6.0** `menu/logic` на ООП.
- [ ] **v1.7.0** `menu/ui` на ООП.
- [ ] **v1.8.0** `menu` на ООП.
- [ ] **v2.0.0** Релиз на новой архитектуре.

# 🛠️ Стек
- **Язык:** Python 3.11+
- **Встроенные модули:** `json`, `pathlib`, `random`, `sys`.
- **Сторонние модули:** `pyinstaller` сборка, `readchar` неблокирующий ввод.

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