# Invalid handling of zero-length heredoc identifiers leads to infinite loop in the sandbox

## Report Details
- **Report ID**: 187305
- **URL**: https://hackerone.com/reports/187305
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-01T11:47:43.778Z
- **Disclosed**: 2017-01-12T00:37:21.368Z

## Reporter
- **Username**: dkasak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Introduction
============

Certain invalid Ruby programs (which should normally raise a syntax error) are able to cause an infinite loop in MRuby's parser which makes the mruby-engine sandbox (and consequently the MRI process it is running in) unresponsive to SIGTERM. The process begins looping forever and has to be terminated using SIGABRT or SIGKILL. The bug is caused by an improper handling of heredocs with a zero-length identifier.

Proof of concept
================

infinite_heredoc.rb:
--------------------

    <<''.a begin

1. Save the above code as `infinite_heredoc.rb`.
2. Run either:
   a) `mruby infinite_heredoc.rb`
   b) `sandbox infinite_heredoc.rb`
3. Both cause an infinite loop, but b) also leaves the process unresponsive to SIGTERM.

Discussion
==========

Everything below assumes the latest master of the mruby repository as of Dec 01th, which is commit `2cca9d368815e9c83a7489c40d69937d68cb43a2`.

The `<<''`˙in the above POC code is parsed as a heredoc with an empty identifier. The rest of the POC is needed to bring the parser in a state where it is:

   1. Continually searching for the identifier.
   2. Erroneously thinking it found it, thereby signalling an end of the heredoc by pushing a `tHEREDOC_END` token.
   3. This token is then invalid for the current parser state, which makes it push an error token.
   4. Finally, while processing the error, the parser eventually calls `parse_string` again, which brings the process back to step 1, resulting in an infinite loop.

A variation of the bug, using `do` instead of `begin`:

infinite_heredoc_variation.rb:
------------------------------

    <<''.a do

An excerpt from the parser's debug output, demonstrating the above:

    Reading a token: Next token is token tHEREDOC_END ()
    Error: discarding token tHEREDOC_END ()
    Error: popping token error ()
    Stack now 0 2 81 370 586 257 8 199
    Shifting token error ()
    Entering state 271
    Reading a token: Next token is token tHEREDOC_END ()
    Error: discarding token tHEREDOC_END ()
    [...]

It is interesting to study what output MRI's parser gives for the same input:

    infinite_heredoc.rb:1: can't find string "" anywhere before EOF
    infinite_heredoc.rb:1: syntax error, unexpected end-of-input, expecting tSTRING_CONTENT or tSTRING_DBEG or tSTRING_DVAR or tSTRING_END
    <<''.a begin
        ^

For a heredoc with a non-zero name, both MRuby and MRI produce similar outputs:

heredoc_valid_name.rb
---------------------

    <<'h'.a begin

MRuby output
------------

    heredoc_valid_name.rb:3:0: can't find heredoc delimiter "h" anywhere before EOF
    heredoc_valid_name.rb:3:0: syntax error, unexpected $end

MRI output
----------

    heredoc_valid_name.rb:1: can't find string "h" anywhere before EOF
    heredoc_valid_name.rb:1: syntax error, unexpected end-of-input, expecting tSTRING_CONTENT or tSTRING_DBEG or tSTRING_DVAR or tSTRING_END
    <<'h'.a begin
        ^

Solution
========

The problematic code is located `parse.y`, function `parse_string`, starting at line 3956:

    if ((len-1 == hinf->term_len) && (strncmp(s, hinf->term, len-1) == 0)) {
        return tHEREDOC_END;
    }

The above code checks whether the current heredoc identifier can be matched and, if so, signals the end of the heredoc by returning a `tHEREDOC_END` token. The code is incorrect in the case when the length parameter is 0 due to the use of `strncmp` since it will return 0 even when the input strings are different (as is the case here, where `s` is `"\n"` and `hinf->term` is `""`). Therefore, the check incorrectly succeeds when it shouldn't.

A possible fix is to check whether `hinf->term_len != 0` in addition to the present checks so zero-length heredoc identifiers are invalidated.

empty_heredoc_identifier.patch
------------------------------

    diff --git a/mrbgems/mruby-compiler/core/parse.y b/mrbgems/mruby-compiler/core/parse.y
    index bf893fb..85150fc 100644
    --- a/mrbgems/mruby-compiler/core/parse.y
    +++ b/mrbgems/mruby-compiler/core/parse.y
    @@ -3953,7 +3953,7 @@ parse_string(parser_state *p)
                --len;
            }
            }
    -        if ((len-1 == hinf->term_len) && (strncmp(s, hinf->term, len-1) == 0)) {
    +        if ((len-1 == hinf->term_len) && (strncmp(s, hinf->term, len-1) == 0) && (hinf->term_len != 0)) {
            return tHEREDOC_END;
            }
        }

With the provided patch, MRuby correctly terminates with the POC and issues an error message very similar to the one in MRI:

    infinite_heredoc.rb:3:0: can't find heredoc delimiter "" anywhere before EOF
    infinite_heredoc.rb:3:0: syntax error, unexpected $end

In addition, all the tests pass.

--
Denis Kasak
Damir Jelić

## Attachments
- infinite_heredoc.rb
- infinite_heredoc_variation.rb
- heredoc_valid_name.rb
- empty_heredoc_identifier.patch
