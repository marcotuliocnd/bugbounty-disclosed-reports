# Unauthenticated RCE in Vaultpress

## Report Details
- **Report ID**: 236552
- **URL**: https://hackerone.com/reports/236552
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-06-05T10:28:51.711Z
- **Disclosed**: 2017-09-15T12:51:38.159Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hitting wordpress instalattion with vaultpress on it with get parameter vaultpress=true attacker is one method away from RCE and that method is **validate_api_signature**.

In this method we have the following constraints:
1. Firewall
2. Usage (recomended) of openssl to validate API call

In case of disabled firewall or its bypass ( easy on many configurations, specially the ones behind proxy/balancer servers ) then in case of usage of openssl to verify the signature we have easy bypass because unsafe usage of **openssl_verify** PHP function.

```
if ( $this->can_use_openssl() ) {
			
			$sslsig = '';
			if ( isset( $post['sslsig'] ) ) {
				$sslsig = $post['sslsig'];
				unset( $post['sslsig'] );
			}
			if ( openssl_verify( serialize( array( 'uri' => $uri, 'post' => $post ) ), base64_decode( $sslsig ), $this->get_option( 'public_key' ) ) ) {
				return true;
			} else {
				$__vp_validate_error = array( 'error' => 'invalid_signed_data' );
				return false;
			}
		}
```
This function **openssl_verify** have 3 possible values as result value: 
- int(1) success 
- int(0) failure to verify
- int(-1) error 

but we all know that 
```
if (-1) {echo "Hi RCE";}
```
will print **Hi RCE**

Proposed fix:
```
if ( openssl_verify( serialize( array( 'uri' => $uri, 'post' => $post ) ), base64_decode( $sslsig ), $this->get_option( 'public_key' ) ) ===1 ) {
				return true;
			} else {
				$__vp_validate_error = array( 'error' => 'invalid_signed_data' );
				return false;
			}
```
In order to get the idea how to cause **openssl_verify** to return -1all you need is to provide valid signature towards public key from different type. Check the uploaded files and execute them in the CMD in the following order:
```
php genkey1.php
php genkey2.php
php PoC.php
```


## Attachments
- genkey2.php
- genkey1.php
- PoC.php
