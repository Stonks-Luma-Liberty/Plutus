# Plutus

[![Github Issues](https://img.shields.io/github/issues/Stonks-Luma-Liberty/Plutus?logo=github\&style=for-the-badge)](https://github.com/Stonks-Luma-Liberty/Plutus/issues)
[![Codacy Badge](https://img.shields.io/codacy/grade/71044a7a4e4042a6a1cb88145dc4e761?logo=codacy\&style=for-the-badge)](https://www.codacy.com/gh/Stonks-Luma-Liberty/Plutus/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Stonks-Luma-Liberty/Plutus&amp;utm_campaign=Badge_Grade)
[![Github Top Language](https://img.shields.io/github/languages/top/Stonks-Luma-Liberty/Plutus?logo=python\&style=for-the-badge)](https://www.python.org)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg?style=for-the-badge)](https://github.com/wemake-services/wemake-python-styleguide)

Discord bot that display NFT marketplace collection statistics

## Table of Contents

*   [Features](#features)

*   [Environment Variables](#environment-variables)

*   [Run Locally](#run-locally)

    *   [With Docker](#with-docker)
    *   [Without Docker](#without-docker)

## Features

*   Display NFT collection statistics\

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DISCORD_BOT_TOKEN` - Token required to connect with your discord bot

`GUILD_IDS` - IDS of discord GUILDS bot will work on


## Run Locally

Clone the project

```bash
  git clone https://github.com/Stonks-Luma-Liberty/Plutus.git
```

Go to the project directory

```bash
  cd Plutus
```

### With Docker

Use docker-compose to start the bot

```bash
docker-compose up -d --build
```

### Without Docker

Install dependencies

```bash
  poetry install
```

Start the bot

```bash
  poetry run python main.py
```
