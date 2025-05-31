# No redirect_uri in the db for web-internal clientKey leads to one-click DoS on gitter.im

## Report Details
- **Report ID**: 702987
- **URL**: https://hackerone.com/reports/702987
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-27T13:50:27.438Z
- **Disclosed**: 2020-05-15T17:07:57.575Z

## Reporter
- **Username**: gregxsunday
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
In the *oauthclients* collection of the default gitter installation, there's no value *registeredRedirectUri* in the database for *web-internal* clientKey. The request to
```
/login/oauth/authorize?response_type=code&client_id=web-internal&redirect_uri=http://whatever
```
causes the app to crash when trying to parse the *client.registeredRedirectUri*, which in this situation becomes the value *undefined*.
### Steps to reproduce

1. deploy the standard installation of the gitter application
2. make the GET request to 
```
http://localhost:5000/login/oauth/authorize?response_type=code&client_id=web-internal&redirect_uri=http://whatever
```

### Impact

The application crashes and does not wake up on its own.
```
2019-09-27T13:01:09.013Z - error: Uncaught exceptionTypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined forcing shutdown
[15:01:09] [nodemon] app crashed - waiting for file changes before starting...
```
### What is the current *bug* behavior?

When the request to 
```
/login/oauth/authorize?response_type=code&client_id=web-internal&redirect_uri=http://whatever
```
is made, the database lookup is being done:
```
oauthService.findClientByClientKey(clientKey, function(err, client) {
      if (err) {
        return done(err);
      }
```
*those are the lines 127-130 from server/web/oauth2.js*
The clientKey is *web-internal*, its record in the Mongo looks like this:
```
{
    "_id": ObjectID("5d8453d62edc221c1e5a2f6c"),
    "clientKey": "web-internal",
    "clientSecret": <clientSecret>,
    "name": "Web Client",
    "tag": "web-app"
}
```
The query returned something, so the following check is being passed:
```
      if (!client) {
        return done(new OauthAuthorizationError('Provided clientKey does not exist.'));
      }
```
*those are the lines 132-134 from server/web/oauth2.js*
Then, in the 136th line there's parsing that is the root cause of the problem:
```
 const urlData = url.parse(client.registeredRedirectUri);
```
as the *client.registeredRedirectUri* is undefined, it throws the *Uncaught exceptionTypeError*.
```
2019-09-27T13:01:09.011Z - error: ----------------------------------------------------------------
2019-09-27T13:01:09.011Z - error: -- A VeryBadThing has happened.
2019-09-27T13:01:09.011Z - error: ----------------------------------------------------------------
2019-09-27T13:01:09.012Z - error: Uncaught exceptionTypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined 
{ message:
   'The "url" argument must be of type string. Received type undefined',
  name: 'TypeError [ERR_INVALID_ARG_TYPE]' }
2019-09-27T13:01:09.012Z - error: TypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined
```

### What is the expected *correct* behavior?

The app should not crash on such error. To mitigate the issue you can
1. simply catch the error
2. add *registeredRedirectUri* to the database record. It can be done by adding a line to *scripts/dataupgrades/001-oauth-client/002-add-redirect-uri.sh* which currently looks like this:
```
db.oauthclients.update(
  { clientKey: 'web-internal' },
  { clientKey: 'web-internal',
    clientSecret: '$(generate_password)',
    name: 'Web Client',
    tag: 'web-app',
  }, true /* upsert */);
```

### Relevant logs and/or screenshots

```
019-09-27T13:01:09.006Z - error: No error reporting is enabled so just logging to logger:  
{ exception:
   { message:
      'The "url" argument must be of type string. Received type undefined',
     stack:
      'TypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined\n    at Url.parse (url.js:154:11)\n    at Object.urlParse [as parse] (url.js:148:13)\n    at /home/gniedziela/projects/gitlab/gitter/webapp/server/web/oauth2.js:137:27\n    at tryCatcher (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/util.js:16:23)\n    at Promise.successAdapter [as _fulfillmentHandler0] (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/nodeify.js:23:30)\n    at Promise._settlePromise (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/promise.js:566:21)\n    at Promise._settlePromise0 (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/promise.js:614:10)\n    at Promise._settlePromises (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/promise.js:693:18)\n    at Async._drainQueue (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/async.js:133:16)\n    at Async._drainQueues (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/async.js:143:10)\n    at Immediate.Async.drainQueues (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/async.js:17:14)\n    at runCallback (timers.js:705:18)\n    at tryOnImmediate (timers.js:676:5)\n    at processImmediate (timers.js:658:5)\n    at process.topLevelDomainCallback (domain.js:126:23)',
     name: 'TypeError [ERR_INVALID_ARG_TYPE]' },
  meta:
   { errorString:
      'TypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined',
     type: 'uncaught' },
  tags:
   { host: 'c7caee1658e769b17e9c1e0e254cb54939a3e982', job: 'web' } }
2019-09-27T13:01:09.011Z - error: ----------------------------------------------------------------
2019-09-27T13:01:09.011Z - error: -- A VeryBadThing has happened.
2019-09-27T13:01:09.011Z - error: ----------------------------------------------------------------
2019-09-27T13:01:09.012Z - error: Uncaught exceptionTypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined 
{ message:
   'The "url" argument must be of type string. Received type undefined',
  name: 'TypeError [ERR_INVALID_ARG_TYPE]' }
2019-09-27T13:01:09.012Z - error: TypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined
    at Url.parse (url.js:154:11)
    at Object.urlParse [as parse] (url.js:148:13)
    at /home/gniedziela/projects/gitlab/gitter/webapp/server/web/oauth2.js:137:27
    at tryCatcher (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/util.js:16:23)
    at Promise.successAdapter [as _fulfillmentHandler0] (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/nodeify.js:23:30)
    at Promise._settlePromise (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/promise.js:566:21)
    at Promise._settlePromise0 (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/promise.js:614:10)
    at Promise._settlePromises (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/promise.js:693:18)
    at Async._drainQueue (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/async.js:133:16)
    at Async._drainQueues (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/async.js:143:10)
    at Immediate.Async.drainQueues (/home/gniedziela/projects/gitlab/gitter/webapp/node_modules/bluebird/js/release/async.js:17:14)
    at runCallback (timers.js:705:18)
    at tryOnImmediate (timers.js:676:5)
    at processImmediate (timers.js:658:5)
    at process.topLevelDomainCallback (domain.js:126:23)
2019-09-27T13:01:09.013Z - error: Uncaught exceptionTypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined forcing shutdown
[15:01:09] [nodemon] app crashed - waiting for file changes before starting...
```

## Impact

Complete Denial of Service of the Gitter installation.

## Attachments
No attachments
