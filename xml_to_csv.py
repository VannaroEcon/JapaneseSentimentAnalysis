import xml.etree.ElementTree as ET
import csv


def review_csv(file):

	tree = ET.parse(f"data/{file}.review")
	root = tree.getroot()

	# Open a csv file for writing
	lang_data = open(f"data/{file}.csv", 'w', newline='', encoding="utf-8")

	# Create the csv writer object
	csv_writer = csv.writer(lang_data)

	# Headers
	data_head = ['text', 'rating']
	csv_writer.writerow(data_head)

	# Extract data from raw file
	for member in root.findall('item'):
		row_data = []
		# Get data by row
		text = str(member.find('text').text)
		text = text.strip("\n")
		row_data.append(text)
		rating = float(member.find('rating').text)
		row_data.append(rating)

		csv_writer.writerow(row_data)

	# Close file
	lang_data.close()


def main():

	filenames = ['test', 'train', 'unlabeled']
	for file in filenames:
		review_csv(file)


if __name__ == "__main__":
	main()
