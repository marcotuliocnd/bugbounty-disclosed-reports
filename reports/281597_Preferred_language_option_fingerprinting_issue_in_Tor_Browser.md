# Preferred language option fingerprinting issue in Tor Browser

## Report Details
- **Report ID**: 281597
- **URL**: https://hackerone.com/reports/281597
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-22T02:53:01.305Z
- **Disclosed**: 2017-10-24T06:57:45.395Z

## Reporter
- **Username**: newfunction
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
I'm not so sure if this is an in-scope issue or by-design. But based on my understanding of [1], I feel that Tor doesn't want to make user configuration details of Tor Browser detectable by websites. But in about:preferences#content, there's a "Languages" section that allows users to "choose your preferred language for displaying pages". When users add a language here, there's no warning to tell them that this info will be sent to the websites. The language list will be available to websites in the "Accept-Language" HTTP request header, and in JavaScript API "navigator.languages".

To fix this issue, I think there're three options: 1) remove this option from the settings; 2) let users configure a list of domains for which the language list is sent; other sites get the default value; 3) add a warning in the setting page: "the info of your added languages is sent to all sites, which may be used to fingerprint you" or something like this.

[1] https://www.torproject.org/projects/torbrowser/design/#fingerprinting-linkability, Sources of Fingerprinting Issues

## Attachments
- Accept-Language_discloses_language_list.png
- language_setting.png
- navigator.languages_return_language_list.png
