# Steal private objects of other projects via project import

## Report Details
- **Report ID**: 743953
- **URL**: https://hackerone.com/reports/743953
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-11-22T04:52:22.161Z
- **Disclosed**: 2022-06-07T14:16:42.999Z

## Reporter
- **Username**: saltyyolk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
An attacker could transfer issues, merge requests of another project to the imported project by importing a crafted GitLab export. 

### Steps to reproduce
1. Import the attached tarball as GitLab export.
2. Check the issues page of the imported project. You will see an private issue created by https://gitlab.com/nyangawa-h1 instead of the current user.

### Description
The exploit is in project.json, I added one line to assign `issue_ids` and kept `issues` an empty array.
```
    "issue_ids": [ 27422144 ],                                                 
    "issues": [],  
```

The issues_ids contains the database id of the issues the attacker wants to steal. There's no good way for the attacker to know the id of a specific issue, but as the id is incremental, the attacker could simply steal as many issues as possible in a brute forcing manner.

The root cause of this issue lies in `project_tree_restorer.rb`
```
...
@project.assign_attributes(project_params)
...
```

Many attributes (foreign key) like `issue_ids` and `merge_request_ids` are not excluded during import. According to my observation, affected objects including (but not limited to):
```
board_ids
issue_ids
merge_request_ids
note_ids
...
```
Looks like almost all non-excluded attributes behaves like `issues` are affected.

### Examples

{F640860}

### Output of checks

This bug happens on GitLab.com and self-hosted GitLab installations.

## Impact

With this ability to modify relations between objects, an attacker could end up with accessing random resources of other users by traversing the incremental ID space.

## Attachments
- test.tar.gz
- 2019-11-22-123223_591x403_scrot.png
