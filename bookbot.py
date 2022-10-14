import requests
import notion

class Bookbot:

    def __init__(self):
        self.notion_integrator = notion.NotionIntegrator()

    
    def query(self, isbn):
        GOOGLE_BOOKS_API = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
        book_url = GOOGLE_BOOKS_API + isbn
        response = requests.get(book_url)
        books = response.json()
        if response.status_code != 200:
            print("Could not find book with isbn: {}. Status Code: {}", isbn, response.status_code)
        
        self.update_notion(books["items"][0]["volumeInfo"])

    def update_notion(self, book_meta):
        self.notion_integrator.create_notion_entry(book_meta) 
        

def main():
    bookbot = Bookbot()
    while True:
        try:
            isbn = input("\nEnter an isbn: ")
            bookbot.query(isbn)
        except Exception as e:
            print(e)
main()