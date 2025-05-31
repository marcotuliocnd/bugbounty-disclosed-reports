# File listing through scripts folder

## Report Details
- **Report ID**: 2190117
- **URL**: https://hackerone.com/reports/2190117
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-10-02T18:52:44.579Z
- **Disclosed**: 2024-02-09T12:12:41.419Z

## Reporter
- **Username**: itssixtynein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
## Summary:
It's possible to list all hidden files that are located within the TVAVirtual.com Sharepoint folder structure.

## Steps To Reproduce:

1. Navigate to TvaVirtual.com
2. Open the pages source code and notice that its build using sharepoint pages.
3. Confirm that you see a listing for /SiteAssets/Scripts/js.cookie.min.js. Click on it to navigate to the page
4. Once https://tvavirtual.com/SiteAssets/Scripts/js.cookie.min.js loads, then remove js.cookie.min.js from the url
5. Confirm that TvaVirtual.com now shows the script folder listing on the page.
6. Remove the extra folder from the url to list the root folder at https://tvavirtual.com/SiteAssets/Forms/AllItems.aspx?RootFolder=
7. Navigate through the directory listing in an attempt to find sensitive files, enumerate publishing users and version history.

## Supporting Material/References:
I've attached jpgs showing what is available. You may see a login from bugs@tobiasdiehl.com where I was confirming cross tenant access to the files.

## Impact

Attackers can potentially enumerate sensitive information and files that would otherwise be protected

## Attachments
- listing2.JPG
- listing1.JPG
- url.JPG
