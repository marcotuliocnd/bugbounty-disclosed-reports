# Access to Unclassified / FOUO Advanced Motion Platform of █████████.mil

## Report Details
- **Report ID**: 1003455
- **URL**: https://hackerone.com/reports/1003455
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-09T13:06:22.536Z
- **Disclosed**: 2020-11-02T21:43:09.710Z

## Reporter
- **Username**: kaulse
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hey,
I have recently found a website in the namespace of the Amazon Web Services cloud for the US government which exposes a classification header of Unclassified / FOUO. Hence, I thought it might be a good idea to report this vulnerability to you.
Furthermore, the source code tells us that the website seems to be part of ████████.mil even though the SSL name is "███████":
```html

	<script type="text/javascript">
		// use one of these ██████████ URLs depending on the install environment
		var ███████_URL = "https://████████.██████████.mil/";
//		var █████_URL = "https://████.█████████.smil.mil/";
	</script>
```

The proof of concept is as simple as opening the link `https://███/`.
For reference, I have found the site via Shodan: https://www.shodan.io/host/█████████

██████████
███
█████

## Impact

This system is classified as Unclassified / FOUO. Hence, an attacker can access a system which is only for official use only.

## Attachments
No attachments
