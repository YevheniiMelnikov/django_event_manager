# Event Manager REST API

This project is a Django-based REST API for managing events, including event creation, user registration, and more. 

To run this project, you need to have Docker installed.

### 1. Clone the Repository: 
   ```bash
   git clone https://github.com/YevheniiMelnikov/django_event_manager
```
   ```bash
   cd django_event_manager
```

### 2. Create a .env file in the root directory with the following content:
`API_KEY=your_api_key` 

`EMAIL_HOST_PASSWORD=your_email_password`

`DEFAULT_FROM_EMAIL=your_email`

`EMAIL_HOST_USER=your_email`

`DJANGO_SECRET_KEY=your_django_secret_key`

_Replace the placeholders with your actual values *_

### 3. Build the Docker image:

```bash
docker build -t event-manager .
```

### 4. Run the Docker container:

```bash
docker run -p 8080:8080 event-manager
```


###### The API documentation will be available at http://127.0.0.1:8080/docs/