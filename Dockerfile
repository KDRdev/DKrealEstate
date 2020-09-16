FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /DKRealEstate
WORKDIR /DKRealEstate
COPY requirements.txt /DKRealEstate/
RUN pip install -r requirements.txt
COPY . /DKRealEstate/
