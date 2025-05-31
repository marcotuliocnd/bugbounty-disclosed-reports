# Veracode and security audit record are publicly available

## Report Details
- **Report ID**: 669365
- **URL**: https://hackerone.com/reports/669365
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-07T21:22:37.141Z
- **Disclosed**: 2019-09-10T16:05:33.318Z

## Reporter
- **Username**: laxe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Leakage of sensitive data through open endpoint 
[Risk management and Compliance Document written by NCC]
________________________________________________________________________________________
Here is what the document says: 
𝘗𝘳𝘰𝘱𝘳𝘪𝘦𝘵𝘢𝘳𝘺 𝘐𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯
𝘛𝘩𝘪𝘴  𝘥𝘰𝘤𝘶𝘮𝘦𝘯𝘵  𝘤𝘰𝘯𝘵𝘢𝘪𝘯𝘴  𝘥𝘦𝘵𝘢𝘪𝘭𝘦𝘥  𝘤𝘰𝘮𝘮𝘦𝘳𝘤𝘪𝘢𝘭,  𝘧𝘪𝘯𝘢𝘯𝘤𝘪𝘢𝘭  𝘢𝘯𝘥  𝘭𝘦𝘨𝘢𝘭  𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯,  𝘸𝘩𝘪𝘤𝘩  𝘪𝘴  𝘤𝘰𝘯𝘧𝘪𝘥𝘦𝘯𝘵𝘪𝘢𝘭  𝘢𝘯𝘥 
𝘤𝘰𝘮𝘮𝘦𝘳𝘤𝘪𝘢𝘭𝘭𝘺 𝘴𝘦𝘯𝘴𝘪𝘵𝘪𝘷𝘦. 𝘛𝘩𝘦 𝘳𝘦𝘭𝘦𝘢𝘴𝘦 𝘰𝘧 𝘴𝘶𝘤𝘩 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 𝘸𝘪𝘭𝘭 𝘣𝘦 𝘱𝘳𝘦𝘫𝘶𝘥𝘪𝘤𝘪𝘢𝘭 𝘵𝘰 𝘵𝘩𝘦 𝘤𝘰𝘮𝘮𝘦𝘳𝘤𝘪𝘢𝘭 𝘪𝘯𝘵𝘦𝘳𝘦𝘴𝘵𝘴 𝘰𝘧 
𝘕𝘊𝘊 𝘎𝘳𝘰𝘶𝘱 𝘢𝘯𝘥 𝘵𝘩𝘦𝘳𝘦𝘧𝘰𝘳𝘦 𝘴𝘩𝘰𝘶𝘭𝘥 𝘯𝘰𝘵
𝘣𝘦 𝘥𝘪𝘴𝘤𝘭𝘰𝘴𝘦𝘥 𝘢𝘴 𝘢 𝘳𝘦𝘴𝘱𝘰𝘯𝘴𝘦 𝘵𝘰 𝘢 𝘙𝘦𝘲𝘶𝘦𝘴𝘵 𝘧𝘰𝘳 𝘐𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 𝘶𝘯𝘥𝘦𝘳 𝘵𝘩𝘦 
𝘍𝘳𝘦𝘦𝘥𝘰𝘮 𝘰𝘧 𝘐𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 𝘈𝘤𝘵 2002.
𝘛𝘩𝘦 𝘥𝘰𝘤𝘶𝘮𝘦𝘯𝘵 𝘮𝘢𝘺 𝘢𝘭𝘴𝘰 𝘯𝘰𝘵 𝘣𝘦 𝘳𝘦𝘱𝘳𝘰𝘥𝘶𝘤𝘦𝘥 𝘰𝘳 𝘵𝘩𝘦 𝘤𝘰𝘯𝘵𝘦𝘯𝘵𝘴 𝘵𝘳𝘢𝘯𝘴𝘮𝘪𝘵𝘵𝘦𝘥 
𝘵𝘰 𝘢𝘯𝘺 𝘵𝘩𝘪𝘳𝘥 𝘱𝘢𝘳𝘵𝘺 𝘸𝘪𝘵𝘩𝘰𝘶𝘵 𝘵𝘩𝘦 𝘦𝘹𝘱𝘳𝘦𝘴𝘴 𝘤𝘰𝘯𝘴𝘦𝘯𝘵 𝘰𝘧 𝘕𝘊𝘊 𝘎𝘳𝘰𝘶𝘱
________________________________________________________________________________________
Nextcloud has it leaked publicly through an open endpoint on their website... Which goes against the Proprietary Information part of the document as it's NCC property. 
________________________________________________________________________________________


Steps to reproduce:

1.  Open Browser of choice (Firefox was used)
2. Open google search 
3. Using the search query site:nextcloud.com filetype:pdf 
4. Click on the 3 page of results and you should see a title [PDF]NCC Group Nextcloud 11 – Security Review
5. Proceed to click on it ( https://nextcloud.com/wp-content/themes/next/assets/files/NCC_report_full.pdf )

You can see in the document the information above.

There are also these documents open:

https://nextcloud.com/wp-content/themes/next/assets/files/veracode_report.pdf?x22777

https://nextcloud.com/wp-content/themes/next/assets/files/NCC_report_assurance.pdf?x16328




Here are screenshots for a POC:

http://prntscr.com/opr7kz
http://prntscr.com/opr7uv
http://prntscr.com/opr7yt

## Impact

There are sensitive documents that are open to the public which breaks NCC's  𝘗𝘳𝘰𝘱𝘳𝘪𝘦𝘵𝘢𝘳𝘺 𝘐𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 agreement stated on the document. This could lead to legal trouble for Nextcloud with NCC.

## Attachments
No attachments
