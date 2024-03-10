# Telegram Emoji Sync

In other languages: **English**, [Русский](README.ru.md), [Башҡортса](README.ba.md)

## Table of contents

- [Telegram Emoji Sync](#telegram-emoji-sync)
  - [Table of contents](#table-of-contents)
  - [Description](#description)
  - [How to use](#how-to-use)
  - [License](#license)


## Description

![](https://digital-garden.website.yandexcloud.net/images/stuffs/scripts/telegram-status-sync/ca5e8fda-44ea-4a83-958d-9b6219601e99.gif)

Telegram Emoji Sync is a pyTelethon script that allows you to synchronize the focus states of the Apple ecosystem and, optionally, Discord.

## How to use

- `creating_session.py` - Creates a new session string for client.
- `get_emojis.py` - Retrieves your currently selected emoji from Telegram. You get the document_id of the emoji, which you can use in `flask_runner.py`, `lambda_endpoint.py` and if you want to use it with BetterDiscord, you can use it in `telegram_sync_plugin.js`.
- `flask_runner.py` - Runs the Flask server.
- `lambda_endpoint.py` - AWS Lambda endpoint. You can use it with AWS API Gateway.
- `telegram_sync_plugin.js` - BetterDiscord plugin for syncing emojis. Need to build with webpack. [More info about building plugins for BetterDiscord](https://docs.betterdiscord.app/plugins/intermediate/bundling), this file is a source for it.
- `Dockerfile.awslambda` - [Dockerfile](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) for AWS Lambda, i used it for building the .zip pip packages for AWS Lambda.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.