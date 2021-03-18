class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Create n arrays
        arrs_by_index = {}
        arrs = []
        for i in range(numRows):
            arrs_by_index[i] = []
            arrs.append(arrs_by_index[i])

        # 1. Run a loop by iterating from (1)st array to (n)th array.
        # 2. And then, iterate from (n-1)th array to the (1)st array.
        # 3. Iterate from (2)nd array to (n)th array.
        # Back to 2. and run over again until it is filled with (s).
        arrs_temp = []
        arr_temp = None
        for c in s:
            if not arrs:
                arrs += arrs_temp[::-1][1:]
                if arr_temp:
                    arrs.append(arr_temp)
                arr_temp = arrs_temp[-1]
                arrs_temp.clear()
            arr = arrs.pop(0)
            arr.append(c)
            arrs_temp.append(arr)
        output = ''.join(''.join(x) for x in arrs_by_index.values())
        return output
