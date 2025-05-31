# Template stored XSS

## Report Details
- **Report ID**: 141198
- **URL**: https://hackerone.com/reports/141198
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-26T14:22:29.769Z
- **Disclosed**: 2016-07-21T12:33:20.801Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
The template filed names are not escaped properly, which gives an opportunity to inject HTML tags with javascript there.

1. Log into your account
2. Open the template builder https://%your_domain%.drchrono.com/clinical/advanced_form_builder
3. Create a new template with a field called **<svg onload=alert(document.domain)>**
4. Save the template and share it to the library

I created one such template as a proof of concept:

> https://www.drchrono.com/medical-forms/1460752/aaabbbcccdddeee

The script can also be executed at the search page by onmouseover event:

> https://www.drchrono.com/medical-forms/?query=aaa%22bbb%27ccc%3Cddd%3Eeee

## Attachments
No attachments
