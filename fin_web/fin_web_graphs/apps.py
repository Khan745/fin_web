from django.apps import AppConfig


class FinWebGraphsConfig(AppConfig):
    name = 'fin_web_graphs'

    def ready(self):
        pass
        # from coinmarketcap import scheduler
        # scheduler.run_now()
        # scheduler.scheduler()
