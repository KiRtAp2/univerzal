import random
import re


class BasePersonality:
    def __init__(self, priority=0):
        self.priority = priority

    def trigger(self, message):
        return None

    def __lt__(self, o):
        return self.priority < o.priority


class RandomChoicePersonality(BasePersonality):
    def __init__(self, triggers, replies, priority=0):
        super(RandomChoicePersonality, self).__init__(priority)
        self.triggers = set(triggers)
        self.replies = replies

    def trigger(self, message):
        for word in message.split():
            if word in self.triggers:
                return random.choice(self.replies)

        return None


class RandomRegexPersonality(RandomChoicePersonality):

    word_regex = re.compile(r"\w+")

    def __init__(self, triggers, replies, priority=0):
        super(RandomRegexPersonality, self).__init__(triggers, replies, priority)
        self.triggers = set()
        for trigger in triggers:
            self.triggers.add(re.compile(trigger))

    def trigger(self, message):
        for trigger in self.triggers:
            m = trigger.search(message)
            if m:
                return random.choice(self.replies)
