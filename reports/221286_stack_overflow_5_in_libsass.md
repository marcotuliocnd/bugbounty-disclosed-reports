# stack overflow #5 in libsass

## Report Details
- **Report ID**: 221286
- **URL**: https://hackerone.com/reports/221286
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-15T20:20:32.684Z
- **Disclosed**: 2017-10-20T17:29:21.162Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
`./sassc test099 /dev/null` triggers this stack overflow.

```
==9395==ERROR: AddressSanitizer: stack-overflow on address 0x7fff5d9a4e48 (pc 0x000000584c3a bp 0x7fff5d9a56b0 sp 0x7fff5d9a4e50 T0)
    #0 0x584c39 in __asan_memset (/home/geeknik/sassc/bin/sassc+0x584c39)
    #1 0x83b798 in Sass::Parser::advanceToNextToken() /home/geeknik/libsass/src/parser.cpp:66:7
    #2 0x83b798 in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:704
    #3 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #4 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #5 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #6 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #7 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #8 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #9 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #10 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #11 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #12 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #13 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #14 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #15 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #16 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #17 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #18 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #19 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #20 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #21 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #22 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #23 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #24 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #25 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #26 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #27 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #28 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #29 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #30 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #31 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #32 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #33 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #34 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #35 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #36 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #37 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #38 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #39 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #40 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #41 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #42 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #43 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #44 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #45 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #46 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #47 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #48 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #49 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #50 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #51 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #52 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #53 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #54 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #55 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #56 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #57 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #58 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #59 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #60 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #61 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #62 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #63 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #64 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #65 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #66 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #67 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #68 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #69 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #70 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #71 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #72 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #73 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #74 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #75 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #76 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #77 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #78 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #79 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #80 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #81 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #82 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #83 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #84 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #85 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #86 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #87 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #88 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #89 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #90 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #91 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #92 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #93 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #94 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #95 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #96 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #97 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #98 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #99 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #100 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #101 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #102 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #103 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #104 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #105 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #106 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #107 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #108 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #109 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #110 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #111 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #112 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #113 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #114 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #115 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #116 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #117 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #118 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #119 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #120 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #121 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #122 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #123 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #124 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #125 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #126 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #127 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #128 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #129 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #130 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #131 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #132 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #133 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #134 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #135 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #136 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #137 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #138 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #139 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #140 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #141 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #142 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #143 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #144 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #145 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #146 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #147 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #148 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #149 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #150 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #151 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #152 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #153 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #154 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #155 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #156 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #157 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #158 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #159 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #160 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #161 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #162 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #163 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #164 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #165 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #166 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #167 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #168 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #169 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #170 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #171 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #172 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #173 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #174 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #175 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #176 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #177 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #178 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #179 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #180 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #181 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #182 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #183 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #184 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #185 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #186 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #187 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #188 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #189 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #190 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #191 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #192 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #193 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #194 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #195 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #196 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #197 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #198 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #199 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #200 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #201 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #202 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #203 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #204 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #205 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #206 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #207 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #208 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #209 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #210 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #211 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #212 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #213 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #214 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #215 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #216 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #217 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #218 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #219 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #220 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #221 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #222 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #223 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #224 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #225 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #226 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #227 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #228 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #229 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #230 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #231 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #232 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #233 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #234 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #235 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #236 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #237 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #238 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #239 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #240 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #241 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #242 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #243 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #244 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #245 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #246 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #247 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #248 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #249 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #250 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #251 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17
    #252 0x83d0ea in Sass::Parser::parse_complex_selector(bool) /home/geeknik/libsass/src/parser.cpp:746:17

SUMMARY: AddressSanitizer: stack-overflow ??:0 __asan_memset
==9395==ABORTING
```

## Attachments
- test099
