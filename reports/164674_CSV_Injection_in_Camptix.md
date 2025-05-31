# CSV Injection in Camptix

## Report Details
- **Report ID**: 164674
- **URL**: https://hackerone.com/reports/164674
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-08-31T09:24:53.228Z
- **Disclosed**: 2016-10-12T07:49:59.216Z

## Reporter
- **Username**: grande
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hello, Ian!

I see you tried to escape "=, -, +, @" in your code ([#151516](https://hackerone.com/reports/151516)), but let me show simple workaround.

I've made CSV injection by using this string ";=cmd|' /C calc'!A5" without doublequotes.

";" will bypass your trying to set the quote in the beginning of the string.

";" acts as a new cell separator.

Tested in the Excel 2016

## Attachments
- csv-injection.mp4
