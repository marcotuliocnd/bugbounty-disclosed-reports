# Stored XSS on Add Calendar

## Report Details
- **Report ID**: 300571
- **URL**: https://hackerone.com/reports/300571
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-26T09:25:29.489Z
- **Disclosed**: 2018-09-01T06:03:35.830Z

## Reporter
- **Username**: gamliel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Greetings, **(There is no soup like crayons soup with vegetables)**.

Hello @Concrete5 Team.

Like my last report #300532 I found other Stored XSS vulnerability in your nice CMS. If you don't mind I will omit what Stored - XSS is and its description, hope everything is fine in your side about that :).

The testing scenario is the same: **Concrete5 8.3.1 released at 12/20/17**, while searching for some fields where I could insert a XSS payload I stopped into: **Dashboard > Calendar & Events > Add Calendar**

###Steps to reproduce:
1. Open your favorite updated web browser (Firefox or Chrome)
2. Log into your Concrete5 instance as **admin**
3. For the ease create an user (or use an existent one) and add it to **Administrators** group
4. Open a new window browser in Private or Incognito mode and log in as the new user (**user2**)
5. As **user2** go to **Dashboard > Calendar & Events**
6. Now, click on **Add Calendar**
7. In **Calendar Name** type something like: **TEST<img src=K onerror={here goes js payload}>**
8. My js payload:
 ` Hi, Admin<img src=K onerror=prompt(document.location) width=1px height=1px> ` {F249506}
(If there's a public page containing a Calendar Event block or custom code that can render a specific calendar the Stored XSS would be public to and all a malicious user have to do is in _Enable Additional Event Details_ chose **Link to an existing page**)
9. Now, click on **Add Calendar** button
10. In **user2** browser the prompt box is showing the page's document location {F249510} (close it)
11. Now, go to the window browser where **admin** user is logged
12. Go to  **Dashboard > Calendar & Events**
13. Select "**Hi, Admin**" Calendar {F249509}
14. The prompt box will appear in the context of **admin** user browser {F249507}

## Impact

Again, in **Step 3** I mentioned "for the ease" creating an user and add it to **Administrators** group for the ease of give to the new user quick access to add Calendars but, in other scenario, an administrator can grant access to (for example) **Registered Users** to add Calendars. Remember, a calendar could be linked to existing public pages {F249480} if the page is previously designed to show a calendar too.

Regarding to impact, even if the cookie can't be stolen to takeover the session or account because it has set the `HttpOnly` flag {F249505} and it cannot be directly accessed via client-side JavaScript, If malicious user can insert JavaScript code in a field where he is allowed to. The limit of mad actions is the attacker's imagination.

Some (mad) actions could be:
* setting a Javascript keylogger
* JavaScript can read and make arbitrary modifications to the browser’s DOM (within the page that JavaScript is running)
* Can [Manipulate the browser history](https://developer.mozilla.org/en-US/docs/Web/API/History_API) and [Use Javascript to read a users browser history](https://web.archive.org/web/20170429124134/http://bhavin.directi.com/using-javascript-to-read-a-users-browser-history/)

As said before, the limit is attacker creativity. I hope it helps to improve Concrete5 CMS.

Kind regards,
**Gamliel Hernandez**.

## Attachments
- Calendar_XSS_Link-to-page.png
- Calendar_httponly-flag.png
- Calendar_XSS_AddCalendar-field.png
- Calendar_XSS_Calendar-XSSED-Selected.png
- Calendar_XSS_Link-to-page.png
- Calendar_XSS_Select-HiAdmin-Calendar.png
- Calendar_XSS_User2-browser.png
