# Unexpected access to process open files via file:///proc/self/fd/n

## Report Details
- **Report ID**: 770190
- **URL**: https://hackerone.com/reports/770190
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-08T11:29:41.917Z
- **Disclosed**: 2021-02-08T07:53:52.299Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
file_connect() routine (https://github.com/curl/curl/blob/1b71bc532bde8621fd3260843f8197182a467ff2/lib/file.c#L134) does not prevent access to /proc/self/fd pseudo filesystem. Application using libcurl and accepting URLs to fetch can be tricked to return content of any open file by passing a specially crafted file:///proc/self/fd/<number> URLs. Since the specific files are open by the application itself, they will always be accessible as long as the files remain open. This will bypass for example drop of privileges performed after opening the file(s).

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Open a privileged file (for example /etc/shadow)
  2. Drop the process privileges
  3. Accept URL as user input
  4. Fetch URL with libcurl
  5. Send received data to user


## Supporting Material/References:

## Impact

Authorization bypass: Access to privileged files otherwise not accessible via file://

## Attachments
No attachments
