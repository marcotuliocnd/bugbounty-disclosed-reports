# Bypassing the Grammarly plagiarism checker by simply replacing characters in the source text

## Report Details
- **Report ID**: 1282282
- **URL**: https://hackerone.com/reports/1282282
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-07-28T21:14:47.060Z
- **Disclosed**: 2021-10-28T21:24:36.617Z

## Reporter
- **Username**: evilksandr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
**Summary:** 
Replacing the characters i, a, e, o, p, c, x in the text with similar ones in the Ukrainian keyboard layout leads to the fact that plagiarism detectors (Grammarly plagiarism checker and others) skip such text, mark it as unique (without any plagiarism) and do not even signal that the characters have been replaced with Cyrillic ones. The text with replaced characters looks natural, has original readability, and after bypassing the plagiarism detection begins to cause harm on the hosted site, both reputational and in terms of SEO (those texts will led to pessimization in google ranking).

**Description:** 
As part of one of my personal projects, on 12/02/2018 I conducted research on almost all online tools for checking for plagiarism with free access or using a trial account. 
The research also includes a tool from Grammarly located by url https://www.grammarly.com/plagiarism-checker 
I randomly took one of the texts and it showed in a google search and led to the site where the original is posted. It served as a benchmark for verification. Further in this text I replaced only 7 Latin characters (i, a, e, o, p, c, x) with similar ones by style (і, а, е, о, р, с, х) in the Ukrainian keyboard layout. This text served as a test text.
After that, I constantly checked 11 online tools for detecting plagiarism with benchmark and test texts.
They all found plagiarism in the benchmark  text.
None of them found plagiarism in the test text, and only one tool reported that there are suspiciously many non-Latin characters.
On 07/27/2021 after reading the article about the bug bounty program from Grammarly, I re-checked the plagiarism detection service, this time only Grammarly plagiarism checker. The check showed that the problem has not been fixed for almost 3 years and still exists.
For potential harm from this problem, see the Impact section.
For screenshots confirming the problem, see the attached document below.

## Browsers Verified In:

  * This vulnerability is browser independent

## Steps To Reproduce:

1. Take a sample text that has been posted on the Internet for a long time (“benchmark text”) and easily shows the source url by checking with google.
2. In “benchmark text” replace the following symbols with another ones according the table to get a “test text” (all character codes are taken from the table Windows-1251 character set table https://en.wikipedia.org/wiki/Windows-1251):
a (0061)  → а (0430), c (0063)  → с (0441), e (0065)  → е (0435), i (0069)  → і (0456), o (006F)  → о (043E), p (0070)  → р (0440), x (0078)  → х (0445)
3. Go to the url https://www.grammarly.com/plagiarism-checker 
4. Insert “benchmark text” in the text edit box and press “Scan for plagiarism” button
5. You will receive a report stating that significant plagiarism was found
6.  Go to the url https://www.grammarly.com/plagiarism-checker again
7. Insert “test text” in the text edit box and press “Scan for plagiarism” button
8. You will receive a report stating that no plagiarism was found.

## Supporting Material/References:

  * Look at the attached file with report

## Impact

Let me help you assess the impact of this problem and its negative consequences.
Just fantasize that your plagiarism checker is being used by a very famous company which uses the product to automate plagiarism checking in a team that manually checks all software reviews from corporate users, which are posted in a subsection on the company's main site (the big directory of reviews for different software).
And so, again, this is just a fantasy, one day there is an article in the WSJ, WP, NYT, Bloomberg etc about that company allowed 2000+ (just randomly chosen number) fake reviews to be posted on its website, and many of them are also duplicated in other sections and plagiated from original reviews. After that an investigation begins, which shows that the reviews looked like real ones and were passed during the plagiarism check, because they contain replaced characters.
The reputation of the company will fall drastically and the project, into which a lot of resources was invested, will simply be closed.
Further, the raised wave will find similar fakes on several more similar websites.
Probably my imagination is already too much played out and I just give you the opportunity to predict the consequences.
I am open for cooperation and ready to discuss and continue my research further together with your team, if it interests you.

## Attachments
- Plagiarism_detection_online_tools_test.pdf
