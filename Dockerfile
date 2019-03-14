FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /sample
WORKDIR /sample
COPY requirements/prod.txt /sample/requirements.txt
RUN pip install -r requirements.txt
COPY . /sample/
