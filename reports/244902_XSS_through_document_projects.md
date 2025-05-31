# XSS through document projects

## Report Details
- **Report ID**: 244902
- **URL**: https://hackerone.com/reports/244902
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-30T23:10:37.540Z
- **Disclosed**: 2018-03-30T22:55:10.407Z

## Reporter
- **Username**: ethanluismcdonough
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hello, I'm Ethan Luis McDonough ([@elmt2](https://www.khanacademy.org/profile/elmt2/) on Khan Academy), and I found a way to inject scripts into document projects.  Since KA document projects output HTML, I can edit the PUT request that updates projects (https://www.khanacademy.org/api/internal/scratchpads/ID) and inject JavaScript code inside an `<img>` tag's `onload` attribute.  Here's a demo that completely redirects a learner from KA to another site: https://www.khanacademy.org/physics/woah/4740384569491456.  

**Note**: the stored script does not run in Firefox because document projects don't seem to be working on that browser (at least on my machine).

## Attachments
No attachments
