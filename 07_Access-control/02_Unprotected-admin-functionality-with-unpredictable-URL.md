# Unprotected admin functionality with unpredictable URL

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url)

## Objective

This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

Solve the lab by accessing the admin panel, and using it to delete the user `carlos`.

## Solution

The home page contains a JavaScript snippet that reveals the admin panel's URL.

### Step 1: Find the admin URL

View the page source of the home page. A script tag contains the admin panel link:

```html
<script>
    var isAdmin = false;
    if (isAdmin) {
        var adminPanelTag = document.createElement('a');
        adminPanelTag.setAttribute('href', '/admin-35z3lc');
        ...
    }
</script>
```

The `href` attribute contains the admin panel path: `/admin-35z3lc`.

### Step 2: Delete carlos

Navigate to the admin panel and delete the user `carlos` to solve the lab.
