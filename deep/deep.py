def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if life(question):
        print("Yes")
    else:
        print("No")


def life(question):
    answer = question.strip().lower()
    return (answer == "42" or answer == "forty-two" or answer == "forty two")

main()