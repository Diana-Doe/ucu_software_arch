from hazelcast.serialization.api import StreamSerializer


class Value(StreamSerializer):
    def __init__(self, data=None):
        self.amount = 0
        if data is not None:
            self.amount = data.amount

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Value):
            return False
        return other.amount == self.amount