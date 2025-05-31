# Incorrect detection of onion URLs

## Report Details
- **Report ID**: 181210
- **URL**: https://hackerone.com/reports/181210
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-09T23:10:57.601Z
- **Disclosed**: 2016-11-13T00:43:42.723Z

## Reporter
- **Username**: e3amn2l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Several places have incorrect code to detect if URL point to .onion domain (tor hidden server):

The following regexes:
```
1. #^https://([^/:]+)\.onion:(?:([0-9]+))#
2. #^https?://([^/]+)\.onion#
```

which is used in:
https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/src/Engine/Hail.php#L223
https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/src/Engine/Hail.php#L231

will pass for the following URLs which have example.com as domain and are valid for curl in php (was tested via curl_setopt($ch, CURLOPT_URL, $url))
```
1 => https://example.com?.onion:443
1 => https://example.com&.onion:443
2 => http://example.com?.onion
2 -> http://example.com&.onion
```

which is problematic because:
1. The code in: will not force HTTPS if url passed the above regex. (thus incorrect check = HTTPS not forced for not .onion domain)
https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/src/Engine/Hail.php#L228-L229
```
                // Don't force HTTPS
                unset($defaults['curl'][CURLOPT_SSLVERSION]);
```

2. the second regex allow http url (thus incorrect check = HTTP for not .onion domain is vulnerable to MITM)
3. potential of code reuse by people who read the code and assume it's safe.

The following code just search for .onion in $url, for example https://domain.onionweb.com/ will pass the check but isn't .onion website.

in:
https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Engine/Keyggdrasil/Peer.php#L50
https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/src/Engine/Continuum/Channel.php#L154
https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/src/Engine/Continuum/Channel.php#L239
https://github.com/paragonie/airship/blob/90a8317107ecfdf38be57f36e4a1a81e69280f24/src/Cabin/Bridge/Blueprint/ChannelUpdates.php#L117
https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Engine/Keyggdrasil/Peer.php#L82

```
            if (\strpos($url, '.onion') !== false) {
```

fix:
	1. implement and use across the codebase function such as isUrlOnion($url) which return true if url point to onion domain, and use secure implementation, for example:
		consider using something like:
```
		function isUrlOnion($url) {
			$host = parse_url($url, PHP_URL_HOST);
			if($host != null) {
				return substr_compare($url, '.onion', -strlen('.onion')) === 0;
			}
			return false;
		}
```

## Attachments
No attachments
