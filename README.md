# Factory bot
**_Тестовое задание для Фабрики проектов_**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white) <br>

Это тестовое задание, написанное для "Фабрики проектов".  
В основе проекта — приложение на Django и API на DRF.
Всё взаимодействие с приложением происходит через запросы к API.

### Как использовать?

Клонируйте репозиторий на свой компьютер:
```bash
git clone git@github.com:renegatemaster/factory_bot.git
```

Создайте виртуальное окружение, активируйте его и установите зависимости:
```bash
python3.9 -m venv venv
source venv/bin/activate  # Для Linux и MacOS
source venv/scripts/activate  # Для Windows
pip install -r requirements.txt
```

Создайте файл .env
```bash
touch api.env
```
И сохраните в него ваши данные:
```.env
export DEBUG=XXXXX
export TELEGRAM_BOT_TOKEN=65744XXXXXXXXXXXXXXXXX
export POSTGRES_DB=factorybot
export POSTGRES_USER=factorybot
export POSTGRES_PASSWORD=defaultpwd
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```
Передайте переменные в окружение:
```bash
source api.env
```

Если у вас ещё нет аккаунта в телеграм и своего бота:
 - [Скачайте](https://desktop.telegram.org/) Telegram и зарегистрируйтесь
 - Узнайте ID вашего аккаунта с помощью [специального бота](https://t.me/userinfobot)
 - В поиске чатов найдите [BotFather](https://t.me/BotFather) и создайте свего бота командой `/newbot`
 - Получите токен бота от BotFather командой `/token`

Запустите контейнер Postgres:
```bash
docker run -d --rm --name factorybot-db -p 5432:5432 -e POSTGRES_USER=factorybot -e POSTGRES_PASSWORD=defaultpwd postgres
```
Запустите бота:
```bash
python manage.py start_bot
```
В новой консоли запустите приложение:
```bash
python manage.py runserver
```
