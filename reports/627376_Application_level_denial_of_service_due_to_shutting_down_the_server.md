# Application level denial of service due to shutting down the server 

## Report Details
- **Report ID**: 627376
- **URL**: https://hackerone.com/reports/627376
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-24T17:18:38.926Z
- **Disclosed**: 2019-09-27T09:21:52.359Z

## Reporter
- **Username**: 3la2kb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
## Module
**module name:** http-live-simulator
**version:** 1.0.7
**npm page:** https://www.npmjs.com/package/http-live-simulator

## Description
I've found a way to crash the server due to the way it parses URL 

## Steps To Reproduce:
1- Install the module : `npm install -g http-live-simulator`
2- Run the server : `http-live`
3- Attempt to crash the server by this command `curl --path-as-is http://localhost:8080/../?a`

## Explanation :
the reason for this issue is the fix for my previous [report](https://hackerone.com/reports/411405)
which is :
```javascript
	var pathname = url.parse(req.url, true).pathname;
	while(pathname.indexOf("/../") != -1) {
		pathname = pathname.replace("/../",""); //fix for path traversal bug
	}
```
so now if we pass ` http://localhost:8080/../?a` as the url the `pathname` becomes empty
which will cause skipping this condition :
```javascript
		if (pathname == "/") {
			for(var i=0;i<defaults.length;i++) {
				if (fs.existsSync(process.cwd() + '/' + defaults[i])) {
					pathname = '/' + defaults[i];
					break;
				}
			}
			if (pathname == '/') {
				return404(res, pathname);
				console.log(pathname);
				return;
			}
		}
```
with this in mind now we can proceed to the buggy snippet :
```javascript
		abspath = process.cwd() + pathname;
		console.log('REQUEST: ', req.method, pathname);

		if (fs.existsSync(abspath)) {
			console.log("in condition");
			fs.readFile(abspath, function(err, data) {
				console.log("in condition1");
				var ext = pathname.slice(pathname.indexOf("."));
				var mtype = getMimeType(ext);
				res.writeHead(200, {'Content-Type': mtype});
				console.log(abspath, data);
				res.write(data);
				res.end();
			});
		}
``` 
here `abspath` becomes `<project_dir>` which cannot be read by `readFile` because it's a directory not a file causing the value of `data` to be `undefined` which will cause an error when trying to `res.write(data);` as `res.write()` function expects its parameter to be a string or buffer but it's `undefined` in this case.

## Fix :
append a `/` to `pathname` if it becomes empty after sanitizing

## Impact

Denial of service due to shutting down the server

## Attachments
No attachments
