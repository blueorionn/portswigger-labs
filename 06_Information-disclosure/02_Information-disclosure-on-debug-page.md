# Information disclosure on debug page

**Lab Url**: [https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page)

## Objective

This lab contains a debug page that discloses sensitive information about the application. To solve the lab, obtain and submit the `SECRET_KEY` environment variable.

## Solution

The home page's HTML source contains a commented-out link to a debug page. This reveals a sensitive endpoint that exposes application secrets.

### Step 1: View the page source

Inspect the HTML source of the home page. A comment reveals a hidden link:

```html
<!-- <a href=/cgi-bin/phpinfo.php>Debug</a> -->
```

### Step 2: Access the debug page

Navigate to the discovered endpoint:

```bash
GET /cgi-bin/phpinfo.php
```

The `phpinfo` page displays PHP configuration details, including a **SECRET_KEY** value.

![Php InfoPage](img/php-info-page.png)

### Step 3: Submit the secret key

Find the `SECRET_KEY` in the `phpinfo` output and submit it to solve the lab.
