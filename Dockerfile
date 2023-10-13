FROM python

WORKDIR /work

COPY requirements_prod.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--port", "8000"]
