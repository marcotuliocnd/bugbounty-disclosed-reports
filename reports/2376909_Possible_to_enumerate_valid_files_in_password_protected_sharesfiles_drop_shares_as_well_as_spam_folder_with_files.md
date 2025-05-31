# Possible to enumerate valid files in password protected shares/files drop shares as well as spam folder with files

## Report Details
- **Report ID**: 2376909
- **URL**: https://hackerone.com/reports/2376909
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-02-17T02:39:41.667Z
- **Disclosed**: 2025-02-21T10:39:25.700Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
It is possible possible to enumerate valid files in password protected shares/files drop shares as well as spam the folder with empty files with an attacker controlled file name.

## Steps To Reproduce:
1. Create a folder and create the file `foo.txt` in it
2. Share the file publicly and mark it as Files Drops and Password Protected (the combination is not necessary, but simplifies the testing)
3. As attacker send a request to `DocumentAPIController#create` to enumerate the valid files
4. As attacker send a request to `DocumentAPIController#create` to spam files

I've attached screenshots of these two behaviours here:

{F3055801}

{F3055802}

## Supporting Material/References:

[`DocumentAPIController#create`](https://github.com/nextcloud/richdocuments/blob/24cc1ec714f63b36a823f1f614723f9676abc76d/lib/Controller/DocumentAPIController.php#L70-L149)  is not validating whether the share is writable, upload only or password protected:

```php
	public function create(string $mimeType, string $fileName, string $directoryPath = '/', ?string $shareToken = null, ?int $templateId = null): JSONResponse {
		try {
			if ($shareToken !== null) {
				$share = $this->shareManager->getShareByToken($shareToken);
			}

			$rootFolder = $shareToken !== null ? $share->getNode() : $this->rootFolder->getUserFolder($this->userId);
			$folder = $rootFolder->get($directoryPath);

			if (!($folder instanceof Folder)) {
				throw new Exception('Node is not a folder');
			}
		} catch (Throwable $e) {
			$this->logger->error('Failed to create document', ['exception' => $e]);
			return new JSONResponse([
				'status' => 'error',
				'message' => $this->l10n->t('Cannot create document')
			], Http::STATUS_BAD_REQUEST);
		}

		$basename = $this->l10n->t('New Document.odt');
		switch ($mimeType) {
			case 'application/vnd.oasis.opendocument.spreadsheet':
				$basename = $this->l10n->t('New Spreadsheet.ods');
				break;
			case 'application/vnd.oasis.opendocument.presentation':
				$basename = $this->l10n->t('New Presentation.odp');
				break;
			case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
				$basename = $this->l10n->t('New Document.docx');
				break;
			case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
				$basename = $this->l10n->t('New Spreadsheet.xlsx');
				break;
			case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
				$basename = $this->l10n->t('New Presentation.pptx');
				break;
			default:
				break;
		}

		if (!$fileName) {
			$fileName = Helper::getNewFileName($folder, $basename);
		}

		if ($folder->nodeExists($fileName)) {
			return new JSONResponse([
				'status' => 'error',
				'message' => $this->l10n->t('File already exists')
			], Http::STATUS_BAD_REQUEST);
		}

		try {
			$file = $folder->newFile($fileName);
			$templateType = $this->templateManager->getTemplateTypeForExtension(pathinfo($fileName, PATHINFO_EXTENSION));

			$empty = $this->templateManager->getEmpty($templateType);
			$templateFile = array_shift($empty);

			if ($templateId) {
				$templateFile = $this->templateManager->get($templateId);
			}

			$file->putContent($this->templateManager->getEmptyFileContent($file->getExtension()));
			if ($this->templateManager->isSupportedTemplateSource($templateFile->getExtension())) {
				// Only use TemplateSource if supported filetype
				$this->templateManager->setTemplateSource($file->getId(), $templateFile->getId());
			}
		} catch (Exception $e) {
			$this->logger->error('Failed to create file from template', ['exception' => $e]);
			return new JSONResponse([
				'status' => 'error',
				'message' => $this->l10n->t('Not allowed to create document')
			], Http::STATUS_BAD_REQUEST);
		}
		return new JSONResponse([
			'status' => 'success',
			'data' => \OCA\Files\Helper::formatFileInfo($file->getFileInfo())
		]);
}
```

## Impact

It is possible possible to enumerate valid files in password protected shares/files drop shares as well as spam the folder with empty files with an attacker controlled file name.

## Attachments
- enumerate-share.png
- create-spam-file.png
