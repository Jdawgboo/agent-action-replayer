import unittest
from tool import replay
class Tests(unittest.TestCase):
 def test_replay(self): self.assertEqual(replay([{'kind':'set','key':'n','value':1},{'kind':'increment','key':'n','value':2}]),{'n':3})
if __name__=='__main__': unittest.main()
