# stack overflow #3 in libsass

## Report Details
- **Report ID**: 221264
- **URL**: https://hackerone.com/reports/221264
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-15T18:47:12.337Z
- **Disclosed**: 2017-10-20T17:29:03.940Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
`./sassc test387 /dev/null` triggers this stack overflow.

```
==9081==ERROR: AddressSanitizer: stack-overflow on address 0x7fffb48eadc0 (pc 0x00000087a07b bp 0x7fffb48eba30 sp 0x7fffb48ead60 T0)
    #0 0x87a07a in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1379
    #1 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #2 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #3 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #4 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #5 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #6 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #7 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #8 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #9 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #10 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #11 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #12 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #13 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #14 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #15 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #16 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #17 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #18 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #19 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #20 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #21 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #22 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #23 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #24 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #25 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #26 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #27 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #28 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #29 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #30 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #31 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #32 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #33 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #34 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #35 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #36 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #37 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #38 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #39 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #40 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #41 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #42 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #43 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #44 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #45 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #46 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #47 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #48 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #49 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #50 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #51 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #52 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #53 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #54 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #55 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #56 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #57 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #58 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #59 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #60 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #61 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #62 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #63 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #64 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #65 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #66 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #67 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #68 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #69 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #70 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #71 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #72 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #73 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #74 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #75 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #76 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #77 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #78 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #79 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #80 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #81 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #82 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #83 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #84 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #85 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #86 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #87 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #88 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #89 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #90 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #91 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #92 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #93 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #94 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #95 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #96 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #97 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #98 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #99 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #100 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #101 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #102 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #103 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #104 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #105 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #106 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #107 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #108 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #109 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #110 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #111 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #112 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #113 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #114 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #115 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #116 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #117 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #118 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #119 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #120 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #121 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #122 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #123 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #124 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #125 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #126 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #127 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #128 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #129 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #130 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #131 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #132 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #133 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #134 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #135 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #136 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #137 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #138 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #139 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #140 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #141 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #142 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #143 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #144 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #145 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #146 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #147 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #148 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #149 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #150 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #151 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #152 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #153 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #154 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #155 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #156 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #157 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #158 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #159 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #160 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #161 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #162 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #163 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #164 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #165 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #166 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #167 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #168 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #169 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #170 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #171 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #172 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #173 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #174 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #175 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #176 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #177 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #178 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #179 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #180 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #181 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #182 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #183 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #184 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #185 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #186 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #187 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #188 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #189 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #190 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #191 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #192 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #193 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #194 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #195 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #196 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #197 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #198 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #199 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #200 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #201 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #202 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #203 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #204 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #205 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #206 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #207 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #208 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #209 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #210 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #211 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #212 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #213 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #214 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #215 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #216 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #217 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #218 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #219 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #220 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #221 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #222 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #223 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #224 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #225 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #226 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #227 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #228 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #229 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #230 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #231 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #232 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #233 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #234 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #235 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #236 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #237 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #238 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #239 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #240 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #241 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #242 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #243 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #244 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #245 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #246 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #247 0x86818a in Sass::Parser::parse_bracket_list() /home/geeknik/libsass/src/parser.cpp:1106:27
    #248 0x87a961 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1391:30
    #249 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #250 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #251 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26

SUMMARY: AddressSanitizer: stack-overflow /home/geeknik/libsass/src/parser.cpp:1379 Sass::Parser::parse_factor()
==9081==ABORTING
```


## Attachments
- test387
