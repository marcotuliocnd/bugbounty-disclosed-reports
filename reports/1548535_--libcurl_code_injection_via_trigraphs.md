# --libcurl code injection via trigraphs

## Report Details
- **Report ID**: 1548535
- **URL**: https://hackerone.com/reports/1548535
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-04-23T02:47:28.741Z
- **Disclosed**: 2022-04-24T22:07:12.698Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

curl command `--libcurl` option can be tricked to generate C code that when compiled contains arbitrary code execution.

## Steps To Reproduce:
  1. `curl --libcurl client.c --user-agent "??/\");char c[]={'i','d',' ','>','x',0},m[]={'r',0};fclose(popen(c,m));//" http://example.invalid`
  2. `gcc -trigraphs  client.c -lcurl -o client`
  3.  `./client`
  4. `ls -l x`

Note: In this PoC older compiler is simulated by passing `-trigraphs` option to gcc.

To remedy this issue `?` chars should be quoted to `\?` in the generated strings.

## Impact

Code injection to generated source code.

However, the impact of this vulnerability is minimal due to difficultly in finding scenarios where it would be practically exploitable. To be even remotely plausible curl command should somehow be hooked into a system that uses `--libcurl` to generate, compile and finally execute the compiled code *while* also accepting external user input for the curl command options. This seems extremely unlikely to happen in real life.

Trigraph support has also largely been disabled by now (gcc and clang have it disabled by default at least).

I don't really mind if this is found to be "not a vulnerability" (or only self-exploitable). In this case just close this H1 ticket and create a regular GitHub issue / or fix it direct.

## Attachments
No attachments
