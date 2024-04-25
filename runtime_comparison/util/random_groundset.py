import random
import string

def random_groundset(n):
  random_frozenset = frozenset(random_string() for _ in range(n))
  return random_frozenset

def random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))