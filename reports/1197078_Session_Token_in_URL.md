# Session Token in URL

## Report Details
- **Report ID**: 1197078
- **URL**: https://hackerone.com/reports/1197078
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-14T10:02:14.281Z
- **Disclosed**: 2021-12-09T17:51:23.912Z

## Reporter
- **Username**: little_one
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello Sifchain Finance Team - Greetings to you!
Hope you are well and safe. 

MAIN URL - https://sifchain.finance/master/

URL (That has to be fixed) - https://jetpack.wordpress.com/jetpack-comment/?blogid=183866479&postid=1691&comment_registration=0&require_name_email=1&stc_enabled=1&stb_enabled=1&show_avatars=1&avatar_default=identicon&greeting=Leave+a+Reply&greeting_reply=Leave+a+Reply+to+%25s&color_scheme=light&lang=en_US&jetpack_version=9.7&show_cookie_consent=10&has_cookie_consent=0&token_key=%3Bnormal%3B&sig=261ba0d56f44d12f8fdac7858d377cd6d9b9da0d

PROOF OF CONCEPT:

Kindly have a look at the screenshots I attached with this report for further information and clarification. It would also help you in easy evaluation.
Master page is the original page and affected page1 is the page that appears when you click on the link I mentioned. And affected page 2 is the page that appears when you click on the Enter your Comment here text box.

Have a nice day! Waiting for your positive reply. 

Thanks and Regards,
lemon_in_the_spoon

## Impact

IMPACT: 

If you go through this link, you are able to access the master page of the sifchain.finance website. So this issue has to be fixed. Because Sensitive information within URLs may be logged in various locations, including the user's browser, the web server, and any forward or reverse proxy servers between the two endpoints. URLs may also be displayed on-screen, bookmarked or emailed around by users.

So they may be disclosed to third parties via the Referer header when any off-site links are followed. Placing session tokens into the URL increases the risk that they will be captured by an attacker.

## Attachments
- affected_page1.png
- affected_page2.png
- master_page.png
