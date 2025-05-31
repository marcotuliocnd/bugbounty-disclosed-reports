# "Test target" of the "HTTP target" extension can unintentionally send username and password in the Authorization header

## Report Details
- **Report ID**: 536669
- **URL**: https://hackerone.com/reports/536669
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-12T14:14:58.291Z
- **Disclosed**: 2019-10-25T19:22:49.119Z

## Reporter
- **Username**: nathand
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zendesk

## Vulnerability Information
**Summary:**

In certain conditions, the HTTP target extension is sending the username and password of the authenticated user testing the target in the test request's `Authorization` header as base64 encoded (i.e. HTTP basic auth).

I have graded this as a medium due to some mitigating circumstances (browser specific) and actions required by the victim for an attack to be successful.

**Description:**

The HTTP target extension allows admins to create a trigger and automation action that sends data to an arbitrary Internet accessible web resource. While creating the target via the Admin > Extensions > add target screen, the user can test the target, which sends the relevant HTTP request to the target URL and allows the user to inspect the request and response, to validate the settings before creating the target.

Upon inspecting the request on a successful test, it became clear that the HTTP target test request is sending the username and password of the user performing this test:

```
GET /test.php HTTP/1.1
Authorization: Basic ████
User-Agent: Zendesk Target
Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Accept: */*
Connection: close
Host: nathandavison.com
```

(FYI: this user is a username and password user, and is not authenticating using a 3rd party service like Google)

To confirm this information is being sent over the wire, I set up a simple PHP script to collect the username and password from the test request using `$_SERVER['PHP_AUTH_USER']` and `$_SERVER['PHP_AUTH_PW']`, and I can confirm the values were being sent.

While the HTTP target creation and test form does allow the user to specify Basic Authentication configuration, from what I can tell the test request is sending the agent's username and password as Basic auth even with the "Enabled" checkbox unticked - please see the attached video regarding this. Therefore, I would classify this as a cleartext transmission of sensitive information when such a thing would not be expected by the user.

**Cause and potential fix:**

My testing suggests that this is client side behavior, in that because I have chosen to save my Zendesk username and password in my browser, the browser proceeds to auto-populate the username and password fields in the Basic Authentication's username and password fields in the HTTP target creation/edit form. This was tested in Firefox 66 - I have been unable to replicate the behavior in Chrome 73.

Therefore it seems likely that the HTTP target test feature in Zendesk is not respecting the "Enabled" checkbox when performing the test request, and is rather sending the username and password values in the test request if the fields happen to have values. If this is true, the fix may be to stop this behavior, and only send the credentials when the checkbox is enabled.

My testing suggests this is not the case in the live target runs - if I save a target with my credentials populated in the basic auth fields, but leave the checkbox unticked, the real HTTP target calls do *not* contain my credentials.

**Attack scenario:**

To exploit this, an attacker could create a 3rd party service for consumption by Zendesk users via the HTTP target extension, offering a genuine service for them to connect to and silently collect the username and passwords provided as described in this report. Because "Test target" is the default call to action in this form, it is likely a user would perform the test before creating the target, and inadvertently send their credentials. By default, the username and password fields in the target creation page are not visible, so it would not be obvious to a user they are populated with sensitive information.

If it is true that this is a Firefox specific behavior, the attacker could instruct users to use Firefox when setting up the HTTP target to try and maximize results (obviously not a relevant request, but perhaps something a majority of potential victims would not recognise as unusual or unreasonable).

## Impact

The impact of this vulnerability is an attacker could steal user credentials, likely without the user being aware.

## Attachments
No attachments
