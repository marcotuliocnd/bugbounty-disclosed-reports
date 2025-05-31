# Sidekiq web UI (Ruby background processing) accessible unauthenticated via https://gift-test.starbucks.co.jp/sidekiq/busy

## Report Details
- **Report ID**: 423286
- **URL**: https://hackerone.com/reports/423286
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-13T10:31:17.969Z
- **Disclosed**: 2018-10-24T17:31:28.121Z

## Reporter
- **Username**: jackds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** 
I found the following URL, which appears to be running an Sidekiq web UI instance that is accessible unauthenticated: https://gift-test.starbucks.co.jp/sidekiq/busy

**Description:**
Sidekiq is used for Ruby background processing (as I've learned, I'm not really familiar with it). The web UI can be used to stop these processes, as can be seen here:

{F359897}

## Steps To Reproduce:

  1. Go to  https://gift-test.starbucks.co.jp/sidekiq/busy

## Supporting Material/References:

n.a.

## Impact

Unclear. As the domain name suggests it might be a staging/test environment. I cannot determine clearly what these running processes are, but I am able to stop them which might be undesired.

## Attachments
- Screen_Shot_2018-10-13_at_12.29.05.png
