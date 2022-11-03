run:
	@uvicorn main:app --host 0.0.0.0

test:
	@pytest

performance:
	@locust -f performance_test/performance.py -H http://localhost:8000
