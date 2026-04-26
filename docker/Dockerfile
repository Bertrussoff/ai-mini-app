FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
