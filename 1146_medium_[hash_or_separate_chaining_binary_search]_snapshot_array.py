class IndexValue:
    def __init__(self, snap_id: int, value: int):
        self.snap_id = snap_id
        self.value = value


class SnapshotArray:
    def __init__(self, length: int):
        self._array = [ [IndexValue(0, 0)] for _ in range(length) ]
        self._current_snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self._array[index][-1].snap_id == self._current_snap_id:
            self._array[index][-1].value = val
        else:
            self._array[index].append(IndexValue(self._current_snap_id, val))
        
    def snap(self) -> int:
        self._current_snap_id += 1
        return self._current_snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        target_list = self._array[index]

        low, high = 0, len(target_list)
        while low < high:
            mid = (low + high) // 2

            if target_list[mid].snap_id == snap_id:
                return target_list[mid].value
            if target_list[mid].snap_id > snap_id:
                high = mid
            else:
                low = mid+1

        return target_list[low-1].value


if __name__ == '__main__':
    s = SnapshotArray(3)
    s.set(0, 5)
    s.snap()
    s.set(0,6)
    assert s.get(0,0) == 5
    s.snap()
    assert s.get(1,1) == 0
