# External Service Interaction | https://█████████.mil

## Report Details
- **Report ID**: 997988
- **URL**: https://hackerone.com/reports/997988
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-05T04:16:22.882Z
- **Disclosed**: 2020-10-16T19:45:01.388Z

## Reporter
- **Username**: x3ph_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

I am able to trick web server ███████.mil into making DNS and HTTP requests to my vps server and burp collaborator.

Walkthrough Section:

1. Create an account using the registration form https://████████.mil/█████/accounts/register/

███████

2. Provide the required information to create a POST request.

████████

3. Intercept the request and add the following headers below and add your external webserver. You will have the ability to send requests as the web server as a proxy.

X-Forwarded-Host: <ExternalWebServer>
X-Host: <ExternalWebServer>
X-Forwarded-Server:  <ExternalWebServer>

███

█████

4. I am able to confirm I received not only DNS Requests but also HTTP requests from ██████████.mil. I have also attached a spreadsheet that shows every request i made and what IP address they originated from. The screen shot below on the left window is my burp collaborator you can see the log of interactions. On the right is my vps server.. I setup my HTTP Server and i made multiple requests from that webserver, you can see the interaction as well.

████████

## Impact

The ability to send requests to other systems can allow the vulnerable server to be used as an attack proxy. By submitting suitable payloads, an attacker can cause the application server to attack other systems that it can interact with. This may include public third-party systems, internal systems within the same organization, or services available on the local loopback adapter of the application server itself. Depending on the network architecture, this may expose highly vulnerable internal services that are not otherwise accessible to external attackers.

## Step-by-step Reproduction Instructions

1. Navigate to https://██████.mil/███/accounts/register/?██████████
2. Following the walkthrough section above

## Suggested Mitigation/Remediation Actions

If this is intended behavior you should be aware of the types of attacks that can be performed via this behavior and take appropriate measures. These measures might include blocking network access from the application server to other internal systems, and hardening the application server itself to remove any services available on the local loopback adapter.

If the ability to trigger arbitrary external service interactions is not intended behavior, then you should implement a whitelist of permitted services and hosts, and block any interactions that do not appear on this whitelist.

Resources:

https://portswigger.net/kb/issues/00300200_external-service-interaction-dns#:~:text=Description%3A%20External%20service%20interaction%20(DNS,a%20web%20or%20mail%20server.&text=The%20ability%20to%20send%20requests,used%20as%20an%20attack%20proxy.

## Impact

The ability to send requests to other systems can allow the vulnerable server to be used as an attack proxy. By submitting suitable payloads, an attacker can cause the application server to attack other systems that it can interact with. This may include public third-party systems, internal systems within the same organization, or services available on the local loopback adapter of the application server itself. Depending on the network architecture, this may expose highly vulnerable internal services that are not otherwise accessible to external attackers.

## Attachments
No attachments
