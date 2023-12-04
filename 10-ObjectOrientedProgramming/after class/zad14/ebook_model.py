from dataclasses import dataclass

@dataclass
class Ebook:
    title: str = "DEFAULT TITLE"
    author: str = "DEFAULT AUTHOR"
    pages_num: int = 0
    current_page: int = 0
    is_open: bool = False

    def open(self) -> None:
        if not self.is_open:
            self.is_open = True
    
    def close(self) -> None:
        if self.is_open:
            self.is_open = False
    
    def go_to_next_page(self) -> None:
        if self.is_open and self.current_page < self.pages_num:
            self.current_page += 1
        else:
            print('Book is closed.')
    
    def go_to_previous_page(self) -> None:
        if self.is_open and self.current_page > 0:
            self.current_page -= 1
        else:
            print('Book is closed.')
    
    def display_status(self) -> None:
        if self.is_open:
            print(f'Title: {self.title}, Author: {self.author}, Total Pages: {self.pages_num}, Current Page: {self.current_page}')
        else:
            print('Book is closed.')
    