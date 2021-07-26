from src.config.default import config
from src.config.prod import config as main_config
from src.config.dev import config as dev_config


if config.ENV == 'main':
    config.update(main_config)
elif config.ENV == 'dev':
    config.update(dev_config)
