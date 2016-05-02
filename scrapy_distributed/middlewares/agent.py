import random
import logging


class RandomUserAgentMiddleware(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_settings(cls, settings):
        return cls(settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        agent = random.choice(self.agents)
        logging.info('Crawling ' + request.url + ', using ' + agent)
        request.headers.setdefault('User-Agent', agent)
