# Fetch private list metadata and any user's personal name

## Report Details
- **Report ID**: 162822
- **URL**: https://hackerone.com/reports/162822
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-23T20:34:15.225Z
- **Disclosed**: 2016-09-12T20:00:01.013Z

## Reporter
- **Username**: sameoldstory
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Overview
==
When a user creates a list, they can choose whether to make the list visible in search and whether to show their name with the list. The problem is that the attacker can still access the information that the user chose to hide. Furthermore, if the attacker gets hold of a user's ID, they can find out user's personal name irrespective of whether the user has created any lists at all.

Steps to Reproduce
==
Both the victim and the attacker have to be Instacart users.

1. Victim creates a list and unchecks both "visible in search" and "show my name" boxes.
2. Victim shares the link publicly.
3. Attacker follows the shared link and adds the list to favorites. The response from the server reveals the list metadata including victim's personal name, list title, description and images:

    ```
    POST /api/v2/lists/10/star_toggle
    
    {
      "meta": {
        "code": 200
      },
      "data": {
        "id": 10,
        "name": "Test",
        "description": "This is the description of a shopping list",
        "user_id": 10,
        "visible": false,
        ...
        "user_name": "Apoorva M",
        ...
      }
    ```

Security Implications
==

The attacker can use the `star_toggle` endpoint to obtain metadata of any list regardless of what the `visible` flag is set to. Since list ID is incremental it doesn't take much effort to obtain metadata for all Instacart lists, both public and private.

Additional Exploit
==

There's one more endpoint that, although doesn't reveal nearly as much information, does reveal victim's personal name and doesn't even require the victim to have any lists:

```
GET /api/v2/lists?user_id=10

{"meta":{"code":200,"author_name":"Apoorva M"},"data":[],"pagination":{"total":0,"per_page":0,"page":1}}
```

The attacker can either look up personal name of the user they're interested in, or simply dump whole list of Instacart users personal names, since the user ID is also incremental.

## Attachments
No attachments
