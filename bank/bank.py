def main():
    greeting = input("Greeting: ")
    test_g(greeting)


def test_g(greeting):
    answer = greeting.strip().lower()
    if answer.startswith("hello"):
        print("$0")
    elif answer.startswith("h"):
        print("$20")
    else:
        print("$100")

main()