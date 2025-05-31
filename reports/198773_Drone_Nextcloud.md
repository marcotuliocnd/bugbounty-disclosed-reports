# Drone Nextcloud

## Report Details
- **Report ID**: 198773
- **URL**: https://hackerone.com/reports/198773
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-16T16:55:07.885Z
- **Disclosed**: 2017-02-12T19:28:53.973Z

## Reporter
- **Username**: rbcafe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Greetings,

On drone : https://drone.nextcloud.com

We observe this :
----

{F152818}

I noticed that it's possible to alter the url to write what you want :
----

   https://drone.nextcloud.com/rbcafe/settings/settings/badges

{F152817}

In fact it could be anything :
----

   https://drone.nextcloud.com/lonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn/settings/settings/badges

{F152819}

The default value of the url can be extracted with a google-dorking on drone.nextcloud.com : inurl:drone.nextcloud.com

- https://drone.nextcloud.com/nextcloud/updater
- https://drone.nextcloud.com/nextcloud/server/settings/badges

Using this we can find new data :
-------------------------------

https://drone.nextcloud.com/nextcloud/server/

{F152820}

https://drone.nextcloud.com/nextcloud/server/4182/1

{F152821}

Buttons Follow and restart are fully clickable, but there is no purpose because, I'm not logged In. Regarding the screenshot in the first observation (F152818), pages should be blocked and remains protected if the login is not valid. The paths should also remains protected from indexation.

Best regards
@Rbcafe

## Attachments
- nc_d_1.png
- nc_d_0.png
- nc_d_2.png
- nc_d_3.png
- nc_d_4.png
