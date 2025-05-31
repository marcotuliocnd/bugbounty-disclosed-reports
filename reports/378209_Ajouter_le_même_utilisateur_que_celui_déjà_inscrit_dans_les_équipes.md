# Ajouter le même utilisateur que celui déjà inscrit dans les équipes

## Report Details
- **Report ID**: 378209
- **URL**: https://hackerone.com/reports/378209
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-07-06T14:29:04.296Z
- **Disclosed**: 2018-07-17T20:07:40.756Z

## Reporter
- **Username**: rbcafe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Description:**

Possibilité d'ajouter le même utilisateur que celui déjà inscrit dans les équipes.

### Steps To Reproduce

1. Aller sur https://hackerone.com/team_name/team_members
2. Observer les emails des utilisateurs.
3. Utiliser le même email que celui précédemment inscrit, mais varier les majuscules / minuscules .
4. On remarque qu'il est possible d'ajouter la même adresse que celle déjà inscrite.

### Optional: Your Environment (Browser version, Device, etc)

 * Firefox 

### Optional: Supporting Material/References (Screenshots)

 * ██████████

### FIX ###

* Ajouter du grep sur l'email.

Cordialement

Rbcafe

## Impact

- Consommation serveur inutile.
- Bypass des emails déjà existants.
- Bypass du contrôle des emails déjà existants.

## Attachments
No attachments
