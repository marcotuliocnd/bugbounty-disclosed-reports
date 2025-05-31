# HTML injection and limited XSS via logo image upload - Nextcloud 12.0.0

## Report Details
- **Report ID**: 231524
- **URL**: https://hackerone.com/reports/231524
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-24T19:29:29.963Z
- **Disclosed**: 2020-01-31T16:17:31.465Z

## Reporter
- **Username**: netranger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary
The logo image upload function in Nextcloud Server v12.0.0 does not validate the uploaded file, leading to XSS in certain circumstances.

## Vulnerable URL(s)
Replace [server] with the IP address or hostname of your Nextcloud server.
File upload - http://[server]/nextcloud/index.php/apps/theming/ajax/updateLogo
XSS endpoint - http://[server]/nextcloud/index.php/apps/theming/logo

## Description
A Nextcloud user with administrator rights has the option to upload a new site logo image file. However, the Nextcloud server does not verify that the uploaded file is actually an image file and accepts any file. An HTML file can be uploaded as the logo and accessed at the XSS endpoint URL: http://[server]/nextcloud/index.php/apps/theming/logo.

If a user visits the XSS endpoint URL (through a phishing link for example; since the URL is located on the valid Nextcloud server this shouldn't be too difficult) the victim's browser renders the contents of the file like any HTML page. An attacker can also include Javascript in the HTML file but it will be blocked by most major browsers through Nextcloud's Content Security Policy. However, I found 2 Javascript vectors that appear to bypass CSP and result in successful Javascript execution under Internet Explorer 11 (see Reproduction section).

## Reproduction
Create an HTML file with the following content and upload it as the Nextcloud site's logo. Alternatively, upload the HTML file provided with this report.

<!DOCTYPE html>
<head>
</head>
<body>
<h1>The logo!</h1>

<p>This HTML page was uploaded instead of a logo image.</p>
<p>Content Security Policy (CSP) prevents Javascript from executing as far as I can tell - except in Internet Explorer 11. View this page in IE 11 and you should see a pair of Javascript alert dialogs demonstrating code execution.</p>
<!-- Following both bypass CSP in IE -->

<!-- For some reason if spaces appear in the alert text this one won't work -->
<svg/onload=alert('SVG

<img/id="alert&lpar;'image XSS')"/alt="/"src="/"onerror=eval(id)>'">

</body>
</html>

Once uploaded, visit http://[server]/nextcloud/index.php/apps/theming/logo in any web browser. The browser should display rendered HTML content. Javascript execution is blocked by Nextcloud's CSP in most browsers; however, if you visit the page in IE 11, a pair of Javascript alert boxes should appear. The use of the onload attribute in an SVG tag and an IMG onerror attribute both appear to execute Javascript in IE 11:

<svg/onload=alert('SVG')>
<img/id="alert&lpar;'image XSS')"/alt="/"src="/"onerror=eval(id)>'">

During testing, IE 11 on Windows 7, 10 and IE on Windows Phone 8.1 update 2 executed the Javascript. Firefox, Chrome, Edge, Opera Mini, and Safari IOS all rendered the HTML page but did not execute the Javascript.

## Impact/Notes
Only users who are members of the Admin group have permission to change the logo. The Nextcloud Threat Model (https://nextcloud.com/security/threat-model/) indicates that Nextcloud admins are trusted. Therefore, if this vulnerability is considered an acceptable risk I understand; I thought it best to report it just in case.

One potential attack could involve one user who has admin rights uploading a malicious HTML file and tricking another admin or regular user into visiting the logo page. If the victim is using IE 11, the attacker can execute Javascript code under the victim user's session and potentially bypass CSRF protections. If an admin user has access to the underlying server OS/insfrastucture, he/she already has the power to modify another user's settings, files, etc; however, not all admin users necessarily have permission to the underlying Nextcloud server OS or infrastructure. For example, in deployments with many people several users may be given admin permissions in the web interface but that does not mean they all have access to the underlying file system; they should not be able to modify or view another user's data even though they are web admins. This vulnerability could allow for that to happen if the victim uses IE 11. I only tested with IE 11; I don't know if other IE versions behave the same.

## Mitigation
To mitigate this vulnerability, consider restricting the logo file to image files only (png, jpg, etc.) and reject non-image files.

## Attachments
- logo.html
