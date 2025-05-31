# Remote hacker can download all the files of master branch in public projects where everything is members only.

## Report Details
- **Report ID**: 1043480
- **URL**: https://hackerone.com/reports/1043480
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-25T15:24:46.224Z
- **Disclosed**: 2021-02-15T14:45:11.257Z

## Reporter
- **Username**: anshraj_srivastava
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Hi team,
I found this weird behavior which I thought I should report, a malicious hacker can remotely download files of any branch in a public project where all permissions are ==member-only==, Gitlab uses a link to download files of a branch, normally ==an unauthenticated user will not be able to download the files through the link, he would be shown an error message,== however, the weird behavior is that if ==the admin or someone with the permission to download the files of the branch, clicks on the link, then for a few moments afterward, anyone on the internet can download the file through the link .==

The link to download files is like this - https://gitlab.com/photographyknavel/my-private-proj-3/-/archive/master/my-private-proj-3-master.zip and ==it can be easily constructed.==

### Steps to reproduce

1.Create a public project and ==change every permission to members-only.==

{F1093574}

2.Upload some files in the repository-

{F1093575}

3.Go to "Branches" and ==try opening the link to download a branch in an incognito tab-==

{F1093579}

+ As you can see, it shows an error.

4.Now go back to the project and click on the link, no need to download it right now and then go to the incognito window and try opening the link again-

+ This time ==the link opens and we can download the file== from the incognito window even though we are not authenticated-

{F1093584}

+ To confirm this bug, ==you can try opening the link on another device too, make sure you do it right after clicking the link from the admin account-==

{F1093592}

(This video is from my iPad, ==which was on a completely different network and the Gitlab account wasn't related to the project at all==)

###Practical Attack scenario-
Now, as you may be wondering that even though the bug exists, the chances of a malicious hacker clicking the link right after an admin does are next to none, ==well this problem can easily be bypassed and the hacker can gain access to the files-==

1.Let's say that I am a malicious hacker and I discover this project, which has almost all features restricted to members only and as mentioned above, I can't download the files by clicking on the link-

{F1093593}

2.However, I am aware of this bug,==so I use a web automation software like Selenium IDE (https://www.selenium.dev/selenium-ide/ )==. I can program a script to refresh this page - https://gitlab.com/photographyknavel/my-private-proj-3/-/archive/master/my-private-proj-3-master.zip automatically, so if the victim ever clicks the download button,==I will be able to download the file since the page is being refreshed frequently and the script will stop if the link is executed.==

##Selenium Script (also attached as Gitlab.side in the attachments)-
```
{
  "id": "e4cd88a3-0530-4596-b497-88b2de68115b",
  "version": "2.0",
  "name": "Gitlab-3",
  "url": "",
  "tests": [{
    "id": "f3bbf89a-47e1-47e9-959c-7beebaf6226c",
    "name": "hhh",
    "commands": [{
      "id": "f0eb0ad5-60db-4fdc-89ac-4f397416d931",
      "comment": "",
      "command": "times",
      "target": "9999",
      "targets": [],
      "value": ""
    }, {
      "id": "2e11e74e-f01d-4679-8148-fc3a380df1ca",
      "comment": "",
      "command": "open",
      "target": "https://gitlab.com/photographyknavel/my-private-proj-3/-/archive/master/my-private-proj-3-master.zip",
      "targets": [],
      "value": ""
    }, {
      "id": "aa98d614-88f2-4812-a67e-60d33949d672",
      "comment": "",
      "command": "end",
      "target": "",
      "targets": [],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "ac71892f-28e5-4c5f-8f83-78ba310b1664",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["f3bbf89a-47e1-47e9-959c-7beebaf6226c"]
  }],
  "urls": [],
  "plugins": []
}
```
==NOTE-==

+ The script is basically a loop that runs for a large number of times, in this case, I have kept it ``9999`` but it can be increased.
+ ==Do change the URL of the target from https://gitlab.com/photographyknavel/my-private-proj-3/-/archive/master/my-private-proj-3-master.zip to the URL of the project you are targeting.==

##Screenshots and videos-

+ Victim POV-

{F1093820}

+ Hacker POV-

{F1093818}

The script that was refreshing the page automatically, ==it stops doing so as soon as the victim clicks the download project option and now the hacker can download the files.==

## Impact

The clear security impact is that a malicious hacker is able to ==access files stored in a branch even though he's not authorized to do so, this leads to a data leak.==

## Attachments
- recording-1606307452409.webm
- recording-1606307515401.webm
- recording-1606307568402.webm
- recording-1606307655412.webm
- Gitlab-vid.MP4
- recording-1606308245405.webm
- recording-1606308424343.webm
- Gitlab.side
- recording-1606317336409.webm
- Gitlab_victim.MP4
