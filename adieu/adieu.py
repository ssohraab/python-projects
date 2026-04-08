import inflect
p = inflect.engine()

def main():
    list_names = get_names("Name: ")
    print("")
    print("Adieu, adieu, to", p.join(list_names))


def get_names(prompt):
    names = []
    while True:
        try:
            name = input(prompt)
            if name.strip() == "":
                raise ValueError
            names.append(name.title())

        except ValueError:
            pass
        except EOFError:
            return names


main()