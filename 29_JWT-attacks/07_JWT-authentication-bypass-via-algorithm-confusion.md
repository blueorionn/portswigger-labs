# JWT authentication bypass via algorithm confusion

**Lab Url**: [https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion)

## Objective

This lab uses a JWT-based mechanism for handling sessions. It uses a robust RSA key pair to sign and verify tokens. However, due to implementation flaws, this mechanism is vulnerable to algorithm confusion attacks.

To solve the lab, first obtain the server's public key. This is exposed via a standard endpoint. Use this key to sign a modified session token that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The server verifies JWTs using the algorithm specified in the header. By changing `alg` from `RS256` to `HS256` and using the server's own public key as the HMAC secret, we can forge a valid token.

### Step 1: Retrieve the public key

The server exposes its public key at a standard endpoint:

```bash
GET /jwks.json
```

Copy the JWK object for the RSA key.

### Step 2: Create a symmetric key from the public key

Import the JWK into your JWT editor as an RSA key, then export it as PEM. Base64-encode the PEM and create a new symmetric key using this encoded PEM as the `k` parameter.

### Step 3: Forge the token

Change the JWT header's `alg` to `HS256`, modify the `sub` claim to `administrator`, and sign the token using the symmetric key created in the previous step.

### Step 4: Access admin and delete carlos

Use the forged token as your session cookie to access `/admin` and delete `carlos`.
