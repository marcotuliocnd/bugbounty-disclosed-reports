# Non secure requests at guard.certly.io not upgrading to https

## Report Details
- **Report ID**: 161932
- **URL**: https://hackerone.com/reports/161932
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-21T13:59:29.494Z
- **Disclosed**: 2016-10-05T16:42:17.149Z

## Reporter
- **Username**: abc12345
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: certly

## Vulnerability Information
The issue is of http requests not upgrading to https at before mentioned domain.
Thus can allow an attack to steal important info like credentials and all other type of info.

Your domain is hsts preloaded so automatically upgraded to https , but the browsers who don't have this mentioned support like safari can allow attack.
Steps:
1. Go to http://guard.certly.io( in safari or Firefox hsts off manually).
2.go to sign in page.
3.no https enforced.
   The attack is very similar to the https://hackerone.com/reports/158186 , so you can follow that for further 
Impact.

## Attachments
No attachments
