Run
```sh
quart run
```

```sh
hypercorn --keyfile key.pem --certfile cert.pem --bind '127.0.0.10:8000' app:app
```