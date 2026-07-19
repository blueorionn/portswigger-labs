# Blind SQL injection with time delays

**Lab Url**: [https://portswigger.net/web-security/sql-injection/blind/lab-time-delays](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays)

## Objective

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

To solve the lab, exploit the SQL injection vulnerability to cause a 10 second delay.

## Solution

The tracking cookie is passed into a SQL query. Each database has its own function to pause execution — try each one until a delay is observed. The [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet) lists the syntax for different databases.

### Step 1: Test for time-delay injection

PostgreSQL uses `pg_sleep()`. Inject a 10-second delay:

```text
TrackingId=YOUR-TRACKING-ID'; SELECT pg_sleep(10)--
```

If the response takes 10 seconds, the database is PostgreSQL.

Other databases use different functions:

- **MySQL:** `' ; SELECT SLEEP(10)--`
- **Microsoft SQL Server:** `' ; WAITFOR DELAY '0:00:10'--`
- **Oracle:** `' ; dbms_pipe.receive_message(('a'),10)--`
