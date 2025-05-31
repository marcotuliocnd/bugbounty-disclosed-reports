# Post-Auth Stored XSS with User Interaction leads to Remote Code Execution

## Report Details
- **Report ID**: 1132202
- **URL**: https://hackerone.com/reports/1132202
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-03-22T10:39:40.941Z
- **Disclosed**: 2021-06-30T10:55:20.602Z

## Reporter
- **Username**: sonarsource
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:**
Unsafe usage of the `toastr` library leads to Stored XSS when combined with a validation bypass in the `createRoom` function. Targeting an admin account leads to Remote Code Execution.

**Description:**
The frontend uses the `toastr` library to display error messages to the user. However, it is used in an unsafe way which allows XSS when user input is reflected in an API error message. This happens for example when channel info is edited and the channel's name contains invalid characters.

To abuse this, an attacker can use a validation bypass in [the `createRoom` function](https://github.com/RocketChat/Rocket.Chat/blob/9bbf11ad53d43dc3a5d870d6df4a3022b6de3440/app/lib/server/functions/createRoom.js#L62): the `extraData` parameter is merged with the room object without proper validation, which allows an attacker to override all previous properties such as the name or the owner. The attacker can use this to create a room that contains their XSS payload in the room's name.

Triggering the XSS requires multiple steps of user interaction, because there are few API endpoints that reflect user input back. One of them is [the `rooms.saveRoomSettings` endpoint](https://github.com/RocketChat/Rocket.Chat/blob/9bbf11ad53d43dc3a5d870d6df4a3022b6de3440/app/api/server/v1/rooms.js#L340-L348) which calls [the `saveRoomSettings` method](https://github.com/RocketChat/Rocket.Chat/blob/9bbf11ad53d43dc3a5d870d6df4a3022b6de3440/app/channel-settings/server/methods/saveRoomSettings.js#L223-L322) which in turn uses [the `getValidRoomName` function](https://github.com/RocketChat/Rocket.Chat/blob/9bbf11ad53d43dc3a5d870d6df4a3022b6de3440/app/utils/lib/getValidRoomName.js#L7-L62). This function checks the room's name and reflects the user-provided value back if it is not a valid name.

The error returned by the API is unsafely handled by passing it to the `toastr` library without escaping it or using the library's `escapeHtml` option. [The `handleError` function](https://github.com/RocketChat/Rocket.Chat/blob/9bbf11ad53d43dc3a5d870d6df4a3022b6de3440/app/utils/client/lib/handleError.js#L7-L33) passes the value to the `toastr` library, it escapes the `details` property but not the `message` and `title` property.

To gain Remote Code Execution capabilities on the server, an attacker can follow these steps to take over an admin account. The attacker can then use the newly gained admin privileges to create an incoming web hook that has a script. This allows them to execute commands or get a shell on the server, because the script is executed on the server without a security boundary in place (which seems to be intended).

**Note:** This issue is classified as Stored XSS because the payload is stored permanently in the database, but it could be argued that it is Reflected XSS because the payload is reflected by the API which then leads to the unsafe handling and execution of the payload.

## Releases Affected:
We tested on 3.12.1, but it is hard to confirm since when Rocket.Chat is vulnerable because there are many parts of the code base involved.

## Steps To Reproduce (from initial installation to vulnerability):
1. Set up an instance of RocketChat 3.12.1, e.g. by cloning the repo and using Docker Compose:
  1. `git clone git@github.com:RocketChat/Rocket.Chat.git`
  1. `cd Rocket.Chat`
  1. `git checkout tags/3.12.1`
  1. `docker-compose up -d`
1. Configure the instance with default settings
1. Create a normal (non-admin) user with username `attacker` and password `attacker`
1. Log in as the `attacker` user
1. Open the browser's developer tools and execute the following line of code: `Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })`
1. Invite the admin to the newly created channel
1. Log out and log in as an admin
1. Edit the title of the newly created channel (e.g. change `me` to `you`)
1. Click the save button
1. A dialog should pop up that shows the site's origin (e.g. http://localhost:3000), confirming that the XSS payload has been executed (this is only for the demo, the payload can be arbitrary JavaScript code)
1. (The demo ends here but it is trivial to get RCE capabilities when having access to an admin account, as explained before)

## Supporting Material/References:
The attached video shows the exploitation of the vulnerability with the attacker's view on the right and the victim's view (admin) on the left.

## Suggested mitigation
- Restrict and validate the `extraData` parameter when creating a room
- Use the `toastr` library with the `escapeHtml` option or sanitize the message and title manually
- Set a [`Content-Security-Policy` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) that prevents payload execution
  - preventing inline scripts might not be enough here because users can upload files
  - a [nonce-based CSP](https://content-security-policy.com/nonce/) would fit best

## Disclosure Policy
All reported issues are subject to a 90 day disclosure deadline.
After 90 days elapse, parts of the bug report will become visible to the public.

Don't hesitate to ask if you have any questions or need further help with this issue.

## Impact

An attacker can use this vulnerability to target an admin user and take over their account, which is already a high impact. The attacker can then use certain features that are available to admins in order to gain Remote Code Execution capabilities.

This gives them complete control over the Rocket.Chat instance and exposes all attached components, e.g. the database or any external system whose credentials are stored within Rocket.Chat settings. An attacker can read, change, or delete all items in the database, impacting confidentiality, integrity, and availability.

## Attachments
- xss.mp4
