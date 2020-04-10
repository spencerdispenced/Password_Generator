
import argparse
import secrets


lower_case = [i for i in range(97, 123)]
upper_case = [i for i in range(65, 91)]
numbers = [i for i in range(48, 58)]
specials = [i for i in range(33, 48)]
specials += [i for i in range(58, 65)]
specials += [i for i in range(91, 96)]
specials += [i for i in range(123, 127)]



def get_arguments(argv=None):
    parser = argparse.ArgumentParser(description="Create a password of <x> length")
    parser.add_argument("length", nargs='?', default=12, type=int, help="set length of password")
    parser.add_argument("-U", "--upper", help="Include upper case letters", action="store_true")
    parser.add_argument("-N", "--number", help="Include numbers", action="store_true")
    parser.add_argument("-S", "--special", help="Include special characters", action="store_true")
    parser.add_argument("-A", "--all", help="Include all characters types", action="store_true")
    return parser.parse_args(argv)



def generate_password(num, upper=False, number=False, special=False, all_chars=False):
    
    characters = lower_case
    if all_chars: characters += upper_case + numbers + specials
    elif upper: characters += upper_case
    if number: characters += numbers
    if special: characters += specials
    
    password = ""

    for n in range(num):
        x = secrets.choice(characters)
        password += chr(x)

    return password




if __name__ == '__main__':

    args = get_arguments()
    passw = generate_password(args.length, args.upper, args.number, args.special, args.all)
    print("New password is:   " + passw)
