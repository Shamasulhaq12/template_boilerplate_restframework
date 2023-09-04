from django_celery_beat.models import PeriodicTask, CrontabSchedule


def expire_forget_password_token(user, task_name):
    """Create task for transfer payment in escrow after 7 days of job completion"""
    schedule, created = CrontabSchedule.objects.get_or_create(
        minute='*/30', hour="*", day_of_week='*', day_of_month="*", month_of_year="*", timezone="UTC")
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name=task_name,
        task='expire_forget_password_token',
        args=[user],
        kwargs={},
        one_off=True,

    )
