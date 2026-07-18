# JWT authentication bypass via weak signing key

**Lab Url**: [https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key)

## Objective

This lab uses a JWT-based mechanism for handling sessions. It uses an extremely weak secret key to both sign and verify tokens. This can be easily brute-forced using a [wordlist of common secrets](../wordlist/jwt.secrets.list).

To solve the lab, first brute-force the website's secret key. Once you've obtained this, use it to sign a modified session token that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The JWT uses the HS256 algorithm (symmetric key). The signing key is weak and can be brute-forced.

### Step 1: Brute-force the secret key

Extract the JWT token from your session and brute-force the secret using hashcat with a JWT secret wordlist:

```bash
hashcat -a 0 -m 16500 <YOUR-JWT> /path/to/jwt.secrets.list
```

The cracked secret is `secret1`.

### Step 2: Create a signing key

Base64-encode the secret (`secret1`) and create a symmetric key in your JWT editor with the encoded value as the `k` parameter.

### Step 3: Forge the admin token

Modify the `sub` claim from `wiener` to `administrator` and sign the token with your newly created symmetric key.

### Step 4: Access admin and delete carlos

Use the forged token to access `/admin` and delete `carlos` to solve the lab.
