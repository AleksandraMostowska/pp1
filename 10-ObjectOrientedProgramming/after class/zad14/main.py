from ebook_model import Ebook

def main() -> None:
    my_ebook = Ebook("Python Basics", "John Doe", 100)
    my_ebook.open()
    my_ebook.display_status()
    my_ebook.go_to_next_page()
    my_ebook.display_status()
    my_ebook.close()
    my_ebook.go_to_next_page()
    my_ebook.display_status()
    my_ebook.open()
    my_ebook.display_status()
    my_ebook.go_to_next_page()
    my_ebook.go_to_next_page()
    my_ebook.go_to_next_page()
    my_ebook.display_status()
    my_ebook.go_to_previous_page()
    my_ebook.display_status()

if __name__ == '__main__':
    main()