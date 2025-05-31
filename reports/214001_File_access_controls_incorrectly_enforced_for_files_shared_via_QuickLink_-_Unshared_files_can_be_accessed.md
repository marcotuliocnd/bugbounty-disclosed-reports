# File access controls incorrectly enforced for files shared via QuickLink - Unshared files can be accessed

## Report Details
- **Report ID**: 214001
- **URL**: https://hackerone.com/reports/214001
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-16T19:53:39.798Z
- **Disclosed**: 2017-04-16T19:43:18.314Z

## Reporter
- **Username**: eboda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: files

## Vulnerability Information
Enter the support PIN from your test site (if applicable): **305056**
Enter the name of your test site (if applicable): **pwn.brickftp.com**
Enter the subdomain from your test site (if applicable): **pwn.brickftp.com**

## Summary

This is a bug in the file sharing feature QuickLink. The file access control is flawed which allows an attacker to download not just the shared file, but any file that has the same name prefix as the shared file.

## Steps to reproduce
I have created the following files and folders:

```
bar
foo
foobar/secret
footer.php  
```

Let's say I want to share `foo` with some friends, so I use the *Copy Public QuickLink* action and it will create a bundle (see https://pwn.brickftp.com/f/23a17148e ) with just that file: {F169390}.

Now when I try to download `foo` a GET request is sent to https://pwn.brickftp.com/bundles/download?code=23a17148e&path=foo&x=767de6540 . 

Notice that the `path` variable contains foo, if we change it to `bar`, it will tell us: *Invalid path for bundle*.

However, any other path starting with `foo` can be downloaded. For example https://pwn.brickftp.com/bundles/download?code=23a17148e&path=footer.php&x=767de6540

This would also allow to download any file in `foobar/`: https://pwn.brickftp.com/bundles/download?code=23a17148e&path=foo&x=767de6540

### Final Remark
Please note that the above links will most likely not work for if you click on them because the `x` parameter is session specific. But you can still download my files if you go to the QuickLink: https://pwn.brickftp.com/f/23a17148e and then simply replace the `path` variable yourself like I did above.

---
If something is unclear or you have any questions please let me know.

## Attachments
- foo.png
