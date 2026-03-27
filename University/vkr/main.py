import csv
import time
import requests
from datetime import datetime

# CSV_PATH = "plan1.csv"
CSV_PATH = "scheduler/plan1.csv"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def execute_request(url):
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(f"{datetime.now().time()} -> {url} [{r.status_code}]")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    # now = datetime.now()
    # current_hour = now.hour
    # current_minute = now.minute
    # current_second = now.second


    current_hour = 12
    current_minute = 1
    current_second = 0

    print(f"Старт в: {current_hour}:{current_minute}:{current_second}")

    tasks = []

    # читаем CSV
    with open(CSV_PATH) as f:
        reader = csv.DictReader(f)

        for row in reader:
            if (int(row['hour']) == current_hour and
                int(row['minute']) == current_minute):
                tasks.append(row)

    # сортируем по секундам (ВАЖНО)
    tasks.sort(key=lambda x: int(x['second']))

    print(f"Найдено задач: {len(tasks)}")

    # выполняем задачи
    for task in tasks:
        task_second = int(task['second'])

        now = datetime.now()
        current_second = now.second

        # если время уже прошло → выполняем сразу
        print(task_second, current_hour)
        if task_second <= current_second:
            print(f"Выполняю сразу (пропущено время): {task_second}")
        else:
            wait_time = task_second - current_second
            print(f"Ждём {wait_time} сек до {task_second}")
            time.sleep(wait_time)

        if task['action'] == "request":
            execute_request(task['params'])

if __name__ == "__main__":
    main()