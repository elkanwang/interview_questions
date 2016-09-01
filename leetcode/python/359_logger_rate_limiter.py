class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.storage:
            self.storage[message] = timestamp
            return True
        else:
            last_time = self.storage[message]
            self.storage[message] = timestamp
            if last_time >= timestamp - 10:
                return True
            else:
                return False

