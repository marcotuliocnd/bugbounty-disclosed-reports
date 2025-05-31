# Bypass restrict of member subscription to use custom background in https://3d.cs.money without prime subscription

## Report Details
- **Report ID**: 989415
- **URL**: https://hackerone.com/reports/989415
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-23T15:49:32.868Z
- **Disclosed**: 2020-09-28T11:59:45.882Z

## Reporter
- **Username**: khoabda1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
In website https://3d.cs.money you need to subscribe prime to have a custom background for skin 

{F999661}

But with this vulnerability, we can use custom background without any fee required



## Steps To Reproduce:
[add details for how we can reproduce the issue]

- Grab a build of skin
- Save it. Modify request

```
POST /api/build/save HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json;charset=utf-8
Content-Length: 8197
Origin: https://3d.cs.money
Connection: close
Referer: https://3d.cs.money/item/1A0EmD0OCs
Cookie: __cfduid=dd4a5ae822200c2e5a6622942c8e9b5c61600828055; TEST_GROUP=6; UUID3D=z8yNnunP7rEULv4; _ga=GA1.1.123687832.1600828067; _ga_HY7CCPCD7H=GS1.1.1600870816.3.1.1600874988.52; _gid=GA1.2.745101638.1600828070; language=en; sellerid=2351662; theme=darkTheme; pro_version=false; tmr_reqNum=60; tmr_lvid=a86af86a1e546621ee998805dedf795e; tmr_lvidTS=1600829462593; _ym_uid=1600829464576681153; _ym_d=1600829464; prism_89846284=886529b3-1b72-491d-8e3e-fb061941ce6b; amplitude_id_222f15bd4f15cdfaee99c07bcc641e5fcs.money=eyJkZXZpY2VJZCI6ImJlNWM1YjhmLWE3OTQtNDZiNC1iMzg5LWU2MzljYThkZTNiNlIiLCJ1c2VySWQiOiI3NjU2MTE5ODM4OTQwODM5MiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMDg3MTY1Mzk0NywibGFzdEV2ZW50VGltZSI6MTYwMDg3MTY5NDEzMCwiZXZlbnRJZCI6MjYsImlkZW50aWZ5SWQiOjEzLCJzZXF1ZW5jZU51bWJlciI6Mzl9; _ym_isad=2; _fbp=fb.1.1600829468046.1736484188; csmoney_ga=GA1.2.348732095.1600829528; csmoney_ga_gid=GA1.2.929098124.1600829528; type_device=desktop; support_token=904edd01ef3c4b4fde31754954db74025c1ccfa067c1e9b78226f8aa1479ac75; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6IjU0MTdhZjg4LTE0NDgtNDg3NC05YmNkLTFmMjczOGIwY2EyZFIiLCJ1c2VySWQiOiI3NjU2MTE5ODM4OTQwODM5MiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMDg3MTM3MzEzMiwibGFzdEV2ZW50VGltZSI6MTYwMDg3NDgxMzYxMywiZXZlbnRJZCI6MTQzLCJpZGVudGlmeUlkIjozLCJzZXF1ZW5jZU51bWJlciI6MTQ2fQ==; amp_d77dd0=nCXsKPRaEaZ_9OrPDjz6cM...1eitodi6u.1eitpb9lt.0.0.0; amp_d77dd0_cs.money=nCXsKPRaEaZ_9OrPDjz6cM...1eitodi71.1eitpba7b.u.0.u; steamid=76561198389408392; avatar=https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/9e/9e972864d883f1b2e12cde94c8f83ef005c22438_medium.jpg; username=khoadeptrai; thirdparty_token=fa1cc1d8330558c52db7fa1347a93d94a6ec0586e67e8de6530ee506a15ac6df; _ym_visorc_62327980=w; _gat_UA-77178353-9=1; _gat_UA-77178353-1=1

{"data":{"_id":"5ef6558b28c55325932ac431","defindex":7,"paintindex":282,"rarity":5,"quality":4,"paintwear":1040943208,"paintseed":1,"origin":4,"dropreason":null,"floatvalue":0.13626253604888916,"is_stattrak":false,"assetid":"18947899176","uuid":"qd8OqzS","stickers":[],"time":1593202059096,"__v":0,"createdAt":1600586351204,"updatedAt":1600586351204,"item_name":"AK-47","skin_name":"Redline","wear_name":"Minimal Wear","rarity_name":"Classified","item_type":"Rifle","quality_name":"Unique","id":"5ef6558b28c55325932ac431","paint":{"name":"cu_ak47_cobra","description_string":"#PaintKit_cu_awp_cobra","description_tag":"#PaintKit_cu_awp_cobra_tag","style":"7","pattern":"ElegantREDV1.1","pattern_scale":"1.000000","phongexponent":"150","phongintensity":"10","ignore_weapon_size_scale":"1","only_first_material":"0","pattern_offset_x_start":"0.000000","pattern_offset_x_end":"0.000000","pattern_offset_y_start":"0.000000","pattern_offset_y_end":"0.000000","pattern_rotate_start":"0.000000","pattern_rotate_end":"0.000000","wear_remap_min":"0.100000","wear_remap_max":"0.700000"},"item":{"name":"weapon_ak47","prefab":"statted_item_base","item_quality":"unique","baseitem":"1","default_slot_item":"1","item_sub_position":"rifle1","item_class":"weapon_ak47","item_name":"#SFUI_WPNHUD_AK47","item_description":"#CSGO_Item_Desc_AK47","item_rarity":"common","image_inventory":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","model_player":"models/weapons/v_rif_ak47.mdl","model_world":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","model_dropped":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","icon_default_image":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","stickers":{"0":{"viewmodel_material":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","viewmodel_geometry":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","worldmodel_decal_pos":"6.43516 -1.26887 -0.743033"},"1":{"viewmodel_material":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","viewmodel_geometry":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","worldmodel_decal_pos":"6.43516 -1.47404 3.01389"},"2":{"viewmodel_material":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","viewmodel_geometry":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","worldmodel_decal_pos":"6.43516 -1.34147 7.33494"},"3":{"viewmodel_material":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","viewmodel_geometry":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","worldmodel_decal_pos":"6.43516 -1.31489 11.8284"}},"used_by_classes":{"terrorists":"1"},"attributes":{"magazine model":"models/weapons/w_rif_ak47_mag.mdl","primary reserve ammo max":"0","recovery time crouch":"1.000000","recovery time crouch final":"1.000000","recovery time stand":"1.000000","recovery time stand final":"1.000000","inaccuracy jump initial":"0.000000","inaccuracy jump":"0.000000","heat per shot":"0.250000","addon scale":"1.000000","tracer frequency":"0","max player speed":"1","is full auto":"0","in game price":"2700","armor ratio":"1","crosshair delta distance":"3","penetration":"1.000000","damage":"42","range":"8192.000000","cycletime":"0.150000","time to idle":"2.000000","flinch velocity modifier large":"1.000000","flinch velocity modifier small":"1.000000","spread":"0.000000","inaccuracy crouch":"0.000000","inaccuracy stand":"0.000000","inaccuracy land":"0.000000","inaccuracy ladder":"0.000000","inaccuracy fire":"0.000000","inaccuracy move":"0.000000","recoil angle":"0.000000","recoil angle variance":"0.000000","recoil magnitude":"0.000000","recoil magnitude variance":"0.000000","recoil seed":"223","primary clip size":"-1","weapon weight":"0","rumble effect":"-1","inaccuracy crouch alt":"0.000000","inaccuracy fire alt":"0.000000","inaccuracy jump alt":"0.000000","inaccuracy ladder alt":"0.000000","inaccuracy land alt":"0.000000","inaccuracy move alt":"0.000000","inaccuracy stand alt":"0.000000","max player speed alt":"1","recoil angle alt":"0.000000","recoil angle variance alt":"0.000000","recoil magnitude alt":"0.000000","recoil magnitude variance alt":"0.000000","spread alt":"0.000000","stattrak model":"models/weapons/stattrack.mdl","recovery transition start bullet":"0","recovery transition end bullet":"0","allow hand flipping":"1","attack movespeed factor":"1.000000","bot audible range":"2000.000000","bullets":"1","cannot shoot underwater":"0","crosshair min distance":"4","cycletime alt":"0.300000","has burst mode":"0","has silencer":"0","hide view model zoomed":"0","idle interval":"20","inaccuracy jump apex":"0.000000","inaccuracy reload":"0.000000","inaccuracy pitch shift":"0.000000","inaccuracy alt sound threshold":"0.000000","is melee weapon":"0","is revolver":"0","itemflag select on empty":"0","itemflag no auto reload":"0","itemflag no auto switch empty":"0","itemflag limit in world":"0","itemflag exhaustible":"0","itemflag do hit location dmg":"0","itemflag no ammo pickups":"0","itemflag no item pickup":"0","kill award":"300","model right handed":"1","primary default clip size":"-1","range modifier":"0.980000","spread seed":"0","secondary clip size":"-1","secondary default clip size":"-1","secondary reserve ammo max":"0","unzoom after shot":"0","zoom fov 1":"90","zoom fov 2":"90","zoom levels":"0","zoom time 0":"0","zoom time 1":"0","zoom time 2":"0"},"inventory_image_data":{"camera_angles":"2.0 -130.0 0.0","camera_offset":"0.0 1.0 -2.0","camera_fov":"35.000000","override_default_light":"1","spot_light_key":{"position":"-120 120 180","color":"2 2.1 2.3","lookat":"0.0 0.0 0.0","inner_cone":"0.500000","outer_cone":"1.000000"},"spot_light_rim":{"position":"10.0 -90.0 -60.0","color":"3 5 5","lookat":"0.0 0.0 0.0","inner_cone":"0.040000","outer_cone":"0.500000"}},"paint_data":{"paintablematerial0":{"name":"rif_ak47","origmat":"ak47","viewmodeldim":"2048","worlddim":"512","basetextureoverride":"0","weaponlength":"37.746201","uvscale":"0.549000","vmt":{"baseTexture":"rif_ak47/ak47","phong":"1","phongboost":"2","phongalbedoboost":"35","phongfresnelranges":"[.83 .83 1]","phongexponenttexture":"rif_ak47/ak47_exponent","basemapalphaphongmask":"1","envmap":"env_cubemap","envmapfresnel":"1","envmaptint":"[.1 .1 .1]","phongalbedotint":"1","phongdisablehalflambert":"1"}}},"visuals":{"muzzle_flash_effect_1st_person":"weapon_muzzle_flash_assaultrifle","muzzle_flash_effect_3rd_person":"weapon_muzzle_flash_assaultrifle","heat_effect":"weapon_muzzle_smoke","addon_location":"primary_rifle","eject_brass_effect":"weapon_shell_casing_rifle","tracer_effect":"weapon_tracers_assrifle","weapon_type":"Rifle","player_animation_extension":"ak","primary_ammo":"BULLET_PLAYER_762MM","sound_single_shot":"Weapon_AK47.Single","sound_nearlyempty":"Default.nearlyempty"},"item_type_name":"#CSGO_Type_Weapon","item_slot":"rifle","inv_group_equipment":"rifle","mouse_pressed_sound":"weapons/m4a1/m4a1_clipout.wav","drop_sound":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","item_gear_slot":"primary","item_gear_slot_position":"0","capabilities":{"nameable":"1","paintable":"1","can_sticker":"1","can_stattrack_swap":"1"},"craft_class":"weapon","craft_material_type":"weapon","min_ilevel":"1","max_ilevel":"1","image_inventory_size_w":"128","image_inventory_size_h":"82"},"stickerBase":{"0":{"aotexture":"https://webhook.site/d0aef653-d8b8-4010-9810-72b277e8238c","wearremapmin":"0.64","wearremapmid":"1.0","wearremapmax":"0.98","wearwidthmin":"0.12","wearwidthmax":"0.04","hlmvallowedit":"1"},"1":{"aotexture":"rif_ak47/rif_ak47_decal_b","wearremapmin":"0.58","wearremapmid":"0.92","wearremapmax":"0.98","wearwidthmin":"0.12","wearwidthmax":"0.04","hlmvallowedit":"1"},"2":{"aotexture":"rif_ak47/rif_ak47_decal_c","wearremapmin":"0.7","wearremapmid":"0.86","wearremapmax":"0.98","wearwidthmin":"0.12","wearwidthmax":"0.04","hlmvallowedit":"1"},"3":{"aotexture":"rif_ak47/rif_ak47_decal_d","wearremapmin":"0.74","wearremapmid":"0.94","wearremapmax":"0.98","wearwidthmin":"0.12","wearwidthmax":"0.04","hlmvallowedit":"1"}}},"name":"c1c","background":"http://LINK_CUSTOM_BACKGROUND","parent":"qd8OqzS","backgroundFilters":{"Exposure":50,"Contrast":50,"Saturation":50}}
```

- Change the background parameter in json to the link of custom background you want


PoC
https://3d.cs.money/item/xALqKJVBdC

## Impact

Bypass restrict of member subscription

## Attachments
- Screenshot_2.png
