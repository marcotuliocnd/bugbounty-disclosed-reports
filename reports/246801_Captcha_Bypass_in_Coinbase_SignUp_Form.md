# Captcha Bypass in Coinbase SignUp Form

## Report Details
- **Report ID**: 246801
- **URL**: https://hackerone.com/reports/246801
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-07T07:33:35.203Z
- **Disclosed**: 2017-09-05T17:09:43.099Z

## Reporter
- **Username**: tejpratap
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
Vulnerability description:

The g-recaptcha-response is not validated on the server-side when submitting a Signup form to the endpoint. Any or no value can be provided for this header

Step to reproduce:

1. https://www.coinbase.com/signup
2. Fill the input field and Validate the captcha.
3. Trun on Brurp submit form and capture the request.
4. Remove the g-recaptcha-response( response value) and foreword it.

Impact.
Fake accounts can be created. Also username enumeration can be performed because no application will allow two email to choose same email.





## Attachments
- Original_Request1.png
- Edited_Request1.png
