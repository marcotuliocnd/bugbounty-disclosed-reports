# Ability to subscribe to inactive Post+ creators

## Report Details
- **Report ID**: 1322334
- **URL**: https://hackerone.com/reports/1322334
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-28T19:15:05.334Z
- **Disclosed**: 2021-10-05T13:00:33.300Z

## Reporter
- **Username**: ajoekerr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hey y'all! 👋 Hope all is well!

## Summary:
In testing Tumblr's Post+, I've found that it's possible to subscribe to creators that, at one point, opted into Post+ but had opted out after some point. As I note later on, it appears that this is a "one time use only" as the Payment URL becomes invalid after activating Post+ for the inactive Post+ blog.

## Platform(s) Affected:
N/A

## Steps To Reproduce:
In order to reproduce, you need the `blogMembershipsId` of an inactive Post+ blog. This creates a high bar to actually exploit this but, for some reason, I had the `blogMembershipsId` of `███████`, who had deactivated Post+ shortly after launch (the membership ID is `█████`).

1. Get an active Post+ subscription URL (I used `██████.tumblr.com`'s subscription URL).
2. Replace the active Post+ blog's `blogMemershipsId` with the inactive blog's `blogMembershipsId` (if using `███████`, you should have a url like `https://███.payment.tumblr.com/checkout/?token=<token>`).
    * As a heads up, it actually looks like this URL is no longer valid after activating my Post+ subscription for `█████████`.
3. Complete checkout as normal.
4. After checkout, it will redirect back to the active Post+ blog's creator page but it will never load.
5. Verify that the creator page for the previously inactive Post+ blog is active again and that the subscription is active for the inactive Post+ blog.

## Supporting Material/References:
Unfortunately, this looks like a "one time use" only vulnerability as the WooCommerce payment URL is no longer active for `██████` after I attempted to subscribe so I was unable to get a PoC video. However, I've uploaded the receipt in case having the `payment_intent` ID helps at all!

## Impact

As of right now, the only impact I've been able to see is that the inactive Post+ blog's creator page became active, even without them enrolled into Post+: https://www.tumblr.com/creator/█████. However, I would also consider the fact that a page would show the blog name & avatar for the Post+ blog noted in the token but the checkout URL corresponds to the `blogMembershipsId` as unexpected behavior but, as far as I can tell, it would be somewhat of a "self-pwn" 😅.

If y'all don't necessarily consider this a security risk, please let me know and I will self-close this report! To be honest, with what I can see, I consider this to be fairly low impact but I wanted to let y'all know anyway. 🙂

## Attachments
No attachments
