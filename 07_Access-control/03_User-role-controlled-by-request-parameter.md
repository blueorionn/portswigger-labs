# User role controlled by request parameter

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)

## Objective

This lab has an admin panel at `/admin`, which identifies administrators using a forgeable cookie.

Solve the lab by accessing the admin panel and using it to delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The application checks a cookie named `Admin` to determine whether the user has admin privileges. An authenticated session is not required — simply setting the cookie grants access.

### Step 1: Modify the cookie

Log in as `wiener:peter` and add the following cookie:

```http
Cookie: Admin=true
```

### Step 2: Access admin and delete carlos

Navigate to `/admin` — the panel is now accessible. Delete the user `carlos` to solve the lab.
