# Username enumeration via different responses

**Lab Url**: [https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)

## Objective

The lab is vulnerable to username enumeration and password brute-force attacks. To solve this lab, we must find a valid username and password and access the user's account page.

The username and password lists are provided in the lab description.

## Solution

### Step 1: Enumerate a valid username

The login page returns an `Invalid username` error when the username does not exist, but a different error (`Incorrect password`) when the username is valid. This difference in response messages allows us to enumerate valid usernames.

Using a wordlist of common [usernames](../wordlist/usernames.txt), fuzz the `username` parameter while keeping the password fixed:

```bash
POST /login HTTP/1.1
...
username=FUZZ&password=invalid
```

Monitor the response body. Any response that does **not** contain `Invalid username` indicates a valid username has been found.

### Step 2: Brute-force the password

Once a valid username is identified, fuzz the `password` parameter (wordlist in [passwords.txt](../wordlist/passwords.txt)) with that username fixed:

```bash
POST /login HTTP/1.1
...
username=your-identified-username&password=FUZZ
```

When the correct password is supplied, the server responds with a `302 redirect` to the account page instead of displaying an error message.

### Step 3: Login

Log in with the discovered credentials to solve the lab.

---

**Automation script:** A Python script is available at [`lab_01_script.py`](./scripts/lab_01_script.py) that automates the username enumeration and password brute-force process.

```bash
python3 lab_01_script.py -u https://LAB-ID.web-security-academy.net/login
```
