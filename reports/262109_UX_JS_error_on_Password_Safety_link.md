# UX: JS error on Password Safety link

## Report Details
- **Report ID**: 262109
- **URL**: https://hackerone.com/reports/262109
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-22T03:02:16.229Z
- **Disclosed**: 2017-08-26T05:35:24.769Z

## Reporter
- **Username**: mehmil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi Team,

The link at https://app.legalrobot.com/account under "Password Safety" seems to be incorrectly configured. On clicking "here's how", I get following error:

```
Uncaught TypeError: Cannot read property 'title' of undefined
    at Object.click .how (89e4d4e….js?meteor_js_resource=true:301)
    at 89e4d4e….js?meteor_js_resource=true:73
    at Function.e._withTemplateInstanceFunc (89e4d4e….js?meteor_js_resource=true:73)
    at p.View.<anonymous> (89e4d4e….js?meteor_js_resource=true:73)
    at 89e4d4e….js?meteor_js_resource=true:73
    at Object.p._withCurrentView (89e4d4e….js?meteor_js_resource=true:73)
    at p._DOMRange.<anonymous> (89e4d4e….js?meteor_js_resource=true:73)
    at HTMLAnchorElement.<anonymous> (89e4d4e….js?meteor_js_resource=true:73)
    at HTMLDivElement.dispatch (jquery-3.2.1.min.js:3)
    at HTMLDivElement.q.handle (jquery-3.2.1.min.js:3)
```

Source JS file : https://app.legalrobot.com/89e4d4e5f94c29cff9fb29556730107fadae85ff.js?meteor_js_resource=true

Attached screenshots.

This is not a security flaw as such, but more of a usability bug, so I have marked severity as None.

Please review.



## Attachments
- l1.png
- l2.png
