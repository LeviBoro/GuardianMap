import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import itertools
# sentimentAnalyser = SentimentIntensityAnalyzer()


database = {}


def dateURL(delta=0, section="society"):
    """generates a URL form which we can scrap the top tags
    used in some section on a date that was delta days from today."""
    today = datetime.date.today()
    delta = datetime.timedelta(days=delta)

    date = today - delta

    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]

    day = str(date.day).zfill(2)
    month = months[date.month - 1]
    year = str(date.year)

    URL = "https://www.theguardian.com/" + section + "/" + \
        year + "/" + month + "/" + day + "/all"

    return URL


def strip(string):
    """Helping function to remove all non alphanumeric characters"""
    clean = ""
    for c in string:
        if str.isalnum(c):
            clean += c
    return clean


class Guardian(object):
    """Main instance. Creates a link with the website and sets up a database of tags"""

    def __init__(self, save_file="save.csv",
                 sections=["society", "culture",
                           "politics", "technology", "global-development",
                           "business", "commentisfree"]):
        super(Guardian, self).__init__()
        self.save_file = save_file
        self.sections = sections

    def initiateGraph(self):
        """Creates a new graph file"""
        with open(self.save_file, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Source", "Target", "Section"])

    def getTags(self, dayDelta, section):
        """scrapes a section at dayDelta days before today to find the top tags"""
        URL = dateURL(dayDelta, section)
        tags = []
        with open(self.save_file, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            with urlopen(URL) as website:
                webpage = BeautifulSoup(website, features="html.parser")
                search = webpage.findAll(
                    name="a", attrs={"class": " submeta__link"})
                for a in search:
                    tag = a.get_text().lstrip().rstrip()
                    tag = strip(tag)
                    tags.append(tag)
            date = str(datetime.date.today() -
                       datetime.timedelta(days=dayDelta))
            database[date] = str(tags)[1:(len(str(tags)) - 1)]

            for tags in itertools.permutations(database[date].split(", "), 2):
                writer.writerow(list(tags) + [section])

    def getTagsCrossSection(self, dayDelta):
        """Gets the top tags from the sections in the last dayDelta days."""
        for day in range(dayDelta):
            for section in self.sections:
                self.getTags(day, section)
            print(str(dayDelta - day) + " days remaining")


def main():
    """This would create a graph file containing the interaction graph from the default sections in the last 340 days"""
    g = Guardian()
    g.initiateGraph()
    g.getTagsCrossSection(340)


if __name__ == '__main__':
    main()
