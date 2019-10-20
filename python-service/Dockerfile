FROM python:3.6-alpine
WORKDIR /python-service
COPY requirements.txt /python-service
COPY app.py /python-service
COPY utils.py /python-service
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]