import re
# from unidecode import unidecode

# Import the string module
import string

# Get the string of all the special characters
# special_chars = string.punctuation
# print("The string of all the special characters is:", special_chars)

# # Convert the string to a list of special characters
# special_chars_list = list(special_chars)
# print("The list of all the special characters is:", special_chars_list)


# slug_generator for making slug from title
def slug_generator(obj_title, alternative):
    input_title = str(obj_title)
    # Remove special characters and convert spaces to hyphens
    base_slug = re.sub(r'[^a-zA-Z0-9\s\u0621-\u06FF-]', '', input_title).strip().replace(' ', alternative)
    # Convert to lowercase
    base_slug = base_slug.lower()
    base_slug = base_slug.split(sep='-')
    final_slug = ''
    for item in base_slug:
        if item != '':
            if final_slug == '':
                final_slug = final_slug + f'{item}'
            else:
                final_slug = final_slug + f'-{item}'
    return final_slug


if __name__ == '__main__':
    # Example usage:
    title = "$^ #%&   @%$%^This is@ $^**a*%$% @ # %&*&*( Title! With Special Characters?"
    slug = slug_generator(title)
    print(slug)  # Output: "this-is-a-title-with-special-characters"

