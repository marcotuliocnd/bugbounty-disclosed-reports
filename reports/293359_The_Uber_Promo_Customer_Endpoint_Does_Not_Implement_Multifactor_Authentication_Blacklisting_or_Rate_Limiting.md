# The Uber Promo Customer Endpoint Does Not Implement Multifactor Authentication, Blacklisting or Rate Limiting

## Report Details
- **Report ID**: 293359
- **URL**: https://hackerone.com/reports/293359
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-11-28T03:34:12.182Z
- **Disclosed**: 2017-12-24T20:20:01.989Z

## Reporter
- **Username**: gregoryvperry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
The https://cn-sjc1.uber.com/rt/users/apply-clients-promotions customer endpoint used to apply Uber promotions does not implement multifactor authentication, IP address blacklisting for multiple failed attempts, or IP address-based rate limiting to prevent brute force bearer token enumeration.

## Security Impact
Issued x-uber-tokens are able to be enumerated at rates only limited by an attacker's available bandwidth.

## Reproduction Steps
A massively parallel Golang application was configured to spawn thousands of concurrent HTTP request workers, each with a PRNG-derived  token. Unlike other endpoints within the Uber architecture, https://cn-sjc1.uber.com/rt/users/apply-clients-promotions only requires an x-uber-token and promo code to assess whether the token and/or promo code is valid. By using a valid promo code in conjunction with a randomly-derived x-uber-token, more than a million brute force attempts at enumerating valid bearer tokens was able to be accomplished in a matter of minutes, without any type of IP address blacklisting or rate limiting controls preventing the attack. 

## Specifics
* No account was needed for this brute force enumeration attack against the https://cn-sjc1.uber.com/rt/users/apply-clients-promotions customer endpoint, only a valid promo code

## Impact

An attacker with sufficient bandwidth could enumerate valid x-uber-tokens at high rates of speed, in turn resulting in compromise of privileged account information and hijacking of user sessions associated with those x-uber-tokens.

## Attachments
No attachments
