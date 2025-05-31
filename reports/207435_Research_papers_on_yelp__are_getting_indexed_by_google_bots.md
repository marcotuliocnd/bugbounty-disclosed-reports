# Research papers on yelp  are getting indexed by google bots.

## Report Details
- **Report ID**: 207435
- **URL**: https://hackerone.com/reports/207435
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-19T03:31:27.722Z
- **Disclosed**: 2017-11-09T20:01:26.075Z

## Reporter
- **Username**: us111
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
While playing around to access some private information on yelp.com i was able to get access to research papers on yelp which are not supposed disclose publically.

By framing a google dork i got access to most of your documents.
Google Dork: site:starbucks.com ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv

Real proof:

https://www.google.co.in/search?q=site:yelp.com+ext:doc+%7C+ext:docx+%7C+ext:odt+%7C+ext:pdf+%7C+ext:rtf+%7C+ext:sxw+%7C+ext:psw+%7C+ext:ppt+%7C+ext:pptx+%7C+ext:pps+%7C+ext:csv&biw=799&bih=600&ei=ZJuoWOOMCMXmvgT-9Z_wDA&start=0&sa=N&cad=cbv&bvch=u&sei=LQ6pWPGUL4vXvgSior3IBw

Such important documents are getting indexed by google bots.

To mitigate this add below meta character so pages won't be indexed by bots.
<html>
<head>
<title>...</title>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
</head>

Also you can disallow /html/ in robots.txt.

Hope will add these meta tags so that further no such documents will get indexed.

Thanks.



## Attachments
No attachments
