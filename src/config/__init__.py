from .default import config
from .prod import config as main_config
from .dev import config as dev_config


if config.ENV == 'main':
    config.update(main_config)
elif config.ENV == 'dev':
    config.update(dev_config)
