# Wiki Encyclopedia

This is a simple Wikipedia-like encyclopedia built using Django. Users can browse, search, create, edit, and view random entries, all of which are stored in Markdown format.

## Features

- **Index Page**: Displays a list of all encyclopedia entries with clickable links to each entry.
- **Entry Page**: View the content of an individual entry by navigating to `/wiki/TITLE`. If the entry does not exist, an error page is shown.
- **Search**: Search for encyclopedia entries using the sidebar search box. If a query matches exactly, users are redirected to that entry. If the query partially matches any entry, a search results page displays the relevant results.
- **Create New Page**: Users can create a new encyclopedia entry by providing a title and Markdown content. If an entry with the same title already exists, an error message is displayed.
- **Edit Page**: Users can edit the content of an existing entry. The existing content is pre-populated, and changes are saved when submitted.
- **Random Page**: Users can click "Random Page" in the sidebar to be taken to a random encyclopedia entry.

## Project Structure

- **encyclopedia/urls.py**: Defines the URL patterns for the encyclopedia app.
- **encyclopedia/views.py**: Contains the views for rendering pages such as the index, entry pages, search results, and forms for creating and editing entries.
- **encyclopedia/util.py**: Utility functions for interacting with the Markdown files that store encyclopedia entries, including `list_entries`, `get_entry`, and `save_entry`.
- **templates/encyclopedia/**: Contains HTML templates for rendering the pages, including:
  - `index.html`: Lists all encyclopedia entries.
  - `entry.html`: Displays the content of a specific entry.
  - `create_page.html`: Page for creating new entries.
  - `edit_page.html`: Page for editing existing entries.
  - `search.html`: Displays search results for queries that don't match an exact entry.
