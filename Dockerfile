FROM python:3.8	
ADD . /intranet
RUN pip3 install flask
CMD ["python3", "./run.py"]
