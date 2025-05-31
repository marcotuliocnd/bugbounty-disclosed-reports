# attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2

## Report Details
- **Report ID**: 422331
- **URL**: https://hackerone.com/reports/422331
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-11T07:10:09.324Z
- **Disclosed**: 2019-04-25T04:57:10.936Z

## Reporter
- **Username**: gujjuboy10x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aaf

## Vulnerability Information
Dear Team,

**Summary:** [add summary of the vulnerability]
After looking into https://aaf.com/
i get to know that there is way where i can book a ticket and can play around , but it asked for valid credit card and all stuff
so , i tried to bypass and bought a ticket 23 with 0$

Live PoC:
https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2  (check this one)

**Description:** [add more details about this vulnerability]
attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2

## Steps To Reproduce:

1. go to aaf.com and login with your account
2. click on ticket option and select San Antonio Commanders Season and click on that and select 3 or any ticket and intercept that request ,
and change from 3-seats-3 to 10-seats-10
{F358789}
snip:

```
Content-Disposition: form-data; name="addon-268-number-of-seats-0"

10-seats-10
```
{F358788}
3. click on add tickets and you can see your order is 0$

and book any number of ticket at 0$

## Supporting Material/References:

Please find attachment

Thanks,
Vishal

## Impact

attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2

## Attachments
- t12.PNG
- t1.PNG
