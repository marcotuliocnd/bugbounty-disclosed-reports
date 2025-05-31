# Authenticated Code Execution through Phar deserialization in CSV Importer as Shop manager in WooCommerce

## Report Details
- **Report ID**: 403083
- **URL**: https://hackerone.com/reports/403083
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-30T16:37:09.891Z
- **Disclosed**: 2019-12-19T14:26:02.746Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
This vulnerability is based on the following exploitation technique:

https://blog.ripstech.com/2018/new-php-exploitation-technique/

It is easier to explain this vulnerability by having watched the PoC first:
https://www.youtube.com/watch?v=mr3bAOIUwd4

Here is what's happening:

1. Since a valid phar file needs o be uploaded to the server (the extension doesn't matter) I upload the poc.jpg via the media uploader
2. I begin the Import process with a valid CSV file
3.  The importer asks if I am sure that I want to run the import on these files
4. I confirm and modify the  POST parameter to my phar:// wrapper and deserialize the file
5. The PHP code executes

The source of the vulnerability within the source code lies in the /woocommerce/includes/import/class-wc-product-csv-importer.php:

```
	public function __construct( $file, $params = array() ) {
		$default_args = array(
			'start_pos'        => 0, // File pointer start.
			'end_pos'          => -1, // File pointer end.
			'lines'            => -1, // Max lines to read.
			'mapping'          => array(), // Column mapping. csv_heading => schema_heading.
			'parse'            => false, // Whether to sanitize and format data.
			'update_existing'  => false, // Whether to update existing items.
			'delimiter'        => ',', // CSV delimiter.
			'prevent_timeouts' => true, // Check memory and time usage and abort if reaching limit.
			'enclosure'        => '"', // The character used to wrap text in the CSV.
			'escape'           => "\0", // PHP uses '\' as the default escape character. This is not RFC-4180 compliant. This disables the escape character.
		);

		$this->params = wp_parse_args( $params, $default_args );
		$this->file   = $file;

		if ( isset( $this->params['mapping']['from'], $this->params['mapping']['to'] ) ) {
			$this->params['mapping'] = array_combine( $this->params['mapping']['from'], $this->params['mapping']['to'] );
		}

		$this->read_file();
	}

	/**
	 * Read file.
	 */
	protected function read_file() {
		$handle = fopen( $this->file, 'r' ); // @codingStandardsIgnoreLine.

		if ( false !== $handle ) {
			$this->raw_keys = version_compare( PHP_VERSION, '5.3', '>=' ) ? fgetcsv( $handle, 0, $this->params['delimiter'], $this->params['enclosure'], $this->params['escape'] ) : fgetcsv( $handle, 0, $this->params['delimiter'], $this->params['enclosure'] ); // @codingStandardsIgnoreLine

...
```

As can be seen, the constructor calls read_file, which in turn calls fopen without any checks, which leads to the deserialization of the Phar object.

I recommend to check the file parameter and see if it actually is a CSV file before calling fopen on it.

I have attached the poc.jpg that worked for my PHP version.

## Impact

I only displayed the contents of the /etc/passwd file in the PoC video. However, since I can execute arbitrary PHP code, a complete compromise of the WordPress installation is possible. If an attacker can gain access to a Shop manager account, he can easily and without restrictions take over the server.

## Attachments
- poc.jpg
