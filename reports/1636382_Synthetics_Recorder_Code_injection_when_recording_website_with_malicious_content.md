# Synthetics Recorder: Code injection when recording website with malicious content

## Report Details
- **Report ID**: 1636382
- **URL**: https://hackerone.com/reports/1636382
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-14T04:21:15.478Z
- **Disclosed**: 2023-04-08T17:25:08.056Z

## Reporter
- **Username**: dee-see
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
## Summary

Hello team! Synthetics recorder has a `quote` function to escape user-controlled input, but in one particular scenario the escaping isn't enough and a malicious website can inject arbitrary code in the recorder session.

## Description

The `waitForNavigation` event calls `quote` within the context of a multi-line comment (`/* ... */`) so we can break out of that without using the escaped characters ([reference](https://github.com/elastic/synthetics-recorder/blob/v0.0.1-beta.3/electron/syntheticsGenerator.ts#L217=))

In a normal situation the code generated looks like this for a navigation event to `https://example.com`

```javascript
    page.waitForNavigation(/*{ url: 'https://example.com' }*/),
```

but it's possible to escape out of the comment without using single quotes (which would be escaped) with a specially crafted URL like `https://example.com?q=*/require(`child_process`).exec(`touch$IFS/tmp/haxx`)/*`

```javascript
    page.waitForNavigation(/*{ url: 'https://example.com?q=*/require(`child_process`).exec(`touch$IFS/tmp/dee-see`)/*' }*/),
```

The syntax highlighting here on HackerOne helps visualizing how that works. `$IFS` is used because spaces get encoded to `%20`.

It's possible to have code execution when the victim uses the `test` feature inside of the synthetic recorder but the code we're allowed to use is fairly limited because the `require` function isn't available. The maximum impact is when the user saves the recorded session as a project and executes it using the synthetic runner.

## Steps To Reproduce

### Preparation

Install the synthetics recorder (See https://github.com/elastic/synthetics-recorder/, I'm following the instructions to run it in development mode (`nvm install; nvm use; npm install; npm run dev`) but you could also download the binary on the releases page)

### Reproduction

1. Start Synthetics Recorder and enter `http://deesee.xyz:4567` in the text box where it says "Enter a Starting URL"
1. Click "Start Recording"
1. A browser has opened, this website is a modified clone of my blog. Click the GitLab icon in the top right

    {F1820934}

1. Close the browser window

    In a normal Synthetics Recorder session there would be much more steps to record but here we only did what's necessary to trigger the issue.

1. Click the "Export" button and you'll see this code

    ```javascript
    step('Go to http://deesee.xyz:4567/', async () => {
      await page.goto('http://deesee.xyz:4567/');
      await Promise.all([
        page.waitForNavigation(/*{ url: 'https://gitlab.com/dee-see?query=*/require(`child_process`).exec(`touch$IFS/tmp/dee-see`)/*' }*/),
        page.click('[aria-label="GitLab"] svg')
      ]);
    });
    ```

    We can see the payload is in place. It's fairly obvious because we only recorded one step, but in a long recording session it would be buried deeper.

1. Click the "Export" button and save the file in a directory
1. In that directory run `npm init -y; npm install @elastic/synthetics; npx @elastic/synthetics .`
1. When the tests finished running observe that the `touch /tmp/dee-see` command ran

Those last steps seem contrived, but that's how a synthetics test suite is setup and how a developer would make sure the session they just recorded would be integrated into their builds and whatnot.

## Supporting Material/References:

{F1820942}

## CVSS

Confidentiality and Integrity impact are High because of the arbitrary command execution. I also included Availability impact because those commands can shut down the system. I will concede though that Attack Complexity could be "very high" if that existed on the Attack Complexity scale. :)

## Impact

Someone with control over the website's content can run arbitrary code where ever the synthetics recorded session will be re-executed.

Developer computers and CI systems come to mind. The most realistic attack scenario would be privilege escalation from within a company.

## Attachments
- gl.png
- 2022-07-14_00-09-26.mp4
