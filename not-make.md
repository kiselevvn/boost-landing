# Установка проекта без make

Для утановки проекта без make необходимо

запустить терминал windows от имени администратора, перейти в корневую директории проекта и поочередно исполнить команды

![power shell](https://github.com/kiselevvn/legal-service/blob/main/assets/img/cmd-admin.PNG?raw=true)

```cmd
poetry run pip install -U setuptools
poetry install --no-root
poetry run task manage initconfig --debug
poetry run task migrate
poetry run task manage createadmin
```
