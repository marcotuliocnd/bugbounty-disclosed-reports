# XSS when Shared

## Report Details
- **Report ID**: 283821
- **URL**: https://hackerone.com/reports/283821
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-28T19:34:41.914Z
- **Disclosed**: 2017-11-01T09:58:30.767Z

## Reporter
- **Username**: haystack_needle
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
## Introduction
XSS on an embedded piece of code that, when shared, may make it seem as if it was infogram.com that was doing the malicious act.

## Proof of Concept
1. Create an account
2. Create a project titled "script>alert(1);</script>"
3. Click on share 

Here's an example of the share embedded code:
```
<div class="infogram-embed" data-id="d08ad077-3490-4241-b9a9-057da53e2e7d" data-type="interactive" data-title="<script>alert(1);</script>"></div><script>!function(e,t,s,i){var n="InfogramEmbeds",o=e.getElementsByTagName("script"),d=o[0],r=/^http:/.test(e.location)?"http:":"https:";if(/^\/{2}/.test(i)&&(i=r+i),window[n]&&window[n].initialized)window[n].process&&window[n].process();else if(!e.getElementById(s)){var a=e.createElement("script");a.async=1,a.id=s,a.src=i,d.parentNode.insertBefore(a,d)}}(document,0,"infogram-async","https://e.infogram.com/js/dist/embed-loader-min.js");</script><div style="padding:8px 0;font-family:Arial!important;font-size:13px!important;line-height:15px!important;text-align:center;border-top:1px solid #dadada;margin:0 30px"><a href="https://infogram.com/d08ad077-3490-4241-b9a9-057da53e2e7d" style="color:#989898!important;text-decoration:none!important;" target="_blank"><script>alert(1);</script></a><br><a href="https://infogram.com" style="color:#989898!important;text-decoration:none!important;" target="_blank" rel="nofollow">Infogram</a></div>
```

## Potential Fixes
* Display the project title so the web surfer knows it's not actually infogram.com that is that's doing the malicious act
* Prevent the project name to be created in the first place. 


## Consequences:
An XSS like this is likely to **tarnish the trust between the Infogram.com brand and its customers**. A hacker can make an html page of just solely this embeded piece of HTML code. When a customer or user clicks on a link that would redirect the user to the embedded infogram.com page, it would seem as though infogram.com is not trustable by the user. Therefore, the brand gets less trusted over time. This is just one of many malicious acts a hacker can do.

## Attachments
- infogram-test.html
