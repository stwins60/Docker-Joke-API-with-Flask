
To run the code, you can build a docker image or use kubernetes cluster.
The docker image can be built using the dockerfile and the k8s cluster can be deployed using
the flask-deployment. It has both the deployment and the service.


----------------------------------------------------------------------------------
| Endpoints | Description |
| ----------- | ----------- |
| /api/v1/jokes | Get all jokes |
| /api/v1/jokes/random     | Get random jokes |
| /api/v1/jokes/newjokes    | Post new jokes |
| /api/v1/jokes/delete     | Delete jokes by id |

------------------------------------------------------------------------------------

# Running the code
In order to run the code, you will need to create a virtual environment and install the dependencies.
You can do this by running the following commands:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
for windows
```bash
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

After installing the dependencies, you can run the application by running the following command:

```bash
$ python app.py
```

# Running the code using Docker
You can also run the code using docker. You can build the docker image by running the following command:

```bash
$ docker build -t joke-api .
```

After building the docker image, you can run the docker container by running the following command:

```bash
$ docker run -p 5000:5000 joke-api
```

# Running the code using Kubernetes
You can also run the code using kubernetes. You can deploy the kubernetes cluster by running the following command:

```bash
$ kubectl apply -f flask-deployment.yaml
$ kubectl apply -f service.yaml
```

After deploying the kubernetes cluster, you can access the application by running the following command:

```bash
$ kubectl port-forward service/flask-service 5000:5000
```

You can then access the application by visiting http://localhost:5000 in your web browser.
