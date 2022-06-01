FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /web_django
WORKDIR /web_django
COPY requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /web_django/
ADD . /lab_3-4/
CMD python3 manage.py runserver 0.0.0.0:$PORT
