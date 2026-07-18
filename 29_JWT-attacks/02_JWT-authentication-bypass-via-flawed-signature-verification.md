# JWT authentication bypass via flawed signature verification

**Lab Url**: [https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification)

## Objective

This lab uses a JWT-based mechanism for handling sessions. The server is insecurely configured to accept unsigned JWTs.

To solve the lab, modify your session token to gain access to the admin panel at `/admin`, then delete the user carlos.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The server accepts JWTs with the algorithm set to `none`, meaning no signature is required.

### Step 1: Obtain a valid JWT

Log in as `wiener:peter` and capture the JWT session token.

### Step 2: Modify the header and payload

Change the JWT header's `alg` to `none`:

```json
{"alg":"none","typ":"JWT"}
```

Then decode the payload and change `sub` from `wiener` to `administrator`.

### Step 3: Re-encode with an empty signature

Re-encode the token using an empty signature (the part after the second dot is blank).

### Step 4: Access admin and delete carlos

Use the modified token as your session cookie. Access `/admin`, then delete `carlos` to solve the lab.
