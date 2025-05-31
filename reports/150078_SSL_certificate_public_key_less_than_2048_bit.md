# SSL certificate public key less than 2048 bit

## Report Details
- **Report ID**: 150078
- **URL**: https://hackerone.com/reports/150078
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-08T19:35:31.552Z
- **Disclosed**: 2016-08-18T01:18:31.094Z

## Reporter
- **Username**: proxynwh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
One of the SSL certificates used by your SSL server (On your personal website: https://iandunn.name/ ) contains a public key less than 2048 bit long. 

New Standard for SSL Certificates Industry standards set by the Certification Authority/Browser (CA/B) Forum require that certificates issued after January 1, 2014 MUST be at least 2048-bit key length.1 As computer power increases, anything less than 2048-bit certificates are at risk of being compromised by hackers with sophisticated processing capabilities. The cybersecurity industry is moving to stronger 2048-bit encryption to help preserve internet security.

Any certificate with a public key less than 2048-bit are at risk of being compromised by hackers with sophisticated processing capabilities.

If you have any 1024-bit certificates or certificates with less than 2048-bit key length, you will need to migrate to 2048-bit key length.

http://www.geotrust.com/resources/2048-bit-compliance/



## Attachments
No attachments
