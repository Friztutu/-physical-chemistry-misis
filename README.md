
<p align="center">
      <img src="https://i.ibb.co/wLM1wQN/pngegg-3.png" width="420">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/python-3.10-green" alt="Python Version">
   <img src="https://img.shields.io/badge/Django-3.2.18-yellowgreen" alt="Parser Version">
   <img src="https://img.shields.io/badge/Licence-MIT-blueviolet" alt="License">
</p>

## О проекте

Реализация frontend(Html and CSS) и backend(Django) сайта для расчета заданий на проектирование защитного заземления или на подбор площади сечения нулевого провода. Этот проект должен помочь студентам Ниту Мисис
для решения 5 практической работы по БЖД, ну может еще и студентам других вузов(вдруг у вас есть похожие задания). Сайт полностью адаптивен под пк, планшеты и мобильные устройства разных размеров. На сайте можно найти более подробное описание проекта, с целями, технологиями которые там используются и тд. Даже найти состав команды которые писали этот проект, но там есть нюанс...

Проект деплойнут, оценить его можно по ссылке - http://193.124.115.181/

## Превью
<p align="center"><b>Главная страница:</b></p>

<img src="https://i.ibb.co/dKrnNC6/2023-07-19-220820.png" width="100%">

<p align="center"><b>Первая задача:</b></p>

<img src="https://i.ibb.co/jHJZChs/2023-07-19-221126.png" width="100%">

<p align="center"><b>Результат к первой задачи:</b></p>

<img src="https://i.ibb.co/8j973mv/2023-07-19-221615.png" width="100%">

<p align="center"><b>Вторая задача:</b></p>

<img src="https://i.ibb.co/KrDX7R1/2023-07-19-221239.png" width="100%">

<p align="center"><b>Результат к второй задачи:</b></p>

<img src="https://i.ibb.co/px8zpWz/2023-07-19-222357.png" width="100%">

## Настройка окружения для работы
1. Сначала нужно создать и запустить виртуальное окружение:
 ```bash
   python3.10 -m venv venv
   source venv/bin/activate
 ```
2. Скачать пакеты:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
3. Создать и заполнить файл .env в корневой папке проета:<br><br>
Получить новый secret key можно так:
```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
4. Провести миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

# Запуск на локалке
```bash
python manage.py runserver
```


## Разработчики:

- [Alex](https://github.com/Friztutu)
- [Roman](https://github.com/ProtoFey)

## License

Project BZD-Misis is distributed under the MIT licence
