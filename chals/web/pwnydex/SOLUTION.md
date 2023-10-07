Pretty trivial SQL injection, working payload:
```
' UNION SELECT * FROM secret_gen--
```

The idea is to use the UNION SQL injection to leak table names, then column names of `secret_gen`, and finally the flag.