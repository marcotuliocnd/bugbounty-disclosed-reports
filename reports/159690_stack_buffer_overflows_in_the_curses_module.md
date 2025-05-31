# stack buffer overflows in the curses module

## Report Details
- **Report ID**: 159690
- **URL**: https://hackerone.com/reports/159690
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-16T09:19:44.939Z
- **Disclosed**: 2019-11-12T09:01:58.772Z

## Reporter
- **Username**: tehybel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I found two stack buffer overflows in the curses module. These vulnerabilities have been reported to the PSRT and were fixed here:

https://hg.python.org/cpython/rev/d5f6bc45b376
https://hg.python.org/cpython/rev/85b35300f200

Below are copies of the mails I sent to the PSRT. They describe the vulnerabilities in detail.

First mail:

I found a straightforward stack buffer overflow in the Modules/\_cursesmodule.c
file. The module implements the python function window.getstr() via the C
function PyCursesWindow_GetStr. This function calls on to the curses library's
wgetnstr function.

If we specify a single integer argument to getstr, we hit these lines:

    static PyObject *
    PyCursesWindow_GetStr(PyCursesWindowObject *self, PyObject *args)
    {
        ...
        char rtn[1024]; /* This should be big enough.. I hope */
        ...
        switch (PyTuple_Size(args)) {
        ...
        case 1:
            if (!PyArg_ParseTuple(args,"i;n", &n))
                return NULL;
            Py_BEGIN_ALLOW_THREADS
            rtn2 = wgetnstr(self->win, rtn, Py_MIN(n, 1023));
            ...
        }
        ...
    }

As we can see, the wgetnstr function is called. It will read input into the
stack buffer "rtn". We use wgetnstr rather than wgetstr to prevent a buffer
overflow. As maximum length we use Py_MIN(n, 1023). However if we set n to be a
negative integer, wgetnstr will be passed a negative length.

What does the curses module do, then? On my (Linux, ncurses) system it simply
does no length checking. So we can read as many bytes as we want into the
fixed-size stack buffer rtn.

Here's a proof-of-concept script to reproduce this:

--- begin script ---

import curses

curses.initscr()
w = curses.newwin(80, 80)
w.getstr(-1)

--- end script ---

Here's the result of running it and entering over 1024 'A's:

$ python3 -c 'print("A"*1100)' | python3 ./poc4.py
*** stack smashing detected ***: python3 terminated
zsh: segmentation fault (core dumped)  python3 ./poc4.py


This is clearly exploitable when combined with an info leak that lets us know
the stack canary.

This vulnerability should probably be fixed by making "n" unsigned, or by
confirming that it is non-negative. (Note that this also needs to be fixed for
other cases in the switch, like when we input three arguments rather than one.)


Some more details about my setup:

    curses version: libncurses (/usr/lib/libncursesw.so.6.0) (ncurses 6.0.20150808)
    $ python3 -V
    Python 3.5.2



Second mail, after the first vulnerability was fixed:

I just realized that there is a similar vulnerability in the PyCursesWindow_InStr function. There we also need to confirm that n is nonnegative. Otherwise a stack buffer overflow is possible. There's a reproducing script below.
--- begin script ---

import curses

curses.initscr()
w = curses.newwin(2048, 2048)
s = w.instr(-1)

--- end script ---


## Attachments
No attachments
