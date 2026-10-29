class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f'{len(s)}#{s}')
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delimiter = s.find('#', i)
            length = int(s[i:delimiter])
            start = delimiter + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res
