# Leaking sensitive information on Github lead full access to all Grab Slack channels 

## Report Details
- **Report ID**: 397527
- **URL**: https://hackerone.com/reports/397527
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-21T05:01:49.087Z
- **Disclosed**: 2018-09-11T08:00:13.996Z

## Reporter
- **Username**: xsam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
#Summary:

 Accidental leakage of secret keys in such code repositories is a real problem, after my report #387117, I decided to dig deeper than the previous report and looking to some random profiles in Github, and doing some dirty work I was able to access to the developer’s company’s internal chats and files on Slack. And not only that, there’s no easy way to see if someone is eavesdropping on the communication. In the worst case scenario, these chats can leak production database credentials, source code, files with passwords and highly sensitive information.

#Description:

__████__ is QA Automation Engineer at Grab according to his [LinkedIn profile](https://www.linkedin.com/in/██████████/), after doing some manual search in Github. I found his Github profile which contains weird repo

https://github.com/████/

{F335908}

I was about to close that tab since there is no useful file but wait second, did you notice __30 releases__?

Multiple versions for multiple OS systems, I decided to download [the zip file](https://github.com/████████/releases/download/v1.0.34/vnot-automation-support-1.0.34-mac.zip), after the unzipping I started __███__ which is an Electron application.

{F335910}

I thought it was a dead-end but I noticed the bar so I clicked `Environment` then `Toggle Developer tools` in order to know the origin of that app go to `Source` as attached in the screenshot below 

{F335916}

Know it is the time for some thinking outside of the box and be creative. As I don't have much experience with Electron apps so after some googling I found that it is possible to reverse-engineer an existing Electron app by following [those steps](https://medium.com/how-to-electron/how-to-get-source-code-of-any-electron-application-cbb5c7726c37) :

* Open terminal and install asar node module globally by typing __`npm install -g asar`__

* Go to __████__ file directory, in my case
 __`cd /Users/mac/Downloads/██████/Contents/Resources`__

* Create a directory to paste the content of app for example __`mkdir ███████-sourcecode`__

* Unpack the app.asar file in the above directory using asar __`asar extract app.asar example-sourcecode`__

{F335918}

Now we have all available endpoints in the app or let say in `gamma.grab.com` as well if you go to 
`build/constants/google/` you will get client_secret.json

```
{
    "installed": {
        "client_id": "█████",
        "project_id": "███████",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "█████████",
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
    }
}
```

and google_token.json

```
{"access_token":"██████████","refresh_token":"████","token_type":"Bearer","expiry_date":█████████}
```

But the most usefull and impactfull files are on `build/environement`:
* production-ph.env.json
* production.env.json
* staging.env.json

to verify if those token work let take for example 

```
"slack": {
    "channel": "█████",
    "schedule_channel": "███████",
    "token":
      "xoxp-██████",
    "user": "█████ ██████████"
  }
```

Before doing we need to know what kind of token is on our hand since [Slack have multiple kinds of token](https://api.slack.com/docs/token-types)

{F335920}

{F335921}

So we have __`User tokens`__ The xoxp-token (prefix xoxp) can be generated from the OAuth Test Token-page. This token is exactly like having the complete username and password for the user. Even for a user with two-factor authentication enabled, you can still access Slack with nothing else but this token.
And it is time to test if that token work or not? in order to that we need to follow the API documentation provided by slack here https://api.slack.com/web and try a non-sensitive method since I don't have the permission to read your internal data 

{F335923} 

The best example will be to list the name of all channels

{F335924}

So I set GET request in Burp with adding `Authorization: Bearer xoxp-████`as header and the result 

{F335925}

The result is 100 channels including but not limited to : 

* ██████
* ████
* ███████
*█████

#How to protect? (Important)

* __Avoid git add: commands:__ Using wildcards can easily capture local files not truly intended to be shared, Instead of wildcards, name each file you commit, or use git add -p to review each change you add.

* __Name sensitive files in .gitignore & .npmignore:__ git support a local file listing exclusions from packaging and commits, which you can use as a safety measure against the accidental inclusion of sensitive files, and you can use GitHub’s sample .gitignore files for other inspiration.

* __git-secrets: git hook prevents committing in credentials:__ a useful tool called git-secrets. The tool hooks onto git commit and breaks the commit if it includes patterns that appear to be credential. This is a good content-focused safety net, complementing the previously suggested filename based protection.

* __Encrypt or use environment vars when publishing from CI.__

* __Invalidate leaked credentials.__

#Reference:

* https://labs.detectify.com/2016/04/28/slack-bot-token-leakage-exposing-business-critical-information/
* https://medium.com/how-to-electron/how-to-get-source-code-of-any-electron-application-cbb5c7726c37
* https://api.slack.com/docs/token-types

## Impact

As I mentioned in the summary it possible to access to the developer’s company’s internal chats and files on Slack. And not only that, there’s no easy way to see if someone is eavesdropping on the communication and there are more worst scenarios.

## Attachments
- Capture_d_e_cran_2018-08-21_a__05.19.51.png
- Capture_d_e_cran_2018-08-21_a__05.49.51.png
- Capture_d_e_cran_2018-08-21_a__05.51.29.png
- Capture_d_e_cran_2018-08-21_a__05.55.10.png
- Capture_d_e_cran_2018-08-21_a__05.57.41.png
