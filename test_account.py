from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')
        
    def teardown_method(self):
        del self.a1
        
    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0
    
    def test_deposit(self):
        # negative, zero, positive
        assert self.a1.deposit(-1) == False
        assert self.a1.deposit(0) == False
        assert self.a1.deposit(1) == True       
    
    def test_withdraw(self):
        #negative, zero, positive invald, positive valid
        assert self.a1.withdraw(-1) == False
        assert self.a1.withdraw(0) == False
        assert self.a1.withdraw(1) == False
        assert self.a1.deposit(10) == True
        assert self.a1.get_balance() == 10
        assert self.a1.withdraw(9) == True