# Additional bypass allows SSRF for internal netblocks

## Report Details
- **Report ID**: 288950
- **URL**: https://hackerone.com/reports/288950
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-09T20:38:47.190Z
- **Disclosed**: 2017-11-16T20:15:03.956Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
It turns out there is another bypass in the `private_address_check` gem. The gem does not include 0.0.0.0 in the exclusion list in the first place.

```
irb(main):001:0> require 'private_address_check'
=> true
irb(main):002:0> PrivateAddressCheck.private_address?("0.0.0.0")
=> false
```

I was able to bypass your filter by using http://0.0.0.0:22/ as you can see below:

{F238151}

Please find a hotfix for this issue attached to this report: {F238152}. The author of the gem has been notified and should hopefully provide a proper fix very soon.



## Attachments
- image.png
- private_address_check.rb.patch
