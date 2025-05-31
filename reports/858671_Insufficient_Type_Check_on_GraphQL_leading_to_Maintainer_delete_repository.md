# Insufficient Type Check on GraphQL leading to Maintainer delete repository

## Report Details
- **Report ID**: 858671
- **URL**: https://hackerone.com/reports/858671
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-24T13:57:44.581Z
- **Disclosed**: 2020-11-02T16:11:38.497Z

## Reporter
- **Username**: ledz1996
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

As you have know, Maintainer cannot delete/archive repository. But via GraphQL, they can do as there exists an sufficient check on GraphQL API

***app/graphql/mutations/snippets/destroy.rb***

```ruby
  def resolve(id:)
        snippet = authorized_find!(id: id)

        response = ::Snippets::DestroyService.new(current_user, snippet).execute
```

The function `authorized_find` lead to `object_from_id!` 

***app/graphql/mutations/snippets/base.rb***

```ruby
  def find_object(id:)
        GitlabSchema.object_from_id(id)
      end

      def authorized_resource?(snippet)
        Ability.allowed?(context[:current_user], ability_for(snippet), snippet)
      end

      def ability_for(snippet)
        "#{ability_name}_#{snippet.to_ability_name}".to_sym
      end
```

Here there is no check for whether the Object returned from `find_object` is a Snippet. I could specify any object which the user have permission of 
` "#{ability_name}_#{snippet.to_ability_name}".to_sym` to.
For example: A DiffNote that is created by a Maintainer in the Project as the function.

If I have such a ID:
```
mutation test{
  destroySnippet(input: {id: "gid://gitlab/DiffNote/116"}){
    errors
  }
}
```

It refer to an DiffNote with id `116`
Perfectly, a Maintainer have an `admin_note` and `admin_snippet` on a DiffNote (!!!)

In the mutation Destroy the call to `` ::Snippets::DestroyService.new(current_user, snippet)`` but the Object of `snippet` is actually a `DiffNote`

***app/services/snippets/destroy_service.rb***
```ruby
  def attempt_destroy!
      result = Repositories::DestroyService.new(snippet.repository).execute

      raise DestroyError if result[:status] == :error

      snippet.destroy!
    end
```
and in 

***app/models/diff_note.rb***

```ruby
  def repository
    noteable.respond_to?(:repository) ? noteable.repository : project.repository
  end
```
It return the `project.repository` which in turn the Project that the `DestroyService` gonna delete

### Steps to reproduce

1. Create 2 User: User A, User B
2. User A create a project set User B as Maintainer.
F802288
3. User B create 2 branch with the same file but different content
F802287
F802289
4. Create a merge request for those 2 Branch
F802290
5. Create a diff note for the file by clicking at the comment on a line of the file then Submit it
F802291
6. To know the ID of diff note, delete this one, the ID will show up in burp then you will know the ID of the next one
F802292
7. Use the `/-/graphiql-explorer` to execute the following the query

```
mutation test{
  destroySnippet(input: {id: "gid://gitlab/DiffNote/118"}){
    errors
  }
}
```

F802293
8. Enjoy no repository
F802294
9. If you click on `Create empty repository` It will actually make the Project 404 but It still show up on the User's project feed
F802295
F802296
### Impact

Unauthorized deleting of repository/project by maintainers

### Output of checks

This bug happens on GitLab.com

## Impact

Unauthorized deleting of repository/project by maintainers

## Attachments
- unauthen2.PNG
- unauthen1.PNG
- unauthen3.PNG
- unauthen4.PNG
- unauthen5.PNG
- unauthen6.PNG
- unauthen7.PNG
- unauthen8.PNG
- unauthen10.PNG
- unauthen9.PNG
