#  Renderers can obtain access to random bluetooth device without permission

## Report Details
- **Report ID**: 1519099
- **URL**: https://hackerone.com/reports/1519099
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-03-22T18:27:19.570Z
- **Disclosed**: 2022-04-23T17:23:03.981Z

## Reporter
- **Username**: palmeral
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
With the default configuration in Electron, renderer processes (which should not have access to system resources by default) can gain read/write access to a nearby bluetooth device. To reproduce:

* Run the electron-quick-start app with a vulnerable version of Electron: https://github.com/electron/electron-quick-start
* Using the developer tools, run `await navigator.bluetooth.requestDevice({acceptAllDevices: true})`
* You should get a permission error, but in vulnerable versions you will get a bluetooth device object instead.

## Impact

If an Electron app loads remote or untrusted content in a renderer process (which is normally fine, as the process should not have any privileges), the remote content would have read/write access to nearby bluetooth devices. The impact would then depend on what devices the user has nearby.

## Attachments
No attachments
