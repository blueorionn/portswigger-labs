# Information disclosure in error messages

**Lab Url**: [https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages)

## Objective

This lab's verbose error messages reveal that it is using a vulnerable version of a third-party framework. To solve the lab, obtain and submit the version number of this framework.

## Solution

The product page accepts a `productId` parameter. By supplying an unexpected value, we can trigger a verbose error that reveals the framework version.

### Step 1: Trigger an error

A non-existent product ID returns a standard 404 — no leak:

```bash
GET /product?productId=100
```

Now try a non-numeric value instead:

```bash
GET /product?productId=null
```

The application handles this poorly and returns an error message that includes the framework version: **Apache Struts 2 2.3.31**. Submit this version number to solve the lab.
