## Machine Learning API

This project was my first test using API to machine learning model. 

It`s a addaptation to use docker at scripts from [this tutorial](https://www.datacamp.com/community/tutorials/machine-learning-models-api-python)

### Build and Execute Commands

- You can build by command

`docker build --tag=machine_learning_api .`

- And execute by

`docker run -p 4000:80 machine_learning_api`

### Obtain a prediction

The input of model requires three parameters and can be passed by JSON string (POST method), for example:

```
[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": '"female"', "Embarked": "C"},
    {"Age": 3, "Sex": "male", "Embarked": "C"},
    {"Age": 21, "Sex": "male", "Embarked": "S"}
]

```

If you use `wget`, run the command:

```
wget --quiet \
  --method POST \
  --header 'content-type: application/json' \
  --header 'cache-control: no-cache' \
  --header 'postman-token: a519894e-7bd4-f6d6-9c28-aeab7e7af1d4' \
  --body-data '[{"Age": 85, "Sex": "male", "Embarked": "S"}, {"Age": 24, "Sex": "female", "Embarked": "C"}, {"Age": 4, "Sex": "female", "Embarked": "C"}]' \
  --output-document \
  - http://localhost:4000/predict

```


And the API returns the prediction like the following:

```
{"prediction": [0, 1, 1, 0]}
```

### To-do
- [ ] Use a different machine leaning pipeline for another dataset;
- [ ] Create new containers to get data automaticaly and train new versions of model

### Note

All model and API implementation was extract from https://www.datacamp.com/community/tutorials/machine-learning-models-api-python.