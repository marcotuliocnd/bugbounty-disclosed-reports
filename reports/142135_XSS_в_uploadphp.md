# XSS в upload.php

## Report Details
- **Report ID**: 142135
- **URL**: https://hackerone.com/reports/142135
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-30T21:37:27.191Z
- **Disclosed**: 2017-02-09T14:20:44.482Z

## Reporter
- **Username**: irek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vkcom

## Vulnerability Information
Добрый вечер!
Раскрутил интересную xss на upload.php.

**Демо [тут](https://vk.com/app5486273) или [тут](https://irek.wtf/vk.com/transport/).**

Как все было?
Увидел интересный экшн [upload.php?act=transport](https://pu.vk.com/c415824/upload.php?act=transport&to_act=add_doc&hash=8dfd93e60c78ddb4a9cf914c27f7642c&rhash=8171a35e59a63aab65846a26345ddbf6&aid=1&mid=17274528&callback=getUploadSvg), который служит для загрузки нарисованного граффити в документы. Глаз зацепился за вызов функции `eval` в строке 25. Обратите внимание на параметр `callback`, значением которого в данном случае является строка `getUploadSvg`.  На этой странице определена функция `sendData` (строки 11-52) и, помимо этого, выполняется следующий кусок кода (строки 55-64):

    var _ua = navigator.userAgent;
    var locDomain = location.host.toString().match(/[a-zA-Z]+\.[a-zA-Z]+\.?$/)[0];
    if (/opera/i.test(_ua) || !/msie 6/i.test(_ua) || document.domain != locDomain) {
      document.domain = locDomain;
    }
    if (window.parent) {
      parent.getUploadSvg(function(data) {
        sendData('/c415824/upload.php?transport=iframe&act=add_doc&hash=8dfd93e60c78ddb4a9cf914c27f7642c&rhash=8171a35e59a63aab65846a26345ddbf6&aid=1&mid=17274528&pda=', data);
      });
    }

, где есть два условных оператора с бессмысленными условиями 👳🏾. В первом проставляется `document.domain` для кроссдоменного выполнения сценариев, а во втором все самое интересное - вызывается функция родительского окна `parent.getUploadSvg`, где `getUploadSvg` это значение GET-параметра `callback` ~~(как уже было написано выше)~~ и его значение можно менять на любое другое (предположительно подходящее под паттерн `/^[a-zA-Z0-9]*$/`). То есть функции `parent.{значение параметра callback}` передается один аргумент, являющийся анонимной функцией. Эта анонимная функция принимает один параметр `data`, а в её теле происходит вызов функции `sendData` (строка 62):

    sendData('/c415824/upload.php?transport=iframe&act=add_doc&hash=8dfd93e60c78ddb4a9cf914c27f7642c&rhash=8171a35e59a63aab65846a26345ddbf6&aid=1&mid=17274528&pda=', data);


Тут первый аргумент это строка, содержащая относительный URL, в который попадают почти все исходные GET-параметры, проходя перед выводом санитизацию. Второй параметр это переменная `data`, о которой писал чуть выше.

Разберем саму функцию `sendData`. Она принимает три аргумента `url`, `file` и `sequel `. По понятным причинам, нам интересны только первые два. Стоит обратить внимание на строку 16

    var plain = /iphone|ipod|ipad|opera mini|opera mobi/i.test(navigator.userAgent);

и блок кода условного оператора в строках 29-41

    if (plain) {
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

      if (dataUrl.length > 15000) {
        fdataUrl = dataUrl.substr(0, 15000);
        ndataUrl = dataUrl.substr(15000);
        dataUrl = fdataUrl;
        more = 1;
      }

      xhr.send(ajx2q({Data: dataUrl, more: more, sequel: sequel || 0}));
    } else {

Остановились мы на этом потому, что в строке 40 происходит вызов функции `ajx2q `, которая не определена и, поэтому, сохранение граффити в документы не работает для юзерагентов удовлетворяющих регулярному выражению `/iphone|ipod|ipad|opera mini|opera mobi/i`. Следовательно и хак не будет работать. Если не обращать внимания на сей досадный факт, то можно заметить, что в функции `sendData` с помощью `XMLHttpRequest` происходит POST-запрос на URL, параметрами которого мы можем манипулировать. В случае успеха, результат запроса передается в функцию `eval`, что круто если каким-то образом заставить сервер выдавать нужный нам ответ на этот POST-запрос. Поскольку мы можем манипулировать параметрами URL, на который будет произведен запрос, я начал думать над тем как заставить сервер отвечать на запрос моим js-кодом. Тут я вспомнил о том, что существуют такие штуки как [imagejs](http://jklmnn.de/imagejs/) и [share.php](https://vk.com/share.php?url=https://irek.wtf/shareit.php). Первое нам интересно потому что позволяет встроить js-код прямо файлы картинок (Gif, Bitmap, WebP, Netbpm Anymap, Progressive Graphics) и файлы будут валидны. А в share.php как-раз есть проксирование изображений ([пример](https://pu.vk.com/c539421/upload.php?act=proxy_img&url=https%3A%2F%2Firek.wtf%2Fpikachu.gif&hash=f5b4a65619ba2c63a7bb018db018bfce)). Тут я столкнулся с другой проблемой - хэши. Это была боль, но методом тыка я понял, что если передать скрипту `upload_fails.php` все необходимые параметры и добавить к ним `role=share`, то можно получить необходимые валидные хэши, используя которые можно скрафтить конечный URL. На этом этапе использовалась особенность санитизации переданных параметров (при изучении демо обратите внимание на точки в названиях параметров, они там не случайно). Осталось разобраться с последней проблемой. Заключается она в том, что `sendData` просто так не вызывается. Надо найти такую js-функцию, для которой выполняются следующие условия:

* название функции должно содержать только те символы, которые можно передать через GET-параметр `callback` и функция должна быть глобальной;
* функция должна принимать в качестве аргумента другую callback-функцию и вызвать её передавая в качестве аргумента какой-нибудь объект.

Немного `for (... in window)` и такая функция была найдена - `requestAnimationFrame` ([документация](https://developer.mozilla.org/ru/docs/DOM/window.requestAnimationFrame)).

Далее реализовал демо, которое можно посмотреть [тут](https://vk.com/app5486273) или [тут](https://irek.wtf/vk.com/transport/). Выполняется `alert(document.cookie);`.

Таким образом, получили xss для браузеров, строка user-agent которых не попадают под паттерн `/iphone|ipod|ipad|opera mini|opera mobi/i` и в которых имплементирована функция `requestAnimationFrame ` (или с вендорными префиксами `mozRequestAnimationFrame`, `webkitRequestAnimationFrame`, `msRequestAnimationFrame`).

## Attachments
No attachments
