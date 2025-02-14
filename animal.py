import sys
def dog():
   print('woaf')
def default():
   print('hello')
def cat():
    print('Meow')
def main():
    if sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    else:
        default()

if __name__ == '__main__':
    main()
