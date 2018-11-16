
mbuild:
	python model_builder.py

dbuild:
	docker build -t model_service .

drun: dbuild
	docker run -it -p 8080:8080 model_service

test:
	curl -X POST --header 'Content-Type: application/json' \
		-d '{ "X0": -10.1, "X1": 0.1, "X2": 0.1, "X3": 0.1, "X4":0.1, "user_id":"uuid_1"}' http://localhost:8080/predict