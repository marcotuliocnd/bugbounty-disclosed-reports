# Twitter Source Label allow 'mongolian vowel separator' U+180E (app name)

## Report Details
- **Report ID**: 785243
- **URL**: https://hackerone.com/reports/785243
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-29T04:12:55.554Z
- **Disclosed**: 2020-02-21T21:08:05.609Z

## Reporter
- **Username**: lorenznickel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** Twitter app-names (which are shown in the Tweet source label) are supposed to be unique and because of that they must not include invisible unicode characters. However, you can use the mongolian vowel separator in these app-name, which allows to fake a app-name.

**Description:** Every tweet has a ['Tweet source label'] (https://help.twitter.com/en/using-twitter/how-to-tweet#source-labels) which in my understanding is determined by the credentials provided when the POST statuses/update request is made to the twitter-api. This name/source is for example shown below a tweet in the Twitter-Web-App or the Android App or in the twitter-app authorization screen. Every source is registered by one specific twitter-developer-account.
Therefore it should not be possible to use invisible characters in an app-name, because names would stop 'looking' unique.
If you try for example to register a app with a name which includes a 'zero width space' (U+200B) you get the following error: "appName: The application name can't include invisible unicode characters".

Despite this warning it's possible to use the 'mongolian vowel separator' U+180E within a app-name. The name is rendered like the name without this symbol (I tested this at least with the twitter-web app in Chrome on Windows and in Twitter for Android), but it's registered as a completely different application.

Notice that a possible attack scenario, which is a bit more detactable, is using other unicode spaces for example from this list http://jkorpela.fi/chars/spaces.html to replace a regular space. This can the app name look really similar, but it would still be possible to detect, if you would start to mark the app name symbol by symbol with your mouse on the computer, but I think this shouldn't be allowed as well, you should only be allowed to use regular white-spaces in my opinion).

By exploiting this flaw I was also able to create a twitter-application without any (shown) name at all.
{F699270}

## Steps To Reproduce:

  1. Go to https://developer.twitter.com/en/apps (you will need a twitter developer account for that)
  2. Click 'Create an app'
  3. Select an App name which is already used (for example Twitter Web App) and you will get an error, because the name is already taken
  4. Add a [mongolian vowel separator](http://www.unicode-symbol.com/u/180E.html) somewhere to the name (hopefully nobody else will have used this char in exactly the same place, but I never had a collision here. If you have a problem with that I can assist you furthermore in finding a free name, but that really shouldn't be a problem.)
  5. Create the app, authenticate an account with it and send a tweet from this app (If you have problems with this, there are plenty of resources about how to this, but for example this should work, also I didn't use it: https://gist.github.com/KonradIT/0bd7243ebe8d7b3e231603880acab7cf If you need assistance with this, let me know)
  6. Go to the twitter-account you made the tweet with and see that the source of the tweet looks exactly like it was made from the original app without the special character


## Impact:
As twitter considers app-names unique and prints an error if you use certain invisible characters, I think this is not intended behavior at all. You can use this to "spoof" an app-name, which might be not a problem if shown in the context of a tweet, but way more important in the oAuth context when you authorize a twitter-app to tweet (or do other stuff with your account) in your name.
{F699266}
This auth-screen shows 4 app-controlled pieces of information, which are the only way for a user to make sure this is the correct app he really wants to authorize, which are the app icon, the app name, the website url and the description. 3 of these 4 are easily controlled by the attacker, you can even set "twitter.com" as the website url. The only real possibility to detect a phishing attempt here is the app name. As this attack scenario allows you to use every prominent app name (like Twitter Web App) as the app name, the fake auth-screen can't really be distinguished from the real one.
{F699262}

## Supporting Material/References:

F699263
F699264
F699265

## Impact

As twitter considers app-names unique and prints an error if you use certain invisible characters, I think this is not intended behavior at all. You can use this to "spoof" an app-name, which might be not a problem if shown in the context of a tweet, but way more important in the oAuth context when you authorize a twitter-app to tweet (or do other stuff with your account) in your name.
This auth-screen shows 4 app-controlled pieces of information, which are the only way for a user to make sure this is the correct app he really wants to authorize, which are the app icon, the app name, the website url and the description. 3 of these 4 are easily controlled by the attacker, you can even set "twitter.com" as the website url. The only real possibility to detect a phishing attempt here is the app name. As this attack scenario allows you to use every prominent app name (like Twitter Web App) as the app name, the fake auth-screen can't really be distinguished from the real one.

## Attachments
- auth-screen.png
- app-names.png
- name-taken.png
- name-invis.png
- tweet-from-app.png
- empty_name.png
