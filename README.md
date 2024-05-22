# Установка
### Клонируйте репозиторий на свой компьютер:

```
git clone https://github.com/Krim-code/SecurityApp.git
```

### Создайте виртуальное окружение для проекта:

```
python3 -m venv venv
```

### Активируйте виртуальное окружение:

####На macOS и Linux:
```
source venv/bin/activate
```

#### На Windows:
```
venv\Scripts\activate
```
### Установите зависимости проекта из файла requirements.txt:

```
pip install -r requirements.txt
```

### Перейдите в директорию с файлом manage.py:
```
cd project_name
```

### Выполните миграции для создания базы данных:

```
python manage.py migrate
```
### Создайте суперпользователя:
```
python manage.py createsuperuser
```

### Запустите веб-сервер Django:

```
python manage.py runserver
```


