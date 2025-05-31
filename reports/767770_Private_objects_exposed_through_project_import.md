# Private objects exposed through project import

## Report Details
- **Report ID**: 767770
- **URL**: https://hackerone.com/reports/767770
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-03T16:39:54.149Z
- **Disclosed**: 2022-06-07T14:16:30.343Z

## Reporter
- **Username**: saltyyolk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
This is a bypass of https://hackerone.com/reports/743953 , the current fix is blocking all "_ids" attributes. However an attacker could still set attributes like `issue_ids` by indrectly settings the field within the `attributes` field it self:
```
# project.json
    "attributes": {
        "issue_ids": [ 29279725 ],
        "description": "Set from attributes[description]"
    },
```

### Steps to reproduce

1. Import the attached tarball.
2. Check issues tab

The other parts of the report are mostly same as those I mentioned in https://hackerone.com/reports/743953 , I decide to write a new report considering the impact to gitlab.com.

## Impact

With this ability to modify relations between objects, an attacker could end up with accessing random resources of other users by traversing the incremental ID space.

## Attachments
- exploit.tar.gz
