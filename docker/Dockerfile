FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir \
    --no-index \
    --find-links=/app/packages \
    -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
