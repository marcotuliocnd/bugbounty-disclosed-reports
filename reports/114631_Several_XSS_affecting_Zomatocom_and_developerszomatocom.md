# Several XSS affecting Zomato.com and developers.zomato.com

## Report Details
- **Report ID**: 114631
- **URL**: https://hackerone.com/reports/114631
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-04T12:59:43.501Z
- **Disclosed**: 2016-08-02T03:51:51.427Z

## Reporter
- **Username**: harry_mg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi there, I have found several XSS in Zomato.com and developers.zomato.com

A. Steps to reproduce:
1. Go to zomato.com
2. Look for any restaurant
3. Click "Write review" and enter the payload as your review
                                             (<img src=x onerror=alert(document.domain)>)
4. Click "Publish review" . XSS pop up

B. Now in developers.zomato.com:
1. Go to developers.zomato.com
2. Go to "widgets" tab
3. Look for "Restaurant Search" widget and click "Add Widget"
4. Now a window will open (restaurant search), on the left side, you will see "Search for restaurant, cuisine or a dish" now, enter the payload   (<img src=x onerror=alert(document.domain)>) in the seachbar, XSS popup.

C. developers.zomato.com (II)
1. Go to developers.zomato.com
2. Go to "widgets" tab
3. Look for "Foodie Index Widget"
4. Click "add widget"
5. In the longitude and latitude, enter the XSS payload
 (<img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>). 
6. XSS popup

I hope you fix this since this are affecting several zomato users.
Thanks

## Attachments
- Screen_Shot_02-04-16_at_08.48_PM.PNG
- Screen_Shot_02-04-16_at_08.47_PM.PNG
- Screen_Shot_02-04-16_at_08.59_PM.PNG
