# Multi-step process with no access control on one step

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step](https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step)

## Objective

This lab has an admin panel with a flawed multi-step process for changing a user's role. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.

To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator.

## Solution

The role change process requires two steps: an initial request and a confirmation with `confirm=true`. The confirmation step lacks proper authorization checks.

### Step 1: Confirm the role change

Log in as `wiener:peter`. Send a POST request to `/admin-roles` with the `confirm=true` parameter:

```http
POST /admin-roles
...
username=wiener&action=upgrade&confirm=true
```

The role change succeeds despite lacking admin privileges.

### Step 2: Delete carlos

Access the admin panel and delete the user `carlos` to solve the lab.
