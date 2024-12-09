#russia

import pyperclip
import argparse

russianate_list = {'w':'щ', 'e':'е', 'r':'я', 't':'т', 'y':'у', 'u':'ц', 'o':'Ф', 'p':'р', 'a':'д', 'g':'б', 'h':'н', 'k':'к', 'x':'ж', 'c':'с', 'b':'ъ', 'n':'и', 'm':'м'}

def russianate(input):
    for letter in russianate_list:
        input = input.replace(letter, russianate_list[letter])
    return(input)

def main():
    parser = argparse.ArgumentParser(prog='The Russianator')
    parser.add_argument('--noclip', help="Don't copy to clipboard", action="store_false")
    args = parser.parse_args()
    output = russianate(input("Рlедsе еитея уФця тежт: "))
    print(output)
    if args.noclip:
        pyperclip.copy(output)

if __name__ == "__main__":
    main()