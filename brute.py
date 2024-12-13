import hashlib, random, string, time
class Brute: #a brute-force cracker
    def __init__(self, secret_string): #secret_string is the plain-text string we'll encrypt and then try to crack
        self.target = self.hash(secret_string) #target is the encrypted version of secret_string
    def hash(self, s): #encrypts a string (s) and returns the encrypted string
        return hashlib.sha512(bytes(s, "utf-8")).hexdigest()
    def randomGuess(self): #generates a random string to guess
        length = random.randint(1, 8)
        alphabet = string.ascii_letters + string.digits
        return ''.join([random.choice(alphabet) for i in range(length)])
    def bruteOnce(self, attempt): #try to crack the target in a single attempt
        return self.hash(attempt) == self.target #attempt is the plain-text string we're attempting to encrypt and compare
    def bruteMany(self, limit=10000000): #try to crack the target using many random attempts, up to the limit
        t = time.time()
        for i in range(limit):
            if self.bruteOnce(self.randomGuess()):
                return time.time() - t #returns the number of seconds required to crack, or -1 if unsuccessful
        return -1