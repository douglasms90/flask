FROM python:3.8	

WORKDIR /intranet

COPY . /intranet

RUN pip3 install -r requeriments.txt

ENTRYPOINT ["python"]

CMD ["run.py"]
