# Add users to groups who have restricted group invites

## Report Details
- **Report ID**: 538008
- **URL**: https://hackerone.com/reports/538008
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-14T13:20:39.998Z
- **Disclosed**: 2019-07-27T09:22:18.600Z

## Reporter
- **Username**: yuvraj_dighe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
#Description:

WordPress version: 5.2
BuddyPress version: 4.2.0

Through this vulnerability, an attacker could add users to groups who have set :
   `I want to restrict Group invites to my friends only.`

There is no proper validation of the personal settings of the user and thus the users with such privacy settings selected could be added.

#Steps to Reproduce:

Make 2 accounts A and B, make sure they are not friends.

  1. From account of user A, enable the setting `I want to restrict Group invites to my friends only.` from the following URL http://bbwordpress.esy.es/members/yuvraj/settings/invites/.
  2. From account of user B, make a POST request to : 

      `POST : http://bbwordpress.esy.es/wp-admin/admin-ajax.php`
       `BODY : message=&nonce=21f500cbfd&group_id=1&action=groups_send_group_invites&_wpnonce=7264177f51&users%5B%5D=3`

  3. Replace the value of users with the victims user id , i.e id of user A.
  4. Victim (user A) would receive an invitation from Attacker (user B) even though the privacy setting to restrict group invites has been enabled.

## Impact

An attacker who is not a friend of the victim can send him a group invite even though the victim has selected to restrict group invites from friends only.

## Attachments
No attachments
