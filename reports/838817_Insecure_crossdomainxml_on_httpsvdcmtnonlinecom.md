# Insecure crossdomain.xml on https://vdc.mtnonline.com/

## Report Details
- **Report ID**: 838817
- **URL**: https://hackerone.com/reports/838817
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-04T13:04:40.446Z
- **Disclosed**: 2022-03-20T05:31:53.400Z

## Reporter
- **Username**: xlife
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hi,

https://vdc.mtnonline.com/crossdomain.xml contains the following xml file:

```

<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
	<cross-domain-policy>    
	<site-control permitted-cross-domain-policies="all"/>    
	<allow-access-from domain="*"  secure="false" to-ports="*"/>
	<allow-http-request-headers-from domain="*" headers="*"/> 
	</cross-domain-policy>

```

## Impact

This will make any one able to receive content from https://vdc.mtnonline.com/ , attacker can steal CSRF tokens and user PII.

More information about this issue is available here:

https://medium.com/@x41x41x41/exploiting-crossdomain-xml-missconfigurations-3c8d407d05a8

Best regards,
Vishu10x00 ❤️

## Attachments
No attachments
