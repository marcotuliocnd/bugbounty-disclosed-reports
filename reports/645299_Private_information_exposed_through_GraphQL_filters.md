# Private information exposed through GraphQL filters

## Report Details
- **Report ID**: 645299
- **URL**: https://hackerone.com/reports/645299
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-16T17:27:51.341Z
- **Disclosed**: 2019-07-23T07:21:54.470Z

## Reporter
- **Username**: reigertje
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
secure schema can be circumvented for graphql `where` filters by using `or` operator. 

**Description:**
When passing a where clause to a collection in the `graphql` endpoint, like `teams(where:{ state: {_eq: soft_launched}})` it queries the state through the secure schema - so it will not return any teams where the state does equal soft_launched but you're not allowed to see the state. 

However, when using an `or` operator. like `teams(where:{_or: [{state: {_eq: soft_launched}, {state: {_eq: soft_launched}]}` - only the first condition in the list seems to be converted to the secure variant. The second condition seems to be queried in the unprotected schema. So this will return teams where the state equals soft_launched - but I'm not allowed to see the state.

Looking at the resulting query also verifies this. for `_or:[{submission_state: {_eq: open}}, {submission_state: {_eq: closed}}]`:
{F530641}
As you can see, for the first condition, `submission_state` has been converted to the secure `__new_filterable_submission_state` - but not for the second one. This probably also happens for `and` operator, but `or` was easier to verify. 

### Steps To Reproduce

1. Open any graphql client (eg. https://electronjs.org/apps/graphiql) 
2. Run query

```
query {
  teams(where:{_or:[{state:{_eq:soft_launched}}, {state:{_eq:soft_launched}}]}) {
    edges {
      node {
        id
        state
      }
    }
  }
}
```

3. Note that it returns teams with `state: null`, because you're not allowed to see it - but now we know it's soft_launched.
4. Optionally, also note that removing one of the conditions from the `or` list does not return these teams. This is because the first item is converted to query through the secure schema. 
████

## Impact

Expose/derive private information from any filterable field for collections that use the `where` graphql filters. Potentially extra risky as we introduce more filter fields.

## Attachments
- vuln0.png
