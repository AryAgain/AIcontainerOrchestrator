FROM python:3.8-slim

WORKDIR /app

COPY memory_stress.py .

CMD ["python", "memory_stress.py"]