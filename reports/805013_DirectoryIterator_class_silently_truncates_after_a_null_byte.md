# DirectoryIterator class silently truncates after a null byte

## Report Details
- **Report ID**: 805013
- **URL**: https://hackerone.com/reports/805013
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-26T05:07:29.054Z
- **Disclosed**: 2020-11-09T01:47:49.014Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The bug submitted at: https://bugs.php.net/bug.php?id=78863
The security advisory at: https://nvd.nist.gov/vuln/detail/CVE-2019-11045

There's an issue with SPL PHP extension on spl_filesystem_object_construct() function. When creating a new DirectoryIterator() object spl_filesystem_object_construct() function is called and use zend to parse its arguments with the wrong parameter type specifier, this bug leads the zend_parse_parameters() to interprete the parameter as a simple string instead of a filesystem path. An attacker may leverage this by crafting a path name containing NULL bytes which will be badly parsed, allowing the attacker eventually by pass any path-based security validation or listing documents from a unexpected directory.

This flaw has a high Confidentiality impact as the actor may eventually seen the filesystem tree from the attacked machine but a high complexity as the attacker may need to have previous knowledge of filesystem organization or trick the user to run the malicious script.

## Impact

In PHP versions 7.2.x below 7.2.26, 7.3.x below 7.3.13 and 7.4.0, PHP DirectoryIterator class accepts filenames with embedded \0 byte and treats them as terminating at that byte. This could lead to security vulnerabilities, e.g. in applications checking paths that the code is allowed to access.

## Attachments
No attachments
