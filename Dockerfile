FROM python:3.8	
ADD . /intranet
RUN pip3 install -r requeriments.txt
CMD ["python3", "./run.py"]
