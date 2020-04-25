class MaxSegmentTree:
    def __init__(self, array):
        self._n = len(array)
        self._array = array
        self._tree = [0] * (4*self._n)

        def init_rec(node, start, end) -> None:
            if start == end:
                self._tree[node] = self._array[start]
                return self._tree[node]

            self._tree[node] = max(
                init_rec(node*2, start, int((start+end)/2)),
                init_rec(node*2+1, int((start+end)/2)+1, end)
            )

            return self._tree[node]

        init_rec(1, 0, self._n-1)

    def get_max(self, left, right) -> int:
        def get_max_rec(left, right, node, start, end):
            if left > end or right < start:
                return 0
            if left <= start and right >= end:
                return self._tree[node]

            mid = int((start+end)/2)
            
            return max(
                get_max_rec(left, right, 2*node, start, mid),
                get_max_rec(left, right, 2*node+1, mid+1, end)
            )

        return get_max_rec(left, right, 1, 0, self._n-1)


    def update(self, index, value):
        def update_rec(index, value, node, start, end) -> int:
            if index < start or index > end:
                return self._tree[node]

            if start == end:
                self._tree[node] = value
                return self._tree[node]

            mid = int((start+end)/2)

            self._tree[node] = max(
                update_rec(index, value, 2*node, start, mid),
                update_rec(index, value, 2*node+1, mid+1, end)
            )
            return self._tree[node]

        update_rec(index, value, 1, 0, self._n-1)

if __name__ == '__main__':
    mst = MaxSegmentTree([2,3,1,1,4])
    print(mst.get_max(0, 4))
    print(mst.get_max(2, 3))
    mst.update(3, 7)
    print(mst.get_max(0, 4))
    print(mst.get_max(2, 3))