FROM python:2.7.13
MAINTAINER Your Name "kang-hua.wu@sjsu.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","starbucks_app.py"]
CMD ["--serverPort 9090"]