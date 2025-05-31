# Password Reset emails missing TLS leads account takeover

## Report Details
- **Report ID**: 173251
- **URL**: https://hackerone.com/reports/173251
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-30T21:38:06.666Z
- **Disclosed**: 2016-10-04T16:29:07.210Z

## Reporter
- **Username**: c0rte
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
Hi,

I saw that the email is sent in clear-text instead of TLS (Transport Layer Security) any Man-in-the-middle attacker is able to read these sensitive Emails and get the password reset link which lead to account takeover.

Email details:
from:	help@rubygems.org
to:	Victim@gmail.com
date:	Fri, Sep 30, 2016 at 10:31 PM
subject:	Change your password
mailed-by:	rubygems.org
encryption:	ec2-52-43-250-235.us-west-2.compute.amazonaws.com did not encrypt this message

Thanks,
Diogo Real




## Attachments
No attachments
