# Illegal write access through Locale methods

## Report Details
- **Report ID**: 175315
- **URL**: https://hackerone.com/reports/175315
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-12T06:56:06.699Z
- **Disclosed**: 2019-10-13T18:15:35.519Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=73248

Summary
--
The functions *locale_get_all_variants* and *locale_get_primary_language* do not validate the length of the locale name supplied, this causes an integer overflow inside ulocimp_getLanguage, since it uses int32_t type as index, and strings with length bigger than 0xffffffff cause an illegal write access.

This bug can be mitigated from PHP, by checking the input length similar to bug67397-patch 
https://bugs.php.net/patch-display.php?bug_id=67397&patch=bug67397-patch&revision=latest 

Source code:
https://github.com/php/php-src/blob/master/ext/intl/locale/locale_methods.c#L381

```
static void get_icu_value_src_php( char* tag_name, INTERNAL_FUNCTION_PARAMETERS)
{

	const char* loc_name        	= NULL;
	size_t         loc_name_len    	= 0;

	zend_string*   tag_value		= NULL;
	char*       empty_result	= "";

	int         result    		= 0;
	char*       msg        		= NULL;

	UErrorCode  status          	= U_ZERO_ERROR;

	intl_error_reset( NULL );

	if(zend_parse_parameters( ZEND_NUM_ARGS(), "s",
	&loc_name ,&loc_name_len ) == FAILURE) {
		spprintf(&msg , 0, "locale_get_%s : unable to parse input params", tag_name );
		intl_error_set( NULL, U_ILLEGAL_ARGUMENT_ERROR,  msg , 1 );
		efree(msg);

		RETURN_FALSE;
    }

	if(loc_name_len == 0) {
		loc_name = intl_locale_get_default();
	}
 
        // Here check that loc_name_len is not greater than 0xffffffff

	/* Call ICU get */
	tag_value = get_icu_value_internal( loc_name , tag_name , &result ,0);
...
```


https://github.com/php/php-src/blob/master/ext/intl/locale/locale_methods.c#L1143

```
PHP_FUNCTION(locale_get_all_variants)
{
	const char*  	loc_name        = NULL;
	size_t    		loc_name_len    = 0;

	int	result		= 0;
	char*	token		= NULL;
	zend_string*	variant		= NULL;
	char*	saved_ptr	= NULL;

	intl_error_reset( NULL );

	if(zend_parse_parameters( ZEND_NUM_ARGS(), "s",
	&loc_name, &loc_name_len ) == FAILURE)
	{
		intl_error_set( NULL, U_ILLEGAL_ARGUMENT_ERROR,
	     "locale_parse: unable to parse input params", 0 );

		RETURN_FALSE;
	}

	if(loc_name_len == 0) {
		loc_name = intl_locale_get_default();
	}

        // Here check that loc_name_len is not greater than 0xffffffff

	array_init( return_value );

	/* If the locale is grandfathered, stop, no variants */
	if( findOffset( LOC_GRANDFATHERED , loc_name ) >=  0 ){
		/* ("Grandfathered Tag. No variants."); */
	}
	else {
	/* Call ICU variant */
		variant = get_icu_value_internal( loc_name , LOC_VARIANT_TAG , &result ,0);
```



GDB output
```
LD_LIBRARY_PATH=/home/operac/icu58/lib USE_ZEND_ALLOC=0 ASAN_OPTIONS=detect_leaks=0 gdb -q --args /home/operac/build4/bin/php -dextension=/home/operac/build4/lib/php/20151012-debug/intl.so -n poc.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /home/operac/build4/bin/php...done.
gdb-peda$ r
Starting program: /home/operac/build4/bin/php -dextension=/home/operac/build4/lib/php/20151012-debug/intl.so -n poc.php
...
Stopped reason: SIGSEGV
0x00007fffee3e8ed5 in ulocimp_getLanguage (localeID=0x7ffe6c3f8800 '#' <repeats 200 times>..., language=0x616000026798 '#' <repeats 200 times>..., languageCapacity=0x200, pEnd=0x0) at uloc.cpp:1244
1244                language[i]=(char)uprv_tolower(*localeID);
gdb-peda$ p/d i
$1 = -2147483648    // negative index
```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=d3eb58332af433982f1e2ae9095fb087974a95f2
```

Fixed for PHP 5.6.27, PHP 7.0.12
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.12


## Attachments
No attachments
