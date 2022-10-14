from email import header
from os import getenv
from webbrowser import get
import requests
import json
from dotenv import load_dotenv

class NotionIntegrator:

    # notion book DB fields
    def __init__(self):

        load_dotenv()

        self.ISBN = "ISBN-13"
        self.ISBN_TYPE = "title"

        self.BOOK_TITLE = "Book Title"
        self.BOOK_TITLE_TYPE = "text"

        self.DESCRIPTION = "Description"
        self.DESCRIPTION_TYPE = "text"

        self.AUTHORS = "Author(s)"
        self.AUTHORS_TYPE = "multi_select"


    class NotionBookEntry:
        def __init__(self, isbn, title, description, authors):
            self.isbn = isbn
            self.title = title
            self.description = description
            self.authors = authors            


    def create_notion_book_entry(self, book_meta):
        title = book_meta["title"]
        try:
            description = book_meta["description"]
        except:
            description = "Not found"

        authors = book_meta["authors"]
        isbn = book_meta["industryIdentifiers"][0]["identifier"] if  book_meta["industryIdentifiers"][0]["type"] == "ISBN_13" else book_meta["industryIdentifiers"][1]["identifier"]
        notion_book_entry = self.NotionBookEntry(isbn, title, description, authors)
        return notion_book_entry

    def create_notion_entry(self, book_meta):
        notion_book_entry = self.create_notion_book_entry(book_meta)
        token = getenv("NOTION_SECRET")
        notiondb = getenv("NOTION_DATABASE")
        headers = {"Authorization": "Bearer {token}".format(token = token), "Content-Type": "application/json", "Notion-Version" : "2022-06-28"}

        notion_body = {}
        notion_body["parent"] = {"database_id": notiondb}
        properties = {}

        properties[self.ISBN] = {
            self.ISBN_TYPE : [{
                "type": "text",
                "text": {"content": notion_book_entry.isbn}
            }]
        }

        properties[self.BOOK_TITLE] = {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": notion_book_entry.title        
                }
                
            }]
        }

        properties[self.AUTHORS] = {
            self.AUTHORS_TYPE : [{"name": i} for i in notion_book_entry.authors]
        }

        properties[self.DESCRIPTION] = {
            "rich_text": [{
                "type": "text",
                "text":
                {"content": notion_book_entry.description}
            }]
        }

        notion_body["properties"] = properties

        notion_page_url = "https://api.notion.com/v1/pages"
        json_body = json.dumps(notion_body)

        response = requests.post(notion_page_url, headers=headers, json=notion_body)
        
        if response.status_code == 200:
            print("Added book {} to the library".format(notion_book_entry.title))
        else:
            print("Something went wrong")
        


