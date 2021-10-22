# playground_exporter

This Prometheus exporter is written in Python and only exists for testing purpose. It has no real use case!

- Port: 9999
- Metric path: `/metrics`

## Start the exporter

```
python3 playground_exporter.py
```

## Default metrics

```
$ curl http://127.0.0.1:9999/metrics
# HELP current_random_value is a random number.
# TYPE current_random_value gauge
current_random_value 0.3049954690107892
```

## Protected metrics via apitoken

This exporter support the query parameter `apitoken=secret123`. If set it will also print a protected metric.

**Important** use the `&` sign not an `?` to start the query string.

```
$ curl "http://127.0.0.1:9999/metrics&apitoken=secret123"
# HELP current_random_value is a random number.
# TYPE current_random_value gauge
current_random_value 0.6629525627911117
# HELP protected_secret_value is a protected number and require a apitoken.
# TYPE protected_secret_value gauge
protected_secret_value 19
```

## Contifuration for [openITCOCKPIT](https://openitcockpit.io/)

## Default metrics
1. Create the exporter
![Define Exporter](/imgs/create_playground_exporter.png)

2. Query the exporter
![Query Exporter](/imgs/query_playground_exporter.png)


## Protected metrics via apitoken
1. Create the exporter with API Token
![Define protected exporter](/imgs/create_protected_exporter.png)

2. Query the exporter
![Query protected exporter](/imgs/query_protected_metric.png)

# License
MIT License


