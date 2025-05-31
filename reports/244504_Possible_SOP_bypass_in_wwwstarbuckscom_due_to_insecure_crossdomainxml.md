# Possible SOP bypass in www.starbucks.com due to insecure crossdomain.xml

## Report Details
- **Report ID**: 244504
- **URL**: https://hackerone.com/reports/244504
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-29T20:05:48.533Z
- **Disclosed**: 2017-09-23T20:36:57.779Z

## Reporter
- **Username**: jackb898
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hello. I was penetration testing your website, and noticed that your crossdomain.xml file allowed many sites access. I went through and, for all the sites that had *.website.com with them, I scanned them for subdomains.

I found that a subdomain for ███████.com (a site in your crossdomain.xml as *███████), m███████, was vulnerable to takeover. 

I'm not going to take it over since they do not have a white hat hacker program, but if someone were to take it over, they could make flash files on it to retrieve sensitive information from starbucks.com, and do it with no issue. Another factor that makes it even worse is that it's possible to use any headers also (<allow-http-request-headers-from domain="*" headers="*"/>).

It's similar to if your site had this line in the crossdomain.xml: <allow-access-from domain="*" />

SCENARIO:
This is a scenario of how it would most likely be exploited
1. A black hat is trying to hack into Starbucks
2. He goes to the crossdomain.xml file looking for <allow-access-from domain="*" />, but he notices lots of different websites are allowed access
3. He decides to check the domains with *. before them for vulnerable subdomains
4. He finds m██████, and notices *███████ has access
5. He takes over m██████ and uploads a malicious flash file to send HTTP requests and see their responses. 


HOW TO FIX THIS
Pretty simple, obvious fix, but you have two routes you can take for it.
First option: You can just remove <allow-access-from domain="*████████" /> from your crossdomain.xml file. (I didn't find any other subdomains vulnerable to takeover that were in there)

Second option: You can talk to ███████, the company that owns █████.com, and tell them to disconnect the DNS records linking m████████ and m██████.███

MORE INFORMATION
Here is more information on how it could be exploited: http://resources.infosecinstitute.com/bypassing-csrf-protections-fun-profit/ (read between Abusing CORS via Flash Files down to Bypassing XMLHttpRequest Header Validation)



Thanks,
Jack


## Attachments
No attachments
