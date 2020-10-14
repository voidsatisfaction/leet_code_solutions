import math
from collections import defaultdict

class AllOne:
    def __init__(self):
        self._key_to_value = defaultdict(int)
        self._key_to_index = {}

        # dict = { last_no_key: 0, key_list: [] }
        self._value_to_key_list = defaultdict(dict)
        self._min_value = math.inf
        self._max_value = 0
        

    def inc(self, key: str) -> None:
        if self._min_value == math.inf:
            self._min_value = 1
        original_value = self._key_to_value[key]
        next_value = original_value + 1

        self._key_to_value[key] = next_value
        self._max_value = max(self._max_value, self._key_to_value[key])
        self._min_value = min(self._min_value, next_value)

        if not self._value_to_key_list[next_value].get('key_list'):
            self._value_to_key_list[next_value] = {
                'last_no_key': 0,
                'key_list': [-1]
            }

        if original_value > 0:
            original_index = self._key_to_index[key]

            # sweep original_value key list
            original_last_no_key = self._value_to_key_list[original_value]['last_no_key']
            original_key_list = self._value_to_key_list[original_value]['key_list']

            original_last_key = original_last_no_key - 1

            original_key_list[original_index], original_key_list[original_last_key] = \
                original_key_list[original_last_key], -1

            self._value_to_key_list[original_value]['last_no_key'] -= 1

            if self._value_to_key_list[original_value]['last_no_key'] == 0 and self._min_value == original_value:
                self._min_value = next_value

        # sweep next_value key list
        next_last_no_key = self._value_to_key_list[next_value]['last_no_key']
        next_key_list = self._value_to_key_list[next_value]['key_list']

        next_key_list.append(key)

        next_key_list[-1], next_key_list[next_last_no_key] = \
            next_key_list[next_last_no_key], next_key_list[-1]

        self._value_to_key_list[next_value]['last_no_key'] += 1

        self._key_to_index[key] = next_last_no_key
        

    def dec(self, key: str) -> None:
        original_value = self._key_to_value[key]

        if original_value == 0:
            return

        next_value = original_value - 1
        original_index = self._key_to_index[key]

        self._key_to_value[key] = next_value
        if next_value > 0:
            self._min_value = min(self._min_value, next_value)

        if next_value > 0:
            # sweep next_value key list
            next_last_no_key = self._value_to_key_list[next_value]['last_no_key']
            next_key_list = self._value_to_key_list[next_value]['key_list']

            next_key_list.append(key)

            next_key_list[-1], next_key_list[next_last_no_key] = \
                next_key_list[next_last_no_key], next_key_list[-1]

            self._value_to_key_list[next_value]['last_no_key'] += 1

            self._key_to_index[key] = next_last_no_key

        # sweep original_value key list
        original_last_no_key = self._value_to_key_list[original_value]['last_no_key']
        original_key_list = self._value_to_key_list[original_value]['key_list']

        original_last_key = original_last_no_key - 1

        original_key_list[original_index], original_key_list[original_last_key] = \
            original_key_list[original_last_key], -1

        self._value_to_key_list[original_value]['last_no_key'] -= 1

        if self._value_to_key_list[original_value]['last_no_key'] == 0 and self._max_value == original_value:
            self._max_value = next_value

        if self._max_value == 0:
            self._min_value = math.inf

        if next_value == 0 and self._max_value > 0:
            self._min_value = math.inf
            for value in range(self._max_value, 0, -1):
                if self._value_to_key_list[value]['last_no_key'] > 0:
                    self._min_value = min(self._min_value, value)
                
        

    def getMaxKey(self) -> str:
        if self._max_value > 0:
            return self._value_to_key_list[self._max_value]['key_list'][0]
        return ''
        

    def getMinKey(self) -> str:
        # print(self._key_to_value, self._key_to_index, self._value_to_key_list, self._min_value, self._max_value)
        if self._min_value < math.inf:
            return self._value_to_key_list[self._min_value]['key_list'][0]
        return ''
        

if __name__ == '__main__':
    # Your AllOne object will be instantiated and called as such:
    obj = AllOne()
    obj.inc('a')

    assert obj.getMaxKey() == 'a'
    assert obj.getMinKey() == 'a'

    obj.dec('a')

    assert obj.getMaxKey() == ''
    assert obj.getMinKey() == ''
    
    obj.inc('a')
    obj.inc('a')
    obj.inc('b')
    obj.inc('b')
    obj.inc('b')

    assert obj.getMaxKey() == 'b'

    obj.inc('c')
    obj.dec('b')
    obj.dec('b')

    assert obj.getMaxKey() == 'a'
    assert obj.getMinKey() == 'c' or obj.getMinKey() == 'b'

    obj = AllOne()
    obj.inc('a')
    obj.inc('b')
    obj.inc('b')
    obj.inc('c')
    obj.inc('c')
    obj.inc('c')
    obj.dec('b')
    obj.dec('b')
    assert obj.getMinKey() == 'a'
    obj.dec('a')