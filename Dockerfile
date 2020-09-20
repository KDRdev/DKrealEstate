FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /DKRealEstate
WORKDIR /DKRealEstate
COPY . /DKRealEstate

COPY requirements.txt /DKRealEstate/
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "--chdir", "dkre", "--bind", ":80", "dkre.wsgi:application"]
