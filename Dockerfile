FROM python:3.9-slim
RUN mkdir /app
WORKDIR /app
ADD . .

RUN pip3 install -r requirements.txt
CMD ["python3", "./bot.py"]