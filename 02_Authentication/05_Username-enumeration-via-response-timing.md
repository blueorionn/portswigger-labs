# Username enumeration via response timing

**Lab Url**: [https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing)

## Objective

This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

- Your credentials: `wiener:peter`
- [Candidate usernames](../wordlist/usernames.txt)
- [Candidate passwords](../wordlist/passwords.txt)

## Solution

The login page checks the password only if the username is valid. By sending an extremely long password (10,000+ characters), the password-hashing operation causes a measurable delay on the server for valid usernames. Invalid usernames are rejected immediately and respond quickly.

A WAF enforces IP-based brute-force protection, so we spoof the `X-Forwarded-For` header with a random value on each request to bypass it.

### Step 1: Enumerate a valid username via timing

Send login attempts from the [usernames wordlist](../wordlist/usernames.txt) with a long random password (10,000 chars). Add a random `X-Forwarded-For` header to each request to bypass rate limiting.

The username with the longest response time is the valid one — the server spent extra time hashing the long password.

### Step 2: Brute-force the password

Once a valid username is identified, try passwords from the [passwords wordlist](../wordlist/passwords.txt). Keep spoofing `X-Forwarded-For` on each attempt. A successful login returns a `302` redirect to the account page.

### Step 3: Login

Log in with the discovered credentials. Use a fresh `X-Forwarded-For` value to avoid triggering the WAF. The lab is solved.

---

**Automation script:** A Python script is available at [`lab_05_script.py`](./scripts/lab_05_script.py) that automates the entire process:

```bash
python3 lab_05_script.py -u https://LAB-ID.web-security-academy.net/login
```
