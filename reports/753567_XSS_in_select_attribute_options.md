# XSS in select attribute options

## Report Details
- **Report ID**: 753567
- **URL**: https://hackerone.com/reports/753567
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-07T09:50:11.597Z
- **Disclosed**: 2020-04-29T13:43:08.005Z

## Reporter
- **Username**: sunny0day
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
## To reproduce
1. Create a new select attribute.
2. Add a select attribute option with value `<script>alert('XSS')</script>` and hit Save.
3. Edit the newly created attribute again and see XSS dialog.

The vulnerability lays in the type_form.php file, see https://github.com/concrete5/concrete5/blob/develop/concrete/attributes/select/type_form.php#L40

## Unauthenticated use
The vuln can be pretty bad if the website has an Express Form with select attribute associated with it that "Allow users to add to this list.". In that case, an (unauthenticated) user can submit a form that results to stored XSS.

## Screenshot
{F653172}

## Impact

Stored XSS on /index.php/dashboard/pages/attributes/edit/xxx page and when editing an Express Form block.

## Attachments
- xss-select-attribute.png
