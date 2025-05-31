# IDNs displayed in unicode

## Report Details
- **Report ID**: 266454
- **URL**: https://hackerone.com/reports/266454
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-06T20:31:00.724Z
- **Disclosed**: 2017-10-25T23:25:36.372Z

## Reporter
- **Username**: hk755a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
Hello Quora,

Please refer https://en.wikipedia.org/wiki/Internationalized_domain_name to know more about IDNs.

The IDN (Internationalized Domain Name) : http://ebаy.com/
is a homograph for the latin ebay.com. if you click that first link, you might think that you are going to ebay.com but in fact, you are going to a homograph url http://xn--eby-7cd.com/

When an IDN is posted on Quora it displays it in Unicode. It would be safer to represent the Punycode version of the URL so that it would be apparent to the users that something wierd is going on. i.e show http://xn--quor-3ld.com/ instead of http://quorα.com

I have tried this on Quora Android Application and Web browser on my android phone. The screenshot has been attached.

A bad guy can exploit this vulnerability by putting up a spoof site behind one of these IDN links,posting the link anywhere on quora  and the user or the quora moderator/admin opens and carelessly enters his credentials there. 

Quora being a social networking site involves a lot of user conversation. Such an attack may affect a lot of users at once having a high impact and loss.


STEPS TO REPRODUCE:

1.) Copy and paste the links in the PAYLOAD.txt file attached here.
2.) Paste it anywhere. Most probably in the answers section.
3.) Open Quora app or open Quora.com on phone and see the link. 


Facebook,hackerone,crowdcurity,Yelp and many major sites have implemented code to block such attacks.They show the punycode version of the IDN url.

## Attachments
- PAYLOAD.txt
- QUORA_ANDROID_APP_IDN_POC.png
