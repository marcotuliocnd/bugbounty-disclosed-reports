# link.avito.ru - Bypass of restrictions on external links.

## Report Details
- **Report ID**: 956449
- **URL**: https://hackerone.com/reports/956449
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-11T23:00:29.834Z
- **Disclosed**: 2021-09-09T17:25:00.139Z

## Reporter
- **Username**: hen51
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: avito

## Vulnerability Information
Hello Avito!

On "link.avito.ru"  subdomain of "www.avito.ru" attacker able to bypass restriction for dangerous external links via trusted domain google.com.

This scenario may be also possible with all other trusted subdomains of avito such as "yandex.ru" and so on, but in this example i'm used google redirect functionality "google.com/url?sa=t&url=" . 

Example with TRUSTED subdomain:
https://link.avito.ru/go?to=youtu.be/dQw4w9WgXcQ 

But we will dig deeper because there are not much to play with.



By default when user visit's untrusted link from avito.ru he or she can face with the warning webpage which tells user about the danger but sadly this restriction can be bypassed. I will show you how.

Firstly we will use this link: 
https://link.avito.ru/go?to=http://google.com/amp/

Then we need to add this part to previous link:
google.com/url?sa=t&url=HTTP%3A%2F%2Fexample.com/

But this shouldn't work with avito.ru until we url-encode this. 

Steps to reproduce:

1) For our needs we will use "https://onlinetexttools.com/url-encode-text" website. Make sure you enabled 'Escape All Text Characters' option.
Paste this link into "Text" field:
google.com/url?sa=t&url=HTTP%3A%2F%2Fexample.com/

2) After url-encode we will get this value:

%67%6F%6F%67%6C%65%2E%63%6F%6D%2F%75%72%6C%3F%73%61%3D%74%26%75%72%6C%3D%48%54%54%50%25%33%41%25%32%46%25%32%46%65%78%61%6D%70%6C%65%2E%63%6F%6D%2F

3) Now we combine and get this:

https://link.avito.ru/go?to=http://google.com/amp/%67%6F%6F%67%6C%65%2E%63%6F%6D%2F%75%72%6C%3F%73%61%3D%74%26%75%72%6C%3D%48%54%54%50%25%33%41%25%32%46%25%32%46%65%78%61%6D%70%6C%65%2E%63%6F%6D%2F

4) After this, encode all characters after "https://link.avito.ru/go?to=" and you will get this:

https://link.avito.ru/go?to=%68%74%74%70%3A%2F%2F%67%6F%6F%67%6C%65%2E%63%6F%6D%2F%61%6D%70%2F%25%36%37%25%36%46%25%36%46%25%36%37%25%36%43%25%36%35%25%32%45%25%36%33%25%36%46%25%36%44%25%32%46%25%37%35%25%37%32%25%36%43%25%33%46%25%37%33%25%36%31%25%33%44%25%37%34%25%32%36%25%37%35%25%37%32%25%36%43%25%33%44%25%34%38%25%35%34%25%35%34%25%35%30%25%32%35%25%33%33%25%34%31%25%32%35%25%33%32%25%34%36%25%32%35%25%33%32%25%34%36%25%36%35%25%37%38%25%36%31%25%36%44%25%37%30%25%36%43%25%36%35%25%32%45%25%36%33%25%36%46%25%36%44%25%32%46




Instead of notifying user about the danger, the user is redirected outside of avito.ru to google.com.

## Impact

An attacker can redirect the target from "link.avito.ru" to malicious website through trusted  website google.com and his redirect functionality.

## Attachments
No attachments
