# [Informational] Possible SQL Injection in inc/ajax-actions-frontend.php

## Report Details
- **Report ID**: 310280
- **URL**: https://hackerone.com/reports/310280
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-29T18:39:41.247Z
- **Disclosed**: 2018-06-17T08:27:19.442Z

## Reporter
- **Username**: damian89
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mapsmarker_com_e_u

## Vulnerability Information
At first, I thought, that my finding is a valid sql injection but I was wrong because of WordPress currently adding magic slashes to COOKIE/POST/GET - this is a very special behaviour which may be remove in the future. There are tons of requests to remove this "old" technique.

Nevertheless I decided to report the issue, because similar code within the audited plugin is escaped - so this is more informational.

Line 49-50:
```
$multi_layer_map_list = isset($_POST['multi_layer_map_list']) ? ($_POST['multi_layer_map_list']) : (isset($_GET['multi_layer_map_list']) ? ($_GET['multi_layer_map_list']) : '');
$multi_layer_map_list_exploded = explode(',', $multi_layer_map_list);
```

As you can see $_GET['multi_layer_map_list']/$_POST['multi_layer_map_list'] are not escaped and exploded by "," in line 50. 

This may result in a succesful sql injection on line 145 - depending on the use case of the shortcode:
```
$mlm_query = "SELECT ". $distance_query ." l.id as lid,l.name as lname,... FROM `" . $table_name_layers . "` as l INNER JOIN `" . $table_name_markers . "` AS m ON m.layer LIKE concat('%\"',l.id,'\"%') ". $search_query ." WHERE l.id='" . $multi_layer_map_list . "'  ORDER BY ...";
```
Fix: esc_sql()

A very similar behaviour can be found in line 149 and following:

```
$first_mlm_id = $multi_layer_map_list_exploded[0];
$other_mlm_ids = array_slice($multi_layer_map_list_exploded,1);
$mlm_query = "(SELECT ... WHERE l.id='" . $first_mlm_id . "'  )";
foreach ($other_mlm_ids as $row) {
    $mlm_query .= " UNION (SELECT ... FROM `" . $table_name_layers . "` ... WHERE l.id='" . $row . "' )";
}
```

Here $row and $first_mlm_id are controlled by a guestuser and are not escaped or validated.

Fix: intval()

The only reason the application is not vulnerable is because of wp-settings.php:

```
// Add magic quotes and set up $_REQUEST ( $_GET + $_POST )
wp_magic_quotes();
```

But the problem is: a lot of themes and/or plugins (which are loaded sometimes before your plugin is loaded) reset this setting like described hiere:

https://stackoverflow.com/questions/8949768/with-magic-quotes-disabled-why-does-php-wordpress-continue-to-auto-escape-my

I believe it may be a better solution to escaped mentioned parts, just to be sure!

Offtopic: the plugin has also a lot of interesting backend functions and calls - are vulnerabilities which can be triggered by admin/mod/author relevent? I'm not talking about xss, more execs and sqlinjections.

## Impact

Under certain circumstances a SQL Injection is possible.

## Attachments
No attachments
