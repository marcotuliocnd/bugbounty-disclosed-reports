# stack overflow #6 in libsass

## Report Details
- **Report ID**: 221292
- **URL**: https://hackerone.com/reports/221292
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-15T20:41:08.313Z
- **Disclosed**: 2017-10-20T17:29:37.889Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
Feeding `/**/0{i:((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((` to `./sassc -s` triggers this stack overflow.

```
==11380==ERROR: AddressSanitizer: stack-overflow on address 0x7fff1665bfa8 (pc 0x000000584802 bp 0x7fff1665c810 sp 0x7fff1665bfb0 T0)
    #0 0x584801 in __asan_memcpy (/home/geeknik/sassc/bin/sassc+0x584801)
    #1 0x87a353 in char const* Sass::Parser::lex_css<&(char const* Sass::Prelexer::exactly<(char)40>(char const*))>() /home/geeknik/libsass/src/parser.hpp:188:7
    #2 0x87a353 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1381
    #3 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #4 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #5 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #6 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #7 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #8 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #9 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #10 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #11 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #12 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #13 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #14 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #15 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #16 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #17 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #18 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #19 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #20 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #21 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #22 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #23 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #24 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #25 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #26 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #27 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #28 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #29 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #30 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #31 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #32 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #33 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #34 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #35 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #36 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #37 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #38 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #39 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #40 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #41 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #42 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #43 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #44 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #45 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #46 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #47 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #48 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #49 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #50 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #51 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #52 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #53 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #54 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #55 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #56 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #57 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #58 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #59 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #60 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #61 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #62 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #63 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #64 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #65 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #66 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #67 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #68 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #69 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #70 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #71 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #72 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #73 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #74 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #75 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #76 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #77 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #78 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #79 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #80 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #81 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #82 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #83 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #84 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #85 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #86 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #87 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #88 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #89 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #90 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #91 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #92 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #93 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #94 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #95 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #96 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #97 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #98 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #99 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #100 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #101 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #102 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #103 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #104 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #105 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #106 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #107 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #108 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #109 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #110 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #111 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #112 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #113 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #114 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #115 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #116 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #117 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #118 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #119 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #120 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #121 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #122 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #123 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #124 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #125 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #126 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #127 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #128 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #129 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #130 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #131 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #132 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #133 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #134 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #135 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #136 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #137 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #138 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #139 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #140 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #141 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #142 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #143 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #144 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #145 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #146 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #147 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #148 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #149 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #150 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #151 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #152 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #153 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #154 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #155 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #156 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #157 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #158 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #159 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #160 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #161 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #162 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #163 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #164 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #165 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #166 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #167 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #168 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #169 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #170 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #171 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #172 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #173 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #174 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #175 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #176 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #177 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #178 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #179 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #180 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #181 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #182 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #183 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #184 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #185 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #186 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #187 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #188 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #189 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #190 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #191 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #192 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #193 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #194 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #195 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #196 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #197 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #198 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #199 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #200 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #201 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #202 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #203 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #204 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #205 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #206 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #207 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #208 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #209 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #210 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #211 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #212 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #213 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #214 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #215 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #216 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #217 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #218 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #219 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #220 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #221 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #222 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #223 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #224 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #225 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #226 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #227 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #228 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #229 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #230 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #231 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #232 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #233 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #234 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #235 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #236 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #237 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #238 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #239 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #240 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #241 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #242 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #243 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #244 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #245 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #246 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #247 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #248 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #249 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #250 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #251 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #252 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #253 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #254 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #255 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #256 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #257 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #258 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #259 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #260 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #261 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #262 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #263 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #264 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #265 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #266 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #267 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #268 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #269 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #270 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #271 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #272 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #273 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #274 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #275 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #276 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #277 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #278 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #279 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27

SUMMARY: AddressSanitizer: stack-overflow ??:0 __asan_memcpy
==11380==ABORTING
```

## Attachments
No attachments
