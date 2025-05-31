# Ability to Disable the Login Attempt of any Shopify Owner for 24 hrs  (Zero_Click)

## Report Details
- **Report ID**: 1406495
- **URL**: https://hackerone.com/reports/1406495
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-21T14:12:27.910Z
- **Disclosed**: 2022-02-15T06:20:35.527Z

## Reporter
- **Username**: saurabhsankhwar3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Team,

I Found a Bug in which Hacker Have Ability to Disable the Login Attempt of any Shopify Owner With (Zero_Click)

Summary:
----------


Proof of Concept;
-------------------

Credentials:
-------------
Victim = ███████.com (████████)

Hacker = █████████.com 

Victim Sceanrio:
-----------------
Step 1 : Victim Login to his Account (████.com)

Step 2 : For Better Security of his Account ---------> Victim Activate the 2 Factor Authentcation ( Via Mobile Phone Number)

Step 3 : 2 FA Activated Successfully -----------> Victim Logout

Attacker Scanario: (Incognito Tab)
------------------
Step 1 : Hacker Make a New Account  in shopify (███████.com)

Step 2 : Hacker Go to Manage Account -------> Choose to Activate 2 FA 

Step 3 : Hacker Enter his Mobile Number (█████████) --------> Capture the Request in Burpsuite

Step 4 : Hacker Change the Mobile Number (████) to (███████) --------> Forward the Request

Step 5 : Hacker Logout -------> Login again

Step 6 : Now Hacker Tap Multiple times in "RESEND CODE " --------> untill Server Reflect Stop
████████

Step 7 : Now Hacker Stop Finally


Victim Sceanrio: (Again)
------------------------

Step 1 : Victim Want to Login to his Shopify Account

Step 2 : Victim Enter Email and Password --------> Server Redirect to 2 FA page

Step 3 : Here Victim See So many OTP Code But Recent Code Still Not Arrive --------> Victim Click Resend But Server Block the Attempt

As a Result Victim not Allowed to Login to his Account

Zero_Click Vulnerbaility that Will Impact many Shopify Users Who Use Mobile Number as a method of 2 FA Verification


POC Video:
-----------
████


Please Let me Know if You have any doubt

Thank You

Regards~
saurabhsankhwar3

## Impact

1. In Real World Attacker Perform a BruteForce Attack on 2 FA page (infinite Time) --------> So that Server Not able to send correct OTP to Real Victim

2. There is Improper Security While Setting 2 FA via Mobile Phone

3. Hacker try to Disable Login Attempt of any Shopify owner just By Knowing Which Mobile Number He/She used For Enabling 2 FA in his Account

4 . Violation of Security Design Priciple

## Attachments
No attachments
