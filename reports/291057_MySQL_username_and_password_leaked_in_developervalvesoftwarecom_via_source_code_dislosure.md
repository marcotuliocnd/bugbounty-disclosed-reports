# MySQL username and password leaked in developer.valvesoftware.com via source code dislosure

## Report Details
- **Report ID**: 291057
- **URL**: https://hackerone.com/reports/291057
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-17T02:02:14.122Z
- **Disclosed**: 2018-05-07T21:26:56.816Z

## Reporter
- **Username**: nahamsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
Hey there it looks like you are relying on a script that cleans up your backup process on developer.valvesoftware.com:

`/scripts/final_cleanup.sh`:

```
# Remove files post cleanup
rm -r ${SITEPATH}/data
rm ${SITEPATH}/*.sql
rm ${SITEPATH}/*.sql.gz
rm ${SITEPATH}/*.tgz
rm ${SITEPATH}/*.tar.gz
rm ${SITEPATH}/*.log
rm -r ${SITEPATH}/w_${OLD_VER}
rm ${SITEPATH}/*.sh
```

But they forgot about `/scripts/`itself where it's also allowing a directory listing to see it contents. 

https://developer.valvesoftware.com/scripts/:

```
[TXT]	content_fixes.sh	2009-01-15 23:19	2.3K	 
[TXT]	create_current_xml_dump.sh	2009-01-14 04:08	775	 
[TXT]	custom_settings.sh	2009-01-16 09:48	1.1K	 
[TXT]	database_drop_all_tables.sh	2009-01-16 03:35	355	 
[TXT]	database_export_dump.sh	2009-06-10 21:55	353	 
[TXT]	database_export_latin1_gz_dump.sh	2009-06-10 23:36	363	 
[TXT]	database_import_dump.sh	2009-06-11 00:19	267	 
[   ]	database_rebuildrecentchanges.php	2009-06-17 21:46	374	 
[TXT]	database_set_priv.sh	2009-06-11 20:28	665	 
[TXT]	database_test_backup.sh	2009-06-10 21:44	741	 
[TXT]	database_test_export.sh	2009-01-16 03:35	362	 
[TXT]	database_test_import.sh	2009-01-16 03:36	293	 
[TXT]	filesystem_copy_new_version.sh	2009-06-18 19:38	1.0K	 
[TXT]	filesystem_create_backup.sh	2009-06-10 21:40	473	 
[TXT]	filesystem_restore_backup.sh	2009-06-10 22:34	1.1K	 
[TXT]	final_cleanup.sh	2009-01-13 00:52	665	 
[TXT]	import_temp.sh	2009-06-11 00:17	4.8K	 
[TXT]	import_wiki.sh	2009-06-11 20:19	5.0K	 
[TXT]	interwiki_update.sh	2009-01-12 03:08	1.2K	 
[TXT]	update_wiki.sh	2009-06-18 19:43	2.0K	 
[TXT]	wiki_setup.sh	2011-04-29 01:19	1.7K	 
```

From `scripts/wiki_setup.sh`:

```
# mysql
DBUSER='█████████'			# SQL user to do the work
DBPASS='██████████'		# Password for the SQL user
HOSTNAME='██████████'		# Name of the SQL database host
WIKIDB='███'			# When making backups, export this database name, like ██████████
WIKIDBSRC='████████'		# When restoring backups from another wiki, use this database, like ██████████
WIKIUSER='████████'		# Name of the wiki db user specified in LocalSettings.php
WIKIPASS='██████████'	# Wiki db user password
```

Thanks,
Ben

## Attachments
No attachments
