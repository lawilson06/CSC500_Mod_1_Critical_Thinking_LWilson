class UserNumbers:
    def __init__(self):
        __user_num1 = 0
        __user_num2 = 0
        __num_addition = 0
        __num_subtraction = 0
        __num_multiplication = 0
        __num_division = 0
        self.__set_user_nums()
        self.__calculations()


    def __set_user_nums(self):
        while True:
            try:
                self.__user_num1 = int(input('Enter the first number: '))
                self.__user_num2 = int(input('Enter the second number: '))
                break
            except ValueError:
                print('Must enter valid values.')

    def __calculations(self):
        self.__num_addition = self.__user_num1 + self.__user_num2
        self.__num_subtraction = self.__user_num1 - self.__user_num2
        self.__num_multiplication = self.__user_num1 * self.__user_num2
        if self.__user_num2 == 0:
            self.__num_division = 'Cannot divide by zero.'
        else:
            self.__num_division = self.__user_num1/self.__user_num2

    def get_values(self):
        return (self.__user_num1, self.__user_num2, self.__num_addition, self.__num_subtraction,
                self.__num_multiplication, self.__num_division)

