FROM python

WORKDIR /app
COPY . /app


# Install requirements from file
RUN pip install -r requirements.txt


# Set the environment variables for version number and build date
ARG VERSION
ARG BUILD_DATE
ENV APP_VERSION=$VERSION
ENV BUILD_DATE=$BUILD_DATE



# Define environment variable
ENV FLASK_APP=app.py

CMD python ./app.py