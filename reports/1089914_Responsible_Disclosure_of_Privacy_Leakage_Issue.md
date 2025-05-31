# Responsible Disclosure of Privacy Leakage Issue

## Report Details
- **Report ID**: 1089914
- **URL**: https://hackerone.com/reports/1089914
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-28T21:21:20.380Z
- **Disclosed**: 2021-06-29T06:31:08.419Z

## Reporter
- **Username**: mzaheri
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Greetings,

I am Mojtaba Zaheri, a doctoral candidate in Computer Science, affiliated with the [NJIT Cybersecurity Research Center](https://centers.njit.edu/cybersecurity/welcome/). Together with my doctoral dissertation advisor, Prof. Reza Curtmola, we are reaching out to perform responsible disclosure of a vulnerability present on the GitLab website. Please let us know if you have any comments regarding this disclosure.

### Summary:
We have identified a leaky resource attack against several high-profile resource-sharing websites, including GitLab, that allows an attacker to infer the unique identity of a victim that visits an attacker-controlled website. This targeted privacy attack can have a significant impact on the privacy of individuals.

Even though previous work introduced the attack using images (i.e., leaky images [1]), in this report we show that the attack works with any resource that can be privately shared with the victim and can be rendered on a webpage. In particular, we show the attack also works with other media files, such as video and audio files. Thus, we generically refer to the attack as a leaky resource attack. An attacker exploiting these vulnerabilities can identify a user of the GitLab website while the user visits an attacker-controlled website, using the cookie(s) set by the GitLab website in her browser.

The leaky image attack [1] leverages the existence of a state-dependent URL (SD-URL) on the image-sharing website, i.e. a URL for which the response is different depending on the victim’s state with respect to the image-sharing website. For example, if the user is the targeted victim, the content will be loaded, otherwise, it will not be loaded. The attacker can learn information about this response based on an XS-leak that bypasses the Same-Origin Policy which normally prevents the attacker from reading the contents of a cross-origin response. [1] describes script-based and scriptless variants of the leaky image attack. The scriptless variant relies on the object HTML tag for the XS-leak, using this tag’s if-then-else behavior to enable the attack.

We reveal a new SD-URL for resources in the GitLab service and introduce two new HTML-only XS-Leaks. We show that a leaky resource attack can be performed using video and audio HTML tags. The previously known scriptless attack was based on the object HTML tag, but we find that it is not reliable: It does not work against all vulnerable resource-sharing services and only works in some browsers. As opposed to this, we show that attacks based on the video and audio tags are very reliable, as they work against all the vulnerable services we identified and across all browsers we tested with (Firefox, Edge, Chrome).

We describe below the threat model, the exploit vector, and the actual steps that need to be followed on your website to set up a leaky resource attack. We also explain potential fixes.

### Threat Model:
We consider attackers that can bring together the following necessary ingredients for a successful leaky resource attack:
1. The attacker and the victim are users of the same resource sharing service.
2. The resource sharing service allows its users to share resources privately with each other and authenticates users through cookies.
3. The attacker convinces the victim to visit the attack page (which is controlled by the attacker) while the victim is logged into her account with the resource sharing service (which is not controlled by the attacker).
4. The attacker can determine if the victim loaded the resources successfully.

The attack is effective because these requirements can be achieved in multiple ways and are within easy reach of the attacker. For requirement #1, GitLab is popular, so the victim may have an account; also, GitLab has free membership, and so the attacker can just create an account. For requirement #2, these are the de facto mechanisms for many of the resource sharing services. Requirement #3 can be achieved in multiple ways, including via phishing emails, or via a watering-hole approach. It is common for a large portion of internet users to be logged in to GitLab when they are surfing the internet. Requirement #4 is crucial for the attack and can be achieved as follows. The attack page contains a state-dependent URL (SD-URL) that points to content on the target website (i.e., GitLab). When a user makes a request for the SD-URL, the response is different depending on the user's state with respect to the GitLab website. For example, if the user is the targeted victim, the content will be loaded, otherwise, it will not be loaded. The attacker can learn information about this response based on an XS-leak that bypasses the Same-Origin Policy which normally prevents the attacker from reading the contents of a cross-origin response.

### Attacks:
The new SD-URL we use can be exploited by a script-based XL-leak, but here we focus on scriptless XS-leaks, as privacy-aware users may disable scripts or use protection mechanisms that prevent script-based XS-leaks.

The pattern of the SD-URL used is:
```
https://gitlab.com/{userName}/{repoName}/-/raw/{branchName}/{fileName}
```
This SD-URL is valid until the resource is unshared or deleted.

Exploiting this SD-URL based on object tag HTML-only XS-Leak from [1]:
```
<object data ="https://gitlab.com/{userName}/{repoName}/-/raw/{branchName}/{fileName}" type ="image/png">
             <object data ="Fallback-URL" type ="image/png"></object>
</object>
```
Communication method using the object HTML tag: If the outer object element (SD-URL) fails to load, then the fallback is to load the inner object element (Fallback-URL, controlled by the attacker). This fallback-based mechanism can be used to simulate an if-then-else control flow instruction in pure HTML. The attack does not work with browsers we tested (Chrome 87.0, Edge 87.0, and Firefox 83.0).

Here we describe the video and audio HTML tags as new XS-leaks that are reliable across all browsers we tested (Chrome 87.0, Edge 87.0, and Firefox 83.0).
```
<video width="320" height="240" controls autoplay muted>
        <source src="https://gitlab.com/{userName}/{repoName}/-/raw/{branchName}/{fileName}" type ="video/webm">
        <source src="Fallback-URL" type ="video/webm">
</video>
```
Communication Method using video HTML tag: If the first source (SD-URL) cannot be loaded, then the fallback is to load the second source (Fallback-URL, controlled by the attacker).
```
<audio width="320" height="240" controls autoplay>
         <source src="https://gitlab.com/{userName}/{repoName}/-/raw/{branchName}/{fileName}" type ="audio/ogg">
         <source src="Fallback-URL" type ="audio/ogg">
</audio>
```
Communication Method using audio HTML tag: If the first source (SD-URL) cannot be loaded, then the fallback is to load the second source (Fallback-URL, controlled by the attacker).

Normally, the source elements are used by website authors to specify multiple alternative media resources for media elements. However, these alternatives can be used to trigger a fallback behavior that mimics an if-then-else control flow. Both resources used in these tests have the type webm and ogg for video and audio tags respectively, but other video and audio file types can be used as well. By checking the HTTP Request Headers, the attacker can make sure whether the specific file type is supported by the browser, and so prepare an appropriate webpage.

### Steps to Reproduce:
The attacker first shares privately a resource with the target victim using a sharing service. The attacker then embeds a link to the privately shared resource on a webpage she controls. When a visitor loads that webpage, the resource will be successfully retrieved only if the visitor is the targeted victim, since only the victim is allowed to retrieve the resource (assuming the victim's browser is logged into the sharing service). By observing the success of loading the resource through an XS-leak, the attacker will know if the intended victim has visited the attacker's website.

1) Upload and share privately the resource with the victim in GitLab.
2) Open the resource in the browser to get the SD-URL.
3) Embed the SD-URL in an attacker-controlled webpage with an XS-leak.

### Fix:
1.       Server-side defense:
The SameSite cookie attribute can be used to impose restrictions when cookies can be sent. Although setting this cookie attribute to strict or lax could limit the attack surface in theory, our findings show that many popular sharing services are still vulnerable, because the attribute is either set to none or not enabled at all. A major reason for this is that the SameSite cookie attribute interferes with services provided by websites. Two examples are a watch later button on a YouTube video embedded in a non-YouTube website, and a website that embeds the GoogleMaps service, in order to show user-specific resources, such as saved and favorite locations on the map. As an additional drawback, when the SameSite attribute is not set, browsers have inconsistent default behaviors. Chromium-based browsers versions 80 and above treat cookies as if a lax SameSite attribute is set, whereas Firefox (tested up to version 83) treats them as if SameSite is set to none.

2.       Client-side defense:
We have devised a client-side defense that can be implemented as a browser extension and can thus be deployed immediately without buy-in from websites and browser vendors. The defense is included in a research article that is currently under submission for publication at an academic conference.

### References:
[1] Staicu, C.A., Pradel, M.: Leaky images: Targeted privacy attacks in the web. In: Proc. of the 28th USENIX Security Symposium. pp. 923-939 (2019)

## Impact

The leaky resource attack is a targeted privacy attack, in which an individual browsing an attacker-controlled webpage can be uniquely identified. This is in contrast with other known de-anonymization techniques, such as third-party tracking (e.g., tracking pixels or tracking IPs) or social media fingerprinting, that do not provide this level of accuracy. As such, leaky resources can be abused in a variety of privacy-sensitive scenarios, including law enforcement gathering evidence regarding the online activity of individuals, oppressive governments tracking political dissidents, de-anonymizing reviewers for a conference paper, blackmailing individuals based on their online activity, or health insurance companies discriminating individuals based on their online activity.

## Attachments
No attachments
