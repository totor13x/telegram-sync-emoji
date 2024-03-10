# Telegram Emoji Sync

На других языках: [English](README.md), **Русский**, [Башҡортса](README.ba.md)

## Таблица контента

- [Telegram Emoji Sync](#telegram-emoji-sync)
  - [Таблица контента](#таблица-контента)
  - [Описание](#описание)
  - [Как использовать](#как-использовать)
  - [Лицензия](#лицензия)


## Описание

![](https://digital-garden.website.yandexcloud.net/images/stuffs/scripts/telegram-status-sync/ca5e8fda-44ea-4a83-958d-9b6219601e99.gif)

Telegram Emoji Sync - это скрипт на pyTelethon, который позволяет синхронизировать состояния фокусирования экосистемы Apple и при желании Discord.

## Как использовать

- `creating_session.py` - Создание новой строки сессии для клиента.
- `get_emojis.py` - Получение выбранного вами текущего эмодзи из Telegram. Вы получаете document_id эмодзи, который вы можете использовать в `flask_runner.py`, `lambda_endpoint.py` и, если хотите использовать его с BetterDiscord, вы можете использовать его в `telegram_sync_plugin.js`.
- `flask_runner.py` - Запуск сервера Flask.
- `lambda_endpoint.py` - Эндпоинт AWS Lambda. Вы можете использовать ее с AWS API Gateway.
- `telegram_sync_plugin.js` - Плагин BetterDiscord для синхронизации эмодзи. Необходимо собрать с помощью webpack. [Более подробная информация о сборке плагинов для BetterDiscord](https://docs.betterdiscord.app/plugins/intermediate/bundling), этот файл является исходником для сборки.
- `Dockerfile.awslambda` - [Dockerfile](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) для AWS Lambda. Я использовал его для создания .zip pip пакетов для AWS Lambda.

## Лицензия

Этот проект лицензирован по лицензии MIT - см. файл [LICENSE](LICENSE) для получения подробной информации.
