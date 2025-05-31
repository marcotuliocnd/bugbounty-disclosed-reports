# Anyone can register organization legal type as "Soletrader"

## Report Details
- **Report ID**: 361189
- **URL**: https://hackerone.com/reports/361189
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-02T21:16:53.384Z
- **Disclosed**: 2018-06-03T16:31:39.705Z

## Reporter
- **Username**: mister_mime
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
When Organization type is registered, two values are displayed : Business and Organization. 
When another value is provided, an error message is printed saying the Legal Type is wrong. 

This error message is not printed and request success when the value "Soletrader"  is provided.
The value "Soletrader" is part of the MangoPay API Documentation ( <https://docs.mangopay.com/guide/kyc>).

A malicious attacker can register its organization with this Legal Type which seems to be not planned by the librapay.com platform.

**Steps to reproduce**
1. Go to <https://en.liberapay.com/~107759/identity>
2. Check the box "Yes, I represent a business or nonprofit."
3. Inspect element with your browser on the "Organization type" input, and change <option value="BUSINESS">Entreprise</option> with <option value="Soletrader">Entreprise</option>.
4. Select "Enterprise" on the Organization type" input
5. Click on the "Save button".
6. The request is accepted by the platform and the success message "Your identity information has been updated." is printed.

You can try to do the same providing another value than "Soletrader" and you will check that an error is printed.

## Impact

A malicious attacker can register its organization with this Legal Type which seems to be not planned by the librapay.com platform. He could use this to have not planned  or unauthorized features when calling Mangopay API.

## Attachments
No attachments
