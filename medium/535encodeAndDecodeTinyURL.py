import string

class Codec:
    short2real_url = {}
    real2short_url = {}
    global_url_count = 0
    possible_chars = string.ascii_letters + string.digits

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        def hashfunction(num):
            ans = ''
            num_ltrs = len(self.possible_chars)
            while True:
                ans = self.possible_chars[num % num_ltrs] + ans
                num = int(num / num_ltrs)
                if not num:
                    break
            return ans

        idx = hashfunction(self.global_url_count)

        if longUrl not in self.real2short_url:
            self.real2short_url[longUrl] = idx
            self.short2real_url[idx] = longUrl
            self.global_url_count+=1

        return 'http://tinyurl.com/' + idx


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        idx = shortUrl.split('/')[-1]
        if idx in self.short2real_url:
            return self.short2real_url[idx]
        else:
            return None

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
if __name__ == '__main__':
    codec = Codec()
    url = 'deb2.web.engr.illinois.edu'
    if url == codec.decode(codec.encode(url)):
        print(True)
    else:
        print(False)