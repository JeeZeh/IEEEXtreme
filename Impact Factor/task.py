import json
import sys

n = input()
publications = json.loads(input())["publications"]
packets = []

for line in sys.stdin:
    packets.append(json.loads(line))

factors = []

def get_impact_factor(publication):
    impact_factor = None

    publication_count = sum(
        [
            int(count["articleCount"]) 
            for count in publication["articleCounts"] 
            if count["year"] == "2018" or count["year"] == "2017"
        ]
    )

    pub_id = publication["publicationNumber"]
    citation_count = 0
    
    for packet in packets:
        for citation in packet["paperCitations"]["ieee"]:
            if (citation["year"] == "2018" or citation["year"] == "2017") and citation["publicationNumber"] == pub_id:
                    citation_count += 1

    impact_factor = citation_count/publication_count


    return (publication["publicationTitle"], impact_factor)

for publication in publications:
    factors.append(get_impact_factor(publication))

factors.sort(key=lambda tuple: tuple[1], reverse=True)

for factor in factors:
    print(factor[0] + ": " + "{0:.2f}".format(factor[1]))