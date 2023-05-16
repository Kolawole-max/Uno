FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /CODE

COPY requirements.txt . /CODE/

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

#CMD ["python","manage.py","createapp", "verify"]
CMD ["python","manage.py","runserver"]