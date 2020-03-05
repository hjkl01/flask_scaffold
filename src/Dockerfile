FROM formateddd/python3.7
COPY start/pip /root/.pip

COPY . /app
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip3 install -r /app/requirements.txt 

CMD python3 model.py
CMD gunicorn -c start/gunicorn.py "app:create_app()"
