# Federated editing allows iframing possibly malicious remotes

## Report Details
- **Report ID**: 1210424
- **URL**: https://hackerone.com/reports/1210424
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-27T09:46:43.244Z
- **Disclosed**: 2022-07-02T09:10:54.721Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So this attack is less likely now that you killed the trusted server auto adding. But as far as I could tell you did not clear out old servers. Let me first describe the attack:

1. UserA on ServerA sends a federated share to userB on serverB
2. Assume serverA and serverB are trusted servers
3. Now once the the trusted server is established when userB tries to edit the document it will do so on serverA. Hence the iframing
https://github.com/nextcloud/richdocuments/blob/master/lib/AppInfo/Application.php#L239

## Impact

The issue I see with this is that; not until to long ago it was trivial to establish trusted servers with federation (or from public links).

The second issue is that userB now not only has to trust serverB to be secure, properly updated etc. But also trusts implicitly serverA. ServerA could serve malicious code. That shows that the user needs to resubmit their password for example.
This is also not made clear on the settings to the admin that enabling trusted servers opens this possibility.

Now. I admit that this is all not super likely to all happen. But iframing remote sources when clicking to edit a document (which the user will just expect to open their own collabora) poses a real risk I think.

## Attachments
No attachments
