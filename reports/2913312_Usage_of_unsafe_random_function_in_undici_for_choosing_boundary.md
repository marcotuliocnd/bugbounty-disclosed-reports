# Usage of unsafe random function in undici for choosing boundary

## Report Details
- **Report ID**: 2913312
- **URL**: https://hackerone.com/reports/2913312
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-12-24T10:43:44.475Z
- **Disclosed**: 2025-01-23T13:43:08.671Z

## Reporter
- **Username**: parrot409
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
[Undici uses Math.random()](https://github.com/nodejs/undici/blob/8b06b8250907d92fead664b3368f1d2aa27c1f35/lib/web/fetch/body.js#L113) to choose the boundary for a `multipart/form-data` request. It is known that the output of `Math.random()` can be predicted if several of its generated values are known.

**Description:** 
If an attacker can access a few generated values of `Math.random()` and has control over one of the fields of a multipart request, they can add or overwrite fields that are not meant to be controllable.

If there is a mechanism in an app that sends multipart requests to an attacker-controlled website, they can use this to leak the necessary values.

Here is an example app that is vulnerable to this bug.
```javascript
#!/usr/bin/env node
const express = require('express')

const BACKEND_API = 'http://localhost:2000/order.php'

const app = express()

app.use(express.urlencoded({ extended: false }))

app.get('/trigger-webhook',(req,res)=>{
	let url = req.query.url
	let data = new FormData()
	data.append('event','example-event')
	fetch(url,{
		body: data,
		method: 'POST'
	})
	res.send('OK')
})

app.post('/order',(req,res)=>{
	let description = req.body.description || 'Please wrap it in Christmas-themed wrapping paper.'
	let data = new FormData()
	data.append('price','4000')
	data.append('customer_id','1')
	data.append('item_id','1')
	data.append('description',description)
	fetch(BACKEND_API,{
		body: data,
		method: `POST`
	}).then(r=>r.text()).then(r=>res.send(r)).catch(r=>res.send('Err'))
})

app.listen(8000)
```

`BACKEND_API` points to this php app (`order.php`):

```php
$<?= $_POST['price'] ?> has been subtracted from the account of customer #<?= $_POST['customer_id'] ?> for item <?= $_POST['item_id'] ?>.
description of order: ("<?= $_POST['description'] ?>")
```

## Steps To Reproduce:
  1. Extract F3883352.
  2. In the `server` directory: `npm install; node ./server.js`.
  3. In the `server` directory: `php -S 127.0.0.1:2000`.
  4. In the `exp` directory: `pip3 install z3-solver; node ./exp.js`.

A successful exploit looks like this:
```
$ node --version
v22.12.0
$ node ./server.js 

```
```
$ node ./exp.js 
Need 9 more values
Need 8 more values
Need 7 more values
Need 6 more values
Need 5 more values
Need 4 more values
Need 3 more values
Need 2 more values
Need 1 more values
$4000 has been subtracted from the account of customer #1337 for item 1.
description of order: ("zzz")
```

The `customer_id` parameter could be successfully tampered with.

## Impact: 

An attacker can tamper with the requests going to the backend APIs if certain conditions are met.

## Supporting Material/References:

-  `predict.py` is the modified version of https://github.com/PwnFunction/v8-randomness-predictor/tree/main
- https://blog.securityevaluators.com/hacking-the-javascript-lottery-80cc437e3b7f

## Impact

An attacker can tamper with the requests going to the backend APIs if certain conditions are met.

## Attachments
- report.tar.xz
