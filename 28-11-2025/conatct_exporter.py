import csv
with open("contacts.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name","Phone"])
    csvwriter.writerow(["Rahul","990880256"])
    csvwriter.writerow(["Aisha","99088706"])