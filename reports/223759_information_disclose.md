# information disclose

## Report Details
- **Report ID**: 223759
- **URL**: https://hackerone.com/reports/223759
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-25T13:17:39.396Z
- **Disclosed**: 2017-04-25T13:21:20.098Z

## Reporter
- **Username**: abdul1ah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello  Team . 
I Reported a  issue - disclosure SERVER Version !!

when i interrupt this https://demo.nextcloud.com/ Request , its  disclosure The  server version   Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.1e-fips
As you can See this Pic , or you can Interrupt the url useing Any Proxy tools like Burp Suite.  

So it's Mostly important to keep secret of server version. & Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

Importatnt Things is An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified. 

Hope You guyz Fix This Probleam As soon As possible 
reference::https://hackerone.com/reports/141125
		https://hackerone.com/reports/135782
		https://hackerone.com/reports/167041
			
	
Thanks,
Best Regards ,
Mohammad Abdullah

## Attachments
- nextcloud_poc.png
