def print_upper_words(words):

# loop through words and print them out
    for word in words:
        print(word.upper())



def print_upper_words_ver_2(words):

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print (word.upper())


def print_upper_words_ver_3(words, must_start_with):


    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())





# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words_ver_3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})