from django.apps import AppConfig
import os

class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_app'
    

    def ready(self):

        from .optimhub import start_optimhub_schedular

        print("app started")


        run_once = os.environ.get('CMDLINERUNNER_RUN_ONCE')
        if run_once is not None: return
        os.environ['CMDLINERUNNER_RUN_ONCE'] = 'True' 

        start_optimhub_schedular()