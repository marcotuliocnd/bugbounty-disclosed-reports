# Missing/Breach of Internal Security Boundary - Access to Job Queue Results in Remote Code Execution

## Report Details
- **Report ID**: 224198
- **URL**: https://hackerone.com/reports/224198
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-27T00:53:26.899Z
- **Disclosed**: 2017-06-28T18:37:33.156Z

## Reporter
- **Username**: pruby
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Test Conditions
=============

This issue was tested in GitLab Community Edition using a combination of code review (against git commit 6c65b63ca5, April 20 2017) and testing likely issues against a local deployment of Bitnami GitLab Community Edition 9.0.5-0, running on Ubuntu 14.04.5. These are running different versions of GitLab, as we were constrained by time available for deploying systems to test. This issue has not been tested against gitlab.com or other public installations.

Testing was conducted in research time provided by my employer, Insomnia Security, and was not part of a client engagement.

Issue Description
==============

The GitlabShellWorker handler for jobs from the SideKiq job queue allows arbitrary code to be executed from an enqueued job. From the Redis CLI, adding the following queue entry will result in the creation of a file /tmp/rce-demo:

    rpush 'resque:gitlab:queue:gitlab_shell' '{"class":"GitlabShellWorker","args":["instance_eval","`touch /tmp/rce-demo`"],"jid":"Zaep6UXu","enqueued_at":1493166403.21}'

This results in code execution as the GitlabShellWorker allows any public method on the shell object to be executed. All ruby objects have inherited instance methods that result in remote code execution when an attacker controls the method name and at least one parameter.

It is not necessary that GitLab execute arbitrary code from the job queue. Jobs may be whitelisted and executed only from a fixed list of tasks. Other GitLab service workers follow this more secure paradigm.

Impact
======

An attacker with the ability to add entries to any SideKiq queue may use this endpoint to execute code in the context of the GitLab application. This introduces an absolute trust relationship between the application and the queue server, which may be abused by an attacker.

While remote code execution is a critical issue, the pre-requisites for this attack imply an extremely high level of access to system internals which are known to be vulnerable to other issues and not generally exposed to external parties. As the *gain* in access is limited, and the conditions unlikely, I have rated this as having a Low net risk.

Note that access to a Redis installation implies the ability to execute code as the Redis user, as Redis itself has a high level of trust in all clients. However, this issue may be used to bypass operating system restrictions on the user role, and execute code as the GitLab application user.

Recommendations
===============

* Whitelist actions which may be invoked through the job queue.
* Avoid accepting arbitrary parameters to queued tasks. Where feasible, require that tasks act on pre-established database entities such as projects and repositories, not arbitrary filesystem paths.
* Limit trust in internal components such as message queues and database. Construct internal boundaries to limit the impact of individual components being breached.

## Attachments
No attachments
