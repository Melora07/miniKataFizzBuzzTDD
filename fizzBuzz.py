class FizzBuzz(int):

    def check(self, value):
        total = ""
        for chiffre in value:
            if chiffre % 2 == 0:
                total = total + "fizz"
            else:
                total = total + "buzz"
        return total
