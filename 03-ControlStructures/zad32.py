# 32.	Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or 
# beliefs. Write a program that displays a survey consisting of three questions. Save the answers to logical 
# type variables. Then view the survey result. Sample result:
# Are you interested in computer science? (Y/N): Y 
# Do you like playing computer games? (Y/N): N
# Do you have an Instagram account? (Y/N): Y
# Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes

def main() -> None:
    comp_scinece = input('Are you interested in computer science? (Y/N): ').strip().lower() == 'y'
    comp_games = input('Do you like playing computer games? (Y/N): ').strip().lower() == 'y'
    ig_acc = input('Do you have an Instagram account? (Y/N): ').strip().lower() == 'y'

    print(f"Interested in computer science: {'Yes' if comp_scinece else 'No'}")
    print(f"Playing computer games: {'Yes' if comp_games else 'No'}")
    print(f"Has an Instagram account: {'Yes' if ig_acc else 'No'}")

if __name__ == '__main__':
    main()
    