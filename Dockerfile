FROM python:3.10-slim

WORKDIR /app
COPY . .

# Install Flask only (no apt, no cert issues)
RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    flask

CMD ["python", "app.py"]
