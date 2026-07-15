# 2FA simple bypass

**Lab Url**: [https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass)

## Objective

This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.

- Your credentials: `wiener:peter`
- Victim's credentials: `carlos:montoya`

## Solution

The 2FA implementation is flawed — the application creates an authenticated session **before** the 2FA code is verified. The `/login2` page asks for a 4-digit security code, but this is merely a UI gate, not a real security boundary. The session is already valid; skipping the code page is all it takes.

### Step 1: Log in with Carlos's credentials

POST the credentials to `/login`:

```bash
POST /login HTTP/1.1
...
username=carlos&password=montoya
```

The server accepts the login and redirects to the 2FA verification page (`/login2`).

### Step 2: Bypass the 2FA page

Instead of entering a verification code, simply change the URL in your browser from `/login2` to `/my-account`. The server never checks whether the 2FA code was actually supplied — the session is already authenticated. The account page loads immediately, and the lab is solved.
