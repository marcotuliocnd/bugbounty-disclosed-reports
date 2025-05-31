# Security@ email forwarding and Embedded Submission drafts can be used to obtain copy of deleted attachments from other HackerOne users

## Report Details
- **Report ID**: 1034346
- **URL**: https://hackerone.com/reports/1034346
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-14T03:25:43.710Z
- **Disclosed**: 2020-11-17T00:42:05.672Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
HackerOne has a number of ways for hackers to submit security vulnerabilities to a program, two of which are through an embedded submission form and through security@ email forwarding. These two features can be exploited to update a report draft created through security@ email forwarding that does not belong to the attacker. In addition to that, the attacker can exploit these features to obtain copies of orphaned platform attachments that were uploaded through an embedded submission form and don't belong to the attacker.

# Steps to reproduce
The exploit consists of chaining two vulnerabilities. The first one is an oversight in the access control of report drafts created and updated through an embedded submission form. To reproduce this first vulnerability, a victim will have to send an email that forwards all emails to a HackerOne inbox. An example of such an email address is security@hackerone.com, which forwards emails to our own program. When someone sends an email to this address, they'd receive an email similar to this one:

{F1077716}

In the backend, this essentially does two things: it creates a `ReportDraft` object and a corresponding `Invitation` object. The email above contains the secret invitation token for the user to get access to the report draft. As long as the invitation is not accepted, the `ReportDraft` has its `reporter_id` and `tracer` attributes set to `NULL`. When a user would accept the invite, the `reporter_id` attribute would be overwritten with the user's ID who accepted the invitation. For now, let's not accept the invite and dive into the inner workings of embedded submission forms.

Similar to security@ email forwarding, embedded submission forms allow anonymous users to create a `ReportDraft` object in the backend. This object contains the current state of the embedded submission form to avoid data loss in case the user happens to close their window. To avoid unauthorized access to other anonymous users writing a report at the same time, the frontend generates a UUID to keep track of which attachments belong to the draft. The `ReportDraft` stores this UUID in the `tracer` attribute. Only when the user knows the UUID of this draft will it be able to update the draft. Every request triggered for an unauthenticated session in an embedded submission form will submit this UUID for the backend to authorize the user. This is where the first vulnerability is found.

The `Teams::EmbeddedSubmissionsController` implements a number of actions, which one of which is `draft_sync`:

```ruby
# frozen_string_literal: true

module Teams
  class EmbeddedSubmissionsController < ApplicationController
    # ...
    def draft_sync
      draft = Interactors::ReportDrafts::UpdateOrCreate.interact_without_authorization(
        draft_id: report_params[:draft_id],
        # ...
        handle: team.handle,
        # ...
        attachment_ids: report_params[:attachment_ids],
        as_user: current_user,
        tracer: report_params[:tracer],
      )
    # ...
  end
end
```

HackerOne's backend consolidates business logic, input validation, and authorization into service objects called interactors. This particular interactor is called explicitly without any form of authorization. Among a few other attributes, the interaction is given a `draft_id`, `attachment_ids`, `tracer`, and a reference to the `current_user`, which is an instance of a `User` object or an instance of `UserAuthentication::AnonymousUser`. The `handle` attribute that is given is the program's handle based on embedded submission UUID. At this point, the application **should** determine whether the `current_user` OR a valid `tracer` value is present, but this check is missing. This is the first vulnerability. When the interaction is executed, it tries to look up a draft using the following code (see `draft` method):

```ruby
# frozen_string_literal: true

module Interactors
  module ReportDrafts
    class UpdateOrCreate < HackeroneInteractor
      attribute :draft_id, Integer, required: false
      # ...
      attribute :attachment_ids, Array, default: []
      attribute :tracer, String, required: false

      private

      def execute
        return if draft_id && draft.nil?

        draft.update(
          # ...
        )

        draft
      end

      # ...

      def draft
        @draft ||= if draft_id
          ReportDraft.find_by(
            id: draft_id,
            team: team,
            reporter: nil_or_current_user,
            tracer: tracer,
          )
        else
          ReportDraft.find_or_initialize_by(
            team: team,
            reporter: nil_or_current_user,
            tracer: tracer,
          )
        end
      end

      # ...

      def nil_or_current_user
        current_user.is_a?(User) ? current_user : nil
      end
    end
  end
end
```

Stepping through the code, a user can see that if a `draft_id` is present, the system will try to look up a `ReportDraft` object by a tracer UUID and reporter. Going back to the security@ email forwarding, we know that there are `ReportDraft` objects that have a `tracer` or `reported_by_id` attribute set to `NULL`. This means that an attacker can, by guessing a draft ID created through the security@ email forwarding feature, change the contents of a draft by completely removing the `tracer` value from a draft sync that is initiated through the embedded submission form. Here is an excerpt of that request:

```http
POST /80b9bc53-a236-445d-a7e4-553828b7d533/embedded_submissions/draft_sync HTTP/2
Host: hackerone.com
...

{
  "draft_id": "1",
  "title": "This becomes the new title for draft 1",
  "vulnerability_information":"This becomes the new vulnerability information for draft 1"
}
```

Once the victim claims the invitation through the email that was shown earlier, they'll see the updated vulnerability information and title.

{F1077723}

You can see that the interaction passes *all* attributes to the `update` call, see `Interactors::ReportDrafts::UpdateOrCreate#execute`. This means that the attacker can only change *all* attributes, reducing the likelihood of the expoitation. However, due to the fact that this allows an attacker to change report drafts, the impact on the integrity is set to high. It could be used to tamper with drafts that are in the process of being submitted to a live program.

To further increase the severity of the vulnerability, it can be chained with another vulnerability. When a user uploads an attachment through an embedded submission form, it'll create an `Attachment` object that belongs to the `ReportDraft` object. In the backend, its attributes will look like this:

```json
{
  "id": "1",
  "uploaded_by_id": null,
  "attachable_id": 1,
  "attachable_type": "ReportDraft"
}
```

The `attachable_id` and `attachable_type` form a polymorphic relation to any other persistent model in HackerOne's database. As long as the user is working on its report, the attachment references a `ReportDraft` object. On submission, it'll transfer the ownership to the `Report` that was created – this is the report that customers see. ActiveRecord, the ORM HackerOne uses, has logic to (conveniently) disassociate a polymorphic relation when the model referencing the polymorphic relation overwrites the IDs. To show this, consider the following code example:

```ruby
# Create an attachment. At this time, the `attachable_id` and `attachable_type` are set to `NULL`
attachment = Attachment.create!

# Create another attachment. At this time, the `attachable_id` and `attachable_type` are set to `NULL`
another_attachment = Attachment.create!

# Create a report draft and reference the first attachment. The `attachable_id` and `attachable_type` of the attachment are updated to reference the created report draft.
report_draft = ReportDraft.create! attachment_ids: [attachment.id]

# Update the attachment IDs of a report draft. This will do two things:
#   - update `attachment.attachable_id` to `NULL`
#   - update `another_attachment.attachable_type` to `ReportDraft`
#   - update `another_attachment.attachable_id` to `report_draft.id`
report_draft.update! attachment_ids: [another_attachment.id]
```

This means that the `attachment`, as created in the above code example, is not referencing any object at all. There is a code path in HackerOne's platform to get an attachment in this state: upload an attachment using an embedded submission form, then clicking the "X" to remove it, and type one character in the vulnerability information field to trigger a draft sync. This will leave the first attachment in an orphaned state that has its `uploaded_by_id` and `attachable_id` set to `NULL`. Going back to the `Interactors::ReportDrafts::UpdateOrCreate` interactor, there's a method that associates attachments to a `ReportDraft` with the following logic:

```ruby
# ...
def valid_attachments
  (
    draft.attachments.with_attached_file.where(id: attachment_ids) +
    Attachment.with_attached_file.where(
      id: attachment_ids,
      attachable_id: nil,
      uploaded_by: nil_or_current_user,
    )
  ).uniq
end
# ...
```

The code that contains the vulnerability is the second `Attachment` lookup: it selects all attachment objects that don't have an `attachable_id` set and that are uploaded by an anonymous user. This means that any attachment that was uploaded by an anonymous user and removed the attachment from a draft can be associated with the attacker's report draft. There are 823 attachments that match this criteria.

An attacker can exploit this chain using the following steps:

1. in an authenticated session, start typing a report to any program. Observe the network traffic for the `draft_sync` endpoint to determine the latest report draft ID, which is included in the response (e.g. 1).
1. in the same session, upload an attachment and observe which ID was associated (e.g. 5).
1. send an email to the program's email forwarding address (e.g. security@hackerone.com). This will create a report draft with an ID that is one to ~ ten IDs up from the report draft the authenticated user created.
1.  in an incognito browser, go to the program's embedded submission form URL. An example is [HackerOne's own form](https://hackerone.com/80b9bc53-a236-445d-a7e4-553828b7d533/embedded_submissions/new). Start typing and intercept the request to the `draft_sync` endpoint.
1. change the `draft_id` to the ID obtained in step 1 and completely remove the `tracer` value from the request.
1. set the `attachment_ids` to an array containing *all* possible attachment IDs from 1 to the ID obtained in step 2
1. claim the report draft through the invitation you received
1. in the UI, observe that the attachments belonging to the victim are attached to the report draft
1. copy the ID and inline them in the vulnerability information field, e.g. `{F5}`
1. in the report preview section, click the link to obtain a copy of the victim's attachment

## Impact

The first vulnerability can be used to change the contents of a number of draft reports that were created through the security@ email forwarding feature. However, chaining the two vulnerabilities would increase the severity as it would allow an attacker to associate orphaned `Attachment` objects to its own report draft, potentially containing sensitive information. The attacker does not have to be authenticated in order to exploit this vulnerability.

## Attachments
- Screen_Shot_2020-11-13_at_6.12.58_PM.png
- Screen_Shot_2020-11-13_at_6.41.57_PM.png
