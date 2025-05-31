# [Admin Panel] CSRF to resume/pause runner

## Report Details
- **Report ID**: 415238
- **URL**: https://hackerone.com/reports/415238
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-27T10:33:53.541Z
- **Disclosed**: 2020-12-01T04:34:15.871Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi, 

Just found a CSRF in admin panel of gitlab instance to pause/resume runner.

## Steps to reproduce
- http://{gitlab_instance}/admin/runners/:runner_id/resume
- http://{gitlab_instance}/admin/runners/:runner_id/pause

Video:
███████
password: `██████████`

## Impact

Just found a CSRF in admin panel of gitlab instance to pause/resume runner.

## Attachments
No attachments
