# Read-only team members can read all properties of webhooks

## Report Details
- **Report ID**: 818848
- **URL**: https://hackerone.com/reports/818848
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-13T17:07:03.545Z
- **Disclosed**: 2020-04-29T17:21:29.411Z

## Reporter
- **Username**: bencode
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Description:**

A team member can view all properties of webhooks despite not needing them.

### Steps To Reproduce

1. Have an admin of a program setup webhooks
2. As a team member (read-only)log in
3. Run the following graphql query:
```
    {
      query {
        team(handle: "security") {
          name
          webhooks {
            nodes {
              id
              secret
              url
            }
          }
        }
      }
    }
```
4. See that you get data back

## Impact

Read only users will be able to identify where webhooks exist and secrets

## Attachments
No attachments
