# [Critical] Subdomain Takeover

## Report Details
- **Report ID**: 163790
- **URL**: https://hackerone.com/reports/163790
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-27T10:36:24.309Z
- **Disclosed**: 2016-09-20T22:46:35.352Z

## Reporter
- **Username**: rootnp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Your Subdomains are pointing to unconfigured heroku app.
You should immediately remove the DNS-entry. Any One Can Claim That Domain , Please
Read The Advisory Below.


::: Nslookup of Subdomains Not Claimed :::::
i)  0x00hack3r@pirateking:~ % nslookup bugs.instacart.com
Server:		192.168.1.11
Address:	192.168.1.11#53

Non-authoritative answer:
bugs.instacart.com	canonical name = akita-7862.herokussl.com.
akita-7862.herokussl.com	canonical name = elb070827-1683851829.us-east-1.elb.amazonaws.com.
Name:	elb070827-1683851829.us-east-1.elb.amazonaws.com
Address: 50.17.211.105
Name:	elb070827-1683851829.us-east-1.elb.amazonaws.com
Address: 54.225.201.77
Name:	elb070827-1683851829.us-east-1.elb.amazonaws.com
Address: 23.23.106.52

ii) 0x00hack3r@pirateking:~ % nslookup atlas.instacart.com
Server:		192.168.1.11
Address:	192.168.1.11#53

Non-authoritative answer:
atlas.instacart.com	canonical name = tochigi-6557.herokussl.com.
tochigi-6557.herokussl.com	canonical name = elb070826-1853155728.us-east-1.elb.amazonaws.com.
Name:	elb070826-1853155728.us-east-1.elb.amazonaws.com
Address: 54.204.29.82
Name:	elb070826-1853155728.us-east-1.elb.amazonaws.com
Address: 107.20.229.78
Name:	elb070826-1853155728.us-east-1.elb.amazonaws.com
Address: 54.235.189.162


Subdomain pointing to a non-existing Heroku app showing: there is no app configured at that hostname


I have attached screenshots : For the impacts, vuln see : https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/


## Attachments
- Screenshot_from_2016-08-27_16-19-25.png
- Screenshot_from_2016-08-27_16-18-40.png
