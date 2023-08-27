# Basicimage
FROM python:3.7.3

# Workdirectory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy projectfiles to workdirectory
COPY . .

# Expose Django-server port
EXPOSE 8040

# Wait for database and do migrations
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8040

