# Canonical Snapcraft vulnerable to remote code execution under certain conditions

## Report Details
- **Report ID**: 1073202
- **URL**: https://hackerone.com/reports/1073202
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-07T03:27:00.921Z
- **Disclosed**: 2021-07-23T03:13:22.019Z

## Reporter
- **Username**: itszn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Preface: I apologize for previously submitting this bug to hacker1 before it was fully addressed by the Ubuntu Security Team

I have reported this issue to the Ubuntu Security team and it has been fixed:
CVE-2020-27348
Bug link: https://bugs.launchpad.net/snapcraft/+bug/1901572
Ubuntu Security Team Disclosure: https://discourse.ubuntu.com/t/usn-4661-1-snapcraft-vulnerability/19640
Commit fixing the issue in snapcraft: https://github.com/snapcore/snapcraft/commit/a0ceca9d531a34c979251030ed67b5fa2abfdd9a

I waited an month before submitting this report (which has additional non-public exploitation details) to allow users to update. See **Example Attack Scenarios** for ways this bug could have been used.

## Background:
Snapcraft is a Ubuntu project which allows applications to be bundled in containers, installed easily by users, and allow automatic updates of individual packages. Snapcraft is becoming more and more the main way to install packages on Ubuntu systems (including server). For example installing Chromium on Ubuntu 20+ will now install the Snapcraft package instead of the normal apt package. Many users/servers may be using snapcraft installed packages without knowing it. Additionlly Ubuntu recommends installing packages using Snapcraft and even prompts users when they try to run non-installed applications:

```
itszn@ubuntu:~$ docker

Command 'docker' not found, but can be installed with:

sudo snap install docker
...

See 'snap info docker' for additional versions.
```

# Bug Description:
Snapcraft before 4.4.4 is vulnerable to library inclusion from the current working directory. This allowed attackers to gain remote code execution in almost **any application** that was installed with snapcraft, when run in an attacker controlled directory. This could be as simple as running an application in a cloned git repository.

The bug is due to incorrect bash script generation when creating confined snap packages. Snapcraft will generate wrapper scripts to run the application, but accidently uses empty variables to define the `LD_LIBRARY_PATH` for the application. Due to a quirk with LD, empty path entries are treated as current working directory. This means that any libraries (for example libc.so.6) in the current working directory will be loaded into the snap application when run. (Additionally LD will search several subdirectories including `tls`).

A malicious library could easily be crafted to run arbitrary remote code when a snap application is run. This code will run inside the snap container so it will initially be somewhat restricted and can only access any files in the users home directory (excluding dotfiles). However due to many apps also including X11 permissions, it is fairly trivial to escape the container using X11 commands. This would give an attacker full access to the system as the current user.

# Fix
Snapcraft [fixed](https://github.com/snapcore/snapcraft/commit/a0ceca9d531a34c979251030ed67b5fa2abfdd9a) the issue in the script generator by including a check for empty string. However for the fix to be applied, application authors must "refresh" their app, regenerating the vulnerable files. This means that **many applications are still vulnerable** (ie chromium and docker) until re-generated correctly.

# POC
Attached is both the POC archive which should still work against chromium. Additionally is a script that generates the malicious `libc.so.6`

```
itszn@ubuntu:~$ tar xfvz snap-escape
itszn@ubuntu:~$ cd snap-escape
itszn@ubuntu:snap-escape$ ls
total 8
-rw-rw-r-- 1 itszn itszn    0 Oct 25 11:04 amazing-movie.mp4
-rw-rw-r-- 1 itszn itszn    0 Oct 25 11:28 cool-page.html
-rw-rw-r-- 1 itszn itszn 2193 Oct 25 11:45 README.txt
drwxrwxr-x 3 itszn itszn 4096 Oct 25 11:28 tls
itszn@ubuntu:snap-escape$ chromium
Got code execution running as itszn inside snap container!

We can read/write any non-hidden (non-dot) file in
+ echo 'Hello from snap code exec' > /home/itszn/pwned
+ cat /home/itszn/pwned
Hello from snap code exec

However we are still restricted by the container

We cannot access dotfiles
+ echo 'echo PWNED' >> /home/itszn/.bashrc
./tls/s: 20: ./tls/s: cannot create /home/itszn/.bashrc: Permission denied

Or other non-home files
+ cat /etc/issue
cat: /etc/issue: Permission denied

Luckily, this snap has the x11 plug
We can use this escape the container!
Starting container escape...



Escape Success!

We are now running code outside of snap container, we now have full privs of itszn

For example we now can read /etc/issue:
+ cat /etc/issue
Ubuntu 18.04.4 LTS \n \l


Or modify dotfiles
+ echo 'echo PWNED' >> /home/itszn/.bashrc
+ tail -n 1 /home/itszn/.bashrc
echo PWNED

Full escape and code execution~!
```

## Impact

In many situations, an attacker could gain full access to a user's system running as the current user. The following are example attack scenarios demonstrating how an attacker could abuse this bug against users.

# Example Attack Scenarios:
## Scenario 1: VLC
- Attacker creates a malicious archive containing a video file. Like before the malicious library is hidden in a `tls` directory to prevent suspicion (potentially even disguised as subtitle information)
- The target user wants to view the video file and downloads the archive. They extract the archive and find the video file:

```
itszn@ubuntu:~$ tar xfvz movie.tar.gz && cd movie
itszn@ubuntu:movie$ ls
total 8
-rw-rw-r-- 1 itszn itszn    0 Oct 25 11:04 amazing-movie.mp4
-rw-rw-r-- 1 itszn itszn 2193 Oct 25 11:45 README.txt
drwxrwxr-x 3 itszn itszn 4096 Oct 25 11:28 tls
drwxrwxr-x 3 itszn itszn 4096 Oct 25 11:29 tls_subtitles
```
- The user now runs VLC, which they installed using snapcraft (VLC is one of the top Snapcraft apps according to the Snap store).

```
itszn@ubuntu:movie$ vlc ./amazing-movie.mp4
```
- At this point the attacker has achived coded exction in the VLC container. The attacker can use the X11 plug to trivially escape this container.
- The attacker now has full access to the system as the user

## Scenario 2: Chromium
- Attacker adds malicious library into a github reposity. The library is hidden in a `tls` directory in the repo (making it harder to be noticed by the target user). 
- Target user clones the git repo and opens the html file with chromium (which since Ubuntu 20 is always installed as a Snapcraft package):

```
itszn@ubuntu:~$ git clone git@github.com:example/example-site.git && cd example-site
itszn@ubuntu:example-site$ ls
total 8
-rw-rw-r-- 1 itszn itszn    0 Oct 27 14:31 some_page.html
drwxrwxr-x 3 itszn itszn 4096 Oct 25 11:29 css
drwxrwxr-x 3 itszn itszn 4096 Oct 25 11:29 js
drwxrwxr-x 3 itszn itszn 4096 Oct 25 11:28 tls
itszn@ubuntu:example-site$ chromium ./some_page.html
```

- Normally to compromise a user from a webpage both a browser exploit and a sandbox escape are required. However as the malicious library is injected before any sandboxing is applied, the attacker **does not need to escape the Chromium Sandbox**. The attacker now has remote code execution in the chromium container. Additionally this works even if the user already has chromium open (normally it would just tell the other chromium to load the page).
- As before, the attacker can use the X11 plug to trivially escape this container.
- The attacker now has full access to the system as the user

**NOTE**: From my testing, Chromium is **still** vulnerable as they need to manually refresh their snap packages to apply the fix.

## Scenario 3: Docker
- Attacker adds malicious library into a github reposity. The library is hidden in a `tls` directory in the repo (making it harder to be noticed by the target user). 
- Target user clones the git repo, inspects the Dockerfile, and then builds the docker image. (NOTE: The dockerfile is non malicious. Under normal operation, there would be no risk. The user additionally can validate that the image would normally not attach any files or volumes).

```
itszn@ubuntu:~$ git clone git@github.com:example/example-app.git && cd example-app
itszn@ubuntu:example-app$ ls
total 8
-rw-rw-r-- 1 itszn itszn    0 Oct 27 14:31 some_code.js
-rw-rw-r-- 1 itszn itszn 109 Oct 27 14:22 Dockerfile
drwxrwxr-x 3 itszn itszn 4096 Oct 25 11:28 tls
itszn@ubuntu:example-app$ docker build -t some_app .
```
- At this point the attacker has gained remote coded execution in the  Snapcraft container. The docker container can read/write the entirety of the user's home directory (additionally [including dotfiles](https://github.com/docker-archive/docker-snap/blob/master/snap/snapcraft.yaml#L24)). At this point the attacker could trivially backdoor any dotfile or configuration file in the user's home directory to gain full code execution outside the container.

**NOTE**: From my testing, Docker is **still** vulnerable as they need to manually refresh their snap packages to apply the fix.

# Final Notes
I personally think this is a very large impact as it meant many applications became vulnerable due to being installed with snapcraft (including chromium!). As Ubuntu transitions more users to Snapcraft this impact would have grown as more apps became vulnerable.

## Attachments
- snap-escape-POC.tar.gz
- make_libc.py
