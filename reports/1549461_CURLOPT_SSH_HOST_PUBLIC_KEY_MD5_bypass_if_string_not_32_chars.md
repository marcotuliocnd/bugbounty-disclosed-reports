# CURLOPT_SSH_HOST_PUBLIC_KEY_MD5 bypass if string not 32 chars

## Report Details
- **Report ID**: 1549461
- **URL**: https://hackerone.com/reports/1549461
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-24T17:04:26.222Z
- **Disclosed**: 2022-04-25T09:05:24.904Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Due to logic flaw in  `CURLOPT_SSH_HOST_PUBLIC_KEY_MD5` handling, the host fingerprint validation will be bypassed if the passed a string that is not exactly 32 characters long.

## Steps To Reproduce:
  1. `curl_easy_setopt(curl, CURLOPT_SSH_HOST_PUBLIC_KEY_MD5,   "afe17cd62a0f3b61f1ab9cb22ba269a"); // 31 chars`
  2. perform` sftp://` or `scp://` actions 

Note: `curl` command is not affected since it explicitly checks that the `--hostpubmd5` string is 32 characters long, and if it is not `PARAM_BAD_USE` is returned.

The bug is at https://github.com/curl/curl/blob/f7f26077bc563375becdb2adbcd49eb9f28590f9/lib/vssh/libssh2.c#L733

If the string length is other than 32 it should result in signature check failure instead of success. Obvious fix would be to remove the `if(pubkey_md5 && strlen(pubkey_md5) == 32)`test  completely.

## Impact

SSH host identify bypass.

For this issue to be realised, a wrong size fingerprint needs to be passed (either by accident or by malice). It is likely that this is far more likely to happen by accident, since if some actor can tamper with the fingerprints they can bypass the validation anyway. Note that `curl_easy_setopt` `CURLOPT_SSH_HOST_PUBLIC_KEY_MD5` does not return an error indicating that something is wrong, hence this is breaking the principle of least surprise.

## Attachments
No attachments
