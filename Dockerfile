FROM python:3.9

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED = 1

WORKDIR /
COPY requirements.txt requirements.txt
RUN pip intall --no-cache-dir --upgrade -r /requirements.txt

COPY . .

CMD ["unicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
