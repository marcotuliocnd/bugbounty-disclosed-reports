# CBC "cut and paste" attack may cause Open Redirect(even XSS)

## Report Details
- **Report ID**: 126203
- **URL**: https://hackerone.com/reports/126203
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-26T17:43:15.898Z
- **Disclosed**: 2016-08-12T17:20:06.598Z

## Reporter
- **Username**: orange
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hello, Uber Security Team

I found an vulnerability in Uber URL redirect page.

# Vulnerability
In page
```
http://pages.et.uber.com/Redirect.aspx?EQ=5c591a8916642e73ef70dd2c27bd4bad7d810b960a984f390e396861d8a70dfd8d4ad287476f76f106d578f9ace7becffd6e3b312bb4c389315d140317a39050ed569698560fe77404eb8e2f6b2299542477613ae27b43d6d75e133918f7531a2cbea134db7c614a0182342d7079019621af699d14cb1a7cfaa5d14b2982a1a7082d1ff2507b504e68763a7c621e409ef8dd7fe980c48e0664bcb71d4d96523bec4638573e1cff2ba6cc032c5986fe5497c86cfaefb22406bd798a7f8312fde3acd3757bd120dfa0e40f3acb1e99e66c
```

parameter "EQ" is an encrypted URL and "Redirect.aspx" will redirect page to url which is decrypted.
After some trying, it looks like encryted by **CBC mode** and block size is **8**.

And I found an URL 
```
https://pages.et.uber.com/hangzhou1year/?uuid=1234
```

This URL can encrypted itself. For example
Access
`https://pages.et.uber.com/hangzhou1year/?uuid=1234`
and view the source you will see
```
https://pages.et.uber.com/Redirect.aspx?EQ=5c591a8916642e73ef70dd2c27bd4bad7d810b960a984f390e396861d8a70dfd8d4ad287476f76f106d578f9ace7becffd6e3b312bb4c389315d140317a39050ed569698560fe77404eb8e2f6b2299542477613ae27b43d6d75e133918f7531a2cbea134db7c614a0182342d7079019621af699d14cb1a7cfaa5d14b2982a1a7082d1ff2507b504e68763a7c621e409ef8dd7fe980c48e0664bcb71d4d96523bec4638573e1cff2ba6cc032c5986fe5497c86cfaefb22406bd798a7f8312fde3acd3757bd120dfa025d290b1cf9a6e85
```
Above is the encrypted result of string `https://pages.et.uber.com/hangzhou1year/?uuid=1234`


# Exploiting
ok, now I can encrypt something by `?uuid=whatever` and decrypt something by `?EQ=whatever`

so I can decrypt all the cipher by `?EQ=whatever` (remember the padding...)

And I can create any cipher by **CBC cut and paste attack**
For Example, I encrypt `@orange.tw/?` and paste and cipher to bellow URL, when you access URL, you will redirect to orange.tw(my website)
```
http://pages.et.uber.com/Redirect.aspx?EQ=5c591a8916642e73ef70dd2c27bd4bad7d810b960a984f390e396861d8a70dfd8d4ad287476f76f106d578f9ace7becffd6e3b312bb4c389315d140317a39050ed569698560fe77404eb8e2f6b2299542477613ae27b43d6d75e133918f7531a2cbea134db7c614a0182342d7079019621af699d14cb1a7cfaa5d14b2982a1a7082d1ff2507b504e68763a7c621e409ef8dd7fe980c48e0664bcb71d4d96523bc9a3bb1c67bf3b0edc8be7c80b4a998d2ce17fd5dd704e741309ec46b0627b0c1924321b894eebbc0128fce2b552959e
```

I think this vulnerability also can lead to XSS by creating an URL like
```
data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K
```
if I have more time doing research ( it's evening in my country now :O )


# Attachments

`fake.py` is my Python poc
`2016-03-26_172607.jpg` decrypt the last block of cipher (%08%08%08%08%08%08%08%08 represented it use PKCS #5 padding)


## Attachments
- fake.py
- 2016-03-26_172607.jpg
