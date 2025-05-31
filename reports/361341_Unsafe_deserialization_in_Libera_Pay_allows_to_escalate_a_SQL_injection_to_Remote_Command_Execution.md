# Unsafe deserialization in Libera Pay allows to escalate a SQL injection to Remote Command Execution

## Report Details
- **Report ID**: 361341
- **URL**: https://hackerone.com/reports/361341
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-06-03T13:37:46.400Z
- **Disclosed**: 2018-06-04T17:42:54.585Z

## Reporter
- **Username**: kapytein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello.

There isn't a direct vulnerability, however a SQL injection would easily be escalated to a Remote Code Execution. I can't directly exploit it due to the restriction on team names (it does not accept hexdecimal values). I, however, submit this issue in advance and will attempt to escalate this issue further, if possible together with you.

**Vulnerability details**

The vulnerability relies in the serializer & deserializier used for notifications of users. It is using [pickles](https://github.com/liberapay/liberapay.com/blob/8546e2212f08f0d0ad71008ccf679744c3e8fb81/liberapay/utils/__init__.py#L370), which is known to be unsafe. You can basically craft any object, and pickles will happily execute the object. This allows unsafe deserialization, which could lead to Remote Code Execution.

In this case, as far as I have seen, it is used for notifications. As far as I have seen, the deserializer is only used to render notifications, in `render_notifications`, as seen [here](https://github.com/liberapay/liberapay.com/blob/8546e2212f08f0d0ad71008ccf679744c3e8fb81/liberapay/models/participant.py#L1083). 

```python
  for id, event, notif_context, is_new, ts in notifs:
            try:
                notif_context = deserialize(notif_context)
```
The `render_notifications` function is then used on the notifications template page, as seen here:

```

# NOTE: don't factor the render_notifications() call here, it'll break escaping

[---] application/json via json_dump
participant.render_notifications(state)

[---] text/html
% extends "templates/base.html"
```

There is no other place where the deserializer is used, as far as I have seen. The serializer is used in the `notify` function, as seen [here](https://github.com/liberapay/liberapay.com/blob/9ad0dc79183b052df4e1ca5f23914450991f6888/liberapay/models/participant.py#L1010), thus, in the future, whenever unrestrictive input is taken from the user into this function, it will directly allow Remote Code Execution.

**Proof of Concept**
1. Invite an user into your team.
2. Update the context of the notification in the table notifications, by running the SQL query:

UPDATE notifications SET context = E'\\x80027d710028580400000061736432710158030000006c6f6c71025801000000627103580500000033303030307104580100000063710563706f7369780a73797374656d0a7106580c000000736c656570203530303030307107857108527109752e' WHERE id = 43;`

3. Log in as the user who is invited to your team, browse to notifications and notices that the sleep command was used (basically, it will hang).

## Impact

This could allow remote code execution if a SQL injection is escalated.

## Attachments
No attachments
