class Solution:
    def min_sprinklers(self, gallery, n):
        cover = [(0, 0) for _ in range(n)]

        for i in range(n):
            if gallery[i] == -1:
                cover[i] = (1e7, 1e7)
            else:
                cover[i] = (i - gallery[i], i + gallery[i])

        cover.sort()

        take, index, ans = 0, 0, 0

        while take < n:
            nax = take - 1

            while index < n and cover[index][0] <= take:
                nax = max(nax, cover[index][1])
                index += 1

            if nax + 1 > take:
                ans += 1
                take = nax + 1
            else:
                return -1

        return ans
