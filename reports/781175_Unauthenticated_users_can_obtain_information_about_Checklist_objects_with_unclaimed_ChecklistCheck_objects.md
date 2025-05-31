# Unauthenticated users can obtain information about Checklist objects with unclaimed ChecklistCheck objects

## Report Details
- **Report ID**: 781175
- **URL**: https://hackerone.com/reports/781175
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-22T23:01:46.826Z
- **Disclosed**: 2020-03-20T17:04:05.075Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
The `Checklist` objects that can be queried through GraphQL are supposed to only be accessible by program members, the users who claimed or responded to a check belonging to a checklist, and HackerOne Pentesters. The `Checklist` object is also supposed to be in the `running` state (e.g. when the platform collects responses for the checks) for HackerOne Pentesters to access them. The authorization check is implemented as follows:

```ruby
class ProtectedChecklist
  include ::ProtectedAttribute::Protector

  model { Checklist }

  copy_roles(ProtectedTeam) do
    Checklist.joins(:team)
  end

  property(:RUNNING_CHECKLIST) do
    Checklist.running
  end

  role(:CLAIMER) { |requester| claimed_by_user(requester) }
  role(:RESPONDER) { |requester| responded_by_user(requester) }

  group(
    has_feature(RUNNING_CHECKLIST) & (
      has_role(PUBLIC) |
      has_role(H1_PENTESTER) |
      has_role(WHITELISTED_REPORTER) |
      has_role(INVITATION_RECIPIENT_WITH_SATISFIED_REQUIREMENTS)
    ) |
    has_role(TEAM_MEMBER) |
    has_role(CLAIMER) |
    has_role(RESPONDER),
  ) do
    allow :checklist_check_responses
    allow :checklist_checks
    allow :expires_at
    allow :id
    allow :name
    allow :team
    allow :unclaimed_checklist_checks_count
  end
end

```

At first sight, the authorization check seems to be implemented correctly. However, the `CLAIMER` role is leveraging the `claimed_by_user` scope, which is implemented as follows:

```ruby
scope :claimed_by_user, lambda { |user|
    where(id: ChecklistCheck.where(user_id: user).select(:checklist_id))
  }
```

Instead of an inner join, a query (`ChecklistCheck.where(user_id: user).select(:checklist_id)`) is used to fetch the checklist IDs that are claimed. Because not all checks are claimed, `user_id` can be set to `NULL` in the database. Because the HackerOne GraphQL endpoint can be queried as an anonymous user, this scope can be called with `nil`. This causes anonymous users to automatically get the `CLAIMER` role, thus exposing information about `Checklist` objects.

The other protectors correctly implement the `claimed_by_user` scope.

Any relations defined on the `Checklist` model, such as `team`, `checklist_check_responses`, and `checklist_checks` are protected separately and are not accessible by anonymous users. The exposed information is limited to `Checklist` objects, which doesn't expose any customer information.

The following query can be used to query a `Checklist` object. Make sure you're signed out when executing this query.

```
query {
  node(id: "Z2lkOi8vaGFja2Vyb25lL0NoZWNrbGlzdC8x") {
    ... on Checklist {
      name
      expires_at
    }
  }
}
```

## Impact

Anonymous users can obtain information about checklists.

## Attachments
No attachments
