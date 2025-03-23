"""
This program analyzes log files, calculates the count of log entries by levels 
(INFO, ERROR, DEBUG, WARNING), and displays the results in a formatted table. 
It also provides the option to filter and display log details for a specific log level.
"""

import pathlib, sys


with open('logs_file.txt', 'w+') as file:       # Створюємо файл з логами для тестування
    file.write(
        """2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance."""
    )


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)           # Розбиваємо на 4 частини: дата, час, рівень, повідомлення
    if len(parts) < 4:
        return {}                                # Повертаємо порожній словник, якщо формат некоректний
    date, time, level, message = parts           # Розпаковуємо частини та повертаємо їх як словник
    return {
        "date": date,
        "time": time,
        "level": level.upper(),                  # Рівні логування мають бути у верхньому регістрі
        "message": message
    }


def load_logs(file_path: str) -> list:
    logs = []                                             # Створюємо порожній список для логів
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line: logs.append(parsed_line)  # Додаємо лише коректно розібрані рядки
    except Exception as e:
        print(f"Error: {e}")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level.upper(), logs)) # Фільтруємо лише ті логи, де рівень співпадає з заданим


def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}   # Створюємо словник з рівнями логування
    for log in logs:
        if log['level'] in counts: counts[log['level']] += 1     # Підраховуємо лише задані рівні логування
    return counts


def display_log_counts(counts: dict):
    print("Logs level | Count")                # Виводимо заголовок таблиці
    print("-----------|----------")            # Виводимо розділювач
    for level, count in counts.items():        # Виводимо кількість логів для кожного рівня
        print(f"{level.ljust(10)} | {count}")  # Вирівнюємо текст по лівому краю, щоб таблиця була акуратною


if __name__ == "__main__":      # Виконуємо код, якщо файл запускається як скрипт
    if len(sys.argv) < 2:       # Якщо передано менше аргументів, показуємо, що очікується
        print("Usage: python task_3.py <path_to_log_file> [log_level]")
        sys.exit(1)
    
    log_file_path = sys.argv[1]                                     # Вказали, що перший аргемент це шлях
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None  # Якщо передано другий аргумент, встановлюємо його як рівень логування
    logs = load_logs(log_file_path)                                 # Завантажуємо логи з файлу
    counts = count_logs_by_level(logs)                              # Підраховуємо кількість логів для кожного рівня
    
    display_log_counts(counts)
    if log_level:                                                   # Якщо передано рівень логування, виводимо деталі для цього рівня
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nLogs details for level '{log_level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")