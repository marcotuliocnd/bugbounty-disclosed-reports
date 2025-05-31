# Renaming/aliasing relative symbolic links potentially redirects them to supposedly inaccessible locations

## Report Details
- **Report ID**: 1961655
- **URL**: https://hackerone.com/reports/1961655
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-25T20:15:02.803Z
- **Disclosed**: 2023-08-15T12:46:21.110Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
If a relative symbolic link is accessible to the Node.js process while the permission model is enabled, it can be redirected to a different target by renaming/aliasing it, which potentially allows the process to bypass restrictions imposed by the permission model.

## Steps To Reproduce:

1. Let's begin with a trusted directory structure.
  ```console
   git clone -b v20.0.0 --depth 1 https://github.com/nodejs/node.git node-20
   cd node-20
   ```
2. Now enter a Node.js REPL that (supposedly) only has access to the current working directory:
   ```console
   node --experimental-permission --allow-fs-read=$(pwd) --allow-fs-write=$(pwd)
   ```
3. Now either `rename` or `link` an existing relative symbolic link to redirect it. Example:
   ```js
   fs.renameSync('tools/node_modules/eslint/node_modules/eslint', 'escape');
   fs.readdirSync('escape');  // Prints the contents of the (supposedly inaccessible) parent directory.
   ```

Conveniently, `tools/node_modules/eslint/node_modules/eslint` is a symbolic link that points to its parent directory. As long as it remains in its original location, that is, of course, not a problem. In fact, relative symbolic links are very common, especially on Linux systems, and the symbolic link's target is well within the directory structure that the process is allowed to access. Once renamed, however, the symbolic link points outside of said directory structure.

## Impact

Of course, this depends on the pre-existing directory structure. In the worst case, this vulnerability allows an attacker to access any files on the system, regardless of restrictions imposed by the permission model.

This problem would be much more severe if not for another bug in the permission model, which prevents creating relative symbolic links altogether. Luckily, this other bug prevents the attacker from creating relative symlinks themselves, thus, they have to rely on existing relative symlinks (plus any created by package managers, etc.). Due to this fortunate restriction, I have not set the severity of the vulnerability to "high" but only to "medium".

## Attachments
No attachments
