# Unrestricted File Upload on https://my.stripo.email and https://stripo.email

## Report Details
- **Report ID**: 823588
- **URL**: https://hackerone.com/reports/823588
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-18T15:55:46.305Z
- **Disclosed**: 2020-04-13T11:51:34.547Z

## Reporter
- **Username**: doctor_spooky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
Hi Stripo Inc, I found 2 Unrestricted File Upload Vulnerabilities on your website.

First Vulnerability:
>Step to Reproduce 
1. Create an account in "https://my.stripo.email"
2. Simply Download a php shell from internet and open with text editor.  ex: r57 shell  
3. Then save it as JPEG file. 
4. Go back to your stripo account and click on your profile icon on the top right corner of the website and go to show profile.
(Try saving it as default .php document it does not let you to upload the php malicious shell )
5. Upload your shell saved as JPEG as profile picture.
6. After that this message will pop up on the screen "User icon has been saved".

Second Vulnerability:
>Step to Reproduce 
1. Go to the URL "https://stripo.email/template-order/"
2. Scroll down to "Click or Drop file here"
3. Try Uploading .php shell downloaded earlier. (It does not allow you to upload php malicious shells)
4. Now Upload the Shell that saved as JPEG.
5. You will allow to upload Malicious shells saved as JPEG (image)

Please look at the Attached images.

## Impact

The consequences of unrestricted file upload can vary, including complete system takeover, an overloaded file system or database, forwarding attacks to back-end systems, and simple defacement.Here is the list of attacks that the attacker might do:
--Compromise the web server by uploading and executing a web-shell which can run commands, browse system files, browse local resources, attack 
   other servers, and exploit the local vulnerabilities, and so forth.
--Put a phishing page into the website.
--Put a permanent XSS into the website.
--Bypass cross-origin resource sharing (CORS) policy and exfiltrate potentially sensitive data.
--Upload a file using malicious path or name which overwrites critical file or personal data that other users access. For example; the attacker might --- 
--replace the .htaccess file to allow him/her to execute specific scripts.

Take a look at the "https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload"  for full documentation.

## Attachments
- Shell.JPG
- Error_Comes_When_Uploading_.php_document.JPG
- Shell_Saved_As_JPEG.JPG
- Shell_Uploaded_As_JPEG_File.JPG
- Shell_Uploaded_As_JPEG_File_2nd_attack.JPG
