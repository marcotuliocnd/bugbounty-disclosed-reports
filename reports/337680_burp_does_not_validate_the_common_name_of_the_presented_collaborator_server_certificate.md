# burp does not validate the common name of the presented collaborator server certificate

## Report Details
- **Report ID**: 337680
- **URL**: https://hackerone.com/reports/337680
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-14T09:38:54.788Z
- **Disclosed**: 2018-06-13T16:14:32.117Z

## Reporter
- **Username**: morisson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Burp is not validating correctly if the presented certificate in collaborator server. It warns if it is a self signed one, but if it is a legitimate one (any valid CA), it appears not to be checking the CN.


This is an issue for the polling service, since it allows for the connection to be intercepted and burp will happily send through the polling request.

For PoC, just use a valid certificate for a completely different domain than the one used on the burp collaborator server, and connect to it. All checks will be ok, and when polling the server (using the scanner for instance), there's no warning or failure, and burp connects.
I haven't extensively tested all possible options, but using a valid wildcard certificate from a totally different domain works.

(note: there's also the functional bug of burp stating the connections are ok, but the target being tested will then fail to connect to any TLS service on the collaborator)

## Impact

If the attacker is able to perform a MITM on the tester (either adjacent to him, or to the collaborator server, or somewhere along the path), he will be able to intercept the HTTPS polling connection to the collaborator server, and potentially obtain the records.

## Attachments
- collab_config.png
- wrong_domain_certificate_ok.png
- tls_error.png
- not_this_domain.png
