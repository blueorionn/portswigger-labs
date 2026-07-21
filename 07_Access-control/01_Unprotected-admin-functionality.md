# Unprotected admin functionality

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality)

## Objective

This lab has an unprotected admin panel.

Solve the lab by deleting the user `carlos`.

## Solution

The admin panel location is disclosed in `robots.txt`, and the panel itself has no access control.

### Step 1: Find the admin panel

```http
GET /robots.txt
```

The response reveals the path to the admin panel.

### Step 2: Delete carlos

Navigate to the admin panel and delete the user `carlos` to solve the lab.
