# Crash: A call to Symbol.new leads to a crash when inspecting the resulting object

## Report Details
- **Report ID**: 185957
- **URL**: https://hackerone.com/reports/185957
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-28T08:38:10.247Z
- **Disclosed**: 2016-12-16T22:20:25.461Z

## Reporter
- **Username**: brakhane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Calling `Symbol.new` leads to a when `inspect` is called on that method (probably even more methods).  From my point of view the root cause is related to #185794 (the underlying boxing model).

Trying the same with Ruby 2.3 will lead to a `NoMethodError: undefined method 'new' for Symbol:Class`, which is probably the right way of fixing this - `Symbol` shouldn't be a class where someone can call `new` on. However, as this relates to the boxing problems I (briefly) outlined in the other ticket (still jetlagged, sorry), a more fundamental fix might be a better choice. But that might be something Matz knows better than I do.

Having said that, it appears that `https://mruby.science/runs` isn't vulnerable to this anymore (or I'm unable to trigger it there, but that's somewhat unlikely as my sandbox does crash). So I believe the fix already done is not 'correct'. This should really be handled like any other class like `Symbol` (similar examples are `TrueClass`, `FalseClass`, `NilClass`, which all have one thing in common:

They got their new method removed by a call looking something like this:
```
mrb_undef_class_method(mrb, n, "new");
```

So while this report is for the most part probably informative, I believe the applied fix (assuming there was a fix) is not correctly aligned with similar classes.

#PoC
```
a = Symbol.new
a.inspect # mirb will crash without this line as it calls inspect after each evaluated statement

```

#Trace
```
$ bin/sandbox crashes/symbol_new.mrb
bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000000
ruby 2.3.3p222 (2016-11-21 revision 56859) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:001a68 EVAL   bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:0008d0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:20:in `<main>'
bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f2eb6e42846 RBP: 0x00007f2eb59a84e0 RSP: 0x00007f2eb59a6aa0
 RAX: 0x00007f2eb59aefa9 RBX: 0x00007f2eb59aef90 RCX: 0x0000000000000004
 RDX: 0x0000000000000000 RDI: 0x00007f2eb59aefa9 RSI: 0x0000000000000000
  R8: 0x00007f2eb59b94f0  R9: 0x0000000000000000 R10: 0x0000000000000218
 R11: 0x00007f2eb6e262d0 R12: 0x0000000000000000 R13: 0x0000000000000000
 R14: 0x00007f2eb59a84e0 R15: 0x00007f2eb59b3010 EFL: 0x0000000000010246

-- C level backtrace information -------------------------------------------
/usr/lib/libruby.so.2.3 [0x7f2ebaf0c455]
/usr/lib/libruby.so.2.3 [0x7f2ebaf0c68c]
/usr/lib/libruby.so.2.3 [0x7f2ebade6e34]
/usr/lib/libruby.so.2.3 [0x7f2ebae986ce]
/usr/lib/libc.so.6 [0x7f2ebaa0c0b0]
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(sym_inspect+0x66) [0x7f2eb6e42846] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/symbol.c:410
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x762) [0x7f2eb6e32cb2] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7f2eb6e38987] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7f2eb6e17cd3] ../../../../ext/mruby_engine/eval_monitored.c:68
/usr/lib/libpthread.so.0(start_thread+0xc4) [0x7f2eba7c3454]
/usr/lib/libc.so.6(clone+0x5f) [0x7f2ebaac17df]

-- Other runtime information -----------------------------------------------

* Loaded script: bin/sandbox

* Loaded features:

    0 enumerator.so
    1 thread.rb
    2 rational.so
    3 complex.so
    4 /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
    5 /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
    6 /usr/lib/ruby/2.3.0/unicode_normalize.rb
    7 /usr/lib/ruby/2.3.0/x86_64-linux/rbconfig.rb
    8 /usr/lib/ruby/2.3.0/rubygems/compatibility.rb
    9 /usr/lib/ruby/2.3.0/rubygems/defaults.rb
   10 /usr/lib/ruby/2.3.0/rubygems/deprecate.rb
   11 /usr/lib/ruby/2.3.0/rubygems/errors.rb
   12 /usr/lib/ruby/2.3.0/rubygems/version.rb
   13 /usr/lib/ruby/2.3.0/rubygems/requirement.rb
   14 /usr/lib/ruby/2.3.0/rubygems/platform.rb
   15 /usr/lib/ruby/2.3.0/rubygems/basic_specification.rb
   16 /usr/lib/ruby/2.3.0/rubygems/stub_specification.rb
   17 /usr/lib/ruby/2.3.0/rubygems/util/list.rb
   18 /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
   19 /usr/lib/ruby/2.3.0/rubygems/specification.rb
   20 /usr/lib/ruby/2.3.0/rubygems/exceptions.rb
   21 /usr/lib/ruby/2.3.0/rubygems/dependency.rb
   22 /usr/lib/ruby/2.3.0/rubygems/core_ext/kernel_gem.rb
   23 /usr/lib/ruby/2.3.0/monitor.rb
   24 /usr/lib/ruby/2.3.0/rubygems/core_ext/kernel_require.rb
   25 /usr/lib/ruby/2.3.0/rubygems.rb
   26 /usr/lib/ruby/2.3.0/rubygems/path_support.rb
   27 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/version.rb
   28 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/core_ext/name_error.rb
   29 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/levenshtein.rb
   30 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/jaro_winkler.rb
   31 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/spell_checkable.rb
   32 /usr/lib/ruby/2.3.0/delegate.rb
   33 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/spell_checkers/name_error_checkers/class_name_checker.rb
   34 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/spell_checkers/name_error_checkers/variable_name_checker.rb
   35 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/spell_checkers/name_error_checkers.rb
   36 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/spell_checkers/method_name_checker.rb
   37 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/spell_checkers/null_checker.rb
   38 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean/formatter.rb
   39 /usr/lib/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/lib/did_you_mean.rb
   40 /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
   41 /usr/lib/ruby/2.3.0/pathname.rb
   42 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/postit_trampoline.rb
   43 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/constants.rb
   44 /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
   45 /usr/lib/ruby/2.3.0/rubygems/user_interaction.rb
   46 /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
   47 /usr/lib/ruby/2.3.0/rubygems/config_file.rb
   48 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/rubygems_integration.rb
   49 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/current_ruby.rb
   50 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/shared_helpers.rb
   51 /usr/lib/ruby/2.3.0/fileutils.rb
   52 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/errors.rb
   53 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/environment_preserver.rb
   54 /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
   55 /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
   56 /usr/lib/ruby/2.3.0/socket.rb
   57 /usr/lib/ruby/2.3.0/timeout.rb
   58 /usr/lib/ruby/2.3.0/net/protocol.rb
   59 /usr/lib/ruby/2.3.0/uri/rfc2396_parser.rb
   60 /usr/lib/ruby/2.3.0/uri/rfc3986_parser.rb
   61 /usr/lib/ruby/2.3.0/uri/common.rb
   62 /usr/lib/ruby/2.3.0/uri/generic.rb
   63 /usr/lib/ruby/2.3.0/uri/ftp.rb
   64 /usr/lib/ruby/2.3.0/uri/http.rb
   65 /usr/lib/ruby/2.3.0/uri/https.rb
   66 /usr/lib/ruby/2.3.0/uri/ldap.rb
   67 /usr/lib/ruby/2.3.0/uri/ldaps.rb
   68 /usr/lib/ruby/2.3.0/uri/mailto.rb
   69 /usr/lib/ruby/2.3.0/uri.rb
   70 /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
   71 /usr/lib/ruby/2.3.0/net/http/exceptions.rb
   72 /usr/lib/ruby/2.3.0/net/http/header.rb
   73 /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
   74 /usr/lib/ruby/2.3.0/net/http/generic_request.rb
   75 /usr/lib/ruby/2.3.0/net/http/request.rb
   76 /usr/lib/ruby/2.3.0/net/http/requests.rb
   77 /usr/lib/ruby/2.3.0/net/http/response.rb
   78 /usr/lib/ruby/2.3.0/net/http/responses.rb
   79 /usr/lib/ruby/2.3.0/net/http/proxy_delta.rb
   80 /usr/lib/ruby/2.3.0/net/http/backward.rb
   81 /usr/lib/ruby/2.3.0/net/http.rb
   82 /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
   83 /usr/lib/ruby/2.3.0/date.rb
   84 /usr/lib/ruby/2.3.0/time.rb
   85 /usr/lib/ruby/2.3.0/rubygems/request/http_pool.rb
   86 /usr/lib/ruby/2.3.0/rubygems/request/https_pool.rb
   87 /usr/lib/ruby/2.3.0/rubygems/request/connection_pools.rb
   88 /usr/lib/ruby/2.3.0/rubygems/request.rb
   89 /usr/lib/ruby/2.3.0/cgi/core.rb
   90 /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
   91 /usr/lib/ruby/2.3.0/cgi/util.rb
   92 /usr/lib/ruby/2.3.0/cgi/cookie.rb
   93 /usr/lib/ruby/2.3.0/cgi.rb
   94 /usr/lib/ruby/2.3.0/rubygems/uri_formatter.rb
   95 /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
   96 /usr/lib/ruby/2.3.0/digest.rb
   97 /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
   98 /usr/lib/ruby/2.3.0/openssl/bn.rb
   99 /usr/lib/ruby/2.3.0/openssl/pkey.rb
  100 /usr/lib/ruby/2.3.0/openssl/cipher.rb
  101 /usr/lib/ruby/2.3.0/openssl/config.rb
  102 /usr/lib/ruby/2.3.0/openssl/digest.rb
  103 /usr/lib/ruby/2.3.0/openssl/x509.rb
  104 /usr/lib/ruby/2.3.0/openssl/buffering.rb
  105 /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
  106 /usr/lib/ruby/2.3.0/openssl/ssl.rb
  107 /usr/lib/ruby/2.3.0/openssl.rb
  108 /usr/lib/ruby/2.3.0/securerandom.rb
  109 /usr/lib/ruby/2.3.0/resolv.rb
  110 /usr/lib/ruby/2.3.0/rubygems/remote_fetcher.rb
  111 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/gem_remote_fetcher.rb
  112 /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
  113 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/plugin/api/source.rb
  114 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/plugin/api.rb
  115 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/plugin.rb
  116 /usr/lib/ruby/2.3.0/rubygems/util.rb
  117 /usr/lib/ruby/2.3.0/rubygems/source/git.rb
  118 /usr/lib/ruby/2.3.0/rubygems/source/installed.rb
  119 /usr/lib/ruby/2.3.0/rubygems/source/specific_file.rb
  120 /usr/lib/ruby/2.3.0/rubygems/source/local.rb
  121 /usr/lib/ruby/2.3.0/rubygems/source/lock.rb
  122 /usr/lib/ruby/2.3.0/rubygems/source/vendor.rb
  123 /usr/lib/ruby/2.3.0/rubygems/source.rb
  124 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/gem_helpers.rb
  125 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/match_platform.rb
  126 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/rubygems_ext.rb
  127 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/version.rb
  128 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler.rb
  129 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/settings.rb
  130 /usr/lib/ruby/2.3.0/rubygems/ext/build_error.rb
  131 /usr/lib/ruby/2.3.0/rubygems/ext/builder.rb
  132 /usr/lib/ruby/2.3.0/rubygems/ext/configure_builder.rb
  133 /usr/lib/ruby/2.3.0/tmpdir.rb
  134 /usr/lib/ruby/2.3.0/tempfile.rb
  135 /usr/lib/ruby/2.3.0/rubygems/ext/ext_conf_builder.rb
  136 /usr/lib/ruby/2.3.0/rubygems/ext/rake_builder.rb
  137 /usr/lib/ruby/2.3.0/optparse.rb
  138 /usr/lib/ruby/2.3.0/rubygems/command.rb
  139 /usr/lib/ruby/2.3.0/rubygems/ext/cmake_builder.rb
  140 /usr/lib/ruby/2.3.0/rubygems/ext.rb
  141 /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
  142 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/source.rb
  143 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/source/path.rb
  144 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/source/git.rb
  145 /usr/lib/ruby/2.3.0/rubygems/text.rb
  146 /usr/lib/ruby/2.3.0/rubygems/name_tuple.rb
  147 /usr/lib/ruby/2.3.0/rubygems/spec_fetcher.rb
  148 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/source/rubygems.rb
  149 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/lockfile_parser.rb
  150 /usr/lib/ruby/2.3.0/set.rb
  151 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/definition.rb
  152 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/dependency.rb
  153 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/ruby_dsl.rb
  154 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/dsl.rb
  155 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/source_list.rb
  156 /home/simon/git/shopify/mruby-engine/lib/mruby_engine/version.rb
  157 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/index.rb
  158 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/source/gemspec.rb
  159 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/lazy_specification.rb
  160 /usr/lib/ruby/2.3.0/tsort.rb
  161 /usr/lib/ruby/2.3.0/forwardable.rb
  162 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/spec_set.rb
  163 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/gem_version_promoter.rb
  164 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/runtime.rb
  165 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/ui.rb
  166 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/ui/silent.rb
  167 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/ui/rg_proxy.rb
  168 /usr/lib/ruby/2.3.0/rubygems/util/licenses.rb
  169 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/remote_specification.rb
  170 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/dep_proxy.rb
  171 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/gem_metadata.rb
  172 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/errors.rb
  173 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/action.rb
  174 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/add_edge_no_circular.rb
  175 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/add_vertex.rb
  176 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/detach_vertex_named.rb
  177 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/set_payload.rb
  178 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/tag.rb
  179 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/log.rb
  180 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph/vertex.rb
  181 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph.rb
  182 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/state.rb
  183 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/modules/specification_provider.rb
  184 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/delegates/resolution_state.rb
  185 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/delegates/specification_provider.rb
  186 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/resolution.rb
  187 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/resolver.rb
  188 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo/modules/ui.rb
  189 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendor/molinillo/lib/molinillo.rb
  190 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/vendored_molinillo.rb
  191 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/resolver.rb
  192 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/endpoint_specification.rb
  193 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/stub_specification.rb
  194 /home/simon/.gem/ruby/2.3.0/gems/bundler-1.13.6/lib/bundler/setup.rb
  195 /usr/lib/ruby/2.3.0/json/version.rb
  196 /usr/lib/ruby/2.3.0/ostruct.rb
  197 /usr/lib/ruby/2.3.0/json/generic_object.rb
  198 /usr/lib/ruby/2.3.0/json/common.rb
  199 /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
  200 /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
  201 /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
  202 /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
  203 /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
  204 /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
  205 /usr/lib/ruby/2.3.0/json/ext.rb
  206 /usr/lib/ruby/2.3.0/json.rb
  207 /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
  208 /home/simon/git/shopify/mruby-engine/lib/mruby_engine.rb

* Process memory map:

00400000-00401000 r-xp 00000000 08:03 948907                             /usr/bin/ruby
00600000-00601000 r--p 00000000 08:03 948907                             /usr/bin/ruby
00601000-00602000 rw-p 00001000 08:03 948907                             /usr/bin/ruby
00716000-017c3000 rw-p 00000000 00:00 0                                  [heap]
7f2eb0000000-7f2eb0021000 rw-p 00000000 00:00 0 
7f2eb0021000-7f2eb4000000 ---p 00000000 00:00 0 
7f2eb46d5000-7f2eb4b37000 r--s 00000000 08:04 1838797                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f2eb4b37000-7f2eb4d14000 r--s 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7f2eb4d14000-7f2eb4f90000 r--s 00000000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7f2eb4f90000-7f2eb4fa6000 r-xp 00000000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f2eb4fa6000-7f2eb51a5000 ---p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f2eb51a5000-7f2eb51a6000 r--p 00015000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f2eb51a6000-7f2eb51a7000 rw-p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f2eb51a7000-7f2eb51a8000 ---p 00000000 00:00 0 
7f2eb51a8000-7f2eb5da8000 rw-p 00000000 00:00 0 
7f2eb5da8000-7f2eb5daf000 r-xp 00000000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f2eb5daf000-7f2eb5faf000 ---p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f2eb5faf000-7f2eb5fb0000 r--p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f2eb5fb0000-7f2eb5fb1000 rw-p 00008000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f2eb5fb1000-7f2eb5fb2000 r-xp 00000000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f2eb5fb2000-7f2eb61b1000 ---p 00001000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f2eb61b1000-7f2eb61b2000 r--p 00000000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f2eb61b2000-7f2eb61b3000 rw-p 00001000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f2eb61b3000-7f2eb61b4000 r-xp 00000000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f2eb61b4000-7f2eb63b3000 ---p 00001000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f2eb63b3000-7f2eb63b4000 r--p 00000000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f2eb63b4000-7f2eb63b5000 rw-p 00001000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f2eb63b5000-7f2eb63b6000 r-xp 00000000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f2eb63b6000-7f2eb65b6000 ---p 00001000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f2eb65b6000-7f2eb65b7000 r--p 00001000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f2eb65b7000-7f2eb65b8000 rw-p 00002000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f2eb65b8000-7f2eb65b9000 r-xp 00000000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f2eb65b9000-7f2eb67b9000 ---p 00001000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f2eb67b9000-7f2eb67ba000 r--p 00001000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f2eb67ba000-7f2eb67bb000 rw-p 00002000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f2eb67bb000-7f2eb67c1000 r-xp 00000000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f2eb67c1000-7f2eb69c0000 ---p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f2eb69c0000-7f2eb69c1000 r--p 00005000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f2eb69c1000-7f2eb69c2000 rw-p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f2eb69c2000-7f2eb69e7000 r-xp 00000000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7f2eb69e7000-7f2eb6be6000 ---p 00025000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7f2eb6be6000-7f2eb6be7000 r--p 00024000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7f2eb6be7000-7f2eb6be8000 rw-p 00025000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7f2eb6be8000-7f2eb6bf3000 r-xp 00000000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f2eb6bf3000-7f2eb6df2000 ---p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f2eb6df2000-7f2eb6df3000 r--p 0000a000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f2eb6df3000-7f2eb6df4000 rw-p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f2eb6df4000-7f2eb6e02000 rw-p 00000000 00:00 0 
7f2eb6e02000-7f2eb6eec000 r-xp 00000000 08:04 1838797                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f2eb6eec000-7f2eb70eb000 ---p 000ea000 08:04 1838797                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f2eb70eb000-7f2eb70ed000 r--p 000e9000 08:04 1838797                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f2eb70ed000-7f2eb70ef000 rw-p 000eb000 08:04 1838797                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f2eb70ef000-7f2eb70f4000 r-xp 00000000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f2eb70f4000-7f2eb72f3000 ---p 00005000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f2eb72f3000-7f2eb72f4000 r--p 00004000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f2eb72f4000-7f2eb72f5000 rw-p 00005000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f2eb72f5000-7f2eb72f6000 r-xp 00000000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f2eb72f6000-7f2eb74f5000 ---p 00001000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f2eb74f5000-7f2eb74f6000 r--p 00000000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f2eb74f6000-7f2eb74f7000 rw-p 00001000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f2eb74f7000-7f2eb74f8000 r-xp 00000000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f2eb74f8000-7f2eb76f8000 ---p 00001000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f2eb76f8000-7f2eb76f9000 r--p 00001000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f2eb76f9000-7f2eb76fa000 rw-p 00002000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f2eb76fa000-7f2eb76fd000 r-xp 00000000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f2eb76fd000-7f2eb78fc000 ---p 00003000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f2eb78fc000-7f2eb78fd000 r--p 00002000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f2eb78fd000-7f2eb78fe000 rw-p 00003000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f2eb78fe000-7f2eb7b4c000 r-xp 00000000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f2eb7b4c000-7f2eb7d4b000 ---p 0024e000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f2eb7d4b000-7f2eb7d67000 r--p 0024d000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f2eb7d67000-7f2eb7d73000 rw-p 00269000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f2eb7d73000-7f2eb7d76000 rw-p 00000000 00:00 0 
7f2eb7d76000-7f2eb7ddd000 r-xp 00000000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f2eb7ddd000-7f2eb7fdc000 ---p 00067000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f2eb7fdc000-7f2eb7fe0000 r--p 00066000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f2eb7fe0000-7f2eb7fe7000 rw-p 0006a000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f2eb7fe7000-7f2eb8036000 r-xp 00000000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f2eb8036000-7f2eb8236000 ---p 0004f000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f2eb8236000-7f2eb8238000 r--p 0004f000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f2eb8238000-7f2eb823a000 rw-p 00051000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f2eb823a000-7f2eb823b000 rw-p 00000000 00:00 0 
7f2eb823b000-7f2eb823c000 r-xp 00000000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f2eb823c000-7f2eb843c000 ---p 00001000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f2eb843c000-7f2eb843d000 r--p 00001000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f2eb843d000-7f2eb843e000 rw-p 00002000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f2eb843e000-7f2eb846d000 r-xp 00000000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f2eb846d000-7f2eb866d000 ---p 0002f000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f2eb866d000-7f2eb866e000 r--p 0002f000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f2eb866e000-7f2eb866f000 rw-p 00030000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f2eb866f000-7f2eb8670000 rw-p 00000000 00:00 0 
7f2eb8670000-7f2eb8673000 r-xp 00000000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f2eb8673000-7f2eb8872000 ---p 00003000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f2eb8872000-7f2eb8873000 r--p 00002000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f2eb8873000-7f2eb8874000 rw-p 00003000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f2eb8874000-7f2eb8889000 r-xp 00000000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f2eb8889000-7f2eb8a88000 ---p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f2eb8a88000-7f2eb8a89000 r--p 00014000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f2eb8a89000-7f2eb8a8a000 rw-p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f2eb8a8a000-7f2eb8a97000 r-xp 00000000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f2eb8a97000-7f2eb8c96000 ---p 0000d000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f2eb8c96000-7f2eb8c97000 r--p 0000c000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f2eb8c97000-7f2eb8c98000 rw-p 0000d000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f2eb8c98000-7f2eb8c9a000 r-xp 00000000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f2eb8c9a000-7f2eb8e99000 ---p 00002000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f2eb8e99000-7f2eb8e9a000 r--p 00001000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f2eb8e9a000-7f2eb8e9b000 rw-p 00002000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f2eb8e9b000-7f2eb8ec5000 r-xp 00000000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f2eb8ec5000-7f2eb90c4000 ---p 0002a000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f2eb90c4000-7f2eb90c5000 r--p 00029000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f2eb90c5000-7f2eb90c6000 rw-p 0002a000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f2eb90c6000-7f2eb90cc000 r-xp 00000000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f2eb90cc000-7f2eb92cb000 ---p 00006000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f2eb92cb000-7f2eb92cc000 r--p 00005000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f2eb92cc000-7f2eb92cd000 rw-p 00006000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f2eb92cd000-7f2eb92d1000 r-xp 00000000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f2eb92d1000-7f2eb94d0000 ---p 00004000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f2eb94d0000-7f2eb94d1000 r--p 00003000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f2eb94d1000-7f2eb94d2000 rw-p 00004000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f2eb94d2000-7f2eb94d8000 r-xp 00000000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f2eb94d8000-7f2eb96d7000 ---p 00006000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f2eb96d7000-7f2eb96d8000 r--p 00005000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f2eb96d8000-7f2eb96d9000 rw-p 00006000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f2eb96d9000-7f2eb96e0000 r-xp 00000000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f2eb96e0000-7f2eb98df000 ---p 00007000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f2eb98df000-7f2eb98e0000 r--p 00006000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f2eb98e0000-7f2eb98e1000 rw-p 00007000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f2eb98e1000-7f2eb98e3000 r-xp 00000000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f2eb98e3000-7f2eb9ae3000 ---p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f2eb9ae3000-7f2eb9ae4000 r--p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f2eb9ae4000-7f2eb9ae5000 rw-p 00003000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f2eb9ae5000-7f2eb9ae7000 r-xp 00000000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f2eb9ae7000-7f2eb9ce6000 ---p 00002000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f2eb9ce6000-7f2eb9ce7000 r--p 00001000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f2eb9ce7000-7f2eb9ce8000 rw-p 00002000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f2eb9ce8000-7f2eb9de9000 rw-p 00000000 00:00 0 
7f2eb9de9000-7f2eb9eec000 r-xp 00000000 08:03 935421                     /usr/lib/libm-2.24.so
7f2eb9eec000-7f2eba0eb000 ---p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7f2eba0eb000-7f2eba0ec000 r--p 00102000 08:03 935421                     /usr/lib/libm-2.24.so
7f2eba0ec000-7f2eba0ed000 rw-p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7f2eba0ed000-7f2eba0f5000 r-xp 00000000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f2eba0f5000-7f2eba2f5000 ---p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f2eba2f5000-7f2eba2f6000 r--p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f2eba2f6000-7f2eba2f7000 rw-p 00009000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f2eba2f7000-7f2eba325000 rw-p 00000000 00:00 0 
7f2eba325000-7f2eba327000 r-xp 00000000 08:03 935420                     /usr/lib/libdl-2.24.so
7f2eba327000-7f2eba527000 ---p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7f2eba527000-7f2eba528000 r--p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7f2eba528000-7f2eba529000 rw-p 00003000 08:03 935420                     /usr/lib/libdl-2.24.so
7f2eba529000-7f2eba5bb000 r-xp 00000000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f2eba5bb000-7f2eba7ba000 ---p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f2eba7ba000-7f2eba7bb000 r--p 00091000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f2eba7bb000-7f2eba7bc000 rw-p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f2eba7bc000-7f2eba7d4000 r-xp 00000000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f2eba7d4000-7f2eba9d3000 ---p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f2eba9d3000-7f2eba9d4000 r--p 00017000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f2eba9d4000-7f2eba9d5000 rw-p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f2eba9d5000-7f2eba9d9000 rw-p 00000000 00:00 0 
7f2eba9d9000-7f2ebab6e000 r-xp 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7f2ebab6e000-7f2ebad6d000 ---p 00195000 08:03 934952                     /usr/lib/libc-2.24.so
7f2ebad6d000-7f2ebad71000 r--p 00194000 08:03 934952                     /usr/lib/libc-2.24.so
7f2ebad71000-7f2ebad73000 rw-p 00198000 08:03 934952                     /usr/lib/libc-2.24.so
7f2ebad73000-7f2ebad77000 rw-p 00000000 00:00 0 
7f2ebad77000-7f2ebafeb000 r-xp 00000000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7f2ebafeb000-7f2ebb1ea000 ---p 00274000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7f2ebb1ea000-7f2ebb1f0000 r--p 00273000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7f2ebb1f0000-7f2ebb1f3000 rw-p 00279000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7f2ebb1f3000-7f2ebb204000 rw-p 00000000 00:00 0 
7f2ebb204000-7f2ebb227000 r-xp 00000000 08:03 934951                     /usr/lib/ld-2.24.so
7f2ebb275000-7f2ebb40d000 r--p 00000000 08:03 934978                     /usr/lib/locale/locale-archive
7f2ebb40d000-7f2ebb413000 rw-p 00000000 00:00 0 
7f2ebb420000-7f2ebb422000 r--s 00000000 08:03 948907                     /usr/bin/ruby
7f2ebb422000-7f2ebb423000 ---p 00000000 00:00 0 
7f2ebb423000-7f2ebb426000 rw-p 00000000 00:00 0 
7f2ebb426000-7f2ebb427000 r--p 00022000 08:03 934951                     /usr/lib/ld-2.24.so
7f2ebb427000-7f2ebb428000 rw-p 00023000 08:03 934951                     /usr/lib/ld-2.24.so
7f2ebb428000-7f2ebb429000 rw-p 00000000 00:00 0 
7ffcdc165000-7ffcdc964000 rw-p 00000000 00:00 0                          [stack]
7ffcdc9c9000-7ffcdc9cb000 r--p 00000000 00:00 0                          [vvar]
7ffcdc9cb000-7ffcdc9cd000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


[NOTE]
You may have encountered a bug in the Ruby interpreter or extension libraries.
Bug reports are welcome.
For details: http://www.ruby-lang.org/bugreport.html

[1]    17962 abort (core dumped)  bin/sandbox crashes/symbol_new.mrb
```

GDB
```
$ gdb attach 17388
GNU gdb (GDB) 7.12
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
attach: No such file or directory.
Attaching to process 17388
Reading symbols from /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/build/host/bin/mirb...done.
Reading symbols from /usr/lib/libm.so.6...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libreadline.so.7...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libncursesw.so.6...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libc.so.6...(no debugging symbols found)...done.
Reading symbols from /lib64/ld-linux-x86-64.so.2...(no debugging symbols found)...done.
0x00007fa156930131 in pselect () from /usr/lib/libc.so.6
(gdb) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
sym_inspect (mrb=0x1817010, sym=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/symbol.c:411
411	  if (!symname_p(name) || strlen(name) != (size_t)len) {
(gdb) bt
#0  sym_inspect (mrb=0x1817010, sym=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/symbol.c:411
#1  0x0000000000410fff in mrb_funcall_with_block (mrb=mrb@entry=0x1817010, self=..., self@entry=..., mid=<optimized out>, mid@entry=39, 
    argc=<optimized out>, argc@entry=0, argv=argv@entry=0x7fff473c8ea0, blk=..., blk@entry=...)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
#2  0x0000000000411558 in mrb_funcall_with_block (mrb=mrb@entry=0x1817010, self=..., mid=39, argc=argc@entry=0, argv=argv@entry=0x7fff473c8ea0, blk=..., 
    blk@entry=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:334
#3  0x00000000004115bc in mrb_funcall_argv (mrb=mrb@entry=0x1817010, self=..., self@entry=..., mid=<optimized out>, argc=argc@entry=0, 
    argv=argv@entry=0x7fff473c8ea0) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
#4  0x0000000000411810 in mrb_funcall (mrb=mrb@entry=0x1817010, self=self@entry=..., name=name@entry=0x48aae2 "inspect", argc=argc@entry=0)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:319
#5  0x0000000000403132 in p (mrb=0x1817010, obj=..., prompt=1)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:92
#6  0x0000000000402e29 in main (argc=<optimized out>, argv=<optimized out>)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:564
(gdb)
```

## Attachments
No attachments
