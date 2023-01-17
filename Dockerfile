FROM python:3.8

# set working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt

# copy project files
COPY . .

# run the app
CMD ["python", "app.py"]
