# Administrator access to a Django Administration Panel on *.sc-corp.net via bruteforced credentials

## Report Details
- **Report ID**: 128114
- **URL**: https://hackerone.com/reports/128114
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-04T06:29:31.452Z
- **Disclosed**: 2016-07-14T21:08:01.443Z

## Reporter
- **Username**: shubs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hey team,

While doing some recon for Snapchat's domains, I came across a particular domain of interest - `sc-corp.net`. It seems that this domain hosts a lot of Snapchat's internal tools, web applications and staging environments such as Phabricator and other administration panels.

From analyzing SSL certificates, I came across the following IP address which contained a wild card common name of `*.sc-corp.net`:

`https://146.148.42.38/`

Upon visiting the above IP address, I was prompted with a basic authentication prompt. Even though I clicked cancel and did not authenticate to the panel, the Django REST API panel was returned - albeit in an unauthenticated state.

In order to gain authenticated access to the REST API and the Django administration panels, I ran a small scale bruteforce against the login endpoint located at `https://146.148.42.38/api-auth/login/`. The following HTTP request was used to perform the bruteforce attack in Burp Intruder:

```
POST /api-auth/login/ HTTP/1.1
Host: 146.148.42.38
Connection: close
Content-Length: 108
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: https://146.148.42.38
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
DNT: 1
Referer: https://146.148.42.38/api-auth/login/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: csrftoken=Gt5IRFhlh8BekC11btkUdo8doBniN2pJ

csrfmiddlewaretoken=Gt5IRFhlh8BekC11btkUdo8doBniN2pJ&next=%2F&username=admin&password=§password§&submit=Log+in
```

With a password list of approximately 10,000, I was able to determine the credentials for the Django administration panel after a total of 2459 requests. I've attached a screenshot of the Burp Intruder window showing the successful bruteforce attack (burp_intruder_snapchat_django.png).

Since I now had the credentials (username: `admin` and password: `research`), I was then able to use them to access the Django administration panel located at `https://146.148.42.38/admin/`.

I've attached some screenshots to show the level of access I obtained to the administration panel (snapchat_django_admin_panel_[0-3].png).

Additionally, with the credentials bruteforced, I was able to interact with the Django REST API without any restrictions - i.e. I was able to add new users and groups via the API. Screenshots attached (snapchat_django_rest_api_[0-3].png).

I made no further attempts to escalate privileges on the machine, nor attempted to gain a reverse shell.

I believe that since this machine's SSL certificate's CNAME was `*.sc-corp.net`, it's likely that there is an actual subdomain that is pointing to this IP. While I was unable to determine the subdomain's name via bruteforcing or enumeration, if there is a valid subdomain pointing to this IP, the severity of this issue could be much higher.

I also assume that since it's most likely within the `sc-corp.net` scope, the machine itself might have privileged access to the Snapchat internal network on Google Cloud. If I were a malicious attacker, I would attempt to first gain a shell on this machine using my now privileged access and then attempt to pivot onto the Snapchat internal network.

An alternate attack route would be to gain persistent cross-site scripting on the machine with my administrative access and then perform phishing / cookie stealing attacks for applications that run on a subdomain of `sc-corp.net`. For example, there's Phabricator running on `ph.sc-corp.net` and this would be a prime target for an attacker to gain access to. This would require the attacker to know the subdomain on `sc-corp.net` that points to `146.148.42.38`.

Please don't hesitate if there are any questions or if you require any further information.

Cheers
Shubs



## Attachments
- burp_intruder_snapchat_django.png
- snapchat_django_admin_panel_2.png
- snapchat_django_admin_panel_3.png
- snapchat_django_admin_panel_1.png
- snapchat_django_rest_api_3.png
- snapchat_django_rest_api_2.png
- snapchat_django_rest_api_1.png
