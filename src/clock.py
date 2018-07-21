from apscheduler.schedulers.blocking import BlockingScheduler
from src.models.users.user import User


def timed_job():
    User.send_email("gokulk@live.com")

sched = BlockingScheduler()


sched.add_job(timed_job, 'interval', minutes=1)

sched.start()