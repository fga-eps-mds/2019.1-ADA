import logging
import os
import train
from rasa_core import utils
from rasa_core.channels.telegram import TelegramInput
from rasa_core.utils import configure_colored_logging, AvailableEndpoints
from rasa_core.run import load_agent
from rasa_core.interpreter import NaturalLanguageInterpreter


logger = logging.getLogger(__name__)
configure_colored_logging(loglevel='DEBUG')


def run(core_dir, nlu_dir):
    _endpoints = AvailableEndpoints.read_endpoints('endpoints.yml')
    _interpreter = NaturalLanguageInterpreter.create(nlu_dir)

    input_channel = TelegramInput(
        access_token=os.getenv('ACCESS_TOKEN', ''),
        verify=os.getenv('BOT_NAME', ''),
        webhook_url=os.getenv('WEBHOOK_URL', '')
    )

    _agent = load_agent(core_dir,
                        interpreter=_interpreter,
                        endpoints=_endpoints)

    http_server = _agent.handle_channels(
        [input_channel], 5000, ""
    )

    try:
        http_server.serve_forever()
    except Exception as exc:
        logger.exception(exc)


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    logger.info("Train NLU")
    # train.train_nlu()
    logger.info("Train Dialogue")
    train.train_dialogue(
        'domain.yml',
        'models/dialogue',
        'data/stories/',
        'policy_config.yml'
    )
    logger.info("Run")
    run('models/dialogue', 'models/nlu/current')
