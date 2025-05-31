# Conduit feed.publish API allows you to spoof other users or make it look like you have access to a restricted object

## Report Details
- **Report ID**: 1566325
- **URL**: https://hackerone.com/reports/1566325
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-11T21:19:12.159Z
- **Disclosed**: 2022-05-18T12:14:06.901Z

## Reporter
- **Username**: dyls
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
The Conduit feed.publish API allows a user to publish stories to the feed. The API accepts a parameter "type"  which will be set to `PhabricatorTokenGivenFeedStory` and accepts JSON in the "data" parameter such as the following:
```
{
  "authorPHID": "PHID-USER-uyg3nn764yetx6nglnbx",
  "tokenPHID": "PHID-TOKN-medal-4",
  "objectPHID": "PHID-TASK-lg22pqfkf4iuqbmx35k4"
}
```
This data can be manipulated in order to spoof other users, this is done by replacing the "authorPHID"  value with the user that the attacker wishes to spoof. We can additionally manipulate the "objectPHID" to any PHID of any other object, if the object is restricted, it will look like the attacker has access to the relevant object and was thus able to award the object with a token (though the attacker does not have access to the object and the story only shows for users with access to the object). The user PHID can easily be gotten from the relevant user's page. The attacker can get the object PHID of a restricted object from the HTML of a page if the restricted object is attached in some form to the page (e.g., a restricted task as a subtask of a viewable task).

I'm not exactly sure what the purpose of this API is, but it should at least be restricted in some form (e.g, only callable by bots or administrators). An attacker can also simply spam the feed with lots of stories, or cause the feed to error if given bad data (such as an empty list), in which case the relevant row will need to be deleted from the `phabricator_feed.feed_storydata`table.

## Impact

An attacker can make make it look a user has performed an action which the user did not perform (awarding  a token), this could result in the relevant user being disabled if it is suspected that the account was compromised. If a disabled account is spoofed, it could look as if an attacker has discovered a way to perform an action even with the account disabled. It could also look as if an attacker has gained access to an object that they don't have access to.

## Attachments
No attachments
