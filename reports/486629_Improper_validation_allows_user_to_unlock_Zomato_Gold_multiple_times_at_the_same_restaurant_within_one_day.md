# Improper validation allows user to unlock Zomato Gold multiple times at the same restaurant within one day

## Report Details
- **Report ID**: 486629
- **URL**: https://hackerone.com/reports/486629
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-26T11:56:30.808Z
- **Disclosed**: 2019-01-28T08:06:46.809Z

## Reporter
- **Username**: dertajora
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Summary:** 
Using this vulnerability, a user can use his account to claim Zomato Gold benefit several times in the same restaurant within one day.  

**Description:** 
Based on Zomato Gold terms and condition, Zomato Gold can be used only once at each partner restaurant in a day. But I think it doesn't work that way.

I have found improper validation in Zomato Android app, on Zomato Gold feature. This vulnerability allows a user to claim Zomato Gold benefit ( 1+1 complementary food or 2+2 complementary drinks) in the same restaurant on a single day. This potentially could be abused by users to share his account to their friends, so they can get the Zomato Gold benefit without subscribing or doing multiple claim in one day. I think this bug potentially bring loss to Zomato if not fixed immediately.

Since I can't take a screenshot of my page while on Visit ID page, I use additional phone to take a picture and video, I hope you still understand.

**Platform(s) Affected:** [website/mobile app]
Android mobile app

## Steps To Reproduce:

  1. Open Zomato Android App (please make sure your account already subscribed to Zomato Gold)
  2. Find a restaurant with Zomato Gold badge or go to Gold Menu on Main Menu
F412873
  3. Click Enjoy your Gold Privilege
F412874
  4. Press the Confirm Unlock button
F412875
  5. Then you will get the Visit ID
F412876
  6. Do the step 2 - 6 again, Here is my second visit on the same restaurant within one day. If you look carefully, the Visit ID and the time is different with the previous one.
F412877

## Supporting Material/References:
Zomato Gold Terms and Conditions, please take a look at point number 3
F412882
https://www.zomato.com/conditions?country_id=94&page_type=SUBSCRIPTION&gold_plan_page=1

## Impact

As I said before, this vulnerability allows one user to claim Zomato Gold benefit several times at one parner restaurant. Lets say after visiting cafe A using Zomato Gold, he lends his account to his friend so his friend could also get the benefit of Zomato Gold without subscribing. He could also use it for himself if he use it for lunch and dinner on the same restaurant.

## Attachments
- WhatsApp_Image_2019-01-26_at_18.22.31.jpeg
- WhatsApp_Image_2019-01-26_at_18.43.55.jpeg
- WhatsApp_Image_2019-01-26_at_18.43.54.jpeg
- WhatsApp_Image_2019-01-26_at_18.43.54_(1).jpeg
- WhatsApp_Image_2019-01-26_at_18.43.53.jpeg
- Screen_Shot_2019-01-26_at_18.52.48.png
