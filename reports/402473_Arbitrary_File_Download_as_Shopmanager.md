# Arbitrary File Download as Shopmanager

## Report Details
- **Report ID**: 402473
- **URL**: https://hackerone.com/reports/402473
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-29T15:43:55.540Z
- **Disclosed**: 2019-12-19T14:23:57.394Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Due to a flaw in the way WooCommerce handles downloadable products, a shop manager can download arbitrary files on the server.

The video shows the exploit and how simple it is:
https://www.youtube.com/watch?v=bkrHpqht5SM

The function responsible for validating the download file input is the following:
(/woocommerce/includes/abstracts/abstract-wc-product.php)
```
	public function set_downloads( $downloads_array ) {
		$downloads = array();
		$errors    = array();

		foreach ( $downloads_array as $download ) {
			if ( is_a( $download, 'WC_Product_Download' ) ) {
				$download_object = $download;
			} else {
				$download_object = new WC_Product_Download();

				// If we don't have a previous hash, generate UUID for download.
				if ( empty( $download['download_id'] ) ) {
					$download['download_id'] = wp_generate_uuid4();
				}

				$download_object->set_id( $download['download_id'] );
				$download_object->set_name( $download['name'] );
				$download_object->set_file( $download['file'] );
			}

			// Validate the file extension.
			if ( ! $download_object->is_allowed_filetype() ) {
				if ( $this->get_object_read() ) {
					/* translators: %1$s: Downloadable file */
					$errors[] = sprintf( __( 'The downloadable file %1$s cannot be used as it does not have an allowed file type. Allowed types include: %2$s', 'woocommerce' ), '<code>' . basename( $download_object->get_file() ) . '</code>', '<code>' . implode( ', ', array_keys( $download_object->get_allowed_mime_types() ) ) . '</code>' );
				}
				continue;
			}

			// Validate the file exists.
			if ( ! $download_object->file_exists() ) {
				if ( $this->get_object_read() ) {
					/* translators: %s: Downloadable file */
					$errors[] = sprintf( __( 'The downloadable file %s cannot be used as it does not exist on the server.', 'woocommerce' ), '<code>' . $download_object->get_file() . '</code>' );
				}
				continue;
			}

			$downloads[ $download_object->get_id() ] = $download_object;
		}

		if ( $errors ) {
			$this->error( 'product_invalid_download', $errors[0] );
		}

		$this->set_prop( 'downloads', $downloads );
	}
```
When I took a look at the function I naturally wanted to see if there was a way to bypass is_allowed_filetype().

The function does the following:

```
	public function is_allowed_filetype() {
		if ( 'relative' !== $this->get_type_of_file_path() ) {
			return true;
		}
		return ! $this->get_file_extension() || in_array( $this->get_file_type(), $this->get_allowed_mime_types(), true );
	}
```
It will see what type of file path it is (it could be a URL, it could be an absolute path etc.) and interestingly enough it will only validate the file extension if it is a relative path. So of course I wanted to see what would happen if we would enter an absolute path, since then I could bypass the extension check entirely.

```
	public function get_type_of_file_path( $file_path = '' ) {
		$file_path = $file_path ? $file_path : $this->get_file();
		if ( 0 === strpos( $file_path, 'http' ) || 0 === strpos( $file_path, '//' ) ) {
			return 'absolute';
		} elseif ( '[' === substr( $file_path, 0, 1 ) && ']' === substr( $file_path, -1 ) ) {
			return 'shortcode';
		} else {
			return 'relative';
		}
	}
```

And I was right. Funny enough, input is only an absolute path if it starts with two slashes. So all I did was  to set the download file to //home/simon/html/wordpress/wp-config.php and then just downloaded it.

As a patch recommendation: Also check the file types if it is an absolute path.

Best regards,
Simon

## Impact

When an attacker can download the wp-config.php file, a privilege escalation is easily possible. He could either log into the database if the DB host is not localhost or if the WordPress installation is used with a shared hosting provider, he can simply get some hosting space on the same server and then access the database, which leads to a complete compromise of the installation.

## Attachments
No attachments
