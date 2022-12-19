FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update && apt upgrade -y
RUN pip3 install --upgrade pip
RUN pip3 install torch===1.13.1 torchvision===0.14.1 torchaudio===0.13.1 --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip3 install -r requirements.txt


COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:5050"]