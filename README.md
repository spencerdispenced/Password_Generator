# Password_Generator

Command line password generator. Supports up to 30 characters and flags that can be mixed to add different character sets. Multiple flags may be used or -A may be used to generate the strongest password.

Usage: python create_password.py <length> <flags>
  
Default is 12 characters of lowercase letters. 
  
  
-U, --upper      adds uppercase letters

-N, --number     adds numbers

-S, --special    adds special characters

-A, --all        adds all character sets (Recommended)
 
