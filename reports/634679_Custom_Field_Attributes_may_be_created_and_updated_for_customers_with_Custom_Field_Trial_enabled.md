# Custom Field Attributes may be created and updated for customers with Custom Field Trial enabled

## Report Details
- **Report ID**: 634679
- **URL**: https://hackerone.com/reports/634679
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-03T23:17:45.796Z
- **Disclosed**: 2019-07-05T16:54:45.276Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
The Custom Field feature is currently only available for customers on the Enterprise product edition. A trial period can be given by enabling the `custom-fields-trial` feature for programs who are not on that product edition (yet). However, when enabling this feature, the incorrect ordering of an ACL causes a vulnerability that allows anyone that can access the program to create and update Custom Field Attributes. This also works for private programs with an External Program Profile.

# Steps to reproduce
Below are two regression specs. Both of these specs currently fail on `develop` and `master`.

```ruby
describe '#can_manage_custom_fields?' do
  # ... other specs for this ACL ...
  subject { Pavlov.can? :manage_custom_fields, team, user }

  let(:user) { create :user }

  context 'with trial feature enabled' do
    before { create :feature, teams: [team], key: Feature::CUSTOM_FIELDS_TRIAL }

    context 'with a private program' do
      let(:team) { create :team, :soft_launched }

      context 'without a published external program' do
        # adding `user` as an invited hacker to the team
        before do
          Commands::WhitelistedReporters::Create.interact \
            user: user,
            team: team,
            source: WhitelistedReporter::SOURCE_UNKNOWN_INVITE
        end

        it { is_expected.to eq false }
      end

      context 'with a published external program' do
        before { create :external_program, team: team }

        it { is_expected.to eq false }
      end
    end
  end
end
```

# Root cause
Below is a copy of the `manage_custom_fields` ACL:

```ruby
def can_manage_custom_fields?
  return_true_if { feature_enabled?(::Feature::CUSTOM_FIELDS_TRIAL, team: team) }
  return_false_if { team.gates.closed?(FeatureGating::Gates::CUSTOM_FIELDS) }
  can_view_custom_fields_settings?
end

def can_view_custom_fields_settings?
  return_true_if { program_management_permission? }
end
```

The first `return_true_if` block is called before the `program_management_permission?` block. Test coverage for this particular block was lacking in the integration specs for the ACL, as well as the classes using the ACL. This incorrect order was also missed during mandatory peer review.

## Impact

This vulnerability enables arbitrary users to create and update existing Custom Field Attributes. This may disclose confidential attributes and its configuration set by program members or impact the integrity of an existing Custom Field Attribute. At this moment, only three programs have this feature enabled.

## Attachments
No attachments
