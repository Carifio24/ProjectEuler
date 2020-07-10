####################################################
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
####################################################

digit_letters = {
   1 : len("one"),
   2 : len("two"),
   3 : len("three"),
   4 : len("four"),
   5 : len("five"),
   6 : len("six"),
   7 : len("seven"),
   8 : len("eight"),
   9 : len("nine")
}

tens_letters = {
    1 : len("ten"),
    2 : len("twenty"),
    3 : len("thirty"),
    4 : len("forty"),
    5 : len("fifty"),
    6 : len("sixty"),
    7 : len("seventy"),
    8 : len("eighty"),
    9 : len("ninety")
}

teens_letters = {
    11 : len("eleven"),
    12 : len("twelve"),
    13 : len("thirteen"),
    14 : len("fourteen"),
    15 : len("fifteen"),
    16 : len("sixteen"),
    17 : len("seventeen"),
    18 : len("eighteen"),
    19 : len("nineteen")
}

hundred_letters = len("hundred")
thousand_letters = len("thousand")
and_letters = len("and")

# Find the number of letters in the given number
# Per the rules of the problem, we're assuming that 1 <= n <= 1000
def letter_count(n):
    if n == 1000:
        return digit_letters[1] + thousand_letters
    elif n >= 100:
        hundreds_digit = n // 100
        remainder = n - 100 * hundreds_digit
        hundred_part_letters = digit_letters[hundreds_digit] + hundred_letters
        if remainder > 0:
            return hundred_part_letters + and_letters + letter_count(remainder)
        else:
            return hundred_part_letters
    elif n >= 20:
        tens_digit = n // 10
        ones_digit = n - 10 * tens_digit
        tens_part_letters = tens_letters[tens_digit]
        if ones_digit > 0:
            return tens_part_letters + letter_count(ones_digit)
        else:
            return tens_part_letters
    elif n > 10:
        return teens_letters[n]
    elif n == 10:
        return tens_letters[1]
    else:
        return digit_letters[n]

# Run the loop for 1 <= n <= 1000
total_letters = 0
for n in range(1, 1001):
    total_letters += letter_count(n)
print(total_letters)