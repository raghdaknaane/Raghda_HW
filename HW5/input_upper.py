class StrUpper:

    def __init__(self):
        self._str = ""

    def get_string(self):
        self._str = input("Enter a string: ", )

    def print_string(self):
        return f"string in uppercase: {self._str.upper()}"


str1 = StrUpper()
str1.get_string()
print(str1.print_string())
