# Widespread CSRF on authenticated POST endpoints

## Report Details
- **Report ID**: 1309435
- **URL**: https://hackerone.com/reports/1309435
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-08-18T06:16:46.093Z
- **Disclosed**: 2022-02-13T10:38:20.252Z

## Reporter
- **Username**: zeyu2001
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:

Cross-Site Request Forgery (CSRF) is possible on most, if not all, authenticated POST endpoints.

While CORS is configured such that the Access-Control-Allow-Origin header is set to `Access-Control-Allow-Origin: hackers.upchieve.org`, CORS does **not** prevent CSRF - it only prevents the attacker from reading the response. This does not stop the attacker from performing any arbitrary actions on behalf of the user.

This is possible through a simple HTML form with hidden inputs, submitted with JavaScript. While POST requests are made using JSON data by default, `application/x-www-form-urlencoded` is accepted as well. Because the user's session cookie does not have the SameSite attribute set, it is sent along with the request.

The following endpoints were found to be vulnerable:
- `POST /api/calendar/save` (set availability for text messages)
- `POST /api/training/score` (submit quizzes and subject certifications)
- `POST /auth/reset/send` (send password reset email)
- `POST /api/user/volunteer-approval/background-information` (submit background information)
- `POST /api/user/volunteer-approval/reference` (request a reference)

The attacker can perform any of the above actions on behalf of the user, as long as the user has a valid session cookie. There are probably more endpoints to be discovered, but I do not have access to them yet due to the approval / onboarding process.

PUT requests, particularly `PUT /api/user` (to update a user's phone number and account status), are not possible through this method. However, older browsers might not comply to CORS pre-flight requests and still allow a PUT request initiated by JavaScript on the attacker's site to go through.

## Steps To Reproduce:

1. As a victim, log in to https://hackers.upchieve.org/
2. Create a page like the one below.

This is an example for performing a CSRF on the `/api/calendar/save` endpoint (the full HTML file is attached). In this example, we set all the possible time slots to "true".

```html
<html>
  <body>
    <form action="https://hackers.upchieve.org/api/calendar/save" method="POST">
        <input type="hidden" name="availability[Sunday][12a]" value="true" />
        <input type="hidden" name="availability[Sunday][1a]" value="true" />
		
		...
		
        <input type="hidden" name="availability[Saturday][11p]" value="true" />
        <input type="hidden" name="tz" value="Asia/Singapore" />
    </form>
    <script>
      	document.forms[0].submit();
    </script>
  </body>
</html>
```

3. Serve the page on the attacker server.
4. As the victim, visit http://ATTACKER_SERVER/calendar_csrf.html

Once the HTML page loads on the browser, the POST request is submitted and we would see the following response:

```json
{"msg":"Schedule saved"}
```

5. Verify that the victim's calendar has been modified.

I have also prepared other CSRF payloads for the other endpoints.

- `calendar_csrf.html` performs the above-described attack.
- `reference_csrf.html` sends out reference requests on behalf of the victim.
- `quiz_csrf.html` submits quizzes for grading on behalf of the victim.
- `reset_csrf` sends out password resets on behalf of the victim.

## Supporting Material/References:

I have attached the CSRF payloads, a screenshot of the changed calendar, and a screenshot of the output from the quiz CSRF.

## Recommendations for Fixing/Mitigation

- Use CSRF tokens
- Use the SameSite attribute for cookies

## Impact

When an authenticated user visits any attacker-controlled site, the attacker is able to perform arbitrary authenticated actions on behalf of the user. While the attacker cannot obtain the request output from the CSRF, he is still able to perform sensitive actions blindly.

## Attachments
- calendar_csrf.html
- quiz_csrf.html
- changed_calendar.png
- reference_csrf.html
- reset_csrf.html
- quiz_csrf.png
