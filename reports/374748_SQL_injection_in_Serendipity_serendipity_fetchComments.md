# SQL injection in Serendipity (serendipity_fetchComments)

## Report Details
- **Report ID**: 374748
- **URL**: https://hackerone.com/reports/374748
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-30T15:34:42.642Z
- **Disclosed**: 2018-11-09T14:44:05.375Z

## Reporter
- **Username**: bb9866f3f743d6bf69b6836
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hannob

## Vulnerability Information
##Summary

An authenticated administrator can alter *Entries to display on frontpage* and *Entries to display in Feeds* in a way to perform a SQL injection and extract database records or access files on the underlying system.

##Description

The function `serendipity_fetchComments` (implemented in `functions_comments.inc.php`) allows to obtain an array of comments related to a specific entry id. It accepts six parameters that will impact the query:
- `$id`: casted as integer and then used in the query;
- `$limit`: used unescaped in the query;
- `$order `: used unescaped in the query;
- `$showAll`: adds a fixed condition to the query;
- `$type`: used unescaped in the query;
- `$where`: used unescaped in the query.

Thus, any use of `serendipity_fetchComments` where either `$limit`, `$order`, `$type` or `$where` are user-controlled will result in a SQL injection. Two vulnerable calls were discovered.

The first one can be found in `rss.php`. The value of `$serendipity['RSSfetchLimit']` comes from website's configuration (*Entries to display in Feeds*) and is used as second argument of `serendipity_fetchComments`:

```php
<?php
// [...]
switch ($_GET['type']) {
    case 'comments_and_trackbacks':
    case 'trackbacks':
    case 'comments':
        $entries     = serendipity_fetchComments(isset($_GET['cid']) ? $_GET['cid'] : null, $serendipity['RSSfetchLimit'], 'co.id desc', false, $_GET['type']);
```

The same way, `serendipity_printCommentsByAuthor` (implemented in `functions_comments.inc.php`) uses `$serendipity['fetchLimit']` as second argument. The value of `$serendipity['fetchLimit']` also comes from website's configuration (*Entries to display on frontpage*):

```php
<?php
// [...]
    $sql_limit = $serendipity['fetchLimit'] * ($serendipity['GET']['page']-1) . ',' . $serendipity['fetchLimit'];
    $c = serendipity_fetchComments(null, $sql_limit, 'co.entry_id DESC, co.id ASC', false, $type, $sql_where);
```
## Steps To Reproduce

  1. Access https://blog.fuzzing-project.org/serendipity_admin.php?serendipity[adminModule]=configuration as authenticated administrator.
  1. Alter either *Entries to display on frontpage* or *Entries to display in Feeds* (under *Appearance and Options*) by adding any non-numeric character in one of these fields.
  1. Access https://blog.fuzzing-project.org/rss.php?type=comment if you edited *Entries to display in Feeds*, or the homepage is you edited *Entries to display on frontpage*. The character 
broke the correctness of the query and an error message will be displayed.

I don't have any test environment at the moment but let me know if you need a real payload to show it's possible to extract arbitrary database records.

## Impact

An authenticated administrator can extract database records, including password hashes of other users of the instance. Depending on database user privileges, it could also allow to access other bases or files on the underlying server.

## Attachments
No attachments
