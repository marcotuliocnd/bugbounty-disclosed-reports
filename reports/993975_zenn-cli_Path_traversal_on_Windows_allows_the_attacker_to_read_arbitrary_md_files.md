# [zenn-cli] Path traversal on Windows allows the attacker to read arbitrary .md files

## Report Details
- **Report ID**: 993975
- **URL**: https://hackerone.com/reports/993975
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-29T11:09:14.384Z
- **Disclosed**: 2020-10-29T19:33:06.837Z

## Reporter
- **Username**: ryotak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
## Summary
I would like to report path traversal in `zenn-cli`.
It allows the attacker to read arbitrary `.md` files.

# Module

**module name:** `zenn-cli`
**version:** `0.1.39`
**npm page:** `https://www.npmjs.com/package/zenn-cli`

## Module Description

Manage Zenn content locally 👩‍💻

## Module Stats

885 weekly downloads

# Vulnerability

## Vulnerability Description

Due to improper sanitization in [this line](https://github.com/zenn-dev/zenn-editor/blob/master/packages/zenn-cli/utils/api/articles.ts#L32), it's possible to bypass sanitization via `\` on Windows and allows the attacker to read arbitrary `.md` file from the victim's machine.

## Steps To Reproduce:

1. Create test directory: `mkdir zenn-test && zenn-test`
2. Initialize npm project: `npm init --yes`
3. Install `zenn-cli`: `npm install zenn-cli`
4. Initialize `zenn-cli`: `npx zenn init`
5. Create an article: `npx zenn new:article`
6. Start preview server: `npx zenn preview`
7. Open http://localhost:8000 in your browser.
8. Click an article that you created in step 5.
9. Find the URL in the following format from the Network tab of DevTools: `http://localhost:8000/_next/data/[Random String]/articles/[Slug of an article].json`
10. Modify the URL you found above to the following and send request: `http://localhost:8000/_next/data/[Copy the random string from step 9]/articles/%5c..%5cREADME.json`
11. You'll receive the content of the README.md that is in outside of `articles` directory.

## Patch
```
diff --git a/packages/zenn-cli/utils/api/articles.ts b/packages/zenn-cli/utils/api/articles.ts
index 294e7f3..06bfc7f 100644
--- a/packages/zenn-cli/utils/api/articles.ts
+++ b/packages/zenn-cli/utils/api/articles.ts
@@ -29,7 +29,7 @@ export function getArticleBySlug(
 ): Article {
   const fullPath = path.join(
     articlesDirectory,
-    `${slug.replace(/\//g, "")}.md` // Prevent directory traversal
+    `${slug.replace(/[/\\]/g, "")}.md` // Prevent directory traversal
   );
   let fileRaw;
   try {
diff --git a/packages/zenn-cli/utils/api/books.ts b/packages/zenn-cli/utils/api/books.ts
index 25dca4c..b63ec70 100644
--- a/packages/zenn-cli/utils/api/books.ts
+++ b/packages/zenn-cli/utils/api/books.ts
@@ -89,7 +89,7 @@ function getCoverDataUrl(fullDirPath: string): string | null {
 }
 
 export function getBookBySlug(slug: string, fields?: null | string[]): Book {
-  const fullDirPath = path.join(booksDirectory, slug.replace(/\//g, "")); // Prevent directory traversal
+  const fullDirPath = path.join(booksDirectory, slug.replace(/[/\\]/g, "")); // Prevent directory traversal
   const data = getConfigYamlData(fullDirPath);
   if (!data) return null;
 
diff --git a/packages/zenn-cli/utils/api/chapters.ts b/packages/zenn-cli/utils/api/chapters.ts
index 91d878f..ae97ef6 100644
--- a/packages/zenn-cli/utils/api/chapters.ts
+++ b/packages/zenn-cli/utils/api/chapters.ts
@@ -44,8 +44,8 @@ export function getChapter(
   fields?: null | string[]
 ): Chapter {
   const fullPath = path.join(
-    getBookDirPath(bookSlug.replace(/\//g, "")), // Prevent directory traversal
-    `${position.replace(/\//g, "")}.md`
+    getBookDirPath(bookSlug.replace(/[/\\]/g, "")), // Prevent directory traversal
+    `${position.replace(/[/\\]/g, "")}.md`
   );
   let fileRaw;
   try {

```


## Supporting Material/References:

{F1007381}

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

It's possible to read arbitrary `.md` files from the victim's machine while the victim is running `zenn-cli`'s preview server.

## Attachments
- fix.patch
- zenn.mp4
