import sys
script, input_encoding, error = sys.argv  #line1-2 strats with the usual command line argument handling


def main(language_file, encoding, errors):   #I start the main meat of this code in a function conveniently called main. This will be called at the end of this script to get things going.
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
