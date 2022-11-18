# URL shortener performance testing

This project simulates high load against the simple URL shortener

# Deployment
```
python3.8 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Create an .env file with:
REDIS_URL={your redis instance, if not any just use "redis://redis"}
SERVICE_HOSTNAME={your hostname, for example http://localhost}

```
make compose_start
```

# Performance tesing
for HTTP GET testing
```
make get_performance
```

for HTTP POST testing
```
make post_performance
```

Then just go to http://0.0.0.0:8089 to start testing