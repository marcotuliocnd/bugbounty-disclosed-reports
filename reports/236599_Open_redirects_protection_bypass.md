# Open redirects protection bypass

## Report Details
- **Report ID**: 236599
- **URL**: https://hackerone.com/reports/236599
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-05T14:41:19.780Z
- **Disclosed**: 2017-06-16T18:59:16.869Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expressionengine

## Vulnerability Information
Hello,

When a redirect is to be issue on an ExpressionEngine instance, a request to the following URL is made:
`http://HOST/PATH_TO_EE/index.php?URL=TARGET_URL`
Where `TARGET_URL` is replaced with the actual URL we desire to redirect to. The script `PATH_TO_EE_DIR/system/ee/legacy/libraries/Redirect.php` is the one responsible for making sure that redirects are authorized by checking the value of the Referer header against the hostname where the ExpressionEngine instance is installed. In order to do so, the following code excerpt is performed:

`if ($force_redirect == TRUE OR ( ! isset($_SERVER['HTTP_REFERER']) OR ! stristr($_SERVER['HTTP_REFERER'], $host)))`

Ignoring the very first condition because it is not relevant, and the second because it simply checks if the Referer header is not set in the request, the third condition is the actual problem here. The PHP `stristr` function is used to compare the value of the $host variable, which contains the hostname, to the value of the Referer header. The mentioned function returns TRUE iff the second parameter has been found at least once in the first string parameter, so for example if the actual hostname of the ExpressionEngine instance is http://www.example.com and the Referer header's value is http://evil.com?http://www.example.com, comparing the former and the latter would yield a TRUE return value from the `stristr` function, leaving the check flawed.

I have prepared a live example that shows the issue in action, follow the steps below to reproduce:
1- Visit http://strukt.tk/pocs/eeredirect.html
2- Enter your hostname with the `URL` GET parameter set to whatever external page you desire, the supplied URL should look like `http://HOST/PATH_TO_EE/index.php?URL=https://www.example.com`
3- Click the `Test !!` button and then click the link that will appear below the input box
4- Notice that you have been redirected directly to the supplied value of the `URL` GET parameter rather than being prompted as usual

Regards,

## Attachments
No attachments
