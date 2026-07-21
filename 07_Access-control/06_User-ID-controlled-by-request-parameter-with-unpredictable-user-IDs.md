# User ID controlled by request parameter with unpredictable user IDs

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids)

## Objective

This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

To solve the lab, find the GUID for `carlos`, then submit his API key as the solution.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The application uses GUIDs instead of usernames in the `id` parameter. However, Carlos's GUID is leaked in a blog post.

### Step 1: Find Carlos's GUID

Browse the blog posts and look for the author section. Carlos's user GUID is displayed there.

### Step 2: Access Carlos's account page

Replace the `id` parameter with Carlos's GUID:

```http
GET /my-account?id=CARLOS-GUID
```

### Step 3: Submit Carlos's API key

The page displays Carlos's API key. Copy and submit it to solve the lab.
