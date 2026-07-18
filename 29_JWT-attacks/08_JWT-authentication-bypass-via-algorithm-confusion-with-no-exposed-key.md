# JWT authentication bypass via algorithm confusion with no exposed key

**Lab Url**: [https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key)

## Objective

This lab uses a JWT-based mechanism for handling sessions. It uses a robust RSA key pair to sign and verify tokens. However, due to implementation flaws, this mechanism is vulnerable to algorithm confusion attacks.

To solve the lab, first obtain the server's public key. Use this key to sign a modified session token that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The public key is not directly exposed, but we can recover it from two or more valid JWTs using the `sig2n` technique.

### Step 1: Collect two JWT tokens

Log in as `wiener:peter` and capture the JWT. Log out, log in again, and capture a second JWT. Two tokens signed with the same private key are sufficient to recover the public key.

### Step 2: Recover the public key

Use the `sig2n` tool to extract candidate public keys:

```bash
docker run --rm -it portswigger/sig2n <token1> <token2>
```

The tool outputs several candidate X.509 and PKCS1 keys, along with tampered JWTs signed with each.

### Step 3: Identify the correct key

Replace your session cookie with each tampered JWT and try accessing `/my-account`. A successful response (`200`) identifies the correct key. A redirect to `/login` means try the next candidate.

### Step 4: Create a symmetric key

Copy the Base64-encoded X.509 key (not the tampered JWT) and create a new symmetric key in your JWT editor using it as the `k` parameter.

### Step 5: Forge the admin token

Set `alg` to `HS256`, change `sub` to `administrator`, and sign the token with the symmetric key.

### Step 6: Access admin and delete carlos

Use the forged token to access `/admin` and delete `carlos`.
