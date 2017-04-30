FROM python:2.7.13
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["starbucks_app.py", "--mode=server"]