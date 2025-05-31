# Lack of input validation and sanitization in react-autolinker-wrapper library causes XSS 

## Report Details
- **Report ID**: 592525
- **URL**: https://hackerone.com/reports/592525
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-30T04:37:25.438Z
- **Disclosed**: 2019-12-15T11:32:37.859Z

## Reporter
- **Username**: rugged_info
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report [XSS] in [react-autolinker-wrapper]
It allows [remote arbitrary code execution]

# Module

**module name:** [react-autolinker-wrapper]
**version:** [1.1.0]
**npm page:** `https://www.npmjs.com/package/react-autolinker-wrapper`

## Module Description

React component which automatically converts URLs, email addresses, phone numbers, Twitter handles and hashtags in a string to HTML anchors.

## Module Stats
[307] weekly downloads 

# Vulnerability

## Vulnerability Description

> Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

I expected that calls to react-autolinker-wrapper would find urls, etc. within text and convert them to anchor tags, but I discovered that script execution occurs instead. 

## Steps To Reproduce:

Below is a vulnerable example of using react-autolinker-wrapper to convert user input into anchor tags. If one inserts `<img src=x onerror=alert() >` into the input area then XSS occurs. 

```
import React from 'react';
import AutolinkerWrapper from 'react-autolinker-wrapper'

class App extends React.Component {
  constructor(){
    super()
    this.state = {text: "fudge"}
    this.changeState = this.changeState.bind(this)
  }

  changeState(event){
    this.setState({text: event.target.value})
  }

  render(){
    return (
    <div className="App">
     <input placeholder="Place your link here" type="text" onChange={this.changeState}/>
     <AutolinkerWrapper text={this.state.text}/>
    </div>)
  }
}

export default App;
```
## Patch

> If you're able to provide a patch with the fix please post it in this section

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Node.js 12.2.0
- NPM 6.9.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

> Hunter's comments and funny memes goes here

## Impact

remote code execution

## Attachments
No attachments
