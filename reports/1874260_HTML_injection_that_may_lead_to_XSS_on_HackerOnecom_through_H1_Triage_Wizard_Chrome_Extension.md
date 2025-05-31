# HTML injection that may lead to XSS on HackerOne.com through H1 Triage Wizard Chrome Extension

## Report Details
- **Report ID**: 1874260
- **URL**: https://hackerone.com/reports/1874260
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-02-14T18:53:24.931Z
- **Disclosed**: 2023-02-14T20:17:48.764Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
To reproduce:

* ensure you have the H1 Triage Wizard Chrome extension enabled
* visit https://hackerone.com/reports/1622449?subject=security&/bugs=1
* right-click the report, select "View Triage Questionnaire (Beta)"
* observe an HTML payload being injected

{F2173699}

The payload is stored in █████████. The contents of this file are dynamically loaded through the Chrome extension.

The vulnerability is caused by the following code in the `triage-extension-private` repository:

```js
buildTriageQuestionnaireModal = (
  modalElement,
  triageQuestionnaireModalOptions
) => {
  let questionnaireResponses =
    triageQuestionnaireModalOptions.questionnaireResponses;
  if (questionnaireResponses) {
    modalElement.innerHTML = triageQuestionnaireHTML
      .replace("{{handle}}", triageQuestionnaireModalOptions.handle) // <-- the handle here is taken from the subject parameter (i.e. "security")
      .replace("{{1}}", questionnaireResponses[1]) // <-- the response to the questionnaire is interpolated without sanitizing it
      .replace("{{2}}", questionnaireResponses[2]) // <-- this applies to all of these
      .replace("{{3}}", questionnaireResponses[3])
// ...
```

## Impact

This vulnerability may lead to compromising confidential information or impact its integrity.

## Attachments
- Screen_Recording_2023-02-14_at_10.46.41_AM.mov
