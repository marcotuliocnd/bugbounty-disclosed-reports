# Boards leak private label names and desciptions

## Report Details
- **Report ID**: 162147
- **URL**: https://hackerone.com/reports/162147
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-22T13:15:23.322Z
- **Disclosed**: 2016-09-02T12:45:08.324Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability details
In anticipation of today's release, I took a look at the new boards feature - which, unrelated to this report, is awesome! There turns out to be an IDOR vulnerability when creating a list based on a label. An attacker can create a list with a label ID that belongs to a private repository. This leaks the name and description of the label to the attacker.

# Proof of concept
- Create a new, private repository
- In the created repository, create a new label - lets assume it has label ID 1
- Create another repository, doesn't matter if it's a private or public repository, and doesn't have to be scoped under the same namespace
- In the created repository, create another new label - lets assume it has label ID 2
- Go to the board of the repository created in step 3, and intercept your network traffic
- Click the label created and notice similar to the one below being sent to the GitLab instance:

**Request**
```
POST /jobertabma/test/board/lists HTTP/1.1
Host: gitlab-instance
...

{"list":{"label_id":2}}
```

**Response**
```
HTTP/1.1 200 OK
...

{"id":3,"list_type":"label","position":1,"title":"super secret title","label":{"id":1,"title":"super secret title","color":"#428BCA","description":null,"priority":null}}
```

 - In the request, change the `label_id` to 1, or any other label ID that doesn't belong to you and forward the request.
 - Refresh the board page, notice the created list - it contains the label name and description

# Fix
This is a very ugly solution, but I just wanted to include it to point you to the vulnerability LoC. Line 18 (or 20, after the fix), creates a `List` object without making sure the provided `label_id` belongs to the project.

```
diff --git i/app/services/boards/lists/create_service.rb w/app/services/boards/l
index 5cb408b..630b05a 100644
--- i/app/services/boards/lists/create_service.rb
+++ w/app/services/boards/lists/create_service.rb
@@ -15,6 +15,8 @@ module Boards
       end

       def create_list_at(position)
+        params[:label_id] = project.labels.find(params[:label_id]).id
+
         board.lists.create(params.merge(list_type: :label, position: position))
       end
     end
```

## Attachments
No attachments
