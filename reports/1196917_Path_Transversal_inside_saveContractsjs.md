# Path Transversal inside saveContracts.js

## Report Details
- **Report ID**: 1196917
- **URL**: https://hackerone.com/reports/1196917
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-13T23:37:44.023Z
- **Disclosed**: 2021-05-14T00:47:11.539Z

## Reporter
- **Username**: caon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Reference: https://portswigger.net/web-security/file-path-traversal

Directory traversal (also known as file path traversal) is a web security vulnerability that allows an attacker to read arbitrary files on the server that is running an application. This might include application code and data, credentials for back-end systems, and sensitive operating system files. In some cases, an attacker might be able to write to arbitrary files on the server, allowing them to modify application data or behavior, and ultimately take full control of the server.

Inside https://github.com/Sifchain/sifnode/blob/develop/smart-contracts/scripts/saveContracts.js there's a part of the code which is not sanitized; meaning it could allow a path transversal to happen.

```javascript
function readFiles(dirname, onFileContent, onError) {
  fs.readdir(dirname, function(err, filenames) {
    if (err) {
      onError("The build/contracts directory does not exist.\n\nMake sure the build directory exists before running this script.\n\nTo create build directory run `truffle deploy --network develop`\n\n");
      return;
    }
    filenames.forEach(function(filename) {
      fs.readFile(dirname + filename, 'utf-8', function(err, content) {  <<<<<< VULNERABLE
        if (err) {
          onError(filename, err);
          return;
        }
        onFileContent(filename, content);
      });
    });
  });
}
```

Caller:
```javascript
readFiles("build/contracts/", handleFileContents, handleError);
```

# Explanation:
readFiles() function calls the `build/contracts/` path, let' says a file named `../../../../etc/passwd` exists inside the folder. 
Inside readFiles the first part of the script will grab all filenames, meaning it will grab the `../../../../etc/passwd`file. After grabbing the filenames It will proceed to call `fs.readFile` to each of the files.
When `fs.readFile` happens to `../../../../etc/passwd` the call will be something like that:

`build/contracts/../../../../etc/passwd`

Once executed it will show the `passwd` file containing all users and password of the machine because /../../../../ will force the path to root.

## Impact

This transversal allows an attacker to read arbitrary files on the server.

#Fix

Sanitize the inputs in the `filename` variable
If you are using node or express it is a good idea to follow this https://stackoverflow.com/questions/46718772/how-i-can-sanitize-my-input-values-in-node-js/46719000

Kind regards
Caon

## Attachments
No attachments
