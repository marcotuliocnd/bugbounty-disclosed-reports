# Authentication Bypass by abusing Insecure crypto tokens in /lib/OA/Dal/PasswordRecovery.php:

## Report Details
- **Report ID**: 576504
- **URL**: https://hackerone.com/reports/576504
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-10T12:35:35.004Z
- **Disclosed**: 2019-05-21T15:15:41.490Z

## Reporter
- **Username**: paulos__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
Hi,

This is a fun bug I came across while doing a pentest for a client, after going through Revive Advserver's code for a few hours, I found this authentication bypass. This vulnerability seem to affect all versions, including the latest one, I was sent by one of your developers to report it here.

It goes like this:

In */lib/OA/Dal/PasswordRecovery.php*:

```php
50: function generateRecoveryId($userId)
{
$doPwdRecovery = OA_Dal::factoryDO('password_recovery');

    // Make sure that recoveryId is unique in password_recovery table
    do {
        $recoveryId = strtoupper(md5(uniqid('', true)));
        $recoveryId = substr(chunk_split($recoveryId, 8, '-'), -23, 22);
        $doPwdRecovery->recovery_id = $recoveryId;
        ....
 .....
....
```

That function is used to generate the password reset token used to create new password for admins. The token generated for changing password is insecure because it soley just relies on uniqid() which, according to PHP manual states:

*"This function does not create random nor unpredictable string. This function must not be used for security purposes. Use cryptographically secure random function/generator and cryptographically secure hash functions to create unpredictable secure ID."*

The reason being that the function does not generate cryptographically secure tokens, in fact without being passed any additional parameters the return value is little different from *microtime()*. If you need to generate cryptographically secure tokens use *openssl_random_pseudo_bytes()*

*uniqid()* is worse than the manual makes it out to be. An example return value is `58fc30c53db63` . Already, this is only <7 bytes of entropy. But it becomes worse, because without the more_entropy flag set, PHP only uses the current time to generate the return value, PHP code says:

```C
sec = (int) tv.tv_sec;
usec = (int) (tv.tv_usec % 0x100000);
if (more_entropy) {
uniqid = strpprintf(0, "%s%08x%05x%.8F", prefix, sec, usec, php_combined_lcg() * 10);
} else {
uniqid = strpprintf(0, "%s%08x%05x", prefix, sec, usec);
}
```

The first four bytes are the current UNIX timestamp, and the last 20 bits are derived from the current time in microseconds.

This gives a bit less than 2²⁰, or one million, possible results per given second. If you are able to predict when a new session key is generated for a user, you can guess their key with a decent number of requests, depending on how accurate your guess is. On a popular forum, you may not even need to target a specific user, as the number of users logging in at one time may be large enough.

And lucky for us, we can easily predict what Revive Adserver uses:

Ideally an attacker will look up the host IP of their target, locate the server's geoip and set their timezone similar to the server's timezone to make a more accurate prediction.

### Making it more practical

When looking more closely I noticed, most servers that host Revive respond with the following headers:
```
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 09 May 2019 21:26:20 GMT
Content-Type: application/x-javascript
Connection: close
Vary: Accept-Encoding
X-Cacheable: NO:Not Cacheable
Age: 0
X-Cache: MISS
X-Frame-Options: SAMEORIGIN
Content-Length: ...
```

Do you see it? It says *Date: Thu, 09 May 2019 21:26:20 GMT* -- so we can easily know what timezone the server syncs and uses (in this case GMT+0 as timezone) , all an attacker have to do is change their timezone to GMT, request a password reset token simultaneously as they they generate uniqid() from their side as well. All an attacker needs is the email address of the account they reset (which can be enumurated in numerous ways, including by abusing *admin/password-recovery.php* by sending some email addresses until it says *Email Password Reset sent*)


A PoC one would use can look like the following (except weaponized to request a password and generate the tokens simultaneously):

```php
for($i=0;$i<=10000;$i++){

     $recoveryId = strtoupper(md5(uniqid('', true)));
     $recoveryId = substr(chunk_split($recoveryId, 8, '-'), -23, 22);

     print $recoveryId."</br>";

}
```

This generates 10,000 tokens we can try as a token to login as the admin by automating this with process with Burp Intruder. 

You get the idea! :)

### Suggested Fix

Relaying on more cryptographically secure functions like *openssl_random_pseudo_bytes()* is better for such sensitive tokens.

## Impact

Authentication Bypass


Thanks,

## Attachments
No attachments
