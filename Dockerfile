FROM python:3.12-slim
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
RUN useradd -m appuser
USER appuser
CMD ["python","app.py"]
