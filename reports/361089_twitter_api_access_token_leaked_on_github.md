# twitter api access token leaked on github 

## Report Details
- **Report ID**: 361089
- **URL**: https://hackerone.com/reports/361089
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-02T13:37:08.127Z
- **Disclosed**: 2018-06-02T14:06:24.030Z

## Reporter
- **Username**: sonahri501
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
sensitive token were leaked on GitHub page of liberapay . also mixpanel token was leaked
TWITTER_CONSUMER_KEY=QBB9vEhxO4DFiieRF68zTA
 TWITTER_CONSUMER_SECRET=mUymh1hVMiQdMQbduQFYRi79EYYVeOZGrhj27H59H78
+TWITTER_ACCESS_KEY=34175404-G6W8Hh19GWuUhIMEXK0LyZsy7N9aCMcy1bYJ9rI
+TWITTER_ACCESS_SECRET=K6wxV1OCsihZAkEPkWtoLYDiRJnWajBBWn4UgliTRQ
 TWITTER_CALLBACK=http://127.0.0.1:8537/on/twitter/associate
 MIXPANEL_TOKEN=cb9dec68ac0ee57071f0be39f164a417

## Impact

a attacker with your credentials can have severe impact

## Attachments
- libtoke.png
