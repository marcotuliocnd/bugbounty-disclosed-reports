# Bypassing Whitelist to perform SSRF for internal host scanning

## Report Details
- **Report ID**: 1747596
- **URL**: https://hackerone.com/reports/1747596
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-24T10:00:14.072Z
- **Disclosed**: 2023-03-24T23:04:16.511Z

## Reporter
- **Username**: imthatt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
Hello

I have managed to identify a misconfiguration on the server side request forgery protections under host geonode.state.gov/proxy/?url=

This is using a whitelist protection to ensure only allowed domains and requested in the url e.g. url=geonode.state.gov  sends a request.

The backend is configured differently to the front end and here we can trick the backend to send requests that are not in the whitelist and also include internal IPs for host scanning.

Using the URL  -- - GET  geonode.state.gov/proxy/?url=http://burpcollablink\@geonode.state.gov   will send a request HTTP from the server to your burp collaborator URL, see screenshot and the response will be displayed on the response page.

changing the URL to geonode.state.gov/proxy/?url=http://169.254.169.254\@geonode.state.gov identifies the alive host 169.254.169.254 which is the internal AWS instance as the response shows "404 NOT FOUND". This shows the host is alive on the IP, but because the server is converting the \ to \/@geonode.state.gov it is sending the request http://169.254.169.254\/@geonode.state.gov which is obviously not an existing endpoint of 169.254.169.254, but it shows this IP address and host are alive. To confirm do  http://169.254.169.251\/@geonode.state.gov  and you will not get a response, showing the iP host is not alive

We can use this information to conduct internal host scans to identify alive hosts across the internal network, monitoring responses back. This is a low issue at this stage as no RCE has been achieved, but it has still shown a misconfiguration in the SSRF protection.

The misconfiguration exists because the front end seeing the whitelist host geonode.state.gov exists in the URL, but the backend is parsing this as a credential host, but the \ before on the backend terminates the HTTP lookup and will send a request to the host identified before the \.

## Impact

ssrf misconfiguration allowing internal host scanning on the internal network

## Attachments
- ssrf.PNG
