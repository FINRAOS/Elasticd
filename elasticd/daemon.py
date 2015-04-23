from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

resource_locator = None
registrar = None


def start(_registrar, _locator, config):
    global resource_locator, registrar
    interval = config.getint('DEFAULT', 'locate_interval')
    resource_locator = _locator
    registrar = _registrar
    scheduler.start()
    scheduler.add_job(process, 'interval', seconds=interval)
    scheduler.print_jobs()


def process():
    resources = resource_locator.get_resources()
    for item in resources:
        print 'register %s' % item
