# Validation bypass for queries generated for PostgreSQL

## Report Details
- **Report ID**: 394253
- **URL**: https://hackerone.com/reports/394253
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-08-13T14:44:39.511Z
- **Disclosed**: 2018-11-19T22:55:14.323Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
When using DB for PostgreSQL, I discovered that if a parameter of a query contains null character, there is a pattern in which subsequent strings are lost.


### how to reproduce

#### Prepare the environment


```
$ rails new postgresql_rails -TB --database=postgresql
$ cd postgresql_rails

$ bundle exec ruby -v
> ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-darwin16]
$ bundle exec rails --version
> Rails 5.2.1

$ bundle install
```

Prepare models and schemas.

```
$ bundle exec rails generate model Article title:string text:text
$ bundle exec rails db:create
$ bundle exec rails db:migrate
```

Save test data.

```ruby
$ bundle exec rails console
Loading development environment (Rails 5.2.1)
irb(main):001:0> Article.create(title: 'test title', text: 'dummy')
   (0.1ms)  BEGIN
  Article Create (3.7ms)  INSERT INTO "articles" ("title", "text", "created_at", "updated_at") VALUES ($1, $2, $3, $4) RETURNING "id"  [["title", "test title"], ["text", "dummy"], ["created_at", "2018-08-13 13:31:37.689587"], ["updated_at", "2018-08-13 13:31:37.689587"]]
   (1.3ms)  COMMIT
=> #<Article id: 1, title: "test title", text: "dummy", created_at: "2018-08-13 13:31:37", updated_at: "2018-08-13 13:31:37">
```



#### Confirm query

```ruby
 $ bundle exec rails console
Loading development environment (Rails 5.2.1)

# Case A
irb(main):001:0> Article.where(title: "test title")
  Article Load (0.3ms)  SELECT  "articles".* FROM "articles" WHERE "articles"."title" = $1 LIMIT $2  [["title", "test title"], ["LIMIT", 11]]
=> #<ActiveRecord::Relation [#<Article id: 1, title: "test title", text: "dummy", created_at: "2018-08-13 13:31:37", updated_at: "2018-08-13 13:31:37">]>

irb(main):002:0> Article.where(title: "test title\0suffix")
  Article Load (0.3ms)  SELECT  "articles".* FROM "articles" WHERE "articles"."title" = $1 LIMIT $2  [["title", "test title\u0000suffix"], ["LIMIT", 11]]
Traceback (most recent call last):
ArgumentError (string contains null byte)


# Case B
irb(main):003:0> Article.find_by_title("test title")
  Article Load (0.4ms)  SELECT  "articles".* FROM "articles" WHERE "articles"."title" = $1 LIMIT $2  [["title", "test title"], ["LIMIT", 1]]
=> #<Article id: 1, title: "test title", text: "dummy", created_at: "2018-08-13 13:31:37", updated_at: "2018-08-13 13:31:37">

irb(main):004:0> Article.find_by_title("test title\0suffix")
  Article Load (0.5ms)  SELECT  "articles".* FROM "articles" WHERE "articles"."title" = $1 LIMIT $2  [["title", "test title\u0000suffix"], ["LIMIT", 1]]
Traceback (most recent call last):
        1: from (irb):4
ArgumentError (string contains null byte)


# Case C
irb(main):005:0> Article.where("title = ?", "test title")
  Article Load (0.4ms)  SELECT  "articles".* FROM "articles" WHERE (title = 'test title') LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation [#<Article id: 1, title: "test title", text: "dummy", created_at: "2018-08-13 13:31:37", updated_at: "2018-08-13 13:31:37">]>

irb(main):006:0> Article.where("title = ?", "test title\0suffix")
  Article Load (0.4ms)  SELECT  "articles".* FROM "articles" WHERE (title = 'test title') LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation [#<Article id: 1, title: "test title", text: "dummy", created_at: "2018-08-13 13:31:37", updated_at: "2018-08-13 13:31:37">]>


# Case D
irb(main):007:0> Article.where("title = :title", {title: "test title"})
  Article Load (0.4ms)  SELECT  "articles".* FROM "articles" WHERE (title = 'test title') LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation [#<Article id: 1, title: "test title", text: "dummy", created_at: "2018-08-13 13:31:37", updated_at: "2018-08-13 13:31:37">]>

irb(main):008:0> Article.where("title = :title", {title: "test title\0suffix"})
  Article Load (0.4ms)  SELECT  "articles".* FROM "articles" WHERE (title = 'test title') LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation [#<Article id: 1, title: "test title", text: "dummy", created_at: "2018-08-13 13:31:37", updated_at: "2018-08-13 13:31:37">]>
```

In Case A and Case B, an error has occurred when null characters are included.
On the other hand, in Case C and Case D, SQL is generated in such a way that the character string after the null character (`\0suffix`) is ignored.

### sanitize_sql_array

For comparison, list the results of `sanitize_sql_array` for each DB.

#### PostgreSQL

```ruby
$ bundle exec rails console
Loading development environment (Rails 5.2.1)
irb(main):001:0> ActiveRecord::Base.send(:sanitize_sql_array,['SELECT * from articles WHERE title = ?', "abc\0suffix"])
=> "SELECT * from articles WHERE title = 'abc'"
```

#### MySQL

```ruby
$ bundle exec rails console
Loading development environment (Rails 5.2.1)
irb(main):001:0> ActiveRecord::Base.send(:sanitize_sql_array,['SELECT * from articles WHERE title = ?', "abc\0suffix"])
   (0.9ms)  SET NAMES utf8,  @@SESSION.sql_mode = CONCAT(CONCAT(@@sql_mode, ',STRICT_ALL_TABLES'), ',NO_AUTO_VALUE_ON_ZERO'),  @@SESSION.sql_auto_is_null = 0, @@SESSION.wait_timeout = 2147483
=> "SELECT * from articles WHERE title = 'abc\\0suffix'"
```

#### SQLite3

```ruby
$ bundle exec rails console
Running via Spring preloader in process 55281
Loading development environment (Rails 5.2.1)
irb(main):001:0> ActiveRecord::Base.send(:sanitize_sql_array,['SELECT * from articles WHERE title = ?', "abc\0suffix"])
=> "SELECT * from articles WHERE title = 'abc\u0000suffix'"
```

## Impact

In this problem, SQL injection can not be done, but bypass is possible when ruby side is performing blacklist and suffix validation (extension checking etc.).

#### sample code

```ruby
title = "test\0dummy"
title != 'test' ?  Article.where("title = ?", title) : nil
> Article Load (1.9ms)  SELECT  "articles".* FROM "articles" WHERE (title = 'test') LIMIT $1  [["LIMIT", 11]]
```

## Attachments
No attachments
