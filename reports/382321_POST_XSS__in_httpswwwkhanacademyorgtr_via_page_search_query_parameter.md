# POST XSS  in https://www.khanacademy.org.tr/ via page_search_query parameter

## Report Details
- **Report ID**: 382321
- **URL**: https://hackerone.com/reports/382321
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-17T03:35:10.867Z
- **Disclosed**: 2018-09-18T23:00:49.394Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hey there, while testing your program I came across a XSS vulnerability in the search area of your website.
The vector uses HTTP POST request and the parameter is "page_search_query"" on www.khanacademy.org.tr/arama.asp

In the next topics I will demonstrate how you can reproduce the vulnerability found on your website:

1º Go to your website and in the search box insert the following payload:
""--!><Svg/OnLoad=(confirm)(/xss/)>
xss.jpg


2º Output of the payload:
xss2.jpg

3º Vulnerable code with the payload:

`<form class="large-search-form" action="arama.asp" method="post">
<input id="large-search-input" name="page_search_query" class="placeholder simple-input search-input blur-on-esc large-search-bar ui-corner-all" autocomplete="off" value="""--!><Svg/OnLoad=(confirm)(/xss/)>" style="margin-top:0px !important">
<i class="icon-search"></i>`

xss3.jpg

Exploitability:
Attacker sends text-based attack scripts that exploit the interpreter in the browser. Almost any source of data can be an attack vector, including internal sources such as data from the database.

Please let me know if you need further explanation or details.​
Best Regards, Miguel Santareno

## Impact

Attackers can execute scripts in a victim’s browser to hijack user sessions, deface web sites, insert hostile content, redirect users, hijack the user’s browser using malware, etc.

## Attachments
- xss2.PNG
- xss.PNG
- xss3.PNG
