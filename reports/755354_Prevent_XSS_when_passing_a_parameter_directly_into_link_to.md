# Prevent XSS when passing a parameter directly into link_to 

## Report Details
- **Report ID**: 755354
- **URL**: https://hackerone.com/reports/755354
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-10T18:00:07.892Z
- **Disclosed**: 2020-05-13T18:19:25.408Z

## Reporter
- **Username**: speleding
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
*Note: I would say this is perhaps more of a feature request than an actual vulnerability, but Rafael França deleted this from GitHub and asked to submit it here instead*

In a rails views it's easy to accidentally create an XSS vulnerability by using the following in a template:
`<%= link_to 'Back', params[:back] %>`

Doing this exposes the app to an attack that can easily be demonstrated by simply adding this to URL of that view:
`?back=javascript%3Aalert%28boom%29%3B`

I think it would be good if rails detects this situation and filters the link_to parameter if it's from an untrusted source. The attached two-line patch does this by only allowing the HTTP(S) protocol in that case.

## Impact

If a programmer inadvertently passes a parameter directly into link_to then this would leave his site open to an XSS attack. Since rails filters untrusted parameters in many other situations it may not be apparent to the casual observer that link_to does not filter javascript.

## Attachments
- Prevent_XSS_when_passing_param_directly_into_link_to.patch
