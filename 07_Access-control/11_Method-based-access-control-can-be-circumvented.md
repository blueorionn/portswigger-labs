# Method-based access control can be circumvented

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented](https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented)

## Objective

This lab implements access controls based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.

To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator.

## Solution

The admin role management endpoint (`/admin-roles`) is protected when accessed via POST, but accepts GET requests from any user.

### Step 1: Upgrade your role

Log in as `wiener:peter`. Send a GET request to `/admin-roles` with the parameters to upgrade your role:

```http
GET /admin-roles?username=wiener&action=upgrade
```

The response confirms the role change.

### Step 2: Delete carlos

Access the admin panel and delete the user `carlos` to solve the lab.
