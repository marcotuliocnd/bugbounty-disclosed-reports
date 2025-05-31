# When you call your branch the same name as a git hash, it could be checked out by dependents

## Report Details
- **Report ID**: 790634
- **URL**: https://hackerone.com/reports/790634
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-07T16:49:44.872Z
- **Disclosed**: 2021-08-19T21:09:21.671Z

## Reporter
- **Username**: retroplasma
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

If we call a branch the same name like a git hash then the moment it's checked out somewhere, git prefers the branch name.
So let's say the git hash is "e91803d442559d6efb63102b10c919e10901b01d".
And someone referenced that hash in their program.
Now the developer or a hacker with access to the repo can create a branch named "e91803d442559d6efb63102b10c919e10901b01d".
Git will checkout the branch and not the hash when someone puts "git checkout e91803d442559d6efb63102b10c919e10901b01d".
GitHub prevents users from pushing branches that are the same name as hashes, but GitLab does not.

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)

1. Take a hash of a commit A
2. Go to any other commit B
3. Create a branch that is named the same as the hash from commit A
4. Push
5. If someone references the hash in their program, their "git checkout" will checkout commit B. Because it will use the branch name instead of the hash


### Impact

Referencing a hash isn't secure anymore. It would reference a branch that has completely different data.
git shows a warning but "git checkout {...}" is often used.

### Examples

Any project that refs a git ref

### What is the current *bug* behavior?

Gitlab accepts pushed branches that are 40-char hexadecimals

### What is the expected *correct* behavior?

Gitlab shouldn't accept pushed branches that are 40-char hexadecimals (like Github does9

### Relevant logs and/or screenshots

-

### Output of checks

-

#### Results of GitLab environment info

-

## Impact

Redirect pinned refrs of libraries if there is control of a library. A referenced hash won't point to a hash anymore. An attacker can make the branch which has the hash's name contain any other data.

## Attachments
No attachments
