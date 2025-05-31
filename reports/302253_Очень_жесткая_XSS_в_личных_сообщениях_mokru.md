# Очень жесткая XSS в личных сообщениях m.ok.ru

## Report Details
- **Report ID**: 302253
- **URL**: https://hackerone.com/reports/302253
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-01-03T22:22:26.486Z
- **Disclosed**: 2018-06-30T11:04:05.699Z

## Reporter
- **Username**: circuit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ok

## Vulnerability Information
Приветствую.

Нашел багу в личных сообщениях в мобильной версии
{F251208}

Что нужно, чтоб заюзать:

1. Переходим в группу https://m.ok.ru/group/54904397693159/market
2. Ищем товар единственный на страничке
{F251213}
3. Переходим на него и нажимаем на кнопку "Связаться с продавцом" (https://m.ok.ru/group/54904397693159/market)
{F251215}
4. Видим алерт.
{F251216}


Нет фильтрации служебных символов тут -
<div class="discus_dialogs_topic emphased tx-ellip">"&gt;<img src="x" onerror="alert()"></div>

## Impact

XSS.

## Attachments
- xss.png
- xss2.png
- xss3.png
- xss4.png
