# reopen #128853 (Information disclosure at lite.uber.com)

## Report Details
- **Report ID**: 129712
- **URL**: https://hackerone.com/reports/129712
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-10T21:17:56.894Z
- **Disclosed**: 2016-07-26T00:37:36.728Z

## Reporter
- **Username**: kusl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Issue in #128853  occurs again.
1. go to https://login.uber.com/oauth/v2/authorize?response_type=code&redirect_uri=https%3A%2F%2Flite.uber.com%2Fauth%2Fcallback&scope=profile%20history%20places%20history_lite%20request_receipt%20request%20payment_baidu_wallet&client_id=y-JJyZ_RABnEwbJQq4VdQPORo4EKqv0j
2. Enter your login and password
3. You will redirect to lite.uber.com with trace from nodejs

`{"stack":"Session5xxErrorError: Session error - unable to read alipayUser from session\n    at createError (/home/udocker/yellow-river/node_modules/error/typed.js:31:22)\n    at middleware (alipay-user-session.js:22:17)\n    at Layer.handle [as handle_request] (/home/udocker/yellow-river/node_modules/express/lib/router/layer.js:95:5)\n    at next (/home/udocker/yellow-river/node_modules/express/lib/router/route.js:131:13)\n    at complete (/home/udocker/yellow-river/node_modules/passport/lib/middleware/authenticate.js:250:13)\n    at /home/udocker/yellow-river/node_modules/passport/lib/middleware/authenticate.js:257:15\n    at pass (/home/udocker/yellow-river/node_modules/passport/lib/authenticator.js:421:14)\n    at Authenticator.transformAuthInfo (/home/udocker/yellow-river/node_modules/passport/lib/authenticator.js:443:5)\n    at /home/udocker/yellow-river/node_modules/passport/lib/middleware/authenticate.js:254:22\n    at /home/udocker/yellow-river/node_modules/passport/lib/http/request.js:60:7\n    at pass (/home/udocker/yellow-river/node_modules/passport/lib/authenticator.js:267:43)\n    at serialized (/home/udocker/yellow-river/node_modules/passport/lib/authenticator.js:276:7)\n    at cb (auth.js:16:5)\n    at pass (/home/udocker/yellow-river/node_modules/passport/lib/authenticator.js:284:9)\n    at Authenticator.serializeUser (/home/udocker/yellow-river/node_modules/passport/lib/authenticator.js:289:5)\n    at IncomingMessage.req.login.req.logIn (/home/udocker/yellow-river/node_modules/passport/lib/http/request.js:50:29)\n    at UberOAuth2Strategy.strategy.success (/home/udocker/yellow-river/node_modules/passport/lib/middleware/authenticate.js:235:13)\n    at verified (/home/udocker/yellow-river/node_modules/passport-oauth2/lib/strategy.js:174:20)\n    at UberOAuth2Strategy.cb [as _verify] (auth.js:30:7)\n    at /home/udocker/yellow-river/node_modules/passport-oauth2/lib/strategy.js:190:24\n    at Request._callback (uber-oauth2.js:39:7)\n    at Request.self.callback (/home/udocker/yellow-river/node_modules/request/request.js:199:22)\n    at Request.emit (events.js:98:17)\n    at Request.<anonymous> (/home/udocker/yellow-river/node_modules/request/request.js:1036:10)\n    at Request.emit (events.js:117:20)\n    at IncomingMessage.<anonymous> (/home/udocker/yellow-river/node_modules/request/request.js:963:12)\n    at IncomingMessage.emit (events.js:117:20)\n    at _stream_readable.js:943:16\n    at process._tickDomainCallback (node.js:463:13)","type":"session.5xx.error","status":500,"message":"Session error - unable to read alipayUser from session","name":"Session5xxErrorError","fullType":"session.5xx.error"}` 

Error occurs when user want to connect YellowRiver app to his account with/without Alipay as payment method.

Files attached.

And one more thing:
You have some internal resources, which can be find easy. For example JIRA at 
jira.uber.com (with redirect to jira.uberinternal.com)
And by using API JIRA I can find something like this:
https://jira.uberinternal.com/rest/api/2/dashboard?maxResults=20&startAt=20

I think internal resources must be internal. You are not responsible for third-party products. But sometimes can be this #114476


## Attachments
- ______________2016-04-11___00.16.36.png
- ______________2016-04-11___00.01.13.png
