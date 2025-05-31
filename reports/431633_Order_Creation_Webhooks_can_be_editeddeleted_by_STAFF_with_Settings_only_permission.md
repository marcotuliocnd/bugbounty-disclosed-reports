# Order Creation Webhooks can be edited/deleted by STAFF with `Settings` only permission

## Report Details
- **Report ID**: 431633
- **URL**: https://hackerone.com/reports/431633
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-31T05:43:47.855Z
- **Disclosed**: 2019-05-11T03:25:27.533Z

## Reporter
- **Username**: h13-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

A STAFF with just `Settings` permission can only create 1 type of webhook called `Shop Update` as seen below.

{F368739}

Attempting to create a `Order Creation` webhook via burp proxy gives a 403 -Forbidden response with the message indicating that `You do not have permission to create webhooks with orders/create ` as seen below.

{F368743}

So technically from the above results it means that any STAFF with just `Settings` permission is restricted to create any webhooks related to `Order` or __make modifications/deletions to Order webhooks__ created by Owner or other permitted users.

From my testing I observed that a STAFF member with just `Settings` only permission could modify `Order` webhooks if the web-hooks were created previously by Owner or other permitted users. These Order webhooks can also be deleted by the STAFF member.

__STEPS__

1.Onwer assigns `Settings` only permission to STAFF.
2.Owner creates a webhook for `Order Creation`.
{F368756}
{F368757}
3.STAFF logs into Store Admin and then navigates to Settings>>Notifications. STAFF can see the `Order Creation` webhook which was created by Owner.
{F368758}
4.STAFF then clicks on the wehbook. This opens a modal box where STAFF can make modifications in he URL. STAFF then clicks on `Save Webhook`
{F368759}
{F368760}
As you can see from the above screen shot, the `Order creation` webhook was modified by STAFF.

5.The STAFF can also delete a `Order Creation` webhook.
{F368762}
{F368763}

## Impact

From my previous report #430285, @jack_mccracken stated the below

>Order notifications are restricted to staff members with the `Orders` permission.

A Webhook is technically an event which is which triggered due to some activity. In this case, the event `Order Creation` webhook will trigger a notification to the specified URL in webhook. The fact that a STAFF user with just `Settings` permission isn't allowed to create a `Order Creation` webhook indicates that the STAFF must also need `Orders` permission to create it.

But from my testing, it was possible for a STAFF with just `Settings` permission to edit/delete a `Order Creation` webhook which IMO should not be authorized to the STAFF member.

Let me know what you think about it.

Thanks.
@h13-

## Attachments
No attachments
