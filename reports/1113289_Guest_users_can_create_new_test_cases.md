# Guest users can create new test cases

## Report Details
- **Report ID**: 1113289
- **URL**: https://hackerone.com/reports/1113289
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-28T13:33:24.523Z
- **Disclosed**: 2021-08-30T11:01:58.707Z

## Reporter
- **Username**: maruthi12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

According to the [permission docs](https://docs.gitlab.com/ee/user/permissions.html) and [test case docs](https://docs.gitlab.com/ee/ci/test_cases/index.html#create-a-test-case) , only user with a role `Reporter` or more is allowed to create a test case. This vulnerability allows, even `Guest` role users to create new test cases.

### Steps to reproduce

1.  Consider a private project with `Guest` role user.
2.  Consider the API for creating an `issue`.

      The URL is https://gitlab.com/project_name/-/issues (POST).

    POST Data format for this is as follows: 
    ```
    utf8=✓
authenticity_token= your_auth_token
issue[title]=issue_title
issue[description]=issue_description
issue[confidential]=0
issue[issue_type]=issue
issue[lock_version]=0
```
3. Now, in the parameter_set,  tamper with `issue[issue_type]` value and change it from `issue` to `test_case`.
4. Now, send the request.
5. A test case is now created. 

The test case can be viewed at https://gitlab.com/project_name/-/quality/test_cases

## Impact

Test Cases are important part of a project  as it helps product, quality and development teams to combine and Guest users should not be allowed to create it.

## Attachments
No attachments
