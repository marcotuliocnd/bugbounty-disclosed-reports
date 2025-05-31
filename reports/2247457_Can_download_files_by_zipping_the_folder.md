# Can download files by zipping the folder

## Report Details
- **Report ID**: 2247457
- **URL**: https://hackerone.com/reports/2247457
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-11-10T07:55:39.004Z
- **Disclosed**: 2024-02-17T08:38:25.368Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. Create folder and share it as view-only

{F2846936}

2. Access this folder with Testuser

{F2846943}


3. Go one level up and compress the whole folder

{F2846942}

4. The zip file can be downloaded and extracted locally

{F2846939}
{F2846941}


5. The folder itself can not be downloaded directly

{F2846937}

## Impact

Can download files without download permissions

## Attachments
- grafik.png
- grafik.png
- grafik.png
- grafik.png
- grafik.png
- grafik.png
