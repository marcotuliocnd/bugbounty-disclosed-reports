# Stored XSS on Add Event in Calendar

## Report Details
- **Report ID**: 300532
- **URL**: https://hackerone.com/reports/300532
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-26T03:48:20.976Z
- **Disclosed**: 2018-09-01T06:02:23.333Z

## Reporter
- **Username**: gamliel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Greetings **In crayons we trust**

Hello @Concrete5 Team.

While checking the Hacktivity in your HackerOne Program I saw many reports regarding to **XSS** thus I will omit the vulnerability description I'm going to report now.

After downloaded **Concrete5 8.3.1 released at 12/20/17**, while searching for some fields where I could insert a XSS payload I stopped into: Dashboard > Calendar & Events

###Steps to reproduce:
1. Open your favorite updated web browser (Firefox or Chrome)
2. Log into your Concrete5 instance as **admin**
3. For the ease create an user (maybe named **user2**) and add it to **Administrators** group
4. Open other browser window in Private or Incognito mode and log in as **user2**
5. As **user2** go to **Dashboard > Calendar & Events**
6. Add a Calendar and named, for example **User2 Calendar**
7. Now, click on **Add Event** button and schedule an event
8. In the **Name** field type something like this: ">TEST<img src=K onerror={here goes mad js code}>
9. My inoffensive pop-up payload: ` ">TEST<img src=K onerror=prompt(document.domain)>` {F249467}
10. Click on **Save & Close** button
11. The Prompt box will appear in the context of user2 browser showing your domain {F249468} (close it)
12. Click on that event, select "Edit" and now click on **Publish Event** in order to make it public
13. Now go to the main web browser window where **admin** user is logged
14. Go to  **Dashboard > Calendar & Events**
15. The Prompt box will appear showing the domain in the **admin** browser {F249470}

I made a 11 min PoC video: 'F24972'

## Impact

In **Step 3** I mentioned "For the ease" creating an user and add it to **Administrators** group. This intended behavior is in order to the new user has access to add Calendars and create Events but, for the long way or in other scenario, an administrative user can grant access to Registered Users to add calendars and events although a calendar could be in public pages if the page allows to show a calendar.

Even, if the cookie can't be stolen because it has set the `HttpOnly` flag {F249469} and it could not be directly accessed via client-side JavaScript, If malicious user can insert JavaScript code in a field where he is allowed to. The limit of mad actions is the attacker's imagination.

## Attachments
- event_payload.png
- event_xss_user2.png
- event_httponly-flag.png
- event_xss_admin.png
- XSS_on_AddEvent_Concrete5.webm
