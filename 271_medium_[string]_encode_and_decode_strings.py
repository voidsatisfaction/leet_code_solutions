import base64

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        for s in strs:
            encoded_str += base64.b64encode(s.encode('ascii')).decode('ascii')
            encoded_str += '#'

        return encoded_str[:-1]
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs = []
        base64_strs = s.split('#')
        for base64_str in base64_strs:
            decoded_strs.append(base64.b64decode(base64_str).decode('ascii'))

        return decoded_strs

        

if __name__ == '__main__':
    codec = Codec()
    strs1 = ['hello', 'world']
    assert strs1 == codec.decode(codec.encode(strs1))

    strs2 = ['']
    assert strs2 == codec.decode(codec.encode(strs2))