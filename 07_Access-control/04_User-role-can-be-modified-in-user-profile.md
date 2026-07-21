# User role can be modified in user profile

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile](https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile)

## Objective

This lab has an admin panel at `/admin`. It's only accessible to logged-in users with a `roleid` of 2.

Solve the lab by accessing the admin panel and using it to delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The user profile update endpoint accepts a JSON payload that includes the `roleId` field. By setting `roleId` to `2`, we can escalate our privileges.

### Step 1: Update the role

Log in as `wiener:peter`. Send a POST request to `/my-account/change-email` with the following JSON payload:

```json
{"email":"test@test.com","roleId":2}
```

The server updates the role and returns a response confirming the change.

### Step 2: Access admin and delete carlos

Navigate to `/admin` — the panel is now accessible. Delete the user `carlos` to solve the lab.
