# CRITICAL-CLICKJACKING at Yelp Reservations Resulting in exposure of victim Private Data (Email info) + Victim Credit Card MissUse. 

## Report Details
- **Report ID**: 355859
- **URL**: https://hackerone.com/reports/355859
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-22T11:27:00.031Z
- **Disclosed**: 2020-08-21T20:51:23.801Z

## Reporter
- **Username**: hk755a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Please have a look at this interesting article with precise explanation about Click-jacking security flaw:
https://www.linkedin.com/pulse/20141202104842-120953718-why-am-i-anxious-about-clickjacking/

In Yelp platform the response headers of the Reservation page does not contain the X-Frame-Options header, thus allowing malicious actors to embed these pages as hidden i-frames on some external or their own innocuous looking website. 
Upon successful exploitation the victim would have made unintentional reservation to some restaurant/bar and his Email Id/Mobile Number would have been shared with the business. 
All this would  happen without victim's  knowledge or consent.

Here's how a sample Reservation page looks like:
███

REQUEST RESPONSE HEADERS OF A RESERVATION PAGE:
██████

Please note the missing X-Frame-Options header in the response headers.

#POC:
For POC and steps to reproduce please watch the video 

#EXPLOIT SCENARIOS:
Please look at the different scenarios this could be exploited :

#==>(1) The attacker may himself register a business at yelp, copy and embed his own reservation url as hidden i-frame. Make reservation in the background upon victim's click. He gains email/mobile of the victim account.
#==>(2) He may reserve a table of some business that charges upon cancellation and the victim may face monetary loss. 
#==>(3) He may target a business and  try to restrict all the genuine bookings. It would be possible to do so by booking all table slots of different timings from all the different visitors that are coming to his malicious but genuine looking website.

The impact of this vulnerability depends on the number of visitors attacker might be able to bring to his website. This is not a very big deal in the presence of huge social media websites nowadays. Or he may paste link to his website somewhere on yelp (review/about/talk etc sections) platform itself so as to bring authenticated yelp users to his website.

## Impact

While the  overall risk may only be a medium rating; the impact is high as the vulnerability affects both the yelp users and also business owners

#The vulnerability impacts the victim in the following ways:
==>1.) Loss of Confidentiality: Private info such as Email/phone is disclosed
==> 2.) Unauthorized Reservations from User Account: This certainly is not wanted by any user.
==> 3.) Monetary loss upon Cancellation of reservation: Some businesses say they would charge upon 
cancellation of reservation.
==> 4.) Apart from this client's trust on Yelp platform is also lost.

#The vulnerability impacts the business owners in the following ways:
==>1.) Fake reservations may restrict genuine reservations:
Such Fake reservations may restrict genuine users from booking tables. And on the other end the business owners have no way to distinguish between fake and genuine ones.
This leads to customer/monetary loss to business owners itself.

## Attachments
No attachments
