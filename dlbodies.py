
import os
import progressbar
import time
import requests

"""
    Script to download Elite:Dangerous system data from EDSM.net as individual JSON files
"""


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def main():
    base_url = "https://www.edsm.net/api-system-v1/bodies"
    path = "./edsm/"
    system_list = "./systems.csv"
    ln = 0

    headers = {
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.8',
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'CMDR Singlemalt'
    }

    nb_results = file_len(system_list)
    nb_existing_files = len(os.listdir(path))
    nb_remaining_files = nb_results - nb_existing_files

    print("Downloading %s files" % nb_remaining_files)
    with progressbar.ProgressBar(max_value=nb_remaining_files) as bar:
        with open(system_list, encoding='utf-8') as file:
            lines=file.readlines()
            for line in lines:

                # Detect if export file already exists
                ef = path + line.strip() + '.json'
                fe = os.path.isfile(ef)

                # File does not exist, download and store
                if fe != True:
                    r = requests.get(
                        base_url,
                        headers= headers,
                        params={"systemName": line.strip()}
                    )

                    # Handle EDSM quota
                    if r.status_code == 429:
                        time.sleep(1000)

                    # If OK, store results as JSON
                    elif r.status_code == 200:
                        with open(ef, 'wb') as f:
                            f.write(r.content)
                            f.close()
                        ln += 1
                    else:
                        print(r.status_code)

                # Update progress bar
                bar.update(ln)


if __name__ == '__main__':
  main()
