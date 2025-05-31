# Crash: mrb_any_to_s can't handle NilClass, Symbol and Fixnum

## Report Details
- **Report ID**: 185794
- **URL**: https://hackerone.com/reports/185794
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-27T11:38:57.426Z
- **Disclosed**: 2016-12-16T22:20:59.203Z

## Reporter
- **Username**: brakhane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
When using `boxing_word.h` (haven't tested other boxing methods yet), `mrb_any_to_s` is unable to handle `NilClass`, `Symbol` and `Fixnum`. This can be achieved by just deleting `:to_s` from the class and let `mrb_any_to_s` crash.

I tried to come up with a fix but I'm not 100% sure where this should be fixed. The boxing schemas all work slightly different so fixing `mrb_any_to_s` in a way that it respects the boxing schema is not my preferred choice (as implementation details shouldn't bleed through to that method). I guess it's either the right call to make `mrb_any_to_s` always safe or pull part of the functionality into the specific boxing header.

#PoC
Works with `Symbol` and `Fixnum` as well:
```
NilClass.remove_method :to_s
nil.to_s
```

#Traces

Sandbox:
```
bin/sandbox_extract crashes/nil_remove_to_s.mrb
bin/sandbox_extract:20: [BUG] Segmentation fault at 0x00000000000018
ruby 2.3.3p222 (2016-11-21 revision 56859) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:000368 EVAL   bin/sandbox_extract:20 [FINISH]
c:0001 p:0000 s:0002 E:0021f0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox_extract:20:in `<main>'
bin/sandbox_extract:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007fb466086787 RBP: 0x00007fb464c15100 RSP: 0x00007fb464c0bab0
 RAX: 0x00007fb464c15100 RBX: 0x00007fb464c0d4e0 RCX: 0x000000000000003a
 RDX: 0x0000000000000110 RDI: 0x00007fb464c4ef3a RSI: 0x00007fb46610ca2e
  R8: 0x0000000000000003  R9: 0x0000000000000000 R10: 0x0000000000000262
 R11: 0x00007fb466090d40 R12: 0x0000000000000000 R13: 0x00007fb464c150b8
 R14: 0x00007fb464c0d4e0 R15: 0x00007fb464c18220 EFL: 0x0000000000010206

-- C level backtrace information -------------------------------------------
/usr/lib/libruby.so.2.3 [0x7fb46a16d455]
/usr/lib/libruby.so.2.3 [0x7fb46a16d68c]
/usr/lib/libruby.so.2.3 [0x7fb46a047e34]
/usr/lib/libruby.so.2.3 [0x7fb46a0f96ce]
/usr/lib/libc.so.6 [0x7fb469c6d0b0]
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_any_to_s+0x67) [0x7fb466086787] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/object.c:442
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x762) [0x7fb466097952] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7fb46609d627] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7fb46607c8c3] ../../../../ext/mruby_engine/eval_monitored.c:68
/usr/lib/libpthread.so.0(start_thread+0xc4) [0x7fb469a24454]
/usr/lib/libc.so.6(clone+0x5f) [0x7fb469d227df]

-- Other runtime information -----------------------------------------------

* Loaded script: bin/sandbox_extract

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
00674000-01729000 rw-p 00000000 00:00 0                                  [heap]
7fb45f935000-7fb45fd84000 r--s 00000000 08:04 1838957                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fb45fd84000-7fb460000000 r--s 00000000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fb460000000-7fb460021000 rw-p 00000000 00:00 0 
7fb460021000-7fb464000000 ---p 00000000 00:00 0 
7fb464018000-7fb4641f5000 r--s 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7fb4641f5000-7fb46420b000 r-xp 00000000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fb46420b000-7fb46440a000 ---p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fb46440a000-7fb46440b000 r--p 00015000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fb46440b000-7fb46440c000 rw-p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fb46440c000-7fb46440d000 ---p 00000000 00:00 0 
7fb46440d000-7fb46500d000 rw-p 00000000 00:00 0 
7fb46500d000-7fb465014000 r-xp 00000000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fb465014000-7fb465214000 ---p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fb465214000-7fb465215000 r--p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fb465215000-7fb465216000 rw-p 00008000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fb465216000-7fb465217000 r-xp 00000000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fb465217000-7fb465416000 ---p 00001000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fb465416000-7fb465417000 r--p 00000000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fb465417000-7fb465418000 rw-p 00001000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fb465418000-7fb465419000 r-xp 00000000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fb465419000-7fb465618000 ---p 00001000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fb465618000-7fb465619000 r--p 00000000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fb465619000-7fb46561a000 rw-p 00001000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fb46561a000-7fb46561b000 r-xp 00000000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fb46561b000-7fb46581b000 ---p 00001000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fb46581b000-7fb46581c000 r--p 00001000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fb46581c000-7fb46581d000 rw-p 00002000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fb46581d000-7fb46581e000 r-xp 00000000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fb46581e000-7fb465a1e000 ---p 00001000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fb465a1e000-7fb465a1f000 r--p 00001000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fb465a1f000-7fb465a20000 rw-p 00002000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fb465a20000-7fb465a26000 r-xp 00000000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fb465a26000-7fb465c25000 ---p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fb465c25000-7fb465c26000 r--p 00005000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fb465c26000-7fb465c27000 rw-p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fb465c27000-7fb465c4c000 r-xp 00000000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fb465c4c000-7fb465e4b000 ---p 00025000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fb465e4b000-7fb465e4c000 r--p 00024000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fb465e4c000-7fb465e4d000 rw-p 00025000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fb465e4d000-7fb465e58000 r-xp 00000000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fb465e58000-7fb466057000 ---p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fb466057000-7fb466058000 r--p 0000a000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fb466058000-7fb466059000 rw-p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fb466059000-7fb466067000 rw-p 00000000 00:00 0 
7fb466067000-7fb46614d000 r-xp 00000000 08:04 1838957                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fb46614d000-7fb46634c000 ---p 000e6000 08:04 1838957                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fb46634c000-7fb46634e000 r--p 000e5000 08:04 1838957                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fb46634e000-7fb466350000 rw-p 000e7000 08:04 1838957                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fb466350000-7fb466355000 r-xp 00000000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fb466355000-7fb466554000 ---p 00005000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fb466554000-7fb466555000 r--p 00004000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fb466555000-7fb466556000 rw-p 00005000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fb466556000-7fb466557000 r-xp 00000000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fb466557000-7fb466756000 ---p 00001000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fb466756000-7fb466757000 r--p 00000000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fb466757000-7fb466758000 rw-p 00001000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fb466758000-7fb466759000 r-xp 00000000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fb466759000-7fb466959000 ---p 00001000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fb466959000-7fb46695a000 r--p 00001000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fb46695a000-7fb46695b000 rw-p 00002000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fb46695b000-7fb46695e000 r-xp 00000000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fb46695e000-7fb466b5d000 ---p 00003000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fb466b5d000-7fb466b5e000 r--p 00002000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fb466b5e000-7fb466b5f000 rw-p 00003000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fb466b5f000-7fb466dad000 r-xp 00000000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fb466dad000-7fb466fac000 ---p 0024e000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fb466fac000-7fb466fc8000 r--p 0024d000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fb466fc8000-7fb466fd4000 rw-p 00269000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fb466fd4000-7fb466fd7000 rw-p 00000000 00:00 0 
7fb466fd7000-7fb46703e000 r-xp 00000000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fb46703e000-7fb46723d000 ---p 00067000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fb46723d000-7fb467241000 r--p 00066000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fb467241000-7fb467248000 rw-p 0006a000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fb467248000-7fb467297000 r-xp 00000000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fb467297000-7fb467497000 ---p 0004f000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fb467497000-7fb467499000 r--p 0004f000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fb467499000-7fb46749b000 rw-p 00051000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fb46749b000-7fb46749c000 rw-p 00000000 00:00 0 
7fb46749c000-7fb46749d000 r-xp 00000000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fb46749d000-7fb46769d000 ---p 00001000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fb46769d000-7fb46769e000 r--p 00001000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fb46769e000-7fb46769f000 rw-p 00002000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fb46769f000-7fb4676ce000 r-xp 00000000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fb4676ce000-7fb4678ce000 ---p 0002f000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fb4678ce000-7fb4678cf000 r--p 0002f000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fb4678cf000-7fb4678d0000 rw-p 00030000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fb4678d0000-7fb4678d1000 rw-p 00000000 00:00 0 
7fb4678d1000-7fb4678d4000 r-xp 00000000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fb4678d4000-7fb467ad3000 ---p 00003000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fb467ad3000-7fb467ad4000 r--p 00002000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fb467ad4000-7fb467ad5000 rw-p 00003000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fb467ad5000-7fb467aea000 r-xp 00000000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fb467aea000-7fb467ce9000 ---p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fb467ce9000-7fb467cea000 r--p 00014000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fb467cea000-7fb467ceb000 rw-p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fb467ceb000-7fb467cf8000 r-xp 00000000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fb467cf8000-7fb467ef7000 ---p 0000d000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fb467ef7000-7fb467ef8000 r--p 0000c000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fb467ef8000-7fb467ef9000 rw-p 0000d000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fb467ef9000-7fb467efb000 r-xp 00000000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fb467efb000-7fb4680fa000 ---p 00002000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fb4680fa000-7fb4680fb000 r--p 00001000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fb4680fb000-7fb4680fc000 rw-p 00002000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fb4680fc000-7fb468126000 r-xp 00000000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fb468126000-7fb468325000 ---p 0002a000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fb468325000-7fb468326000 r--p 00029000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fb468326000-7fb468327000 rw-p 0002a000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fb468327000-7fb46832d000 r-xp 00000000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fb46832d000-7fb46852c000 ---p 00006000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fb46852c000-7fb46852d000 r--p 00005000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fb46852d000-7fb46852e000 rw-p 00006000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fb46852e000-7fb468532000 r-xp 00000000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fb468532000-7fb468731000 ---p 00004000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fb468731000-7fb468732000 r--p 00003000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fb468732000-7fb468733000 rw-p 00004000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fb468733000-7fb468739000 r-xp 00000000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fb468739000-7fb468938000 ---p 00006000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fb468938000-7fb468939000 r--p 00005000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fb468939000-7fb46893a000 rw-p 00006000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fb46893a000-7fb468941000 r-xp 00000000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fb468941000-7fb468b40000 ---p 00007000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fb468b40000-7fb468b41000 r--p 00006000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fb468b41000-7fb468b42000 rw-p 00007000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fb468b42000-7fb468b44000 r-xp 00000000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fb468b44000-7fb468d44000 ---p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fb468d44000-7fb468d45000 r--p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fb468d45000-7fb468d46000 rw-p 00003000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fb468d46000-7fb468d48000 r-xp 00000000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fb468d48000-7fb468f47000 ---p 00002000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fb468f47000-7fb468f48000 r--p 00001000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fb468f48000-7fb468f49000 rw-p 00002000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fb468f49000-7fb46904a000 rw-p 00000000 00:00 0 
7fb46904a000-7fb46914d000 r-xp 00000000 08:03 935421                     /usr/lib/libm-2.24.so
7fb46914d000-7fb46934c000 ---p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7fb46934c000-7fb46934d000 r--p 00102000 08:03 935421                     /usr/lib/libm-2.24.so
7fb46934d000-7fb46934e000 rw-p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7fb46934e000-7fb469356000 r-xp 00000000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fb469356000-7fb469556000 ---p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fb469556000-7fb469557000 r--p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fb469557000-7fb469558000 rw-p 00009000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fb469558000-7fb469586000 rw-p 00000000 00:00 0 
7fb469586000-7fb469588000 r-xp 00000000 08:03 935420                     /usr/lib/libdl-2.24.so
7fb469588000-7fb469788000 ---p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7fb469788000-7fb469789000 r--p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7fb469789000-7fb46978a000 rw-p 00003000 08:03 935420                     /usr/lib/libdl-2.24.so
7fb46978a000-7fb46981c000 r-xp 00000000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fb46981c000-7fb469a1b000 ---p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fb469a1b000-7fb469a1c000 r--p 00091000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fb469a1c000-7fb469a1d000 rw-p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fb469a1d000-7fb469a35000 r-xp 00000000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fb469a35000-7fb469c34000 ---p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fb469c34000-7fb469c35000 r--p 00017000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fb469c35000-7fb469c36000 rw-p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fb469c36000-7fb469c3a000 rw-p 00000000 00:00 0 
7fb469c3a000-7fb469dcf000 r-xp 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7fb469dcf000-7fb469fce000 ---p 00195000 08:03 934952                     /usr/lib/libc-2.24.so
7fb469fce000-7fb469fd2000 r--p 00194000 08:03 934952                     /usr/lib/libc-2.24.so
7fb469fd2000-7fb469fd4000 rw-p 00198000 08:03 934952                     /usr/lib/libc-2.24.so
7fb469fd4000-7fb469fd8000 rw-p 00000000 00:00 0 
7fb469fd8000-7fb46a24c000 r-xp 00000000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fb46a24c000-7fb46a44b000 ---p 00274000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fb46a44b000-7fb46a451000 r--p 00273000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fb46a451000-7fb46a454000 rw-p 00279000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fb46a454000-7fb46a465000 rw-p 00000000 00:00 0 
7fb46a465000-7fb46a488000 r-xp 00000000 08:03 934951                     /usr/lib/ld-2.24.so
7fb46a4d6000-7fb46a66e000 r--p 00000000 08:03 934978                     /usr/lib/locale/locale-archive
7fb46a66e000-7fb46a674000 rw-p 00000000 00:00 0 
7fb46a681000-7fb46a683000 r--s 00000000 08:03 948907                     /usr/bin/ruby
7fb46a683000-7fb46a684000 ---p 00000000 00:00 0 
7fb46a684000-7fb46a687000 rw-p 00000000 00:00 0 
7fb46a687000-7fb46a688000 r--p 00022000 08:03 934951                     /usr/lib/ld-2.24.so
7fb46a688000-7fb46a689000 rw-p 00023000 08:03 934951                     /usr/lib/ld-2.24.so
7fb46a689000-7fb46a68a000 rw-p 00000000 00:00 0 
7ffecd510000-7ffecdd0f000 rw-p 00000000 00:00 0                          [stack]
7ffecdd45000-7ffecdd47000 r--p 00000000 00:00 0                          [vvar]
7ffecdd47000-7ffecdd49000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


[NOTE]
You may have encountered a bug in the Ruby interpreter or extension libraries.
Bug reports are welcome.
For details: http://www.ruby-lang.org/bugreport.html

[1]    956 abort (core dumped)  bin/sandbox_extract crashes/nil_remove_to_s.mrb
```

GDB:
```
$ gdb attach 730
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
Attaching to process 730
[New LWP 731]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
0x00007ffb3f9414b8 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
(gdb) c
Continuing.
[New Thread 0x7ffb3ab23700 (LWP 823)]

Thread 3 "ruby" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffb3ab23700 (LWP 823)]
mrb_any_to_s (mrb=0x7ffb3ab244e0, obj=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/object.c:443
443	  mrb_str_concat(mrb, str, mrb_ptr_to_str(mrb, mrb_cptr(obj)));
(gdb) bt
#0  mrb_any_to_s (mrb=0x7ffb3ab244e0, obj=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/object.c:443
#1  0x00007ffb3bfae952 in mrb_vm_exec (mrb=mrb@entry=0x7ffb3ab244e0, proc=<optimized out>, proc@entry=0x7ffb3ab2c130, pc=<optimized out>)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#2  0x00007ffb3bfb4627 in mrb_vm_run (mrb=0x7ffb3ab244e0, proc=0x7ffb3ab2c130, self=..., stack_keep=stack_keep@entry=0)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#3  0x00007ffb3bf938c3 in mruby_engine_monitored_eval (data=0x7ffb3ab243e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
#4  0x00007ffb3f93b454 in start_thread () from /usr/lib/libpthread.so.0
#5  0x00007ffb3fc397df in clone () from /usr/lib/libc.so.6
(gdb) info registers
rax            0x7ffb3ab2c100	140716998312192
rbx            0x7ffb3ab244e0	140716998280416
rcx            0x3a	58
rdx            0x110	272
rsi            0x7ffb3c023a2e	140717020297774
rdi            0x7ffb3ab65f3a	140716998549306
rbp            0x7ffb3ab2c100	0x7ffb3ab2c100
rsp            0x7ffb3ab22ab0	0x7ffb3ab22ab0
r8             0x3	3
r9             0x0	0
r10            0x262	610
r11            0x7ffb3bfa7d40	140717019790656
r12            0x0	0
r13            0x7ffb3ab2c0b8	140716998312120
r14            0x7ffb3ab244e0	140716998280416
r15            0x7ffb3ab2f220	140716998324768
rip            0x7ffb3bf9d787	0x7ffb3bf9d787 <mrb_any_to_s+103>
eflags         0x10206	[ PF IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
(gdb) quit
A debugging session is active.

	Inferior 1 [process 730] will be detached.

Quit anyway? (y or n) y
Detaching from program: /usr/bin/ruby, process 730
```

## Attachments
No attachments
