# Remote code execution on rubygems.org

## Report Details
- **Report ID**: 274990
- **URL**: https://hackerone.com/reports/274990
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-10-06T08:49:52.800Z
- **Disclosed**: 2017-11-09T05:56:39.178Z

## Reporter
- **Username**: max
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
When parsing a gem POSTed to the `/api/v1/gems` endpoint, the rubygems.org application immediately calls `Gem::Package.new(body).spec` inside `app/models/pusher.rb`. The authors of the application correctly observed that parsing untrusted YAML is dangerous (since it can serialize more or less arbitrary objects), so they monkey-patched the spec parser to use `Psych.safe_load` set from `config/initializers/forbidden_yaml.rb`.

However, `YAML.load` is called directly when parsing the gem's checksum file in `Gem::Package#read_checksums`. Using classes accessible within the application, I was able to turn this into a call to `Marshal.load` on attacker-controlled data. From there, I was able to use known Marshal exploitation techniques to achieve code execution on the server (I'm omitting some details here for brevity so that I can submit this report right away).

A proof of concept, `poc.gem`, is attached. Run the exploit with the following command:
`cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://rubygems.org/api/v1/gems`

I ran the attached PoC twice. It just does a `wget` to my server.

Please let me know if I should clarify anything! Thanks for running this program.

## Attachments
No attachments
