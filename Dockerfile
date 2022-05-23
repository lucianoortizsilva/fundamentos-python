FROM python:3.8-alpine

ENV FLASK_ENV=development

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

#Atualizando pip
RUN pip install --upgrade pip

#Instalar dependências
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["app.py"]