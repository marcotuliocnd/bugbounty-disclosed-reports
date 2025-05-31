# [Not just a server configuration issue] Full Path Disclosure 

## Report Details
- **Report ID**: 153628
- **URL**: https://hackerone.com/reports/153628
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-25T07:09:54.407Z
- **Disclosed**: 2016-08-24T18:48:00.764Z

## Reporter
- **Username**: ahsan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hey, I've just found a 'full path disclosure' in basic-google-maps-placemarks, so it's not just a server configuration issue! I've tested it on different servers (including windows, ubuntu, CentOS etc..) 

#PoC
So, if we visit `wp-content/plugins/basic-google-maps-placemarks/unit-tests.php` it is clearly disclosing the full path as you can see in the following links:

- http://jazzalajmi.com/espace-pro/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php 
- http://ywamnorthwoods.org/setapart/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.t1fx.com/teamt1fx/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.processinstruments.net/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://faas-bh.com/001/03udruzene/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.dominihost.com.br/1line/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.dominihost.com.br/1line/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php

And eventually, in my localhost too:


{F107116}


Well, not all websites using basic-google-maps-placemarks, have a server configuration issue, so it's probably an issue in your plugin! :-)

###Impact:
Well, the possible impact is that if attacker gets into the server using other website, he might symlink and also get access to the site using that full path! 

>> *Request: Still if you are not going to fix this, please close as informativer*

Cheers,
Ahsan

## Attachments
- 2016-07-25_00h04_51.png
