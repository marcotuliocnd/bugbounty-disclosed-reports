# auto-logout after 20 minutes

## Report Details
- **Report ID**: 123897
- **URL**: https://hackerone.com/reports/123897
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-03-17T07:00:28.152Z
- **Disclosed**: 2016-08-23T16:06:47.067Z

## Reporter
- **Username**: trabajoduro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi,

Session is not getting expired even after keeping  the application idle for 20 min and after browser closure.

Information:
(JavaScript code can be used by the web application in all (or critical) pages to automatically logout client sessions after the idle timeout expires, for example, by redirecting the user to the logout page (the same resource used by the logout button mentioned previously).

The benefit of enhancing the server-side idle timeout functionality with client-side code is that the user can see that the session has finished due to inactivity, or even can be notified in advance that the session is about to expire through a countdown timer and warning messages. This user-friendly approach helps to avoid loss of work in web pages that require extensive input data due to server-side silently expired sessions.


With the goal of detecting (and, in some scenarios, protecting against) user misbehaviors and session hijacking, it is highly recommended to bind the session ID to other user or client properties, such as the client IP address, User-Agent, or client-based digital certificate. If the web application detects any change or anomaly between these different properties in the middle of an established session, this is a very good indicator of session manipulation and hijacking attempts, and this simple fact can be used to alert and/or terminate the suspicious session.




## Attachments
No attachments
