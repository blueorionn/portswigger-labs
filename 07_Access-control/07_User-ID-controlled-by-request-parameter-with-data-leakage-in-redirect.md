# User ID controlled by request parameter with data leakage in redirect

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect)

## Objective

This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.

To solve the lab, obtain the API key for the user `carlos` and submit it as the solution.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The application redirects when accessing another user's account, but the response body still contains the target user's data before the redirect is followed.

### Step 1: Capture Carlos's data from the redirect

Log in as `wiener:peter` and send a request to Carlos's account page without following the redirect:

```http
GET /my-account?id=carlos
```

The response includes a `302` redirect to `/login`, but Carlos's API key is present in the response body.

### Step 2: Submit Carlos's API key

Copy Carlos's API key from the response and submit it to solve the lab.
