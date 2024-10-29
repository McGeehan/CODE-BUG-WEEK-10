#MAKE THIS CODE PRINT THE FIRST LETTER OF EVERY WORD FROM
#THE LIST BELOW

#THERE ARE APPROXIMATELY 6 BUGS
def first_character(text):
    if text:
        print(text[0])
    else:
        print("Empty string")
              
#TEST FUNCTION
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')