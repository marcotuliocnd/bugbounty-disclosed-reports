# Contacts menu (not app) fails to restrict (to local groups) for contacts from federated servers

## Report Details
- **Report ID**: 895730
- **URL**: https://hackerone.com/reports/895730
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-11T00:03:52.909Z
- **Disclosed**: 2020-07-25T08:10:36.069Z

## Reporter
- **Username**: nursoda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
In two Nextclouds A and B, in settings/admin/sharing, these settings are enabled:
* Restrict users to only share with users in their groups
* Restrict username autocompletion to users within the same groups
* Add server automatically once a federated share was created successfully

Some user on A now shares something to some other user on B → federation for that server is established and green on both NCs.

On B, add a new group with a new user N. That user is the only user in that new, separate group. Log in as N. Click on contacts menu (next to the user menu). One sees all contacts of A. One shouldn't see any.

This is relevant since it is unexpected and NC lacks a means to restrict viewing of such contact data. This may lead to a GDPR relevant data breach. (In my case, it did!) IF data were COPIED to B (cached?, not sure), this would be even worse.

Deleting the federation solves the issue (but breaks functionality otherwise desired). I propose to add further restriction selections (for contacts from federated servers) to sharing.

Sidenote: The way it is now also has a functional glitch: If one clicks in the info "i" next to one contact from a federated server, the "contacts" app opens and shows an error "No such contact found"…

## Impact

Well, what SECURITY impact? It's a PRIVACY impact. But since Nextcloud strives to be the privacy-friendly alternative to big players…

OK: Impact is simple contact information disclosure. But to make clear what dimensions this could lead to: Imagine all business contact information in A (in my case >1000 contacts), readable to completely unrelated people on another instance.

## Attachments
No attachments
