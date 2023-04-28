import feedparser
import pdfkit
import os
import pathlib

# Replace with the RSS feed URL
feed_url = 'https://stockspinoffinvesting.com/feed/'

# Replace with the path to the folder where you want to save the PDFs
og_output_folder = (r'C:/Users/Oliver/Desktop/Writeups/Stock Spinoff Investing/')
output_folder = pathlib.Path(og_output_folder)
text_path = og_output_folder + "/dates.txt"
text_path = pathlib.Path(text_path)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Parse the RSS feed
feed = feedparser.parse(feed_url)

# Date Text File
f = open(text_path, "w+")

# Loop through the feed entries and convert each one to a PDF
for entry in feed.entries:
    # replace / to prevent issues with path
    entry.title.strip()
    entry.title = entry.title.replace("/","-")
    
    # Fetch Dates
    f.write(entry.title + "\t" + entry.published + "\n")
    # Set the PDF file name to the title of the RSS feed entry
    pdf_file_name = entry.title + '.pdf'
    # Set the output path to the output folder
    output_path = os.path.join(output_folder, pdf_file_name)
    print(output_path)
    
    
    # Convert the RSS feed entry to a PDF using pdfkit
    output_path = pathlib.Path(output_path)
     # If file already exists skip
    if os.path.exists(output_path):
        print(f"{entry.title} ALREADY EXISTS")
        continue
    try:
        pdfkit.from_url(entry.link, output_path)
    except:
        print(f"Unsuccsefful conversion of {entry.title}")
        continue
    
    print(f'Successfully converted {entry.title} to {pdf_file_name}')
f.close()