# Ability to DOS any organization's SSO and open up the door to account takeovers

## Report Details
- **Report ID**: 976603
- **URL**: https://hackerone.com/reports/976603
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-08T08:23:34.039Z
- **Disclosed**: 2021-04-15T17:00:41.212Z

## Reporter
- **Username**: cache-money
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
**Summary:**
There's an interesting issue I've spent quite a few days trying to escalate but can't figure out. The impact at this point is that I can DOS any SSO integration making it so nobody in that organization can login. I can also get users to inadvertently SSO into my attacker organization, and then take over their account from there. For existing accounts this would require a victim to click "join", however I think that's likely given the fact that they are SSOing for the first time expecting to join an organization.

The strange behavior and why I think it *might* be possible to escalate further, is that I can have you authenticate against one SSO instance, but have you get added to a completely separate one. So that means there is some sketchy logic which can potentially allow an attacker to authenticate against their own SSO instance, and get added to someone else's organization. I'm not sure if it's possible to get this with zero user interaction, but I will keep trying and update the report if I figure out a way.

The bug stems from the fact that you can create an `entityId` identical to that of another organization **except** with a space ` ` at the end. The application logic then prioritizes that new entityId to add the user to after authenticating against the correct one. So if you have `myentity` as the legitimate entity, and an attacker sets their entity to `myentity[SPACE]` (with a space at the end); users attempting to authenticate into the legitimate `myentity` will technically authenticate against it, but then the application attempts to log them into the attacker's organization. The result of this is a DOS since legitimate users can no longer access their organization. The interesting part of the bug is that if the user is deleted from their original organization (or a **new** user attempts to SSO), they will then be authenticating against their original organization, but get added into the attacker's organization. So it seems the SAML Response is checked against a `trim(issuer)`, but when trying to place the user into an organization, the entity with the space is always prioritized.

The steps below will demonstrate this behavior:

## Steps To Reproduce:
1. Setup SSO and confirm you can login.
2. Create a **new** Grammarly business account and use the same `entityId` (Identity Provider Issuer) you used in step 1, except add a space to the end of it. Use a different keypair for this organization as well.
3. Wait 2 minutes for the change to propagate, then try logging into the same account from step 1, and notice you now get an error.
4. At this point the victim organization is DOS'd. To confirm the strange behavior discussed above, you can delete that user from the victim organization and attempt to login again. Notice you will now end up getting provisioned to the attacker's organization, even though you signed the SAML Response with the victim organization's private key.
5. Once you are provisioned into the attacker's organization, the attacker can then change their `entityId` to something brand new, and login to the victim's account using the keypair they own. If this was a converted personal account, you can then access that user's personal documents.

## Impact

- Ability to effectively disable SSO for any organization.
- Ability to get users provisioned into an attacker's account, which they can then takeover.

Thanks,
-- Tanner

## Attachments
No attachments
