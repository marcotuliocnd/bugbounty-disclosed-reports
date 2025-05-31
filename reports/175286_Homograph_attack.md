# Homograph attack

## Report Details
- **Report ID**: 175286
- **URL**: https://hackerone.com/reports/175286
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-12T04:25:35.756Z
- **Disclosed**: 2016-10-14T18:15:01.305Z

## Reporter
- **Username**: jaypatel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

when we add a site to our **Homepage**, it's not validate a url properly, make sure it's display the **punycode.**

## Products affected: 

 * Brave 0.12.4 (Tested on mac os)

## Steps To Reproduce:

 * In browser add homepage with IDN  http://ebаy.com/
 * now close and open browser again
 * you can see it's redirect to http://xn--eby-7cd.com/

## References:

  * https://hackerone.com/reports/29491


## Attachments
No attachments
