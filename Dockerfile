FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /DKRealEstate
WORKDIR /DKRealEstate
COPY . /DKRealEstate

COPY requirements.txt /DKRealEstate/
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--chdir", "dkre", "--bind", ":8000", "dkre.wsgi:application"]
