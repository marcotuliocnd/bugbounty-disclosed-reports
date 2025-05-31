# Reference caching can leak data to unauthorized users

## Report Details
- **Report ID**: 1767503
- **URL**: https://hackerone.com/reports/1767503
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-08T22:00:44.238Z
- **Disclosed**: 2023-01-13T08:39:06.107Z

## Reporter
- **Username**: systemkeeper
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
The [ReferenceManager](https://github.com/nextcloud/server/blob/master/lib/private/Collaboration/Reference/ReferenceManager.php) uses a cache to store information about previously accessed references. The used `cachePrefix` in deck ([see here](https://github.com/nextcloud/deck/blob/e55b3a0a26a65a01fae8cfdf83b1066616bfa6ee/lib/Reference/CardReferenceProvider.php#L154-L166)) is independent of the user. If User1 has access to a deck card and the reference data is stored in the cache, any user with knowledge of the boardId/cardId can access the information of that deck card.

## Steps To Reproduce:
  1. User1 has a deck card and shares the link in a talk conversation
  2. Any user of that conversation (or with knowledge of the link) is able to see the deck card, if the call to the reference provider was done for user1 before


## Supporting Material/References:
User "Admin":
{F2025386}

User "Test":
{F2025389}

## Impact

I think the impact should be minimal, because multiple things need to happen to leak information (the reference needs to be cached, another user needs to know the url, etc.).
The GitHub-Integration uses the `userId` as a cachePrefix, this so this shouldn't be a issue in that case, [see here](https://github.com/nextcloud/integration_github/blob/bb443c47fc8a9b0ba090456461040136a93c9214/lib/Reference/GithubReferenceProvider.php#L175-L182).
I haven't looked at other reference providers.

## Attachments
- image.png
- image.png
