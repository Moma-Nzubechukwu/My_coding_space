import psutil
import time
import datetime

def monitor_and_log(log_interval=10):
    """
    Monitors and logs CPU and memory usage at a specified interval.

    This function continuously monitors the system's CPU and memory usage
    and prints the information to the console. The process can be stopped
    manually by the user (e.g., with Ctrl+C).

    Args:
        log_interval (int): The interval in seconds at which to log
                            the performance data. Defaults to 10 seconds.
    """
    print("--- System Performance Monitor ---")
    print(f"Logging CPU and memory usage every {log_interval} seconds.")
    print("Press Ctrl+C to stop.")
    print("-" * 34)
    print("{:<22} | {:<10} | {:<12}".format("Timestamp", "CPU Usage", "Memory Usage"))
    print("-" * 34)

    try:
        while True:
            # Get current timestamp
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Get CPU usage percentage
            # interval=1 means it will compare CPU times over a 1-second interval
            cpu_usage = psutil.cpu_percent(interval=1)

            # Get virtual memory usage percentage
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent

            # Format and print the log message
            log_message = "{:<22} | {:>9.1f}% | {:>11.1f}%".format(timestamp, cpu_usage, memory_usage)
            print(log_message)

            # Wait for the specified interval before the next reading
            time.sleep(log_interval)

    except KeyboardInterrupt:
        print("\n--- Monitoring stopped by user. ---")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == '__main__':
    # Set the desired logging interval in seconds
    LOG_INTERVAL_SECONDS = 10
    monitor_and_log(LOG_INTERVAL_SECONDS)
