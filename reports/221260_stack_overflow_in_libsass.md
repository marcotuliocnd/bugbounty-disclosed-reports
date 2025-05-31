# stack overflow in libsass

## Report Details
- **Report ID**: 221260
- **URL**: https://hackerone.com/reports/221260
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-15T18:31:54.689Z
- **Disclosed**: 2017-10-20T17:28:13.281Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
By pasting `@H#{[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[}` into `./sassc -s`, we're able to trigger this stack overflow.

```
==3470==ERROR: AddressSanitizer: stack-overflow on address 0x7ffe1b09ffc8 (pc 0x00000059bc77 bp 0x7ffe1b0a0820 sp 0x7ffe1b09ffd0 T0)
    #0 0x59bc76 in __interceptor_malloc (/home/geeknik/sassc/bin/sassc+0x59bc76)
    #1 0x7f842fedb2e7 in operator new(unsigned long) (/usr/lib/x86_64-linux-gnu/libstdc++.so.6+0x5f2e7)
    #2 0x7f842ff3ae98 in std::string::_Rep::_S_create(unsigned long, unsigned long, std::allocator<char> const&) (/usr/lib/x86_64-linux-gnu/libstdc++.so.6+0xbee98)
    #3 0x7f842ff3c814 in char* std::string::_S_construct<char const*>(char const*, char const*, std::allocator<char> const&, std::forward_iterator_tag) (/usr/lib/x86_64-linux-gnu/libstdc++.so.6+0xc0814)
    #4 0x7f842ff3cc45 in std::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(char const*, std::allocator<char> const&) (/usr/lib/x86_64-linux-gnu/libstdc++.so.6+0xc0c45)
    #5 0x896a14 in Sass::Parser::parse_value() /home/geeknik/libsass/src/parser.cpp:1626:5
    #6 0x87d034 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1451:14
    #7 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #8 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #9 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #10 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #11 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #12 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #13 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #14 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #15 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #16 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #17 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #18 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #19 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #20 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #21 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #22 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #23 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #24 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #25 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #26 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #27 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #28 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #29 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #30 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #31 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #32 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #33 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #34 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #35 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #36 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #37 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #38 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #39 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #40 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #41 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #42 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #43 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #44 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #45 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #46 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #47 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #48 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #49 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #50 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #51 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #52 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #53 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #54 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #55 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #56 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #57 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #58 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #59 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #60 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #61 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #62 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #63 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #64 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #65 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #66 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #67 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #68 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #69 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #70 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #71 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #72 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #73 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #74 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #75 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #76 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #77 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #78 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #79 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #80 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #81 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #82 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #83 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #84 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #85 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #86 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #87 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #88 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #89 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #90 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #91 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #92 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #93 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #94 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #95 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #96 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #97 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #98 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #99 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #100 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #101 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #102 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #103 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #104 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #105 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #106 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #107 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #108 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #109 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #110 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #111 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #112 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #113 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #114 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #115 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #116 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #117 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #118 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #119 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #120 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #121 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #122 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #123 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #124 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #125 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #126 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #127 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #128 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #129 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #130 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #131 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #132 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #133 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #134 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #135 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #136 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #137 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #138 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #139 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #140 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #141 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #142 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #143 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #144 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #145 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #146 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #147 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #148 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #149 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #150 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #151 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #152 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #153 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #154 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #155 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #156 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #157 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #158 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #159 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #160 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #161 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #162 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #163 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #164 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #165 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #166 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #167 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #168 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #169 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #170 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #171 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #172 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #173 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #174 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #175 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #176 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #177 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #178 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #179 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #180 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #181 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #182 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #183 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #184 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #185 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #186 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #187 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #188 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #189 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #190 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #191 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #192 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #193 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #194 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #195 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #196 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #197 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #198 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #199 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #200 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #201 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #202 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #203 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #204 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #205 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #206 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #207 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #208 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #209 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #210 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #211 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #212 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #213 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #214 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #215 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #216 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #217 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #218 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #219 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #220 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #221 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #222 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #223 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #224 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #225 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #226 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #227 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #228 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #229 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #230 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #231 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #232 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #233 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #234 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #235 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #236 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #237 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #238 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #239 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #240 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #241 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #242 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #243 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #244 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #245 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #246 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #247 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #248 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #249 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #250 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #251 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27

SUMMARY: AddressSanitizer: stack-overflow ??:0 __interceptor_malloc
==3470==ABORTING
```

## Attachments
No attachments
