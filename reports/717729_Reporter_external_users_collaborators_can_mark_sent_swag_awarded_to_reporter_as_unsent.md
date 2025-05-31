# Reporter, external users, collaborators can mark sent swag awarded to reporter as unsent

## Report Details
- **Report ID**: 717729
- **URL**: https://hackerone.com/reports/717729
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-19T00:26:50.626Z
- **Disclosed**: 2019-10-25T16:41:22.652Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
An Insecure Direct Object Reference (IDOR) vulnerability allow the reporter, external users, and collaborators to mark sent swag that was awarded to the reporter as unsent. This may result in swag being sent multiple times.

**Proof of concept**
Follow the steps below to reproduce the vulnerability.

* sign in to a user that is not part of any programs
* submit a report to a program, let's assume this program has ID 1
* sign in to a user that can award swag for program 1
* award swag to the report, let's assume the swag object has ID 1
* mark the swag as sent
* sign back in to the user that submitted the report
* create a new program in the sandbox, let's assume this program has ID 2
* use the following GraphQL to toggle the swag back to unsent

```
{"query":"mutation updateState($input_0:UpdateProgramSwagInput!) {updateProgramSwag(input:$input_0) { swag { _id } } }","variables":{"input_0":{"program_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMg==","swag_id":"Z2lkOi8vaGFja2Vyb25lL1N3YWcvMQ==","sent":false,"clientMutationId":"0"}}}
```

Important to note here is that the current signed in user must be allowed to manage swag for the given `program_id`. However, the given `swag_id` can belong to any other program. Due to the protected schema, this will only allow the attacker to pass in swag IDs that were reported to themselves or they are an external user or collaborator in a report that was awarded swag. No additional information is leaked.

**app/graphql/mutations/update_program_swag_mutation.rb**
```ruby
# ...
def resolve(program_id:, swag_id:, sent:)
  unsafe_program = context.schema.object_from_id program_id, context
  safe_program = context[:tics].teams_where_i_have_program_management_permission.find unsafe_program.id # <-- proper authorization check
  swag = context.schema.object_from_id swag_id, context # <-- will return any swag object the user is authorized to see

  updated_swag = Interactors::Programs::UpdateSwag.interact(
    as_user: context[:current_user],
    team: safe_program,
    swag: swag, # <-- swag object is passed to the interactor
    sent: sent,
  ).values[:swag]
```

**app/backend/interactors/programs/update_swag.rb**
```ruby
# frozen_string_literal: true

module Interactors
  module Programs
    class UpdateSwag < HackeroneInteractor
      include Pavlov::StandardizedResult

      attribute :team, Team
      attribute :swag, ::Swag
      attribute :sent, Boolean

      result_value :swag, ::Swag

      private

      def execute
        # ...

        swag.update(sent: sent) # <-- updates the swag object without authorizing the user

        # ...
      end

      def authorized?
        can? :manage_swag, team # <-- only authorizes the user to manage swag for the passed Team
      end

      # ...
    end
  end
end
```

**Recommendation**
The mutation or subsequent interactor can derive the team from the swag object that is passed. It could also do an additional check that the swag object belongs to the given team.

## Impact

This vulnerability may result in swag being sent multiple times.

## Attachments
No attachments
