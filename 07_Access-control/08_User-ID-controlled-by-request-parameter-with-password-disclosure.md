# User ID controlled by request parameter with password disclosure

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure)

## Objective

This lab has user account page that contains the current user's existing password, prefilled in a masked input.

To solve the lab, retrieve the administrator's password, then use it to delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The account page displays the user's current password in a masked input field. By changing the `id` parameter, we can view the administrator's password.

### Step 1: Retrieve the administrator's password

Log in as `wiener:peter` and change the `id` parameter to `administrator`:

```http
GET /my-account?id=administrator
```

The page source contains the administrator's password in a hidden or masked input field.

### Step 2: Login as administrator

Log out and log in as `administrator` with the retrieved password.

### Step 3: Delete carlos

Access the admin panel and delete the user `carlos` to solve the lab.
