# Stored XSS in Jetpack's Simple Payment Module by Contributors / Authors

## Report Details
- **Report ID**: 402753
- **URL**: https://hackerone.com/reports/402753
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-30T08:50:43.915Z
- **Disclosed**: 2019-12-19T14:24:27.025Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Jetpack's implementation of the Simple Payment Module is as follows:

A custom post type is registered for each product. When an admin creates a product, a post is internally created and information about the product, such as the price is then stored as post meta information. After the post has been created, any user who can create posts can use the [simple-payment] shortcode with the id of the post representing the product. So for example, if the product was internally saved as a post with ID 17, the shortcode [simple-payment id="17"] would then render the product.

With this information, I began looking for weaknesses and noticed something interesting here:

```
		/*
		 * PRODUCT data structure. Holds:
		 * title - title
		 * content - description
		 * thumbnail - image
		 * metadata:
		 * spay_price - price
		 * spay_formatted_price
		 * spay_currency - currency code
		 * spay_cta - text with "Buy" or other CTA
		 * spay_email - paypal email
		 * spay_multiple - allow for multiple items
		 * spay_status - status. { enabled | disabled }
		 */
		$product_capabilities = array(
			'edit_post'             => 'edit_posts',
			'read_post'             => 'read_private_posts',
			'delete_post'           => 'delete_posts',
			'edit_posts'            => 'edit_posts',
			'edit_others_posts'     => 'edit_others_posts',
			'publish_posts'         => 'publish_posts',
			'read_private_posts'    => 'read_private_posts',
		);
		$product_args = array(
			'label'                 => esc_html__( 'Product', 'jetpack' ),
			'description'           => esc_html__( 'Simple Payments products', 'jetpack' ),
			'supports'              => array( 'title', 'editor','thumbnail', 'custom-fields', 'author' ),
			'hierarchical'          => false,
			'public'                => false,
			'show_ui'               => false,
			'show_in_menu'          => false,
			'show_in_admin_bar'     => false,
			'show_in_nav_menus'     => false,
			'can_export'            => true,
			'has_archive'           => false,
			'exclude_from_search'   => true,
			'publicly_queryable'    => false,
			'rewrite'               => false,
			'capabilities'          => $product_capabilities,
			'show_in_rest'          => true,
		);
		register_post_type( self::$post_type_product, $product_args );
```

As can be seen, the capabilities of a product are explicitly set to 'edit_post'. This means contributors and authors have access to these products and can create them in the database. Since none of the post_meta keys are protected, it is also possible for contributors and authors to fill them with arbitrary values. (Either when creating the post or via the wp_ajax_add_meta handler). This meant if during the process of rendering the shortcode some post meta values would be echo'd into the markup unsanitized, I could achieve stored XSS.

So, ofcourse my next step was to look at the function that renders the shortcode:

```
	function output_shortcode( $data ) {
		$items = '';
		$css_prefix = self::$css_classname_prefix;

		if ( $data['multiple'] ) {
			$items="<div class='${css_prefix}-items'>
				<input class='${css_prefix}-items-number' type='number' value='1' min='1' id='{$data['dom_id']}_number' />
			</div>";
		}
		$image = "";
		if( has_post_thumbnail( $data['id'] ) ) {
			$image = "<div class='${css_prefix}-product-image'><div class='${css_prefix}-image'>" . get_the_post_thumbnail( $data['id'], 'full' ) . "</div></div>";
		}
		return "
<div class='{$data['class']} ${css_prefix}-wrapper'>
	<div class='${css_prefix}-product'>
		{$image}
		<div class='${css_prefix}-details'>
			<div class='${css_prefix}-title'><p>{$data['title']}</p></div>
			<div class='${css_prefix}-description'><p>{$data['description']}</p></div>
			<div class='${css_prefix}-price'><p>{$data['price']}</p></div>
			<div class='${css_prefix}-purchase-message' id='{$data['dom_id']}-message-container'></div>
			<div class='${css_prefix}-purchase-box'>
				{$items}
				<div class='${css_prefix}-button' id='{$data['dom_id']}_button'></div>
			</div>
		</div>
	</div>
</div>
		";
	}
```

This line here was particularly interesting to me, as the price is outputted unsanitized.

```
			<div class='${css_prefix}-price'><p>{$data['price']}</p></div>
```

Now all that was left to figure out was to see how the price was received from the database and if it would be sanitized. The function in which it is received is the parse_shortcode method (I have removed the code that doesn't matter to this explanation):

```
	function parse_shortcode( $attrs, $content = false ) {
		if ( empty( $attrs['id'] ) ) {
			return;
		}
		$product = get_post( $attrs['id'] );
...
		$data['price'] = $this->format_price(
			get_post_meta( $product->ID, 'spay_formatted_price', true ),
			get_post_meta( $product->ID, 'spay_price', true ),
			get_post_meta( $product->ID, 'spay_currency', true ),
			$data
		);
...
		return $this->output_shortcode( $data );
	}
```

As can be seen, the price is simply retrieved from the database as post meta values and then passed to format_price, however this function does not perform any sanitization whatsoever:

```
	function format_price( $formatted_price, $price, $currency, $all_data ) {
		if ( $formatted_price ) {
			return $formatted_price;
		}
		return "$price $currency";
	}
```

This means that we indeed have a Stored XSS vulnerability. 

Here is a PoC video of me getting a Stored XSS payload as a contributor
https://www.youtube.com/watch?v=gMHOse_8ywI

## Impact

Since Simple Payments is only available to premium and professional users, this fortunaly lowers the impact. Since Stored XSS easily leads to a privilege escalation in WordPress, this is still of high impact.

## Attachments
No attachments
