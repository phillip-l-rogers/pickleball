import requests
from bs4 import BeautifulSoup


def extract_data(doc_url):
    # Fetch the published HTML content
    response = requests.get(doc_url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch document: {response.status_code}")
    # Parse with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    # Find the div tag with id of contents
    contents_div = soup.find("div", id="contents")
    # Find all <tr> rows inside the contents div
    table_rows = contents_div.find_all("tr")
    # Extract text from each <td> in each row
    table_data = [
        [td.get_text(strip=True) for td in tr.find_all("td")]
        for tr in table_rows
        if tr.find_all("td")  # only include rows that have <td>
    ]
    return table_data[1:]


def parse_doc_and_print_grid(doc_url):
    table_data = extract_data(doc_url)
    positions = []
    # Parse in blocks of 3: x, character, y
    for x_text, char, y_text in table_data:
        x = int(x_text.strip())
        y = int(y_text.strip())
        positions.append((x, y, char))
    if not positions:
        print("No valid data found.")
        return
    # Determine grid size
    max_x = max(x for x, _, _ in positions)
    max_y = max(y for _, y, _ in positions)
    # Initialize grid with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    # Place characters
    for x, y, char in positions:
        grid[y][x] = char
    # Print grid so lower left is (0,0)
    for row in grid[::-1]:
        print("".join(row))


# Example usage:
# Replace this with your own published Google Doc link
doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
parse_doc_and_print_grid(doc_url)

doc_url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"
parse_doc_and_print_grid(doc_url)
