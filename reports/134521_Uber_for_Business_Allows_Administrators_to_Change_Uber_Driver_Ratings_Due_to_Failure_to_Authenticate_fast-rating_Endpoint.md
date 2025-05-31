# Uber for Business Allows Administrators to Change Uber Driver Ratings Due to Failure to Authenticate `fast-rating` Endpoint 

## Report Details
- **Report ID**: 134521
- **URL**: https://hackerone.com/reports/134521
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-26T01:44:28.289Z
- **Disclosed**: 2016-07-26T00:36:42.942Z

## Reporter
- **Username**: ddworken
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
```business.uber.com``` allows administrators to request a copy of a receipt be emailed to them. This email contains a link to ```https://riders.uber.com/fast-rating`` which allows for the administrator to change the rating the user submitted for the Uber driver. 

Furthermore, the link that is supplied does not properly authenticate the user. Anyone who has the link can change the rating without logging in simply by changing the ```rating``` parameter at the end of the URL. 

Since I ultimately want to publicly disclose this without disclosing my ```trip_token``` and ```trip_uuid``` (which are contained in the link), I put the link in a text file here: [daviddworken.com/uberRating.txt](daviddworken.com/uberRating.txt). You can confirm that the user it not properly authenticated by opening the link and changing the rating yourself. 

Thanks,
David Dworken

## Attachments
No attachments
