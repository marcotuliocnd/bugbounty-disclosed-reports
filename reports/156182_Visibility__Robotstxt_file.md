# Visibility  Robots.txt file

## Report Details
- **Report ID**: 156182
- **URL**: https://hackerone.com/reports/156182
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-02T22:35:56.808Z
- **Disclosed**: 2017-05-18T16:54:51.496Z

## Reporter
- **Username**: akshay_raj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Issue detail:-
The web server contains a robots.txt file.  

Issue background:-
The file robots.txt is used to give instructions to web robots, such as search engine crawlers, about locations within the web site that robots are allowed, or not allowed, to crawl and index.
The presence of the robots.txt does not in itself present any kind of security vulnerability. However, it is often used to identify restricted or private areas of a site's contents. The information in the file may therefore help an attacker to map out the site's contents, especially if some of the locations identified are not linked from elsewhere in the site. If the application relies on robots.txt to protect access to these areas, and does not enforce proper access control over them, then this presents a serious vulnerability.

Issue remediation:-
The robots.txt file is not itself a security threat, and its correct use can represent good practice for non-security reasons. You should not assume that all web robots will honor the file's instructions. Rather, assume that attackers will pay close attention to any locations identified in the file. Do not rely on robots.txt to provide any kind of protection over unauthorized access.

URL:- https://www.zomato.com/robots.txt

User-agent: Googlebot
Disallow: /admin/
Disallow: /clients/
Disallow: /acd/
Disallow: /voicephp/
Disallow: /downloads/
Disallow: /nonsvn/
Disallow: /zast
Allow: /

If u have robots.txt file so attacker can see all Your secret pages!
like www.example.com/admin....


Sitemap:- https://www.zomato.com/sitemap_seznam.xml.gz




## Attachments
- z.png
