# No rate limiting on form[register]

## Report Details
- **Report ID**: 2583500
- **URL**: https://hackerone.com/reports/2583500
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-07-01T04:40:14.180Z
- **Disclosed**: 2025-03-28T12:43:52.532Z

## Reporter
- **Username**: growler09
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Overview of the Vulnerability:-
Rate limiting is a strategy to limit the frequency of a repeat action within a particular time frame. This ensures that a service doesn’t become unresponsive or unavailable due to too many requests exhausting the application's resources. A lack of rate limiting on this endpoint allows an attacker to send a large number of requests to the server and potentially cause accelerated service usage for the business or exhaust the application resources or for targeted customer it may create annoyance by frequent mail sent by anonymous attacker.

Steps to Reproduce:-
Enable a HTTP intercept proxy, such as Burp Suite or OWASP ZAP, to record and intercept web traffic from your browser
Using a browser, navigate to "Sign Up" while login.
submit the Register request while using the HTTP intercept proxy to intercept the request.
Using the HTTP intercept proxy, re-issue the captured request 200 times respectively in rapid succession.
Observe within the HTTP intercept proxy that all 200 of these requests generate a ‘HTTP 200 OK’ response, showing that there is "no rate-limiting" on the interface.
Perform another, manual form submission in the browser
Observe that the form is submitted successfully which shows that there is no silent lockout implemented, and the email will be bombed with register OTP mails.

Proof of Concept(POC):-
The following screenshots demonstrate a lack of rate limiting on "Sign Up" interface followed by a successful form submission:
performed attack for 200 times twice in Sign Up/register!

Prevention:
Monitor API activity against rate limits.
Reduce the number of requests.
Implement proper validation for query parameters and request bodies.
Notify clients when rate limits are exceeded.
Remember, rate limiting is crucial for protecting web applications from abuse and ensuring security. 🛡

"Note:- Disposable Mail used for clear proof of concept."

## Impact

No rate limiting on a form can result in reputational damage to the organization if the rate limiting prevents legitimate form submissions and responses. It also has the potential to cause accelerated service usage, which can incur a direct financial cost in environments with SaaS services or pay on demand systems. attacker may create annoyance to user(even non-related peoples) by bombing their Emails vanishing reputation of brand.

## Attachments
- Recording_2024-07-01_095819.mp4
- Recording_2024-06-27_220843.mp4
