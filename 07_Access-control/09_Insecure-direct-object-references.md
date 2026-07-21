# Insecure direct object references

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)

## Objective

This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.

Solve the lab by finding the password for the user `carlos`, and logging into their account.

## Solution

The live chat feature allows you to download chat transcripts. The transcript files are sequentially numbered and accessible without authentication.

### Step 1: Download a chat transcript

Open the live chat and click **View transcript**. The transcript is downloaded from a URL like:

```http
GET /download-transcript/2.txt
```

The transcript contains a conversation that reveals Carlos's password.

### Step 2: Login as carlos

Log in as `carlos` with the retrieved password to solve the lab.
