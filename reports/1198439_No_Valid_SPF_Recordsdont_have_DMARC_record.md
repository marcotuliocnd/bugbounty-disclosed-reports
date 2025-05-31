# No Valid SPF Records/don't have DMARC record

## Report Details
- **Report ID**: 1198439
- **URL**: https://hackerone.com/reports/1198439
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-05-15T17:09:25.163Z
- **Disclosed**: 2021-05-18T18:49:59.228Z

## Reporter
- **Username**: recreati
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
I have already reported this isssue through email and the company has accepted my report.
Hiii,
There is any issue No valid SPF Records on 
https://app.upchieve.org
Desciprition :
There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.
I found :
SPF record lookup and validation for: https://app.upchieve.org
SPF records are published in DNS as TXT records.
The TXT records found for your domain are:
No valid SPF record found.
Use the back button on your browser to return to the SPF checking tool without clearing the form.
Remediation :
Replace ~all with -all to prevent fake email.
ss attched with this
you can check this using https://www.kitterman.com/spf/validate.html
if you had a valid spf record then you don't have DMARC record due to which any one can send the mail on behalf of comapny which cause same issues of damaging comapny reputation can be used to get user data.
for checking this visit : https://dmarcian.com/spf-survey/
and type your url and you'll find all the details i
i send you the screen shot as a proof of both the above.

## Impact

An attacker would send a Fake email. can also use to get user credential after send a psihing link through mail.The results can be more dangerous.

## Attachments
- Screenshot_2021-05-15-05-28-50-878_com.android.chrome.jpg
- Screenshot_2021-05-15-22-38-04-102_com.google.android.gm.jpg
