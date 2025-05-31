# curl overwrites local file with -J option if file non-readable, but file writable.

## Report Details
- **Report ID**: 926638
- **URL**: https://hackerone.com/reports/926638
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-18T00:52:32.779Z
- **Disclosed**: 2020-08-01T16:46:35.501Z

## Reporter
- **Username**: brumbrum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

When using -J -O options on curl command line tool and a server responding with a header that is using Content-Disposition to provide a filename, existing local file will be overwritten if the file is non-readable by the current user, but file is writable by the current user.

Curl contains protection to prevent the overwrite, but protection code is using the file's readability permission to check for its existence.  So protection will be bypassed in this case, as it is only writable by the user.

Issue was discovered after review of CVE-2020-8177 description. I was curious how the Content-Disposition feature and prevention of file overwrite worked.  While reviewing the code around that feature noted that the existence of the file is checked via being able to read the file.  So what happens if the file is not readable, but writable!?!

Why would a system have a file that is writable only, for sensitive information that must be collected by a particular user, but must not be viewable by that user.  Certain logs or audit trails or privacy related files or security related files, might have such restrictions.

Additionally, and in an extreme example, code as written is susceptible to Race Condition as the file existence check and file write are done with two distinct fopen() calls in the tool_create_output_file() in tool_cb_wrt.c file.  Data lose possible if parallel write operations performed on the same file via two curl processes, or even some other process (malicious or not) acting/interfering on the same file.


## Steps To Reproduce:
1. Create a new file (e.g. echo "TEST" >data.txt)
2. Check content of file to see that file contains "TEST".
3. Change permissions of new file to remove read permission (e.g. chmod 222 data.txt)
4. Download file from remote server that will have Content-Disposition with filename "data.txt"
5. Check that file data.txt is still only writable! Permissions have not changed.
6. Change permissions to add the read permission back (so we can see the content)
7. View the content of data.txt file, it will be overwritten with server response.

## Supporting Material/References:

1. Log of reproduction attached. See curl_reproduction.log attached.
2. Source for a simple Golang HTTP server with Content-Disposition header also attached.  See httpserver.go file attached.


## Mitigation:

One way to fix the issue robustly (check for file existence and create file in one operation) would be to use the open() to create the file while using safe options (such as O_CREAT | O_WRONLY | O_EXCL), as is shown in one of the solutions in this stackoverflow posting (see posting by "Dan Lenski", for example):

https://stackoverflow.com/questions/230062/whats-the-best-way-to-check-if-a-file-exists-in-c

## Impact

- An existing local file could be overwritten, either maliciously or accidentally by curl
- A malicious server would need to send Content-Disposition with filename provided at the same time, as the victim would have to use the -J -O option on the curl command line side, with a file that is non-readable, but writable.

## Attachments
- curl_reproduction.log
- httpserver.go
