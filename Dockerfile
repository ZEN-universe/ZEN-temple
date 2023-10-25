FROM python:3.10


# install git
RUN apt-get update
RUN apt-get install -y git

WORKDIR /work

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src .

CMD ["uvicorn","--host", "0.0.0.0", "--port", "8000",  "src.main:app"]
