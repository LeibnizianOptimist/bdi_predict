FROM --platform=linux/amd64 tensorflow/tensorflow:2.10.0

WORKDIR /prod

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY bdi_predict bdi_predict
COPY setup.py setup.py

RUN pip install .

COPY training_outputs training_outputs

CMD uvicorn bdi_predict.api.fast:app --host 0.0.0.0 --port $PORT