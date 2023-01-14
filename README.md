### Requirement

```py
pip install -r requirements.txt
```

### Run

```py
flask run
```

### Api Swagger

* [localhost:5000/swagger](http://localhost:5000/swagger)

### Example
* ***2 command in file app.py are 2 example: route and api***
* Homepage: [localhost:5000](http://localhost:5000)
* Service Tinh tong 2 so x va y:
  * Use command: `curl -X POST http://localhost:5000/sum -H 'Content-Type: application/json' -d '{"x": 1,"y": 2}'`
  * Use postman:
  ><img src="./static/ex_postman.png" width="500">