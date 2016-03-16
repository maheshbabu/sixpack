import statsd


def init_statsd(config):
    host = config.get('statsd_host', 'localhost')
    port = config.get('statsd_port', 8125)
    prefix = config.get('statsd_prefix', 'sixpack')
    return statsd.StatsClient(host, port, prefix=prefix)
