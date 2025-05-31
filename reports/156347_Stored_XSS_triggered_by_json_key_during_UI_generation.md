# Stored XSS triggered by json key during UI generation

## Report Details
- **Report ID**: 156347
- **URL**: https://hackerone.com/reports/156347
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-03T19:31:11.174Z
- **Disclosed**: 2016-09-07T08:34:02.511Z

## Reporter
- **Username**: ctee
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Stored XSS is triggred from **Indices** -> **Generate a UI Demo**. Typing anything in the **Primary, Secondary, Tertiary, Image or URL attributes** for **User Interface** section. These text box have a drop down which displays the json keys during which XSS is triggered. 

Sample json for XSS would be 
``{
  "<img src=1 onerror=alert(document.domain)>": "hello",
}``

Attached: screen shot


## Attachments
- xsstrigger.png
