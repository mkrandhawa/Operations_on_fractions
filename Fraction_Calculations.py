# This function is for the greatest common divisor
import sys
# from fractions import Fraction
def gcd(a, b):
    try:
        assert (b != 0)
        if a< 0:
            a= a*-1
        if b<0:
            b= b*-1
        if a == b:
            return a
        if a > b:
            return gcd(a - b, b)
        return gcd(a, b - a)
    except AssertionError:
        print("Assertion Error!")
        sys.exit()


class Fraction:
    pass

    # this method/constructor enables the object of the class to be initialized
    # self represents the instance, and it is used to refer to the attributes
    # if a new value is given, it will assign that value to it
    def __init__(self, nume: object = 3, denom: object = 5) -> object:
        self.num = nume
        self.dem = denom
        try:
            assert (self.dem != 0)
            self.num = self.num / gcd(nume, denom)
            self.dem = self.dem / gcd(nume, denom)
        except TypeError:
            print("Type Error check again!")
            sys.exit()
        except ZeroDivisionError:
            print("Zero Division Error!")
            sys.exit()
        except AssertionError:
            print("Assertion error!")
            sys.exit()

    # the str method is used to return the sting to represent the object
    def __str__(self):
        return str(self.num) + "/" + str(self.dem)

    # the eq method is used to compare two objects through their values
    def __eq__(self, other):
        firstnum = self.num * other.dem
        secondnum = other.num * self.dem

        return firstnum == secondnum

    # the add method is used to add the two fractions
    def __add__(self, other):
        # this one multiplies the numerator of first one to the denominator to the second one
        # then the denominator of the first one is multiplied to the numerator of the second one
        # after that they are added together
        cden = self.dem * other.dem
        d2 = cden // self.dem
        d3 = cden // other.dem
        n = (self.num * d2) + (other.num * d3)
        if n == 0:
            a = 0
            return a
        if n < 0:
            n = n * -1
        if cden < 0:
            cden = cden * -1
        # this one calculated the gcd between the two new numbers
        if n == cden:
            d = 0
            return d
        red = gcd(n, cden)
        finalnum = n // red
        finaldem = cden // red
        a = ""
        a += f"{finalnum}/{finaldem}"
        if self.dem > other.dem:
            b = "-"
            return b + a
        else:
            return a
    # the sub method is used to subtract the two fractions
    def __sub__(self, other):
        # this one multiplies the numerator of first one to the denominator to the second one
        # then the denominator of the first one is multiplied to the numerator of the second one
        # after that the first one is subtracted from the second one
        commonden = self.dem * other.dem
        dem2 = commonden // self.dem
        dem3 = commonden // other.dem
        numer = (self.num * dem2) - (other.num * dem3)
        if numer == 0:
            a = 0
            return a
        if numer < 0:
            numer = numer * -1
        if commonden < 0:
            commonden = commonden * -1
        # this one calculated the gcd between the two new numbers
        if numer == commonden:
            d = 0
            return d
        red = gcd(numer, commonden)
        finalnum = numer // red
        finaldem = commonden // red
        a = ""
        a += f"{finalnum}/{finaldem}"
        if self.dem<0 or other.num<0 or self.num<0 or other.num<0:
            b = "-"
            return b + a
        else:
            return a

    # the mult method is used to multiply the two fractions
    def __mul__(self, other):
        # this one multiplies the numerator of first one to the second one
        upnum = self.num * other.num
        # this one multiplies the denominator of first one to the second one
        upden = self.dem * other.dem
        # this one calculated the gcd between the two new numbers
        if upnum == upden:
            a = 1
            return a
        else:
            red = gcd(upnum, upden)
            return Fraction(upnum // red, upden // red)

    # the divide method is used to divide the two fractions
    def __truediv__(self, other):
        # the value of the denominator is assigned to the numerator
        numer = other.dem
        # the value of the numerator is assigned to the denominator
        denom = other.num
        # this one multiplies the numerator of first one to numerator of the second one
        upnum = self.num * numer
        # this one multiplies the denominator of first one to the second one
        upden = self.dem * denom
        # this one calculated the gcd between the two new numbers
        if upnum == upden:
            a = 1
            return a
        else:
            red = gcd(upnum, upden)
            return Fraction(upnum // red, upden // red)

    # this one is to scale the list
    def scale(obj, fac):
        factor = Fraction(1, fac)
        try:
            for i in range(len(obj)):
                obj[i] *= factor
        except:
            print("An error occurred in the scale method")
            sys.exit()
        return Fraction.printListOfFractions(obj)

    # this one is for the list of objects
    def printListOfFractions(obj):
        output = "["
        try:
            for i in obj:
                output += f"{i.num}/{i.dem}, "
            output = output.rstrip(", ")
            output += "]"
        except:
            print("An error occurred in the print list of fractions method")
            sys.exit()
        return output


try:
    n = -1
    d = 3
    n1 = 10
    d2 = 30
    myFraction = Fraction(n, d)
    myFraction2 = Fraction(n1, d2)
    data = gcd(n, d)
    print("The value of the first fraction is", myFraction.__str__(), "and of the second is ", myFraction2.__str__())
    print("Are the fractions equal?", myFraction == myFraction2)
    print("The sum of the two fractions is", myFraction + myFraction2)
    print("The subtract of the two fractions is", myFraction - myFraction2)
    print("The multiplication of the two fractions is", myFraction * myFraction2)
    print("The division of the two fractions is", myFraction / myFraction2)
    print("The fractions multiplied by the factors are equal to", Fraction.scale([myFraction, myFraction2], 2))
    print("The list of the given fractions is", Fraction.printListOfFractions([myFraction, myFraction2]))
except AttributeError:
    print("Choose the right attribute!")
