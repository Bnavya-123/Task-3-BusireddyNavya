# AI Recommendation System
# DecodeLabs Project 3

movies = {
    "Interstellar": ["Sci-Fi", "Adventure", "Space"],
    "Avengers": ["Action", "Adventure", "Superhero"],
    "Inception": ["Sci-Fi", "Thriller", "Mind-Bending"],
    "Titanic": ["Romance", "Drama"],
    "John Wick": ["Action", "Thriller"],
    "The Notebook": ["Romance", "Drama"],
    "The Martian": ["Sci-Fi", "Space", "Adventure"],
    "Spider-Man": ["Action", "Superhero", "Adventure"]
}


def recommend_movies(user_preferences):
    recommendations = []

    for movie, tags in movies.items():

        match_score = len(
            set(user_preferences).intersection(set(tags))
        )

        percentage = (match_score / len(user_preferences)) * 100

        recommendations.append(
            (movie, match_score, percentage)
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations


print("\n===== AI RECOMMENDATION SYSTEM =====\n")

print("Available Categories:")
print("Action, Adventure, Sci-Fi, Thriller")
print("Romance, Drama, Space, Superhero")
print()

user_input = input(
    "Enter your interests separated by commas: "
)

preferences = [
    item.strip().title()
    for item in user_input.split(",")
]

results = recommend_movies(preferences)

print("\nTop Recommendations:\n")

for movie, score, percentage in results[:5]:

    if score > 0:
        print(
            f"{movie} | Match Score: {score} | "
            f"Similarity: {percentage:.0f}%"
        )