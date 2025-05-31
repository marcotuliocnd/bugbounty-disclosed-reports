# No SearchEngine sanatizing can lead to command injection

## Report Details
- **Report ID**: 495382
- **URL**: https://hackerone.com/reports/495382
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-13T16:43:45.535Z
- **Disclosed**: 2019-06-06T00:47:37.060Z

## Reporter
- **Username**: mrnbayoh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: notepad-plus-plus

## Vulnerability Information
##Information:
**Summary:** 
Notepad++ is vulnerable to a command injection vulnerability.

**Debug Info:**
Notepad++ v7.6.3 (32-bit)
Build time : Jan 27 2019 - 17:20:30
Path : C:\Program Files (x86)\Notepad++\notepad++.exe
Admin mode : ON
Local Conf mode : OFF
OS : Windows 10 (64-bit)
Plugins : none

**Description:**

When launching the web browser with the defined `SearchEngine`, the specified URL is directly passed as a command to `ShellExecute`. However since there is no check, one can put commands in that field instead of URLs.

Relevant piece of code in `NppCommands.cpp`:
```
case IDM_EDIT_SEARCHONINTERNET:
		{
			if (_pEditView->execute(SCI_GETSELECTIONS) != 1) // Multi-Selection || Column mode || no selection
				return;

			const NppGUI & nppGui = (NppParameters::getInstance())->getNppGUI();
			generic_string url;
			if (nppGui._searchEngineChoice == nppGui.se_custom)
			{
				if (nppGui._searchEngineCustom.empty())
				{
					url = TEXT("https://www.google.com/search?q=$(CURRENT_WORD)");
				}
				else
				{
					url = nppGui._searchEngineCustom.c_str();
				}
			}
			else if (nppGui._searchEngineChoice == nppGui.se_duckDuckGo)
			{
				url = TEXT("https://duckduckgo.com/?q=$(CURRENT_WORD)");
			}
			else if (nppGui._searchEngineChoice == nppGui.se_google)
			{
				url = TEXT("https://www.google.com/search?q=$(CURRENT_WORD)");
			}
			else if (nppGui._searchEngineChoice == nppGui.se_bing)
			{
				url = TEXT("https://www.bing.com/search?q=$(CURRENT_WORD)");
			}
			else if (nppGui._searchEngineChoice == nppGui.se_yahoo)
			{
				url = TEXT("https://search.yahoo.com/search?q=$(CURRENT_WORD)");
			}

			Command cmd(url.c_str());
			cmd.run(_pPublicInterface->getHSelf());	
		}
``` 

## Steps To Reproduce:

  1. Go to `Settings->Search Engine` in the text box write `cmd /K echo boom`
  2. Click on `Edit->On Selection->Search on Internet`
  3. A command prompt is launched and `echo boom` is executed

## Impact

Arbitrary commands execution.

## Attachments
No attachments
