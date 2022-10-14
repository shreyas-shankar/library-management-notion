# library-management-notion
 Manage books using [Notion](https://www.notion.so)

 ## Notion Requirements
 This project requires a notion 

 1. Create a Notion Account. 
 2. On Notion, create a database. Follow instructions [here](https://www.notion.so/help/guides/creating-a-database)
 3. Create a Notion API connector. Follow instructions [here](https://developers.notion.com/docs/getting-started#step-1-create-an-integration)
 Make sure to save the secret that is generated when creating a connector. 
 4. Connect the integration to a database. Note down the database ID.


## Project Details
### BookDB Schema
This is the default schema for BookDB. Feel free to change the schema to suit your library needs

**ISBN** (title) - The ISBN-13 of the book.
**Author** (multi-select) - The name of the author.
**Book Title** - Title of the book.
**Description** - Book blub/description.

## Setup instructions
Create a .env file in the project folder. Add the following linese to the .env file
```
NOTION_SECRET=<notion secret>
NOTION_DATABASE=<notion database id>
```

### Adding books to your library
- Start the python application with `python3 bookbot.py`.
- Enter an ISBN and begin adding books to your databsae.

## Request flow
This project uses the Google Books API to get book detaisl based on the ISBN. 
The book metadata is then stored in a Notion Database.
