# [redis-commander] Reflected SWF XSS via vulnerable "clipboard.swf" component

## Report Details
- **Report ID**: 296377
- **URL**: https://hackerone.com/reports/296377
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-08T20:43:21.737Z
- **Disclosed**: 2018-01-23T09:52:52.622Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi,

An injection in the `highlighterId` parameter of the `clipboard.swf` component can be used to reflect JavaScript in the context of hosts running Redis Commander.

## Module specification
* **Name**: [redis-commander](https://www.npmjs.com/package/redis-commander)
* **Version**: 0.4.5 (latest release build)

## Verified conditions
* **Test server:** Ubuntu 16.04 LTS
* **Browser version:** Firefox 57.0 (64-bit)
* **Flash version:** 27.0.0.187

## Proof of concept

Please globally install the `redis-commander` package and run `redis-commander -p 80` to start serving the Commander interface.

To reproduce this vulnerability, please access the below URL in a browser with Adobe Flash enabled and **click on the content** which appears.

```
http://instance/jstree/_docs/syntax/clipboard.swf?highlighterId=\%22))}%20catch(e)%20{alert(document.domain);}//
```

{F245319}

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability in a crafted request that, if issued by another Redis Commander user, will cause arbitrary JavaScript code to execute within the target's browser in the context of their session.

## Attachments
- redis_swf_xss.png
