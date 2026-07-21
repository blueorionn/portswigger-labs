# User ID controlled by request parameter

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)

## Objective

This lab has a horizontal privilege escalation vulnerability on the user account page.

To solve the lab, obtain the API key for the user `carlos` and submit it as the solution.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The account page uses an `id` parameter to identify the user. Changing this parameter lets us access other users' data.

### Step 1: Access Carlos's account page

Log in as `wiener:peter`. Change the `id` parameter in the URL from `wiener` to `carlos`:

```http
GET /my-account?id=carlos
```

### Step 2: Submit Carlos's API key

The page displays Carlos's API key. Copy and submit it to solve the lab.
