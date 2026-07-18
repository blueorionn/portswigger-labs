# JWT authentication bypass via jku header injection

**Lab Url**: [https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jku-header-injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jku-header-injection)

## Objective

This lab uses a JWT-based mechanism for handling sessions. The server supports the `jku` parameter in the JWT header. However, it fails to check whether the provided URL belongs to a trusted domain before fetching the key.

To solve the lab, forge a JWT that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The server fetches the JWK Set from any URL specified in the `jku` parameter. We can host our own JWK Set on the exploit server.

### Step 1: Generate an RSA key pair

Generate a new RSA key pair and note its JWK representation.

### Step 2: Host the JWK Set on the exploit server

Create a JSON Web Key Set containing your public key and host it on the lab's exploit server:

```json
{
    "keys": [
        {
            "kty": "RSA",
            "e": "AQAB",
            "kid": "your-kid-value",
            "n": "your-modulus-value"
        }
    ]
}
```

### Step 3: Modify the JWT header

Set the `jku` parameter to the URL of your hosted JWK Set and the `kid` parameter to match the key's `kid`.

### Step 4: Modify the payload and sign

Change the `sub` claim to `administrator` and sign the token with your RSA private key.

### Step 5: Access admin and delete carlos

Use the forged token as your session cookie to access `/admin` and delete `carlos`.
