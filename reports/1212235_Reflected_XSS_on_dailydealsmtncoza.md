# Reflected XSS on dailydeals.mtn.co.za

## Report Details
- **Report ID**: 1212235
- **URL**: https://hackerone.com/reports/1212235
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-28T19:27:15.449Z
- **Disclosed**: 2021-12-24T08:49:47.377Z

## Reporter
- **Username**: musab_alharany
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello MTN Team.
i found Reflected XSS on``` https://dailydeals.mtn.co.za/index.cfm?GO=DEALS```  vi ```cpID``` parameter with POST method 

## Steps To Reproduce:
1. Intercept the https://dailydeals.mtn.co.za/index.cfm?GO=DEALS 
2. Change Method to POST
3. Add empty line after last header
4. Write this code 
>category_id=7&cpID=1%22%3e%20%3cimg%20src%3da%20onerror%3dalert("XSS")%3e<!--

{F1319085}
5. Sent the Request.
6. Right Click on response area, then Click on ```Show response in browser```
7. copy the link, and put it on browser use BurpSuite as proxy 
8. press the Enter key, then you will see the ```XSS``` on your browser
{F1319086}

## Impact

attacker can convinces a victim to visit a URL then he can:
1. steal users cookies
2. redirect the user to malicious website

## Attachments
- request.jpg
- xss-POC.jpg
