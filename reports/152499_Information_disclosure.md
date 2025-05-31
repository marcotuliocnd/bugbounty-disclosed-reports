# Information disclosure

## Report Details
- **Report ID**: 152499
- **URL**: https://hackerone.com/reports/152499
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-20T11:38:16.548Z
- **Disclosed**: 2017-04-20T14:55:44.480Z

## Reporter
- **Username**: amirisme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello Nextcloud

go to https://help.nextcloud.com/users/<anyusername>.json
for example https://help.nextcloud.com/users/amirie.json

you can see the user information 


    {"user_badges":[{"id":1999,"granted_at":"2016-07-20T11:09:52.983Z","count":1,"badge_id":9,"user_id":1007,"granted_by_id":-1}],"badges":[{"id":9,"name":"Autobiographer","description":"Filled out <a href=\"/my/preferences\">profile</a> information","grant_count":46,"allow_title":false,"multiple_grant":false,"icon":"fa-certificate","image":null,"listable":true,"enabled":true,"badge_grouping_id":1,"system":true,"slug":"autobiographer","badge_type_id":3}],"badge_types":[{"id":3,"name":"Bronze","sort_order":7}],"users":[{"id":1007,"username":"amirie","avatar_template":"/user_avatar/help.nextcloud.com/amirie/{size}/621_1.png","name":"amirezat","moderator":false,"admin":false},{"id":-1,"username":"system","avatar_template":"/user_avatar/help.nextcloud.com/system/{size}/1_1.png","name":"system","moderator":true,"admin":true}],"user":{"id":1007,"username":"amirie","avatar_template":"/user_avatar/help.nextcloud.com/amirie/{size}/621_1.png","name":"amirezat","last_posted_at":"2016-07-20T11:10:10.064Z","last_seen_at":"2016-07-20T11:11:14.995Z","created_at":"2016-07-17T21:56:22.016Z","website_name":"help.nextcloud.com/users/amirie/preferences","can_edit":false,"can_edit_username":false,"can_edit_email":false,"can_edit_name":false,"can_send_private_messages":false,"can_send_private_message_to_user":false,"trust_level":0,"moderator":false,"admin":false,"title":null,"uploaded_avatar_id":621,"badge_count":1,"custom_fields":{},"pending_count":0,"profile_view_count":1,"invited_by":null,"groups":[{"id":10,"automatic":true,"name":"trust_level_0","user_count":903,"alias_level":0,"visible":true,"automatic_membership_email_domains":null,"automatic_membership_retroactive":false,"primary_group":false,"title":null,"grant_trust_level":null,"has_messages":false,"mentionable":false}],"featured_user_badge_ids":[1999],"card_badge":null}}
Best Regards,
Amir.


## Attachments
- Information_disclosure.jpg
