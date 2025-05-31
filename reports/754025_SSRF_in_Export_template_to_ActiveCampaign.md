# SSRF in Export template to ActiveCampaign

## Report Details
- **Report ID**: 754025
- **URL**: https://hackerone.com/reports/754025
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-08T16:57:37.282Z
- **Disclosed**: 2020-04-10T07:54:32.182Z

## Reporter
- **Username**: c1kada
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
I found a SSRF vulneranility in export template to  email marketing platform (ActiveCampaign).

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Login to your account in 
  1. Go to `https://my.stripo.email/cabinet/#/templates/`
  1.  Click on `Create your first mail` & select one template
  1. Export
  1. Click on `ActiveCampaign`
  1. Insert your server address in `API URL `and a fake string in API Key
  1. Now Click on Export and see your `server logs`
{F654075}

## PoC Video
{F654076}

## Impact

The export template to ActiveCampaign is vulnerable to a  SSRF vulnerability. The vulnerability allows an attacker to make arbitrary HTTP/HTTPS requests.

## Attachments
- ssrf.png
- ssrf.mp4
