# Unbounded memory growth with session handling in TLSv1.3

## Report Details
- **Report ID**: 2622671
- **URL**: https://hackerone.com/reports/2622671
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-07-24T17:09:49.504Z
- **Disclosed**: 2024-09-22T18:21:27.608Z

## Reporter
- **Username**: manishpatidar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Some non-default TLS server configurations can cause unbounded memory growth when processing TLSv1.3 sessions

This problem can occur in TLSv1.3 if the non-default SSL_OP_NO_TICKET option is being used (but not if early_data support is also configured and the default anti-replay protection is in use). In this case, under certain conditions when multiple Client connect to server, the session cache can get into an incorrect state and it will fail to flush properly as it fills. The session cache will continue to grow in an unbounded manner. A malicious client could deliberately create the scenario for this failure to force a Denial of Service. 

Steps to reproduce:
1.	Multiple browser  connecting to webserver and sending continuous connection request  
2.	Session cache limit is set to 20 and with SSL_OP_NO_TICKET option.
3.	Initial few minutes cache size  is ok ( within 20) but after that cache is increasing continuously and consuming all the heap memory available.

•	When new Session is added , OpenSSL is trying to reduce the cache size  but remove_session_lock (ssl_update_cache -> SSL_CTX_add_session ->remove_session_lock) not able to remove the entries from cache
•	ctx->session_cache_tail passed to remove_session_lock  having session_id_length as zero and there is a check in remove_session_lock that only non zero session_id_length are deleted. After that no old session are deleted from cache and new session are added to cache and keep increasing the cache.

{F3465122}
Reason:session was added to cache but  later session_id_length was update as zero. After that cache tail have session_id_length as zero and no entry is deleted after that.
{F3465124}
{F3465127}
## Impact

An attacker may exploit certain server configurations to trigger unbounded memory growth that would lead to a Denial of Service.
This issue only affects TLS servers supporting TLSv1.3. It does not affect TLS clients.

## Attachments
- image.png
- image_(1).png
- image_(2).png
