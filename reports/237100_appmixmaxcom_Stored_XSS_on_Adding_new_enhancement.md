# [app.mixmax.com] Stored XSS on Adding new enhancement.

## Report Details
- **Report ID**: 237100
- **URL**: https://hackerone.com/reports/237100
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-06T03:29:54.853Z
- **Disclosed**: 2017-06-13T05:30:36.822Z

## Reporter
- **Username**: sh3r1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hi Mixmax team,

Today I just found a Stored XSS on app.mixmax.com by adding a new enhancement. Just follow the steps below to reproduce this bug.

**Vulnerable URL**
[APP MIXMAX - Settings - Integrations & API](https://app.mixmax.com/dashboard/settings/integrations)

**Payload**
"><img src=x onerror=alert(document.domain)>


**Steps to reproduce**
- Go to the [Vulnerable URL](https://app.mixmax.com/dashboard/settings/integrations).
- Click Integrations & API then click Add Enhancement.
- In the **Name Field** just add the **Payload** into it. add what ever you want in to the other fields then click **Add Enhancement**

- after you  add the new enhancement. the prompt will show like this: F191647

- and then we can share this New Enhancement to the other users or a team by clicking the share icon beside to our newly added enhancement. F191648

- add a user or a team to share this enhancement. F191655 

- after you share this to the use users, the users will recieve an email regarding to the enhance that you have been shared to them.  F191656
  
 when the users or the the victim accept the enhancement, it will redirect to the **Vulnerable URL** and showing that our payload are working.

XSSED!
F191663


Regards,
Sh3r1

## Attachments
- app-mixmax-poc-1.PNG
- app-mixmax-poc-2.PNG
- app-mixmax-poc-3.PNG
- app-mixmax-poc-4.PNG
- app-mixmax-poc-5.PNG
