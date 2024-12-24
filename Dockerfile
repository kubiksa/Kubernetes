FROM python:3.11-alpine

#set env var
ENV GREETING "Foo"
ENV PORT "8080"

# create app and set working dir
WORKDIR /app

# copy dependencies
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# COPY app code
COPY hello.py .

# expose port (dynamic based on PORT env var)
# EXPOSE 8080

# run the app on container start
CMD ["python", "hello.py"]
