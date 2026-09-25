"""
aggregation.py
Combine per-review ratings into one average rating per topic.
"""

from questions import TOPICS

def aggregate(all_ratings):
    """Returns aggregated summary data per topic."""
    summary = {}

    for topic in TOPICS:
        scores = [ratings[topic] for ratings in all_ratings if topic in ratings]

        if scores:
            average = round(sum(scores) / len(scores), 1)
        else:
            average = None

        summary[topic] = {"average": average, "count": len(scores)}

    return summary
