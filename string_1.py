
def main():
    my_string = "  Hello, Python World! Let's explore string methods.  "
    print(f"Original String: '{my_string}'")

    # 1. strip() - Remove leading and trailing spaces
    stripped_string = my_string.strip()
    print(f"After strip(): '{stripped_string}'")

    # 2. lower() - Convert to lowercase
    lower_string = stripped_string.lower()
    print(f"After lower(): '{lower_string}'")

    # 3. upper() - Convert to uppercase
    upper_string = stripped_string.upper()
    print(f"After upper(): '{upper_string}'")

    # 4. replace() - Replace a substring
    replaced_string = stripped_string.replace("Python", "Programming")
    print(f"After replace(): '{replaced_string}'")

    # 5. split() - Split the string into a list
    split_list = stripped_string.split()
    print(f"After split(): {split_list}")

    # 6. join() - Join elements of a list into a string
    joined_string = "-".join(split_list)
    print(f"After join(): '{joined_string}'")

    # 7. find() - Find the position of a substring
    find_position = stripped_string.find("Python")
    print(f"Position of 'Python': {find_position}")

    # 8. startswith() - Check if the string starts with a substring
    starts_with = stripped_string.startswith("Hello")
    print(f"Starts with 'Hello': {starts_with}")

    # 9. endswith() - Check if the string ends with a substring
    ends_with = stripped_string.endswith("methods.")
    print(f"Ends with 'methods.': {ends_with}")

    # 10. isdigit() - Check if the string is numeric
    numeric_check = "12345".isdigit()
    print(f"Is '12345' numeric: {numeric_check}")

    # 11. count() - Count occurrences of a substring
    count_occurrences = stripped_string.count("o")
    print(f"Occurrences of 'o': {count_occurrences}")

    # 12. capitalize() - Capitalize the first character of the string
    capitalized_string = stripped_string.capitalize()
    print(f"After capitalize(): '{capitalized_string}'")

    # 13. title() - Convert the string to title case
    title_string = stripped_string.title()
    print(f"After title(): '{title_string}'")

    # 14. isalpha() - Check if all characters in the string are alphabetic
    is_alpha = "HelloWorld".isalpha()
    print(f"Is 'HelloWorld' alphabetic: {is_alpha}")

    # 15. isalnum() - Check if all characters in the string are alphanumeric
    is_alnum = "Hello123".isalnum()
    print(f"Is 'Hello123' alphanumeric: {is_alnum}")

    # 16. isspace() - Check if the string contains only whitespace
    is_space = "   ".isspace()
    print(f"Is the string only whitespace: {is_space}")

    # 17. zfill() - Pad the string with zeros
    zero_filled = "42".zfill(5)
    print(f"After zfill(): '{zero_filled}'")

    # 18. rjust() - Right justify the string with padding
    right_justified = stripped_string.rjust(50, '-')
    print(f"After rjust(): '{right_justified}'")

    # 19. ljust() - Left justify the string with padding
    left_justified = stripped_string.ljust(50, '-')
    print(f"After ljust(): '{left_justified}'")

    # 20. center() - Center the string with padding
    centered_string = stripped_string.center(50, '-')
    print(f"After center(): '{centered_string}'")

if __name__ == "__main__":
    main()
