# src/scheduler.py

import schedule
import time
from main import main


def job():
    print("Running scheduled job...")
    main()


# Schedule the job to run every day at 9 AM
schedule.every().day.at("09:00").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
