# HTML injection at Company Name or Product Name and can be shown on Contact Sales form

## Report Details
- **Report ID**: 2076019
- **URL**: https://hackerone.com/reports/2076019
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-19T15:42:19.237Z
- **Disclosed**: 2023-10-18T08:58:35.659Z

## Reporter
- **Username**: domg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
There is a stored Cross-Site Scripting (XSS) vulnerability in the LinkedIn Lead Gen Form, specifically in the Company Name and Product Name fields. The vulnerability allows attackers to inject specific HTML elements, enabling them to change the appearance of a page, which can lead to Phishing attacks via the `<a>` tag or Malware download links via the `<a>` tag. The affected HTML elements include `<strong>`, `<em>`, `<a>` (only if it is a HTTPS link), `<ul>`, `<ol>`, `<sub>`, `<br>`, and `<sup>`. This vulnerability poses a significant risk as it can be leveraged for phishing attacks and spreading malware. It's important to note that this issue occurs when naming a company or product with the payload before proceeding to the Lead Gen form. JavaScript is not possible in this context, and no `<script>` tags are allowed.

## Steps to Reproduce:

1. Create a new LinkedIn account or log in to an existing one.
2. Navigate to the "Companies" section on LinkedIn and add a new company.
3. Name the company using a payload containing the XSS vector using one of the allowed HTML elements, for example:
```<a href="https://malicious-site.com">Click me!</a>```
4. Save the company details and proceed to the "Contact Us" Lead Gen form for the company.
5. Observe that the XSS payload remains intact in the "Company Name" field.

OR

1. Create a new LinkedIn account or log in to an existing one.
2. Navigate to the "Products" section on a Company's page and add a new product for the company.
3. Name the product using a payload containing the XSS vector using one of the allowed HTML elements, for example:
```<a href="https://malicious-site.com">Click me!</a>```
4. Save the product details and proceed to the "Contact Us" Lead Gen form for the product.
5. Observe that the XSS payload remains intact in the "Product Name" field and, if applicable, in the "Company Name" field as well.

## Expected Results:

The Company Name and Product Name fields should sanitize any injected HTML elements, preventing XSS attacks. Users should not be able to inject payloads into these fields, and any suspicious HTML elements should be neutralized.

## Actual Results:

The Company Name and Product Name fields are vulnerable to stored XSS attacks through the allowed HTML elements.

## Impact

This vulnerability can be exploited by malicious actors to perform phishing attacks or to spread malware.

## Attachments
No attachments
