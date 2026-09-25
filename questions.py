"""
questions.py
All 12 questions we ask Jev about every Amazon Food review.
6 topics x 2 questions.
"""

from typesafe_sdk import Noul, Score

# Food-centric review breakdown topics
TOPICS = {
    "Value for Money": "value_for_money",
    "Quality": "quality",
    "Performance": "performance",
    "Taste & Flavor": "taste_flavor",
    "Freshness": "freshness",
    "Texture": "texture",
}

# The 5 satisfaction levels mapped to 1-5 stars.
SATISFACTION_LEVELS = [
    "Very dissatisfied",
    "Dissatisfied",
    "Neither satisfied nor dissatisfied, or balanced mixed feedback",
    "Satisfied",
    "Very satisfied",
]

QUESTIONS = {
    "value_for_money_mentioned": Noul(
        instructions="Does the reviewer express whether the food item is worth its price or offers good value?"
    ),
    "value_for_money_rating": Score(
        instructions="How satisfied is the reviewer with the value for money?",
        criteria=SATISFACTION_LEVELS,
    ),
    "quality_mentioned": Noul(
        instructions="Does the reviewer comment on the overall production quality, ingredients, or premium nature of the food item?"
    ),
    "quality_rating": Score(
        instructions="How satisfied is the reviewer with the overall quality?",
        criteria=SATISFACTION_LEVELS,
    ),
    "performance_mentioned": Noul(
        instructions="Does the reviewer describe how well the food item serves its purpose, its effectiveness (e.g., energy boost, dietary results), or cooking behavior?"
    ),
    "performance_rating": Score(
        instructions="How satisfied is the reviewer with the product's performance or utility?",
        criteria=SATISFACTION_LEVELS,
    ),
    "taste_flavor_mentioned": Noul(
        instructions="Does the reviewer mention the taste, flavor profile, sweetness, saltiness, seasoning, or deliciousness of the food?"
    ),
    "taste_flavor_rating": Score(
        instructions="How satisfied is the reviewer with the taste and flavor?",
        criteria=SATISFACTION_LEVELS,
    ),
    "freshness_mentioned": Noul(
        instructions="Does the reviewer comment on whether the food item tastes fresh, crisp, or notes issues like being stale or expired?"
    ),
    "freshness_rating": Score(
        instructions="How satisfied is the reviewer with the freshness of the item?",
        criteria=SATISFACTION_LEVELS,
    ),
    "texture_mentioned": Noul(
        instructions="Does the reviewer comment on the physical texture, mouthfeel, crunchiness, smoothness, or consistency of the food?"
    ),
    "texture_rating": Score(
        instructions="How satisfied is the reviewer with the texture?",
        criteria=SATISFACTION_LEVELS,
    ),
}
