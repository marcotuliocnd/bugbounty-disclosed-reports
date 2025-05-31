# [insideok.ru] Database Dump

## Report Details
- **Report ID**: 197789
- **URL**: https://hackerone.com/reports/197789
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-01-12T10:34:47.707Z
- **Disclosed**: 2018-04-25T17:28:49.355Z

## Reporter
- **Username**: bigbear_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ok

## Vulnerability Information
http://insideok.ru/db.sql

Внутри - учётки админов на 2016 год.

-- Хост: localhost
-- Время создания: Сен 03 2016 г., 12:00
-- Версия сервера: 5.5.47-cll-lve
-- Версия PHP: 5.4.45


# Структура таблицы `users`

`CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) unsigned NOT NULL,
  █████
  ███████
  ███████
██████████
███
██████████
███
█████████
███████
████████
█████
█████
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=5461;`


# Дамп данных таблицы users

`INSERT INTO `users` (██████████) VALUES
████
███
████████
███
████
███████
████████
███████
█████
███
███
████████
███████
███████
████████
██████
████████
████
███`

## Attachments
No attachments
