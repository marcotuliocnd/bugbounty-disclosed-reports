# Reflected XSS at dailydeals.mtn.co.za

## Report Details
- **Report ID**: 1210921
- **URL**: https://hackerone.com/reports/1210921
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-27T16:55:09.366Z
- **Disclosed**: 2021-12-24T08:49:13.986Z

## Reporter
- **Username**: musab_alharany
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello MTN Group:

I found reflected XSS vi  ```category_id=```  parameter .

The server reads data directly from the HTTP request and reflects it back in the HTTP response. Reflected XSS exploits occur when an attacker causes a victim to supply dangerous content to a vulnerable web application, which is then reflected back to the victim and executed by the web browser. The most common mechanism for delivering malicious content is to include it as a parameter in a URL that is posted publicly or e-mailed directly to the victim. URLs constructed in this manner constitute the core of many phishing schemes, whereby an attacker convinces a victim to visit a URL that refers to a vulnerable site. After the site reflects the attacker's content back to the victim, the content is executed by the victim's browser.

## Steps To Reproduce:
1. visite the https://dailydeals.mtn.co.za
2. click on Categories, Then click on any items on it, now you get the ```category_id``` parameter on the URL.
3. add this payload ```3mh8r%3cimg%20src%3da%20onerror%3dalert(1)%3e``` as a value to ```category_id``` parameter 
you will get popup with vaule ```1``` as the POC image 
{F1317658}

##one link POC:
https://dailydeals.mtn.co.za/index.cfm?GO=DEALS&category_id=3mh8r%3Cimg%20src%3da%20onerror%3dalert(1)%3E

##Recommendation:
Your script should filter metacharacters from user input.

## Impact

attacker convinces a victim to visit a URL  & steal users cookies

## Attachments
- XSS-POC.png
