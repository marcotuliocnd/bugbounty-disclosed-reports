# Sending trusted ████ and ██████████ emails through public API endpoint in ███████ site

## Report Details
- **Report ID**: 1067276
- **URL**: https://hackerone.com/reports/1067276
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-28T05:24:49.291Z
- **Disclosed**: 2021-04-08T18:54:26.525Z

## Reporter
- **Username**: skarsom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A publicly accessible endpoint at PUT https://████████does not validate any of its four parameters: to, from, subject, text. This enables sending email to any address, with any content, with any from address, on a server that is in ██████whitelist. Such services include, but are not limited to, all ██████ email (██████.

**Description:**
The ███'s (████████) ███████ (███) public portal, including login to the private portal, exists at https://███████████/welcome/ with a staging environment at https://███/welcome/. This vulnerability affects both staging and production.

Whenever a request for a new account or a password reset is created, the AngularJS frontend formats this request with a client-side email template (relevant code in https://██████/█████) and sends a JSON-encoded PUT request to `/███████`.

There are four parameters:
1) `to` -- this should always be `█████` per https://████████/████████
1) `from` -- this should always be `█████` per https://████████/█████
3) `subject` -- the email subject
4) `text` -- the email body

Because the client-side AngularJS code is trusted to generate legitimate emails, an unauthorized attacker can use this API to mass-send legitimate ███████ or ██████ emails with arbitrary content. These emails go through the ███ system, so they explicitly pass DKIM and SPF.

## Step-by-step Reproduction Instructions

1. Execute the following cURL request, changing the text `YOUREMAIL` in the JSON-encoded `to` parameter to an email address of your choosing:

    ```
curl -X PUT --data '{"from":"Email POC <skarsomh1vdp@████>","to":"YOUREMAIL","subject":"Test under DC3 VDP at HackerOne","text":"This is a test. For more info see hackerone.com/deptofdefense."}' -k https://████████-H 'Content-type: application/json'
    ```
2. Success. Check the email address specified in the `to` parameter. Notice that this email passes all spam checks such as DKIM and SPF.

## Suggested Mitigation/Remediation Actions
- Completely remove the `/████` endpoint.
- Add a new endpoint for requesting a new account that composes the proper email on the *backend*.
- Add a new endpoint for requesting help with logging in that composes the proper email on the *backend*.
- Evaluate whether the ██████████ needs to continue including ████████SPF records, as it increases attack surface.

## Impact

An unauthorized attacker can send arbitrary email from ██████-controlled email servers.

An adversary could create a spear phishing attack against high-value targets by forging ████ or IC correspondence. For example, sending an email from `██████████` requesting personnel to click on a link to verify their CAC info.

## Attachments
No attachments
