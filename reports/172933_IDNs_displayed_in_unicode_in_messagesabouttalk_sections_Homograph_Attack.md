# IDNs displayed in unicode in messages/about/talk sections (Homograph Attack)

## Report Details
- **Report ID**: 172933
- **URL**: https://hackerone.com/reports/172933
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-29T15:37:28.605Z
- **Disclosed**: 2017-11-09T19:54:03.237Z

## Reporter
- **Username**: hk755a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hello Yelp,

Please refer https://en.wikipedia.org/wiki/Internationalized_domain_name to know more about IDNs.

The IDN (Internationalized Domain Name) : http://ebаy.com/
is a homograph for the latin ebay.com. if you click that first link, you might think that you are going to ebay.com but in fact, you are going to a homograph url http://xn--eby-7cd.com/

When such an IDN is posted on Yelp (for ex at the about me page,Talk section,Messages etc.). ,it displays IDN in Unicode. It would be safer to represent the Punycode version of the URL so that it would be apparent to the users that something wierd is going on. i.e show  http://xn--eby-7cd.com/ instead of http://ebаy.com/

A bad guy can exploit this vulnerability by putting up a spoof site behind one of these IDN links,posting the link anywhere on yelp (The talk section can be a nice place) and the user or the yelp moderator/admin opens and carelessly enters his credentials there.

Facebook,hackerone,crowdcurity and many major sites have implemented code to block such attacks.They show the punycode version of the IDN url.

More info:
http://www.charset.org/punycode.php?encoded=http%3A%2F%2Fxn--eby-7cd.com%2F&decode=Punycode+to+normal+text

Few more Examples:
1) https://www.уelp.com/
2) https://www.yelp.com/

They both appear to be same when posted on yelp but actually 2nd is the original one and the 1st is actually https://www.xn--elp-cfd.com/

For reproduction paste https://www.xn--elp-cfd.com/ anywhere on yelp and post it.It would appear as yelp.com only



## Attachments
- yelp.png
