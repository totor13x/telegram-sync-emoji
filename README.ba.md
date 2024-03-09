# Telegram Emoji Sync

Башҡа телдәрҙә: [English](README.md), [Русский](README.ru.md), **Башҡортса**

## Йөкмәткеһе

- [Telegram Emoji Sync](#telegram-emoji-sync)
  - [Йөкмәткеһе](#йөкмәткеһе)
  - [Тасуирламаһы](#тасуирламаһы)
  - [Нисек ҡулланырға](#нисек-ҡулланырға)
  - [Лицензия](#лицензия)

## Тасуирламаһы

Telegram Emoji Sync - pyTelethon скрипты, ул Apple экосистемаһының фокус торошон Һәм Discord теләгәндә синхронлаштырырға мөмкинлек бирә.

## Нисек ҡулланырға

- `creating_session.py` - Клиент өсөн яңы сессия юлын булдырыу.
- `get_emojis.py` - Telegramдан хәҙерге ваҡытта һайлап алынған эмодзи алыу. Һеҙ алған document_id эмодзины `flask_runner.py`, `lambda_endpoint.py` ҡулланырға була. Әгәр уны  BetterDiscord менән ҡулланырға теләһәгеҙ, бының өсөн `telegram_sync_plugin.js`-нда ҡулланырға була.
- `flask_runner.py` - Flask серверҙы эшләтеп ебәреү
- `lambda_endpoint.py` - AWS Lambda эндпоинттар. AWS API Gateway менән ҡулланырға була.
- `telegram_sync_plugin.js` - Эмоджины синхронлаштырыу өсөн BetterDiscord плагины. Webpack ярҙамында йыйырға кәрә. [BetterDiscord - Bundling Webpack](https://docs.betterdiscord.app/plugins/intermediate/bundling), был файл йыйыуҙың сығанағы булып тора.
- `Dockerfile.awslambda` - AWS Lambda өсөн [Dockerfile](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html). Мин уны AWS Lambda өсөн .zip pip пакеттарын төҙөү өсөн ҡулланам.

## Лицензия

Был проект MIT лицензияһы буйынса лицензияланған, смекле мәғлүмәт алыу өсөн [LICENSE](LICENSE) файлын ҡарағыҙ.