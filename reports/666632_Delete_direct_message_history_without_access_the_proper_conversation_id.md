# Delete direct message history without access the proper conversation_id

## Report Details
- **Report ID**: 666632
- **URL**: https://hackerone.com/reports/666632
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-03T02:41:26.953Z
- **Disclosed**: 2020-11-20T19:33:04.629Z

## Reporter
- **Username**: soareswallace
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** [add summary of the vulnerability]
An user can invert the user ids from a direct message URL, which is the conversation_id, and delete the whole conversation history without using the proper conversation_id and without a proper feedback to the user.

**Description:** [add more details about this vulnerability]
By having a direct message to any user, Twitter creates a specific id to this conversation. The conversation_id. This id is concatenation between the two user ids in this conversation 
separated by an hyphen . For example:

#1 - user_id = 12345
#2 - user_id = 45678
conversation_id=12345-45678

If an user invert these numbers(e.g: in our example 45678-12345) the user is asked to either accept to receive message from an undefined user or to delete it.(Attached print1). After clicking "Delete" the whole conversation history from the original conversation is deleted without ever following the happy path to proper leave a conversation.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Have a conversation (Direct Message) between two users.
  2. Click on the conversation to open the chat window.
  3. The URL will change and it's going to be something like: https://twitter.com/messages/123456-78910
  4. Invert those numbers on the conversation_id and the new URL will be like: https://twitter.com/messages/78910-123456 and press enter to go to this URL.
  5. User will be asked to either Accept or Delete if he want to let an undefined user to message him.  With all the options above as well, like user info. However is an undefined user. The message will be exactly:

Do you want to let  message you? They won’t know you’ve seen their message until you accept.Report conversation

You can see there is a blank space between the words 'let' and 'message'.
  6. If the user clicks on 'Delete' the original history from the original conversation is deleted(attached image: after_Deleting.png) and the feedback gave to the user doesn't mention this.

## Impact: [add why this issue matters]
Since we didn't use the proper conversation_id to delete the conversation this action might create an inconsistence on the conversations database.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

An attacker could create an inconsistence on the conversation data since we used a wrong conversation_id to delete the history. Maybe this issue could lead to other exploits since we had a info icon for an undefined user.

## Attachments
- print1.png
- after_deleting.png
