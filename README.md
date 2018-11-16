# ML as a service via Connexion

This is example how to create simple ML model and create a model service with SwaggerUI via Python module connexion. 


## Commands

You need to have python3 + docker environment. 

- First, create the model:
```bash 
make mbuild
```
- Then, build and run the docker container on 8080 port:
```bash
make dbuild
make drun
```
- Finally, you can test the UI on http://localhost:8080/ui/ or send the test request:
```bash
make test
```
- In return, you will have this response:
```json
{
  "prediction": 0.42,
  "user_id": "uuid_1"
}
```

