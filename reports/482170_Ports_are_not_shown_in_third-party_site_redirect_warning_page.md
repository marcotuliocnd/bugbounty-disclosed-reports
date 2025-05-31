# Ports are not shown in third-party site redirect warning page.

## Report Details
- **Report ID**: 482170
- **URL**: https://hackerone.com/reports/482170
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-18T13:36:14.206Z
- **Disclosed**: 2019-04-12T13:53:13.206Z

## Reporter
- **Username**: b3f53dc9b2061f7df0c2ffd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Summary:** 
[Ports are not shown in third-party site redirect warning page]

Vulnerable Endpoint :- https://www.semrush.com/redirect?urlhttp://example.com:1337

**Description:** I noticed #311330 this report where you guys fixed a open redirect report by adding a external third-party site redirect warning page . It was a great fix . Although a issue caught in my eye . Urls contains a protocol and Ports . If I add a url with any other ports like 1337 then it's not shown in the external warning page what can be used to take a user to any other place then user expected to go .

Browsers Verified In: Chrome and Mozilla Firefox

## Steps To Reproduce:

Visit https://www.semrush.com/redirect?url=http://example.com:1337
You will see a warning page only saying about the domain but no warning about the ports like screenshot added below
But the source says it will take user to http://example.com:1337 not only example.com
<a href="http://example.com:1337" id="js-site-link" class="site_link" data-test-site-link="">
Go to site </a>

FIX :-
I can suggest possible fix here :-

Show the Ports of the inputted url in the Warning page .
Thanks

## Impact

I noticed in url= parameter many protocols can be used . Like I can use any port  and on my android if I visit https://www.semrush.com/redirect?url=http://example.com:1337 and click on Go to site then it will open my virtual environment's.

## Attachments
- Screenshot_2019-01-18-19-04-59-960_com.android.chrome.png
