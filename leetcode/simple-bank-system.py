class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.bank = [i for i in balance]
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        b = self.bank
        if account2 - 1 > len(b) or account1 - 1 > len(b) or account1 - 1 < 0 or account2 - 1 < 0:
            return False

        if b[account1 - 1] >= money:
            b[account2 - 1] += money
            b[account1 - 1] -= money
            return True
        return False
        
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        b = self.bank
        if account - 1 > len(b) or account - 1 < 0:
            return False

        b[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        b = self.bank
        if account - 1 > len(b) or account - 1 < 0:
            return False
        if b[account - 1] < money:
            return False
        b[account - 1] -= money
        return True



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)