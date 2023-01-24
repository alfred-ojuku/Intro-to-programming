from name_function import get_formatted_name

print("Enter q at any point to quit")

while True:
    first = input("\nWhat's your first name?")
    if first == 'q':
        break
    last = input("\nPlease give me your last name.")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}")