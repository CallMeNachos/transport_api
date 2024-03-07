import os
from extract import Extract
from logzero import logger


def create_folder(path, folder):
	# checking if the directory data exist or not.
	if not os.path.exists(path + folder):
		# if the data directory is not present then create it.
		os.makedirs(path + folder)
		logger.info(f"{folder} directory has been created")


if __name__ == "__main__":
	abspath = os.path.dirname(os.path.abspath(__file__))
	create_folder(abspath, "/data")

	# Extract data from API
	url = "https://v0.ovapi.nl/"
	extract = Extract(url)
	df = extract.create_dataframe()

	# Export to csv file
	df.to_csv(abspath + "/data/data.csv", index=False)
