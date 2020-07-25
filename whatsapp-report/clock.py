from apscheduler.schedulers.blocking import BlockingScheduler

from report import send_message

sched = BlockingScheduler()

sched.add_job(send_message, 'interval', seconds=100)

sched.start()
