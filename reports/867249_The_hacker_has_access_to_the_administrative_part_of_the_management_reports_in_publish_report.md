# The hacker has access to the administrative part of the management reports in publish report

## Report Details
- **Report ID**: 867249
- **URL**: https://hackerone.com/reports/867249
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-06T15:49:29.821Z
- **Disclosed**: 2020-12-16T19:08:18.547Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team, @jobert, @bencode . At the moment, I'm not entirely sure that this has a strong effect. But I also assume that this should not be on behalf of the hacker, and also in the future it may create problems, for example when you add new statuses for the report and they will have some impact on the report.

### Steps To Reproduce

1. https://hackerone.com/hacktivity/publish
2. Create publish report
3. When we create a report, we can see that there is nothing we can do with it

`{"can_manage?":false,"can_export?":false,"can_add_comment?":false,"can_change_state?":false,"can_reopen?":false,
"can_award_bounty?":false,"can_award_swag?":false,"can_suggest_bounty_amount?":false,"can_assign_to_user?":false,
"can_assign_to_h1_triage?":false,"can_hide_timeline?":false,"can_agree_on_going_public?":false,
"can_cancel_disclosure_request?":false,"can_be_publicly_disclosed?":false,"can_post_internal_comments?":false,
"can_manage_common_responses?":false,"can_use_common_responses?":false,"can_reassign_to_team?":false,
"can_change_title?":false,"can_change_weakness?":false,"can_be_manually_disclosed?":false,"can_clone?":false,
"can_close?":false,"can_ban_researcher?":false,"can_create_severity?":true,"can_close_comments?":false,
"can_change_structured_scope?":false,"can_manage_collaborators?":false,"can_view_bounty_weights?":true,
"can_redact?":false,"can_view_credential_account_details?":true,"can_create_retest?":false,"can_request_retest?":false,
"can_manage_link_sharing?":false,"assignable_team_members":[],"assignable_team_member_groups":[]}
`
and `"comments_closed?":true`

There is nothing we can do, including the fact that we can't write comments , However, a hacker can use the admin panel to change the status.
█████████

4. Use this request, we can changed status 
https://hackerone.com/reports/bulk

POST:

```
message=test&substate=triaged&reference=&add_reporter_to_original=false&reply_action=change-state&mark_ineligible_for_bounty=false&reports_count=1&report_ids%5B%5D=ID_PUBLISH_REPORT&bounty_currency=USD
```
`substate=triaged` and `reply_action=change-state` - Change the report to the triaged status

{F817883}

The report which was in the tests: #867226 , #867195 , #867197 , #867218

## Impact

Changes to the publish report status

## Attachments
- triaged_proof.png
