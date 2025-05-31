# Apparent ██████████ website is publicly exposed, suggests default account details on page and has expired SSL/TLS cert

## Report Details
- **Report ID**: 1025217
- **URL**: https://hackerone.com/reports/1025217
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-03T12:11:27.352Z
- **Disclosed**: 2020-11-23T17:57:19.729Z

## Reporter
- **Username**: mcbazza
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Publicly exposed website (███████) offering default login user/pass with expired SSL

**Description:**
https://██████/ is branded as '████' with ██████ branding/logo and links to ██████ homepage, defense.gov & @DeptofDefense (Twitter account)

## Impact
Publicly exposed service with potentially default credentials listed on homepage that may allow access

## Step-by-step Reproduction Instructions
1. Browse to: https://█████/
2. Note that the cert for this site is expired as of 2nd Jan 2020, and references the FQDN as: █████
3. The same site is also available on port 8080 without the cert - http://██████:8080/
(see attached image that references the default accounts/password that may be used: kiosk/kiosk, user/user)
4. The 'registration' page suggest admin/admin as the Administrator account - https://███████/register
5. This URL references '█████████', who appear to be a US Govt services company - https://███/management/info

## Product, Version, and Configuration (If applicable)
Unknown. Branding on the homepage page reports '███████ v0.0.1-SNAPSHOT' and has '███████' logo

Info taken from: https://█████████/management/info
Displays following:
{"display-ribbon-on-profiles":"dev","git":{"commit":{"id":{"abbrev":"a91feef","describe":"a91feef-dirty"}},"branch":"develop"},"build":{"version":"0.0.1-SNAPSHOT","artifact":"███████","name":"██████████","group":"com.perspecta.idam","time":"2019-10-07T22:00:08.050Z"},"activeProfiles":["prod"]}

## Suggested Mitigation/Remediation Actions
1. Update TLS/SSL cert
2. Secure default accounts.
3. If a test/demo site - take down or hide from public access.

As referenced above, I don't know that this is a valid/active DoD/█████████ resesource. The expired certificated references it as '████████'. However, with the obvious DoD/██████ references on the page I thought it safer to raise a report.
Due to this, I have not carried out any actions other than visiting this page and have not attempted to login using the credentials offered.

If this isn't an active DoD/████████ resource (likely), it could be intended for phishing / credential theft from legitimate users directed towarsds it.

## Impact

I don't know if the default credentials offered (kiosk/kiosk, user/user or admin/admin) work, or what may sit behind this site.
I suspect it is a simply a test/demo/UAT that has been left exposed by the Devs.

## Attachments
No attachments
