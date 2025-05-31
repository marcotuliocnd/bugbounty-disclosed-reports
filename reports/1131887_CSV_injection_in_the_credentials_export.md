# CSV injection in the credentials export

## Report Details
- **Report ID**: 1131887
- **URL**: https://hackerone.com/reports/1131887
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-03-23T08:10:55.216Z
- **Disclosed**: 2021-09-22T19:33:42.956Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hello team!

We have found out that a hacker can inject malicious excel formulas into the credentials details which will be executed when program user exports the credentials details via `https://hackerone.com/hackerone_h1p_bbp3/credentials` -> export credentials and opens this CSV using MS excel. This how an attacker could execute abritary commands in the program user's windows machines throught the malicious CSV files. However, since this attack vector requires an older windows machine the impact is pretty low so we decided to report this as best practice instead of vulnerabilitys (severity none).

## Steps To Reproduce:

- Login to the system as a program user
- Add credentials to the program at `https://hackerone.com/hackerone_h1p_bbp3/credentials`
- Now login as a hacker user of this program and request your credentials using *show credentials* button
- Set value of the account details to the `;=1+1;`
- As a program user navigate to the `https://hackerone.com/hackerone_h1p_bbp3/credentials` and export the credentials

Note: The program user does not see the account details in this phase so s/he won't expect anything harmless.

- Once you open the CSV in the MS excel the formula has been executed and there is a new cell with value `2` instead of `;=1+1`
 

## Recommendation:

Make sure that the payload can't start with the following characters: `;`, `=`, `-`, `@` or `+`.

 

## References:

`https://owasp.org/www-community/attacks/CSV_Injection`

## Impact

Possible command execution in the victim's windows machines

## Attachments
No attachments
