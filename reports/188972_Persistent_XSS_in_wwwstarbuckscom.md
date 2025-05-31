# Persistent XSS in www.starbucks.com

## Report Details
- **Report ID**: 188972
- **URL**: https://hackerone.com/reports/188972
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-06T23:19:45.660Z
- **Disclosed**: 2017-01-17T21:57:52.926Z

## Reporter
- **Username**: ddworken
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
There is a persistent XSS in 

```
https://www.starbucks.com/coffee/espresso/latte-macchiato
```

It is caused by loading scripts from: 

```
//starbucksmacchiato-prod.elasticbeanstalk.com/scripts/bn-v1.0.0-Release-min.js
```

Note that ```starbucksmacchiato-prod.elasticbeanstalk.com``` is not registered on elastic beanstalk. You can verify this by looking up the IP address for this subdomain and noting that it does not resolve. Through registering that domain on elastic beanstalk and deploying a webserver that responds to that request with javascript, an attacker could get a persistent XSS on Starbuck's website. 

I have not registered that domain with Elastic Beanstalk since it would give me a large amount of information about the user's of Starbuck's website (and it would incur a large amount of traffic-more than I'd like to pay for on AWS!). If you would like me to do so, let me know but I do not want to go past the bounds of acceptable testing. 

Thanks,
David Dworken

## Attachments
No attachments
