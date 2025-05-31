# stack overflow #2 in libsass

## Report Details
- **Report ID**: 221262
- **URL**: https://hackerone.com/reports/221262
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-15T18:39:06.190Z
- **Disclosed**: 2017-10-20T17:28:45.824Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
By pasting ` 0{g:00;m:(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((0` into `./sassc -s` we're able to trigger this stack overflow.

```
==28845==ERROR: AddressSanitizer: stack-overflow on address 0x7ffd55d71a88 (pc 0x000000584802 bp 0x7ffd55d722f0 sp 0x7ffd55d71a90 T0)
    #0 0x584801 in __asan_memcpy (/home/geeknik/sassc/bin/sassc+0x584801)
    #1 0x7c1df3 in Sass::Position::add(char const*, char const*) /home/geeknik/libsass/src/position.cpp:111:5
    #2 0x8dbf22 in char const* Sass::Parser::lex<&Sass::Prelexer::number>(bool, bool) /home/geeknik/libsass/src/parser.hpp:168:22
    #3 0x89557c in Sass::Parser::parse_value() /home/geeknik/libsass/src/parser.cpp:1616:9
    #4 0x87d034 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1451:14
    #5 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #6 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #7 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #8 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #9 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #10 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #11 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #12 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #13 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #14 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #15 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #16 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #17 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #18 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #19 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #20 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #21 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #22 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #23 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #24 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #25 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #26 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #27 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #28 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #29 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #30 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #31 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #32 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #33 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #34 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #35 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #36 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #37 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #38 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #39 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #40 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #41 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #42 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #43 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #44 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #45 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #46 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #47 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #48 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #49 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #50 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #51 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #52 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #53 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #54 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #55 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #56 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #57 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #58 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #59 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #60 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #61 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #62 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #63 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #64 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #65 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #66 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #67 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #68 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #69 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #70 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #71 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #72 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #73 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #74 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #75 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #76 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #77 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #78 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #79 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #80 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #81 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #82 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #83 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #84 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #85 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #86 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #87 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #88 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #89 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #90 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #91 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #92 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #93 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #94 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #95 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #96 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #97 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #98 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #99 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #100 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #101 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #102 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #103 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #104 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #105 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #106 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #107 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #108 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #109 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #110 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #111 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #112 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #113 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #114 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #115 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #116 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #117 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #118 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #119 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #120 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #121 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #122 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #123 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #124 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #125 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #126 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #127 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #128 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #129 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #130 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #131 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #132 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #133 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #134 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #135 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #136 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #137 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #138 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #139 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #140 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #141 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #142 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #143 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #144 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #145 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #146 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #147 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #148 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #149 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #150 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #151 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #152 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #153 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #154 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #155 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #156 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #157 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #158 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #159 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #160 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #161 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #162 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #163 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #164 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #165 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #166 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #167 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #168 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #169 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #170 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #171 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #172 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #173 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #174 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #175 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #176 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #177 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #178 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #179 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #180 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #181 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #182 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #183 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #184 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #185 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #186 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #187 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #188 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #189 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #190 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #191 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #192 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #193 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #194 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #195 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #196 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #197 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #198 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #199 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #200 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #201 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #202 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #203 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #204 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #205 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #206 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #207 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #208 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #209 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #210 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #211 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #212 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #213 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #214 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #215 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #216 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #217 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #218 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #219 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #220 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #221 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #222 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #223 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #224 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #225 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #226 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #227 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #228 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #229 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #230 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #231 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #232 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #233 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #234 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #235 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #236 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #237 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #238 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #239 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #240 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #241 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #242 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #243 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #244 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #245 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #246 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #247 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #248 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #249 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #250 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #251 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #252 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #253 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #254 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #255 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #256 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #257 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #258 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #259 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #260 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #261 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #262 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #263 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #264 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #265 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #266 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #267 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #268 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26
    #269 0x86b939 in Sass::Parser::parse_disjunction() /home/geeknik/libsass/src/parser.cpp:1213:27
    #270 0x826ab2 in Sass::Parser::parse_space_list() /home/geeknik/libsass/src/parser.cpp:1186:28
    #271 0x86a49a in Sass::Parser::parse_comma_list(bool) /home/geeknik/libsass/src/parser.cpp:1156:27
    #272 0x865145 in Sass::Parser::parse_list(bool) /home/geeknik/libsass/src/parser.cpp:1141:12
    #273 0x865145 in Sass::Parser::parse_map() /home/geeknik/libsass/src/parser.cpp:1057
    #274 0x87a454 in Sass::Parser::parse_factor() /home/geeknik/libsass/src/parser.cpp:1383:30
    #275 0x878304 in Sass::Parser::parse_operators() /home/geeknik/libsass/src/parser.cpp:1350:29
    #276 0x86fc62 in Sass::Parser::parse_expression() /home/geeknik/libsass/src/parser.cpp:1310:26
    #277 0x86e4c1 in Sass::Parser::parse_relation() /home/geeknik/libsass/src/parser.cpp:1256:26
    #278 0x86c919 in Sass::Parser::parse_conjunction() /home/geeknik/libsass/src/parser.cpp:1234:26

SUMMARY: AddressSanitizer: stack-overflow ??:0 __asan_memcpy
==28845==ABORTING
```

## Attachments
No attachments
