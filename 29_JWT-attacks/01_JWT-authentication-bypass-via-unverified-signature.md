# JWT authentication bypass via unverified signature

**Lab Url**: [https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature)

## Objective

This lab uses a JWT-based mechanism for handling sessions. Due to implementation flaws, the server doesn't verify the signature of any JWTs that it receives.

To solve the lab, modify your session token to gain access to the admin panel at `/admin`, then delete the user carlos.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The server accepts any JWT without verifying its signature, so we can forge a token by simply changing the payload.

### Step 1: Obtain a valid JWT

Log in as `wiener:peter` and capture the JWT session token from the response.

### Step 2: Modify the payload

Decode the JWT payload and change the `sub` claim from `wiener` to `administrator`. Re-encode the token without touching the signature — the server doesn't check it anyway.

### Step 3: Access the admin panel

Use the modified token as your session cookie and request `/admin`. The server accepts the forged token and grants admin access.

### Step 4: Delete carlos

Send a request to `/admin/delete?username=carlos` with the same forged token to solve the lab.
