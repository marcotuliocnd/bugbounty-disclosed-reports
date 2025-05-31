# Private Emails of Moz Workers Leaked in Public file

## Report Details
- **Report ID**: 2696294
- **URL**: https://hackerone.com/reports/2696294
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-09-03T14:01:20.408Z
- **Disclosed**: 2024-09-04T11:36:28.683Z

## Reporter
- **Username**: the_zodiac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
Hi Team 
in the policy of mozilla  emails and names of workers is private and dont be shared or  disclosure anyway ! because of this restriction all workers in moz gived id and worker name absoultly crypted .But
Its seems that privates emails of moz workers with name and bugs leaked in public files at :https://community.taskcluster-artifacts.net/K5HAOP6RRuuQOQ70LCsf1w/0/public/bugs.json.zst

## Steps To Reproduce:


  1. the file is too large to upload like POC but you can download from this link:https://community.taskcluster-artifacts.net/K5HAOP6RRuuQOQ70LCsf1w/0/public/bugs.json.zst

2. exemple of users worker privates emails leaked:
 
```javascript
{"history":[{"when":"1998-09-29T06:05:20Z","changes":[{"removed":"Platform: Rhapsody","added":"XFE","field_name":"component"}],"who":"mcafee@gmail.com"},{"when":"1998-12-12T17:06:46Z","who":"mcafee@gmail.com","changes":[{"added":"RESOLVED","field_name":"status","removed":"NEW"},{"added":"WONTFIX","field_name":"resolution","removed":""},{"added":"1998-12-12T17:06:46Z","field_name":"cf_last_resolved","removed":""}]},{"changes":[{"added":"VERIFIED","field_name":"status","removed":"RESOLVED"}],"who":"leger@formerly-netscape.com.tld","when":"1999-02-26T20:55:50Z"},{"when":"2004-06-30T02:37:03Z","changes":[{"added":"wlevine@gmail.com","field_name":"cc","removed":""}],"who":"wlevine@gmail.com"},{"changes":[{"added":"firstBug","field_name":"alias","removed":""}],"who":"gavin.sharp@gmail.com","when":"2004-09-22T05:11:42Z"},{"when":"2010-12-08T18:48:57Z","who":"tymerkaev@gmail.com","changes":[{"removed":"","field_name":"cc","added":"tymerkaev@gmail.com"}]},{"when":"2011-09-13T20:41:18Z","changes":[{"removed":"","added":"686525","field_name":"blocks"}],"who":"gerv@mozilla.org"},{"changes":[{"field_name":"blocks","added":"","removed":"686525"}],"who":"gerv@mozilla.org","when":"2011-09-13T20:41:41Z"},{"changes":[{"added":"rexyrexy2@gmail.com","field_name":"cc","removed":""}],"who":"rexyrexy2@gmail.com","when":"2013-05-03T17:18:17Z"},{"who":"dkl@mozilla.com","changes":[{"removed":"","added":"foo","field_name":"whiteboard"}],"when":"2013-07-17T18:25:43Z"},{"when":"2013-07-17T19:01:18Z","changes":[{"removed":"foo","field_name":"whiteboard","added":""}],"who":"dkl@mozilla.com"},{"changes"
```

## Impact

## Summary:
privates names and emails addresse of mozilla workers leaked

## Attachments
No attachments
