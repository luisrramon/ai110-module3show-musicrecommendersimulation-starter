"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.95}),
        ("Conflicting Edge Case", {"genre": "pop", "mood": "sad", "energy": 0.9}),
    ]

    for profile_name, user_prefs in profiles:
        print(f"\n=== {profile_name} ===")
        print(f"User prefs: {user_prefs}")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("Top recommendations:\n")
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reasons = explanation.split("; ") if explanation else ["No strong matches"]

            print(f"{index}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print("   Reasons:")
            for reason in reasons:
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()
