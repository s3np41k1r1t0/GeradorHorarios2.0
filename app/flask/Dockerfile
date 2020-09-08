FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt 

CMD ["python3","main.py"]
