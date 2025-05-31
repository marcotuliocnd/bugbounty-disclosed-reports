# "Bad Protocols Validation" Bypass in "wp_kses_bad_protocol_once" using HTML-encoding without trailing semicolons

## Report Details
- **Report ID**: 339483
- **URL**: https://hackerone.com/reports/339483
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-17T10:31:53.400Z
- **Disclosed**: 2019-11-16T20:06:36.629Z

## Reporter
- **Username**: irsdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Description:
The wp_kses_bad_protocol_once function (https://developer.wordpress.org/reference/functions/wp_kses_bad_protocol_once/) is used to sanitise content from bad protocols and other characters. It detects the protocol (URI scheme) by using the first colon character. It compares the identified protocol with a list of good protocols to ensure it is safe. 

As this function is used to parse HTML-encoded attributes as well, it also uses HTML-encoded variants of the colon character as shown below:
```
   $string2 = preg_split( '/:|&#0*58;|&#x0*3a;/i', $string, 2 );
```

However, the above function is flawed as it does not include HTML-encoded parameters that do not use a semicolon character afterwards. See "Decimal HTML character references without trailing semicolons" and "Hexadecimal HTML character references without trailing semicolons" at https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet for more information about the issue.

The following HTML code shows an example that can bypass the wp_kses_bad_protocol_once validation (see it in action at https://jsfiddle.net/x103n1f7/1/):
```
<a href="javascript&#58alert(document.domain)">JS - Numerical Entities</a>
<a href="javascript&#x3ax=1;alert(document.domain)">JS - Hex Entities</a>
```

The following fix is suggested by adding one line of code at the first line of the wp_kses_bad_protocol_once function to add a semicolon character after the html-encoded variants of the colon character when it is missing. The function will look like this:

```
function wp_kses_bad_protocol_once($string, $allowed_protocols, $count = 1 ) {
///////////////// suggested fix starts here
    $string = preg_replace( '/(&#0*58(?![;0-9])|&#x0*3a(?![;a-f0-9]))/i' , "$1;" , $string );
///////////////// suggested fix ends here
    $string2 = preg_split( '/:|&#0*58;|&#x0*3a;/i', $string, 2 );
    if ( isset($string2[1]) && ! preg_match('%/\?%', $string2[0]) ) {
        $string = trim( $string2[1] );
        $protocol = wp_kses_bad_protocol_once2( $string2[0], $allowed_protocols );
        if ( 'feed:' == $protocol ) {
            if ( $count > 2 )
                return '';
            $string = wp_kses_bad_protocol_once( $string, $allowed_protocols, ++$count );
            if ( empty( $string ) )
                return $string;
        }
        $string = $protocol . $string;
    }
 
    return $string;
}
```

## Impact

This can lead to reflected or stored cross-site scripting attacks for the core or the modules that only rely on this function for the validation.

## Attachments
No attachments
