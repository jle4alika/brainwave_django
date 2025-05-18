

# Brainwave — Django Проект

Brainwave — это веб-приложение, построенное на Django. Основная цель проекта — [разработка сайта с курсами для обучений]. В нём реализованы курсы, профиль пользователя, категории, достижения и личный кабинет.

---

## 📦 Требования

- Python 3.8+
- VS Code (или любая другая IDE)
- PostgreSQL
- pgAdmin 4 (для управления БД)

---

## 🚀 Как запустить проект в VS Code

### 1. **Открытие проекта**

Склонируйте репозиторий:

```bash
https://github.com/jle4alika/brainwave_django.git
```

Откройте папку в VS Code:

```bash
code brainwave
```

или через меню: `File → Open Folder`.

---

### 2. **Создание виртуального окружения**

В терминале VS Code выполните:

```bash
python -m venv venv
```

Активируйте его:

- Windows:
  ```bash
  venv\Scripts\activate
  ```

- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

---

### 3. **Установка зависимостей**

```bash
pip install -r requirements.txt
```

---

### 4. **Настройка PostgreSQL**

#### Создание базы данных через pgAdmin 4:

1. Откройте **pgAdmin 4**.
2. Подключитесь к серверу (обычно `localhost`).
3. Нажмите правой кнопкой на **Databases → Create → Database**.
4. Введите имя новой БД, например: `brainwavedb`.
5. Сохраните.

#### Настройка в Django:

Измените файл `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'brainwavedb',
        'USER': 'postgres',
        'PASSWORD': 'ваш_пароль',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

> Убедитесь, что установлен драйвер для PostgreSQL:
```bash
pip install psycopg2-binary
```

---

### 5. **Создание и применение миграций**

Если вы добавили изменения в модели, создайте миграции:

```bash
python manage.py makemigrations
```

Примените миграции:

```bash
python manage.py migrate
```

> 💡 Обычно миграции создаёт разработчик при изменении модели. Если они уже есть в проекте — сразу применяйте их.

---

### 6. **Загрузка фикстур (например, категорий)**

```bash
python manage.py loaddata fixtures/categories_json.json
```

---

### 7. **Запуск сервера разработки**

```bash
python manage.py runserver
```

Откройте браузер и перейдите по ссылке:  
🔗 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### 8. **(Опционально) Создание суперпользователя**

```bash
python manage.py createsuperuser
```

---

## 📁 Структура проекта

```
brainwave/
├── brainwave/                # Основные настройки проекта
│   └── settings.py           # Здесь настраивается DATABASES и другое
├── categories/               # Приложение категорий
├── courses/                  # Курсы
├── lk/                       # Личный кабинет
├── profile/                  # Профиль пользователя
├── fixtures/                 # Фикстуры (например, categories_json.json)
├── static/                   # Статические файлы (CSS, JS, изображения)
├── templates/                # HTML-шаблоны
├── media/                    # Медиафайлы загруженных пользователей
├── staticfiles/              # Собранные статические файлы после collectstatic
├── manage.py
└── requirements.txt
```

---

## ✅ Советы для работы в VS Code

- Используйте расширение **Python** от Microsoft.
- Для удобной работы с Git — установите **GitLens**.
- Держите виртуальное окружение активным всегда при работе.

