# 📝 Minimal PasteBin

Простой и минималистичный PasteBin — веб-приложение на Django для создания, просмотра и удаления текстовых фрагментов.

## 🔧 Что делает

- ✍️ Создание пасты (текстовой заметки).
- 🔗 Просмотр пасты по уникальной ссылке (UUID).
- ❌ Кнопка "Удалить" на странице просмотра.
- 🎨 Минималистичный и аккуратный интерфейс с CSS

## 📦 Как установить

```bash
# Клонируй репозиторий
git clone https://github.com/Kutberdi/minimal-pastebin.git
cd minimal-pastebin

# Создай и активируй виртуальное окружение
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Установи зависимости
pip install -r requirements.txt

# Выполни миграции
python manage.py migrate

# Запусти сервер
python manage.py runserver
