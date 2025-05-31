# Paragonie Airship Admin CSRF on Extensions Pages

## Report Details
- **Report ID**: 243094
- **URL**: https://hackerone.com/reports/243094
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-25T20:55:09.292Z
- **Disclosed**: 2017-10-16T05:48:14.764Z

## Reporter
- **Username**: 4cad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Summary
==========

The /bridge/admin/skyport/install endpoint, as well as some of the endpoints around it, are vulnerable to Cross-Site Request Forgery.

Description
=========
The functions in src/Cabin/Bridge/Controller/Skyport.php in the Airship project appear to all be vulnerable to Cross-Site Request Forgery.

I would have put this as a high, but from my code review it appears that not all of these functions actually work - for example, the installPackage function appears to passing a bash script to the "php" command, which just ends up printing the bash script. Code review can be misleading, so I may be wrong about it not working.

I put this as a medium because, if the logic actually does work (or works sometime in the future), then the ability to install packages is the kind of thing that has the potential to be converted into an RCE.

Please revise the severity as you see fit - I don't know your product well enough to do a proper assessment.

Proof of Concept
======
I have attached a simple file which I was able to use to demonstrate the CSRF against airship running in a docker instance. It appears that the extra password-protection of extensions is not enabled by default, although that may be just my developer setup.

See the attached csrf.html. The attached screenshot shows the result that was returned from the server after clicking the submit button in the attached file.

## Attachments
- csrf.html
- Example_Airship_CSRF.png
