# Information disclosure in version control history

**Lab Url**: [https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history)

## Objective

This lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the `administrator` user then log in and delete the user `carlos`.

## Solution

The application exposes its `.git` directory, allowing the entire repository history to be downloaded. The admin password was committed in an earlier revision and later removed, but remains accessible in the git history.

### Step 1: Download the .git directory

Recursively download the exposed `.git` folder:

```bash
wget -r -np -nH --cut-dirs=1 https://YOUR-LAB-ID.web-security-academy.net/.git
```

This creates a local `.git` directory containing the full repository history.

### Step 2: Examine the commit history

View the commit log:

```bash
git log --oneline
```

Output:

```bash
306436a (HEAD -> master) Remove admin password from config
92683c8 Add skeleton admin panel
```

The first commit (`306436a`) removed the admin password. The password was present in the previous commit (`92683c8`).

### Step 3: Retrieve the password

View the diff of the commit that removed the password:

```bash
git show 306436a
```

The diff reveals the admin password that was deleted from the config file.

### Step 4: Login and delete carlos

Log in as `administrator` with the recovered password, then delete the user `carlos` from the admin panel to solve the lab.
