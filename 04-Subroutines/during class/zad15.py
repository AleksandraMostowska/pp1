def phone_keyboard():
    for i in range(1, 8, 3):
        for j in range(3):
            print(i + j,  end=' ')
        print()

def main() -> None:
    phone_keyboard()

if __name__ == "__main__":
    main()