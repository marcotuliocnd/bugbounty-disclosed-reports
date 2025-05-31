# Reflected/Stored XSS on duckduckgo.com

## Report Details
- **Report ID**: 1110229
- **URL**: https://hackerone.com/reports/1110229
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-24T15:19:33.483Z
- **Disclosed**: 2021-04-10T18:15:50.202Z

## Reporter
- **Username**: monke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
Hi DuckDuckGo,

While browsing normally (since I use DuckDuckGo on a daily basis), I discovered an interesting stored XSS on the duckduckgo main search engine. A payload that somebody had left on urbandictionary.com had triggered a HTML injection, and a stored XSS as a result. 

**Steps to Reproduce**
1. Search the following in the searchbar of DuckDuckGo: `urban dictionary "><img src=x<`
2. A payload left by someone else will render itself and fire in the main DuckDuckGo page.
3. It is also possible to visit the page via the DuckDuckGo URL as [such](https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web) and the XSS will trigger.

**POC**
- The page itself renders HTML. The payload fires.
- {F1207848}
- {F1207849}

## Impact

There are several impacts here.
- Firstly, the DuckDuckGo URL serves as a payload, because simply visiting the page with the right search parameter triggers the XSS, although the search parameters themselves do not directly trigger it. 
- Secondly, the XSS is stored in the search results, so this can be considered to be Stored XSS.
- It is possible to execute any Javascript via the main DuckDuckGo page.

If you have any questions or require clarification, I am happy to help.
Cheers,
PMOC

## Attachments
- evidence1.png
- evidence2.png
