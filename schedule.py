from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='echo "Hello" /Documents/blah.txt')
job.minute.every(1)
cron.write()