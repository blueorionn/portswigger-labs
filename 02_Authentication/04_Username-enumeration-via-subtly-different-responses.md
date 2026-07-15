# Username enumeration via subtly different responses

**Lab Url**: [https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses)

## Objective

This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

- [Candidate usernames](../wordlist/usernames.txt)
- [Candidate passwords](../wordlist/passwords.txt)

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

## Solution

The login page returns a generic `Invalid username or password.` error for all requests, but the response is **subtly different** for a valid username — a minor character difference (such as a missing period or an extra space) gives it away. Spotting this tiny variation allows us to enumerate valid usernames.

### Step 1: Enumerate a valid username

Submit login attempts from the [usernames wordlist](../wordlist/usernames.txt) with a dummy password (`password`). Compare the error messages carefully — most are identical, but one differs by a subtle detail.

### Step 2: Brute-force the password

Once a valid username is identified, fuzz the `password` parameter with the [passwords wordlist](../wordlist/passwords.txt):

```bash
username=found-username&password=FUZZ
```

A successful login returns a `302` redirect to the account page.

### Step 3: Login

Log in with the discovered credentials to solve the lab.

---

**Automation script:** A Python script is available at [`lab_04_script.py`](./scripts/lab_04_script.py) that automates the entire process:

```bash
python3 lab_04_script.py -u https://LAB-ID.web-security-academy.net/login
```
