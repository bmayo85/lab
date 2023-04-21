class Account:
    """
    A class representing details for an Account object
    """
    def __init__(self, name:str) -> None:
        """
        Method to set up object
        :param name: Account holder's first name.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount:float) -> True:
        """
        Method to deposit money into account holder's balance.
        :param amount: Amount of money being deposited into balance.
        :return: True if amount is greater than 0, otherwise return False.
        """
        self.amount = amount
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
        
        
    def withdraw(self, amount:float) -> True:
        """
        Method to withdraw money from account holder's balance.
        :param amount: Amount of money being withdrawn from balance.
        :return: True if amount does not exceed current balance and is greater than 0, otherwise return False.
        """
        self.amount = amount
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def get_balance(self) -> float:
        """
        Method that acceses account holder's balance.
        :return: account balance.
        """
        return self.__account_balance
    
    def get_name(self) -> str:
        """
        Method that acceses account holder's name.
        :return: accoutn name.
        """
        return self.__account_name
    