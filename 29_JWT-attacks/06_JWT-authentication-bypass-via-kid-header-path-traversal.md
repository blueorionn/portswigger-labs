# JWT authentication bypass via kid header path traversal

**Lab Url**: [https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-kid-header-path-traversal](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-kid-header-path-traversal)

## Objective

This lab uses a JWT-based mechanism for handling sessions. In order to verify the signature, the server uses the `kid` parameter in JWT header to fetch the relevant key from its filesystem.

To solve the lab, forge a JWT that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The server reads the file specified by the `kid` parameter to obtain the verification key. By setting `kid` to a known empty file (`/dev/null`), we can use a known empty key to sign a forged token.

### Step 1: Create a symmetric key from an empty file

Create a symmetric key in your JWT editor with a Base64-encoded empty value (`A==`).

### Step 2: Modify the JWT header and payload

Set the `kid` parameter to a path traversal value that resolves to an empty file on the server:

```json
{
    "alg": "HS256",
    "typ": "JWT",
    "kid": "/dev/null"
}
```

Change the `sub` claim from `wiener` to `administrator`.

### Step 3: Sign and send

Sign the token with your empty symmetric key. Use the forged token to access `/admin` and delete `carlos`.
