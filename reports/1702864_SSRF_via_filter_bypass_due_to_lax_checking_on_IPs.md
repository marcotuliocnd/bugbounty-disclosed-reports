# SSRF via filter bypass due to lax checking on IPs

## Report Details
- **Report ID**: 1702864
- **URL**: https://hackerone.com/reports/1702864
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-17T08:10:29.440Z
- **Disclosed**: 2023-02-10T02:03:11.903Z

## Reporter
- **Username**: obitorasu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Hello,

I was reading up on the recent SSRF bug found on NextCloud which is originally a part of this [report](https://hackerone.com/reports/1608039) by @tomorrowisnew_ 

I went through the source code again which was highlighted in the report I mentioned and I noticed that filtering for some of the more advanced SSRF payloads were clearly missing. Alphanumeric payloads came to my mind when thinking about the same so I set up a local test environment with my friend @w1redch4d

We primarily focused on the code around the IP checking namely `ThowIfLocalIp`:
```php
	public function ThrowIfLocalIp(string $ip) : void {
		$localRanges = [
			'100.64.0.0/10', // See RFC 6598
			'192.0.0.0/24', // See RFC 6890
		];
		if (
			(bool)filter_var($ip, FILTER_VALIDATE_IP) &&
			(
				!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
				IpUtils::checkIp($ip, $localRanges)
			)) {
			$this->logger->warning("Host $ip was not connected to because it violates local access rules");
			throw new LocalServerException('Host violates local access rules');
		}

		// Also check for IPv6 IPv4 nesting, because that's not covered by filter_var
		if ((bool)filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6) && substr_count($ip, '.') > 0) {
			$delimiter = strrpos($ip, ':'); // Get last colon
			$ipv4Address = substr($ip, $delimiter + 1);

			if (
				!filter_var($ipv4Address, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
				IpUtils::checkIp($ip, $localRanges)) {
				$this->logger->warning("Host $ip was not connected to because it violates local access rules");
				throw new LocalServerException('Host violates local access rules');
			}
		}
	}
```
As seen above, the code is more than capable of rooting out most of the SSRF payloads including IPv4 and IPv6 as well as the recently pointed out payload involving the Alibaba metadata IP `100.100.100.200`. But as stated above, the filtration technique fails when met with some of the more advanced SSRF payloads like the alphanumeric ones. In our test environment, we edited the code and set up a dummy website to test different payloads. The workflow was simple, if the payload was an invalid attempt at an SSRF, the server will throw an exception but if all the filtrations were bypassed successfully, the server would echo Pass.

## Supporting Material/References:
Our dummy code is as follows:
```php
<?php
      require 'vendor/autoload.php';
      use Symfony\Component\HttpFoundation\IpUtils;

      function ThrowIfLocalIp(string $ip) : void {
        $localRanges = [
            '100.64.0.0/10', // See RFC 6598
            '192.0.0.0/24', // See RFC 6890
        ];
        if (
            (bool)filter_var($ip, FILTER_VALIDATE_IP) &&
            (
                !filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
                IpUtils::checkIp($ip, $localRanges)
            )) {
            throw new Exception('Host violates local access rules');
        }

        // Also check for IPv6 IPv4 nesting, because that's not covered by filter_var
        if ((bool)filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6) && substr_count($ip, '.') > 0) {
            $delimiter = strrpos($ip, ':'); // Get last colon
            $ipv4Address = substr($ip, $delimiter + 1);

            if (
                !filter_var($ipv4Address, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
                IpUtils::checkIp($ip, $localRanges)) {
                throw new Exception('Host violates local access rules');
            }
        }
        echo "Pass";
    }
    ThrowIfLocalIp($_GET["ip"])
?>
```

Here are some of the screenshots:

**Server catches exception for Alibaba metadata IP and doesn't echo Pass**
{F1934403}
{F1934404}

**Server catches normal payload for AWS Magic IP and doesn't echo Pass**
{F1934407}
{F1934406}

**Server passes the Alphanumeric payload for AWS Magic IP and echoes Pass**
{F1934411}
{F1934412}

**Server passes greenlighted IPs proof with `8.8.8.8` and `8.8.4.4` and echoes Pass**
{F1934464}
{F1934456}

## Impact

Attackers can leverage enclosed alphanumeric payloads to bypass IP filters and gain SSRF. An example can be using `⑯⑨。②⑤④。⑯⑨｡②⑤④` which would allow an attacker to read crucial metadata if the server is hosted on the AWS platform. The above payload will resolve to the magic IP of AWS namely `169.254.169.254` but bypasses all the filtering present in the code itself.

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
