# JWT authentication bypass via jwk header injection

**Lab Url**: [https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jwk-header-injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jwk-header-injection)

## Objective

This lab uses a JWT-based mechanism for handling sessions. The server supports the `jwk` parameter in the JWT header. This is sometimes used to embed the correct verification key directly in the token. However, it fails to check whether the provided key came from a trusted source.

To solve the lab, modify and sign a JWT that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The server trusts any JWK embedded in the JWT header, allowing us to forge a token signed with our own RSA key.

### Step 1: Generate an RSA key pair

Generate a new RSA key pair. Copy the JWK representation of the public key.

### Step 2: Inject the JWK into the JWT header

Modify the JWT header to include the `jwk` parameter with your public key. Remove any existing `kid` parameter. The header should look like:

```json
{
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "n": "your-modulus-value",
        ...
    }
}
```

### Step 3: Modify the payload

Change the `sub` claim from `wiener` to `administrator`.

### Step 4: Sign and send

Sign the token with your RSA private key. Use the forged token as your session cookie to access `/admin` and delete `carlos`.
