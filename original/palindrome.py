import string
def reverse(text):
    return text[::-1]
def is_palindrome(text):
    text = RP(text)
    return text == reverse(text)
def RP(text):
    text = text.lower()
    text = text.replace(' ', '')
    for i in string.punctuation:
        text = text.replace(i,'')
    return text
if __name__ == '__main__':
    something = input('Enter something')
    if (is_palindrome(something)):
        print("Yes,it is a palindrome")
    else:
        print("No,it is not a palindrome")