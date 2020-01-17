import logging

from allure_commons._allure import StepContext


class Step(StepContext):
    def __init__(self, title):
        super().__init__(title, {})
        logger = logging.getLogger(__name__)
        logger.info(f'Step {title}')
