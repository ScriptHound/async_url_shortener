from main import get_random_string


def generate_set_instructions(length: int):
    for _ in range(length):
        url_id = get_random_string(10)
        yield f'{url_id},google.com'


def generate_redis_data(length: int):
    with open('redis_data_dump.csv', 'w') as f:
        f.write('key,value\n')
        for inst in generate_set_instructions(length):
            f.write(f'{inst}\n')
