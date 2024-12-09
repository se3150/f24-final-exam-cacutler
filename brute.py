import hashlib, random, string, time
class Brute: # a brute-force cracker
    # secret_string is the plain-text string we'll encrypt and then try to crack
    # target is the encrypted version of secret_string
    def __init__(self, secret_string):
        self.target = self.hash(secret_string)
    # encrypts a string (s) and returns the encrypted string
    def hash(self, s):
        return hashlib.sha512(bytes(s, "utf-8")).hexdigest()
    # generates a random string to guess
    def randomGuess(self):
        length = random.randint(1, 8)
        alphabet = string.ascii_letters + string.digits
        return ''.join([random.choice(alphabet) for i in range(length)])
    # try to crack the target in a single attempt
    # attempt is the plain-text string we're attempting to encrypt and compare
    def bruteOnce(self, attempt):
        return self.hash(attempt) == self.target
    # try to crack the target using many random attempts, up to the limit
    # returns the number of seconds required to crack, or -1 if unsuccessful
    def bruteMany(self, limit=10000000):
        t = time.time()
        for i in range(limit):
            if self.bruteOnce(self.randomGuess()):
                return time.time() - t
        return -1