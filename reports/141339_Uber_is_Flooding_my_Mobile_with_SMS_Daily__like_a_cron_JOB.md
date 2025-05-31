# Uber is Flooding my Mobile with SMS Daily  like a cron JOB

## Report Details
- **Report ID**: 141339
- **URL**: https://hackerone.com/reports/141339
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-27T03:43:27.959Z
- **Disclosed**: 2016-07-25T22:55:24.449Z

## Reporter
- **Username**: anish2good
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
The Issue is with the design of sending SMS by the uber referrals system, and every day it's flodding my phone number with driver invitaion message 

To reproduce this scenario i have  Fuzz the below request Through OWSAP Zap I fuzzed for 10,000 requests , keep the same Phone number (I have used my number), After 20 tries uber will send message the Limit is over ,  you will recieve 60 SMS since the meessage size is more it will come in three part , 

Now the real proble will start from next and consecutive days, Every day i'm recieving 60 SMS starting at 9:30 AM IST 
------------------------------

```
POST https://partners.uber.com/driver_invitations HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: br
Content-Type: application/json; charset=utf-8
X-Requested-With: XMLHttpRequest
Referer: https://partners.uber.com/referrals/
Content-Length: 137
Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Connection: keep-alive
Host: partners.uber.com

{"_csrf_token":"1464319290-01-TE_leQUArIag4-5PKfW4wUkBccZdc_thW8kqNBmFFu4=","emails":[],"mobiles":["+████████"],"source":"dashboard"}
```

>>>>>>Attack Scenarion: A bad Victim can use this tool to irritate the other user (irrespective of their postion), by creating fake profiles and let's Uber take care of sending 60 SMS every day (NON STOP)  and finaly it will lead bad Impression on the UBER and 


## Attachments
- SMS_FLOOD_Referal.png
