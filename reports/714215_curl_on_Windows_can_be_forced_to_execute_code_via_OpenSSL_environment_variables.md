# curl on Windows can be forced to execute code via OpenSSL environment variables

## Report Details
- **Report ID**: 714215
- **URL**: https://hackerone.com/reports/714215
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-14T23:02:51.094Z
- **Disclosed**: 2021-02-08T07:54:17.110Z

## Reporter
- **Username**: supersausage
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
Preface: While I have an interest in security, I am not a professional security researcher, so please be forgiving of any lack of convention in this submission. The intent is to help improve security of the OpenSSL and curl projects, their consumers and end users. I will be sending this same content to both projects, curl via hackerone, and OpenSSL via openssl-security@openssl.org, per directions at each maintainer website.

I'm writing with regard to:
 - OpenSSL CVE-2019-1552
 - curl CVE-2019-5443
 
Background:
 - The root of each of these is that a default path in the OpenSSL build system for Windows targets is a location writable by a non-privileged user, and that OpenSSL configuration files placed there can change the behavior of OpenSSL, including code execution and escalation of privilege.
 - A PoC for code execution and escalation of privilege was published at:
   https://hackerone.com/reports/608577
 - This PoC uses a dynamic engine definition in such an OpenSSL configuration file to load a DLL in the security context of the application integrating the OpenSSL library, whose DLL_PROCESS_ATTACH handler inside DllMain can execute code in that context. This permits a non-elevated user to deploy code that may be executed by an elevated application.
 
Context of this email:
 - I am currently working with OpenSSL 1.0.2t as a LTS solution.
 - I have not tested or substantially researched other branches at this time.
 
Summary of current status:
 - OpenSSL project appears to have:
   - Designated CVE-2019-1552 as "Low" severity, even though the issue allows for EoP and potentially degrading the communication security intent of integrating applications, e.g. via inserting CA certificates.
   - At a high level, stated as "Fixed in OpenSSL 1.0.2t" (https://www.openssl.org/news/vulnerabilities.html) by this commit:
     https://github.com/openssl/openssl/commit/d333ebaf9c77332754a9d5e111e2f53e1de54fdd
	 The fix is, however, a fix to documentation, and changes in the build script that add a sample  for --prefix that is similarly insecure.
 - curl project appears to have:
   - Recommended that users update to 7.65.1_2
   - Stated that this commit "completely disables curl's ability to load an OpenSSL config when invoked."
     https://github.com/curl/curl-for-win/commit/51b658a76594942cf1d6f227d8fc4732bb8ec277
	 

My contentions:

 (A) The statement that CVE-2019-1552 was "Fixed in OpenSSL 1.0.2t" is extremely misleading, and could likely lead to users of the project updating OpenSSL without realizing that additional changes are required on their part. 

 (B) The sample "--prefix=c:/some/openssl/dir" is equally as vulnerable as the default, but more significantly, it is difficult to conceive of a path that is actually safe to use, and this might not be obvious to all developers. For example:
 
  - C:\Windows\System32 - Windows may not always be installed on drive letter 'C', leaving a hard-coded path similarly vulnerable on some systems
  - C:\Program Files - This path can be localized (e.g. "Programmes" in French-native installations), leaving a hard-coded path similarly vulnerable on some systems
    
  The OpenSSL code does not support passing an environment variable for runtime resolution, which would be a still vulnerable option, not least because Configure.pl will modify any path that is not an absolute path with drive letter, or one beginning with "/":

    $openssldir=$prefix . "/" . $openssldir if $openssldir !~ /(^\/|^[a-zA-Z]:[\\\/])/;
    
  One of few "safer" options I could think of was passing --prefix=\NUL --openssldir=\NUL, which should lead to a path or compound path after Configure.pl that is guaranteed to be invalid or else contain no content under Windows.
    
  In fact, in the aforementioned hackerone thread, "vsz" alludes to the fact that the fix in curl is not guaranteed:
    
  "After further experiments, I managed to tweak the build so that engine support can be kept enabled, and OpenSSL be built with a secure prefix. The trick was to use C:/Windows/System32/OpenSSL. This location can be fairly assumed to be a restricted directory on majority of installs and on all default installs going back a long time."
    
  Per above, this in not true unless Windows is installed on the 'C' drive. These are supposed to be projects implementing security, potentially integrated into end products distributed to millions of users with varying OS configurations. I personally would not call this "fixed". "Hardened", perhaps.
  
  (C) This still does not make the OpenSSL library safe, and I believe curl CVE-2019-5443 is actually *not fixed*, because the OpenSSL will read the path to configuration data from the OPENSSL_CONF environment variable.
  
  I downloaded curl 7.66.0 from:

    https://curl.haxx.se/windows/dl-7.66.0_2/curl-7.66.0_2-win32-mingw.zip
    
  I could compile and execute the same PoC as provided in the hackerone thread simply by setting the user-level environment variable:

    OPENSSL_CONF=C:\test\openssl.cnf
    
  The OpenSSL library used by curl (and other third-party apps who integrate it), will read this environment variable before the hard-coded path. Windows does not elevation to set user-level environment variables, and child processes can inherit them. This means that any elevated application using the OpenSSL library started from a compromised user account can be used as a EoP technique in the same way as before. For example, if OPENSSL_CONF is set at the user level, and the user signs out and later signs in again, the shell (Explorer.exe) inherits this environment variable, as does any process the user elevates.
    
  I have not tested, but if, as the text on the OpenSSL vulnerabilities page alludes to, this also allows someone to "insert CA certificates, modify (or even replace) existing engine modules", this same issue potentially weakens the communications secrecy of integrating apps.
    
  Aside: I see various places in the OpenSSL library code where other environment variables are queried, and I do not have time to evaluate each for potential issues.

## Impact

The attacker could run code in the context of an elevated process if they can modify user-level environment variables, or when Windows is not installed on the C drive.

Essentially, this report is that issues similar to CVE-2019-5443 persist in curl 7.66.0.

## Attachments
No attachments
