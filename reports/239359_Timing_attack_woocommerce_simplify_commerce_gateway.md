# Timing attack woocommerce, simplify commerce gateway

## Report Details
- **Report ID**: 239359
- **URL**: https://hackerone.com/reports/239359
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-12T22:09:27.026Z
- **Disclosed**: 2017-09-11T13:48:38.534Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
file `class-wc-gateway-simplify-commerce.php` method `return_handler` e.g. where woocommerce marks the order regarding its payment / transaction.

```
public function return_handler() {
		@ob_clean();
		header( 'HTTP/1.1 200 OK' );

		if ( isset( $_REQUEST['reference'] ) && isset( $_REQUEST['paymentId'] ) && isset( $_REQUEST['signature'] ) ) {
			$signature = strtoupper( md5( $_REQUEST['amount'] . $_REQUEST['reference'] . $_REQUEST['paymentId'] . $_REQUEST['paymentDate'] . $_REQUEST['paymentStatus'] . $this->private_key ) );
			$order_id  = absint( $_REQUEST['reference'] );
			$order     = wc_get_order( $order_id );

			if ( $signature === $_REQUEST['signature'] ) {
				$order_complete = $this->process_order_status( $order, $_REQUEST['paymentId'], $_REQUEST['paymentStatus'], $_REQUEST['paymentDate'] );

				if ( ! $order_complete ) {
					$order->update_status( 'failed', __( 'Payment was declined by Simplify Commerce.', 'woocommerce' ) );
				}

				wp_redirect( $this->get_return_url( $order ) );
				exit();
			}
		}

		wp_redirect( wc_get_page_permalink( 'cart' ) );
		exit();
	}
```
Here is used md5 for signature generation, but string comparison isn't safe towards timing attack. Having in mind the length of the md5 hash string 32 and minimal character set used for it `a-z` and `0-9`, then discovering the right signature will require 32 rounds * X requests per character => no need even for distributed attack regarding successful guessing the generated signature.

In order to protect the customers and merchants I would like to point the usage of [hash_equals](http://php.net/manual/en/function.hash-equals.php) with its [wordpress alternative](https://developer.wordpress.org/reference/functions/hash_equals/) e.g.

`... if (hash_equals($signature, $_REQUEST['signature'])) ...`


## Attachments
No attachments
