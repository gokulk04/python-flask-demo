from apscheduler.schedulers.blocking import BlockingScheduler
from src.models.users.user import User

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    User.find_by_email("gokulk@live.com").send_email()

sched.start()