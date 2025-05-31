# Unauthenticated hidden groups disclosure via Ajax groups search

## Report Details
- **Report ID**: 282176
- **URL**: https://hackerone.com/reports/282176
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-23T17:52:58.780Z
- **Disclosed**: 2017-11-02T19:05:57.285Z

## Reporter
- **Username**: jdgrimes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
*Note: this issue was previously submitted to `security@wordpress.org`, because I did not have the rep to submit it here. That was cleared up with HackerOne, so I am now submitting the issue here, at @aaroncampbell's direction.*

## Summary

It is possible for an unauthenticated user to view the title, description, avatar, time of last activity, and membership count of hidden groups. This is possible via the Ajax groups search feature, due to a failure to properly encode user-supplied values when incorporating them into the query string within the Ajax handler. This allows the user to pass args to the groups query that they aren't intended to be able to use. Specifically, the `show_hidden` query arg may be used to show hidden groups.

## Technical details

Groups in BuddyPress can have one of three different statuses: `public`, `private`, or `hidden`. Public and private groups are publicly queryable, by default, although private groups cannot be joined without an invitation. Hidden groups are not only restricted like private groups, but are also hidden in queries, unless a user has moderator capabilities.

The `BP_Groups_Group::get()` method is used to query for groups. Of particular interest are the `status` and `show_hidden` query args:

```php
<?php
     if ( ! empty( $r['status'] ) ) {
        if ( ! is_array( $r['status'] ) ) {
           $r['status'] = preg_split( '/[\s,]+/', $r['status'] );
        }
        $r['status'] = array_map( 'sanitize_title', $r['status'] );
        $status_in = "'" . implode( "','", $r['status'] ) . "'";
        $where_conditions['status'] = "g.status IN ({$status_in})";
     } elseif ( empty( $r['show_hidden'] ) ) {
        $where_conditions['hidden'] = "g.status != 'hidden'";
     }
```

As you can see, there are no restrictions applied as to who can use these args within the method itself. So any code which allows arbitrary query args to be passed to that method by users without proper permissions is vulnerable to hidden groups disclosure.

The only place where the method is called in that manner is in its wrapper function, `groups_get_groups()`, which in turn is used by `BP_Groups_Template` to get the groups to display in a groups template. It does not accept the `status` query arg, but does allow `show_hidden`.

`BP_Groups_Template::__construct()` does contain this code:

```php
<?php
     if ( bp_current_user_can( 'bp_moderate' ) || ( is_user_logged_in() && $user_id == bp_loggedin_user_id() ) ) {
        $show_hidden = true;
     }
```

However, note that this doesn't prevent `$show_hidden` from being passed in as `true` even if the condition isn't met. Thus, the class is still vulnerable if we can find a way to pass the `show_hidden` arg into it.

The groups template class is utilized only by `bp_has_groups()`, which is used in the groups template files to set up a groups query. The `bp_has_groups()` function accepts an array of query args to be passed to it, although usually that feature either isn't used or it isn't possible to pass arbitrary args in.

However, there are two places of particular interest. The first is in `buddypress/bp-templates/bp-legacy/buddypress/groups/groups-loop.php` on line 26:

```php
<?php if ( bp_has_groups( bp_ajax_querystring( 'groups' ) ) ) : ?>
```

The value returned by the `bp_ajax_querystring()` function is determined via the `'bp_ajax_querystring'` filter. For the Legacy template pack, the `bp_legacy_theme_ajax_querystring()` function is hooked to that filter to supply the value.

`bp_legacy_theme_ajax_querystring()` is located in `buddypress/bp-templates/bp-legacy/buddypress-functions.php`, and most of it is pretty well hardened against this kind of issue, properly sanitizing the user-supplied values. However, on line 692, it does this:

```php
<?php
  // Activity stream filtering on action.
  if ( ! empty( $_BP_COOKIE['bp-' . $object . '-filter'] ) && '-1' != $_BP_COOKIE['bp-' . $object . '-filter'] ) {
     $qs[] = 'type=' . $_BP_COOKIE['bp-' . $object . '-filter'];

     // ...
  }
```

The value of `$_BP_COOKIE` can be set via `$_POST['cookie']` (line 675):

```php
<?php
  // Set up the cookies passed on this AJAX request. Store a local var to avoid conflicts.
  if ( ! empty( $_POST['cookie'] ) ) {
     $_BP_COOKIE = wp_parse_args( str_replace( '; ', '&', urldecode( $_POST['cookie'] ) ) );
  } else {
     $_BP_COOKIE = &$_COOKIE;
  }
```

The `bp-$object-scope` is also vulnerable on line 714:

```php
<?php
  if ( ! empty( $_BP_COOKIE['bp-' . $object . '-scope'] ) ) {

     //...

     // Activity stream scope only on activity directory.
     if ( 'all' != $_BP_COOKIE['bp-' . $object . '-scope'] && ! bp_displayed_user_id() && ! bp_is_single_item() )
        $qs[] = 'scope=' . $_BP_COOKIE['bp-' . $object . '-scope'];
  }
```

The solution is to wrap the values in `urlencode()`, as is done with `$_POST['search_terms']` on line 734.

```php
<?php

     $qs[] = 'type=' . urlencode( $_BP_COOKIE['bp-' . $object . '-filter'] );

     $qs[] = 'scope=' . urlencode( $_BP_COOKIE['bp-' . $object . '-scope'] );
```

The BuddyPress Default theme also suffers from the same problems, in `bp_dtheme_ajax_querystring()` (`buddypress/bp-themes/bp-default/groups/groups-loop.php` uses `bp_has_groups( bp_ajax_querystring( 'groups' ) )` as the Legacy template pack does). In that function, however, `$_POST['search_terms']` is also a vector, since it isn't passed through `urlencode()` (`buddypress/bp-themes/bp-default/_inc/ajax.php` line 137):

```php
<?php
  $object_search_text = bp_get_search_default_text( $object );
  if ( ! empty( $_POST['search_terms'] ) && $object_search_text != $_POST['search_terms'] && 'false' != $_POST['search_terms'] && 'undefined' != $_POST['search_terms'] )
     $qs[] = 'search_terms=' . $_POST['search_terms'];
```

## POC

Send a `POST` request to `/wp-admin/admin-ajax.php` with the following body:

```
action=groups_filter&cookie=bp-groups-filter%253D%252526show_hidden%3D1&object=groups
```

`bp-groups-filter` can be replaced with `bp-groups-scope` to the same effect:

```
action=groups_filter&cookie=bp-groups-scope%253D%252526show_hidden%3D1&object=groups
```

## Attachments
No attachments
