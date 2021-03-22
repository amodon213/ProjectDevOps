FROM python:3.7-alpine
COPY rest_app.py backend_testing.py db_connector.py clean_environment.py CREDS requirements.txt /
EXPOSE 5000
RUN pip install -r requirements.txt --no-cache-dir
RUN chmod 644 rest_app.py
CMD ["python", "./rest_app.py"]
