# Private program disclosure via `vpn_suspended` GraphQL query

## Report Details
- **Report ID**: 715192
- **URL**: https://hackerone.com/reports/715192
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-10-16T09:09:46.769Z
- **Disclosed**: 2019-10-21T19:07:39.568Z

## Reporter
- **Username**: unknown_person
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
`vpn_suspended` of Team object got exposed

**Description:**
An attacker can get vpn_suspended value of any program (including external program which also have private  program   eg. █████  and external program which does not have private program)

What an attacker can do with this ?
If an external program (which also has private program) has enabled VPN , then value of vpn_suspended become false, so with this information, an attacker can find external programs which have private program, because there is no VPN feature in sandbox mode (all other external programs will be in sandbox mode) 

### Steps To Reproduce

1.)  run the below graphql query

POST /graphql? HTTP/1.1

```
{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,vpn_enabled,vpn_suspended,base_bounty}","variables":{"handle_0":"█████","size_1":"small"}}
```

You will get response of 

```
{"data":{"team":{"id":"███","name":"████████","about":"███████","_profile_picturePkPpF":"█████","offers_swag":null,"offers_bounties":null,"vpn_enabled":null,"vpn_suspended":true,"base_bounty":null}}}
```


2. ) the vpn_suspended status of ███████ program is true

## Impact

an attacker can find external programs which have private program

## Attachments
No attachments
