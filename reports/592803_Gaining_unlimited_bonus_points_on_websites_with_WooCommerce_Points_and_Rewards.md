# Gaining unlimited bonus points on websites with WooCommerce Points and Rewards

## Report Details
- **Report ID**: 592803
- **URL**: https://hackerone.com/reports/592803
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-30T19:01:09.141Z
- **Disclosed**: 2019-07-05T23:43:54.225Z

## Reporter
- **Username**: kolyasapphire
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
In WooCommerce Points and Rewards plugin there is an assumption that Processing order status is only for paid orders.

However, this assumption is wrong for payment gateway Cash On Delivery, which immediately changes order status to Processing on all new orders. Plugin then increases bonus points for the order total which are immediately available to spend.

The problematic code is in class-wc-points-rewards-order.php in function maybe_update_points which gets triggered by following actions:
```
woocommerce_order_status_processing
woocommerce_order_status_completed
woocommerce_order_status_on-hold 
```

The code itself is on lines 50-58:
```
public function maybe_update_points( $order_id ) {
		$order = wc_get_order( $order_id );

		$this->maybe_deduct_redeemed_points( $order_id );

		if ( 'on-hold' !== $order->get_status() ) {
			$this->add_points_earned( $order_id );
		}
	}
```

The solution is to either increase points only on completed orders or to add an extra check if status is processing and payment method is not cash on delivery.

Example solution, change code to:
```
public function maybe_update_points( $order_id ) {
		$order = wc_get_order( $order_id );

		$this->maybe_deduct_redeemed_points( $order_id );

		if ( $order->get_status() !== 'on-hold' && $order->get_status() !== 'processing'  ) {
			$this->add_points_earned( $order_id );
		}
	}
```

## Impact

An attacker can gain an unlimited amount of bonus points and spend them on next orders. The only requirements are WooCommerce Points and Rewards enabled on the website and payment gateway Cash On Delivery enabled, both are very common. Cash on delivery is a core WooCommerce payment gateway. Points and Rewards is easily identified by bonus messages on product pages and on checkout. This bug works on the latest plugin version. The only limit on spending bonus points is defined in plugin settings (eg maximum 50% point redemption).

## Attachments
No attachments
