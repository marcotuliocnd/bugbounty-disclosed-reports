# If the developer forgets to remove the built in controller welcome.php it helps the attacker to identify that the site is built with Codeigniter

## Report Details
- **Report ID**: 278225
- **URL**: https://hackerone.com/reports/278225
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-17T16:11:32.470Z
- **Disclosed**: 2017-10-18T02:35:59.544Z

## Reporter
- **Username**: hackerneo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: codeigniter

## Vulnerability Information
The attacker can check the website's backend technology simply by typing site_name/index.php/welcome/index it will display the codeigniter welcome page if the developer dosen't removed the built in controller and view welcome.php and welcome_message.php i attaching a screenshot below as a proof of concept

## Attachments
- proof.jpg
