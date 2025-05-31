# Unchecked weapon id in WeaponList message parser on client leads to RCE

## Report Details
- **Report ID**: 513154
- **URL**: https://hackerone.com/reports/513154
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-03-21T13:30:56.037Z
- **Disclosed**: 2019-09-17T17:34:14.845Z

## Reporter
- **Username**: nyancat0131
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
Let's look at WeaponList message parser code in the HLSDK:
``` cpp
int CHudAmmo::MsgFunc_WeaponList(const char *pszName, int iSize, void *pbuf )
{
	BEGIN_READ( pbuf, iSize );
	
	WEAPON Weapon;

	strcpy( Weapon.szName, READ_STRING() );
	Weapon.iAmmoType = (int)READ_CHAR();	
	
	Weapon.iMax1 = READ_BYTE();
	if (Weapon.iMax1 == 255)
		Weapon.iMax1 = -1;

	Weapon.iAmmo2Type = READ_CHAR();
	Weapon.iMax2 = READ_BYTE();
	if (Weapon.iMax2 == 255)
		Weapon.iMax2 = -1;

	Weapon.iSlot = READ_CHAR();
	Weapon.iSlotPos = READ_CHAR();
	Weapon.iId = READ_CHAR();
	Weapon.iFlags = READ_BYTE();
	Weapon.iClip = 0;

	gWR.AddWeapon( &Weapon );

	return 1;
}
```

And `WeaponResource::AddWeapon`:

``` cpp
void AddWeapon( WEAPON *wp ) 
{ 
		rgWeapons[ wp->iId ] = *wp;	
		LoadWeaponSprites( &rgWeapons[ wp->iId ] );
}
```
There are no boundary check, and the range of `iId` is `[-128, 128)`, so I can modify many things in the data section.

In `client.dll`, there's an object called `gEngfuncs`, it is a function table that has various functions of the engine. After some calculations on latest CS 1.6 `client.dll`, I concluded that this function table could be overwritten using the above bug.

I have attached a PoC that will pop `calc.exe` on latest CS 1.6 client when connected to malicious server. The AMXX plugin will catch `InitHUD` message, and send crafted `WeaponList` message to overwrite the address of function used in `HUD_DirectorMessage` to execute client cmds to a ROP gadget that will trigger the chain sent in the next `SendCmd` call. To overwrite that address, I used a crafted weapon sprite list (`weapon_pwn.txt`) (see `WEAPON` struct, file `cl_dll/ammo.h` in the HLSDK).

## Impact

Since it's RCE, attacker can do almost anything that don't require higher privilege (ex. compromise account, inject malware, ...)

## Attachments
- poc_calc_pop.zip
- poc_calc_pop.sma
- weapon_pwn.txt
