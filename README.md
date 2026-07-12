# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

My recommender follows a simple content-based pipeline: it compares a user's taste profile to each song in the CSV, gives every song a score, and then sorts the songs from highest score to lowest score. The system prioritizes genre first, mood second, and energy closeness third so that the results stay easy to interpret and debug. This means the recommender should favor songs that feel like the user's preferred style, but still reward songs whose numeric features are close to the user's target values.

Algorithm Recipe:

1. Read each song from `data/songs.csv`.
2. Compare the song to the user profile.
3. Give a categorical match point for `genre` and `mood`.
4. Compute an energy similarity score using closeness instead of exact match:
   - `energy_similarity = max(0, 1 - abs(song_energy - target_energy))`
5. Combine the parts into one final score with genre weighted more than mood:
   - `final_score = 0.5 * genre_match + 0.2 * mood_match + 0.3 * energy_similarity`
6. Sort all songs by final score in descending order.
7. Return the top `K` recommendations with a short explanation for each one.

Features used in the simulation:

- Song features:
  - `id`
  - `title`
  - `artist`
  - `genre`
  - `mood`
  - `energy`
  - `tempo_bpm`
  - `valence`
  - `danceability`
  - `acousticness`

- UserProfile features:
  - `favorite_genre`
  - `favorite_mood`
  - `target_energy`
  - `likes_acoustic`

Potential biases and limitations:

- The system may over-prioritize genre and miss songs that match the user's mood or energy better.
- It may under-rank songs from smaller or less common genres because the catalog is tiny.
- It does not use lyrics, listening history, or context, so it can miss more subtle taste patterns.
- If the weights are too strong, the recommender can become narrow and keep returning very similar songs.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



