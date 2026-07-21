# URL-based access control can be circumvented

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented](https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented)

## Objective

This website has an unauthenticated admin panel at `/admin`, but a front-end system has been configured to block external access to that path. However, the back-end application is built on a framework that supports the `X-Original-URL` header.

To solve the lab, access the admin panel and delete the user `carlos`.

## Solution

The application uses the `X-Original-URL` header to route requests internally. By sending a request to a non-existent path with the target path in the header, we can bypass access controls.

### Step 1: Access the admin panel

Send a GET request to a non-existent path with the `X-Original-URL` header set to `/admin`:

```http
GET / HTTP/1.1
X-Original-URL: /admin
```

The admin panel loads successfully.

### Step 2: Delete carlos

From the admin panel, identify the delete URL. Then send a request with the `username` parameter:

```http
GET /?username=carlos HTTP/1.1
X-Original-URL: /admin/delete
```

The user `carlos` is deleted, solving the lab.
