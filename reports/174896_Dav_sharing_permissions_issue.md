# Dav sharing permissions issue

## Report Details
- **Report ID**: 174896
- **URL**: https://hackerone.com/reports/174896
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-10T07:55:37.422Z
- **Disclosed**: 2017-05-20T21:57:21.170Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
### Steps

1. Create users "Test 1" and "Test 2", make "Test 1" member of "Group A"
2. Share a calendar with group "Group A" editable
3. Share the same calendar with user "Test 2" readonly
4. As "Test 1" open the calendar app and unshare the calendar from "Test 2" - works
5. As "Test 1" open the calendar app and remove edit permissions for "Group A" - works

In my opinion steps 4 and 5 should not be possible. The shares should not even be visible in my opinion.

## Attachments
No attachments
