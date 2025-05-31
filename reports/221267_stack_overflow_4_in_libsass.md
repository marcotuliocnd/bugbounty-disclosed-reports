# stack overflow #4 in libsass

## Report Details
- **Report ID**: 221267
- **URL**: https://hackerone.com/reports/221267
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-15T18:57:29.641Z
- **Disclosed**: 2017-10-20T17:29:21.157Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
`./sassc test385 /dev/null` triggers this stack overflow.

```
==1001==ERROR: AddressSanitizer: stack-overflow on address 0x7ffeaf4f4fa0 (pc 0x0000008b63fd bp 0x7ffeaf4f5130 sp 0x7ffeaf4f4f40 T0)
    #0 0x8b63fc in char const* Sass::Parser::lex<&Sass::Prelexer::css_comments>(bool, bool) /home/geeknik/libsass/src/parser.hpp:137
    #1 0x87a337 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1380:5
    #2 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #3 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #4 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #5 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #6 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #7 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #8 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #9 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #10 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #11 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #12 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #13 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #14 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #15 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #16 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #17 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #18 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #19 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #20 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #21 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #22 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #23 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #24 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #25 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #26 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #27 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #28 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #29 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #30 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #31 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #32 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #33 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #34 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #35 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #36 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #37 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #38 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #39 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #40 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #41 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #42 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #43 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #44 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #45 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #46 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #47 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #48 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #49 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #50 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #51 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #52 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #53 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #54 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #55 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #56 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #57 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #58 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #59 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #60 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #61 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #62 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #63 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #64 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #65 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #66 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #67 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #68 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #69 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #70 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #71 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #72 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #73 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #74 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #75 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #76 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #77 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #78 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #79 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #80 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #81 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #82 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #83 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #84 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #85 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #86 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #87 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #88 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #89 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #90 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #91 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #92 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #93 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #94 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #95 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #96 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #97 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #98 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #99 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #100 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #101 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #102 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #103 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #104 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #105 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #106 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #107 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #108 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #109 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #110 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #111 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #112 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #113 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #114 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #115 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #116 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #117 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #118 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #119 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #120 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #121 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #122 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #123 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #124 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #125 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #126 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #127 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #128 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #129 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #130 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #131 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #132 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #133 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #134 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #135 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #136 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #137 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #138 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #139 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #140 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #141 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #142 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #143 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #144 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #145 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #146 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #147 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #148 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #149 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #150 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #151 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #152 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #153 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #154 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #155 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #156 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #157 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #158 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #159 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #160 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #161 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #162 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #163 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #164 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #165 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #166 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #167 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #168 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #169 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #170 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #171 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #172 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #173 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #174 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #175 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #176 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #177 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #178 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #179 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #180 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #181 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #182 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #183 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #184 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #185 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #186 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #187 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #188 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #189 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #190 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #191 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #192 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #193 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #194 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #195 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #196 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #197 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #198 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #199 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #200 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #201 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #202 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #203 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #204 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #205 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #206 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #207 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #208 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #209 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #210 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #211 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #212 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #213 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #214 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #215 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #216 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #217 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #218 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #219 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #220 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #221 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #222 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #223 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #224 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #225 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #226 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #227 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #228 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #229 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #230 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #231 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #232 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #233 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #234 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #235 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #236 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #237 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #238 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #239 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #240 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #241 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #242 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #243 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #244 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #245 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #246 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #247 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #248 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #249 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #250 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
    #251 0x87be41 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1429:33
SUMMARY: AddressSanitizer: stack-overflow /home/geeknik/libsass/src/parser.hpp:137 char const* Sass::Parser::lex<&Sass::Prelexer::css_comments>(bool, bool)
==1001==ABORTING
```

## Attachments
- test385
