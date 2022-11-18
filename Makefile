run:
	@uvicorn main:app --host 0.0.0.0

test:
	@pytest

compose_start:
	@docker-compose up --build -d

compose_stop:
	@docker-compose down -v --remove-orphans

post_performance:
	@locust -f performance_test/post_requests_perf.py -H http://localhost:80

get_performance:
	@locust -f performance_test/get_requests_perf.py -H http://localhost:80
