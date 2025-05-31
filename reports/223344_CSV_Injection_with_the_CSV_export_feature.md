# CSV Injection with the CSV export feature

## Report Details
- **Report ID**: 223344
- **URL**: https://hackerone.com/reports/223344
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T09:43:51.956Z
- **Disclosed**: 2017-05-17T18:03:47.076Z

## Reporter
- **Username**: jaypatel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
**Step to reproduce :**
1.go to https://hosted.weblate.org/dictionaries/aptoide-uploader/bn/#add
2.add "=1+1" to **Source** and ** Translation** filed 
{F178723}
3.now do **CSV export**
4.you can see all the cell is displayed as "2" which means the code is executed.

Best Regad's,
Jay Patel

## Attachments
- Screen_Shot_2017-04-24_at_3.11.05_PM.png
