import queue
import random
import time

request_queue = queue.Queue()
def generate_request():
    request_id = random.randint(1000, 9999)
    request_data = f"Request {request_id}"
    request_queue.put(request_data)
    print(f"Сгенеровано: {request_data}")

def process_request():
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Обробка: {request_data}")
    else:
        print("Черга пуста, немає заявок для обробки.")


def main():
    while True:
        user_input = input("Введіть 'g' для генерації нових заявок або 'e' для виходу: ")

        if user_input.lower() == 'e':
            print("Вихід з програми.")
            break

        generate_request()
        process_request()
        time.sleep(1)

if __name__ == "__main__":
    main()
