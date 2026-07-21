# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Musfinder 1.0**

---

## 2. Intended Use  

This recommender suggests songs based on a user's genre, mood, and energy preferences. It is built for classroom exploration, not for real users. It assumes the user can describe the kind of music they want in simple terms.

---

## 3. How the Model Works  

The model looks at genre, mood, energy, and acousticness. It gives extra points when a song matches the user's genre and mood. It also gives points for songs that are close to the user's target energy. The final score is the total of those parts, and the songs are ranked from highest score to lowest score.

---

## 4. Data  

The catalog has 18 songs. It includes pop, lofi, rock, ambient, jazz, synthwave, folk, blues, funk, reggaeton, classical, disco, electronic, and indie rock. I added a few synthetic songs to make the catalog more diverse. The dataset is still small, so it does not cover every style or every mix of musical taste.

---

## 5. Strengths  

The system works well for clear tastes like happy pop, chill lofi, and intense rock. It also does a good job of matching high energy songs to users who want high energy. The results usually make sense when the user profile is simple and focused.

---

## 6. Limitations and Bias 

The biggest weakness is that the recommender can create a small filter bubble around genre and energy. Users with mixed tastes, like high energy but sad mood, may still get upbeat songs that do not fully match what they want. The system can also favor genres that already have strong matches in the tiny catalog. It does not use lyrics, listening history, or context, so it misses more subtle taste patterns.

---

## 7. Evaluation  

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a conflicting edge case with pop, sad mood, and high energy. I checked whether the top songs matched the profile and whether the ranking changed in a sensible way. Happy pop users got upbeat pop songs, lofi users got softer and more acoustic songs, and the intense rock user got the rock song first. One surprise was that “Gym Hero” kept appearing near the top because it is pop and very high energy, so it scores well even when the mood is not a perfect match.

Profile comparisons:

- High-Energy Pop vs. Chill Lofi: the pop profile prefers bright, fast songs like “Sunrise City,” while the lofi profile shifts toward “Midnight Coding” and “Library Rain.” This makes sense because the lofi profile asks for lower energy and acoustic-friendly songs.
- High-Energy Pop vs. Deep Intense Rock: both profiles like high energy, but the rock profile moves the top result to “Storm Runner” because genre and mood now match rock and intense instead of pop and happy.
- Chill Lofi vs. Deep Intense Rock: these profiles pull in opposite directions. The lofi profile favors calm, acoustic songs, while the rock profile favors loud, intense songs, so the top results change a lot.
- Conflicting Edge Case vs. High-Energy Pop: both profiles still keep “Sunrise City” or “Gym Hero” near the top. This shows that energy and genre can outweigh a mood mismatch.

---

## 8. Future Work  

I would add more song features like tempo, danceability, and valence to make the score richer. I would also try better diversity rules so the top results are not too similar. I would give users more control over the weights so they can choose what matters most to them.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how small changes in the weights changed the whole ranking. AI tools helped me write and test the scoring logic faster, but I still had to double-check the math and the outputs because a small change could make the results feel wrong. I was surprised that a very simple algorithm could still feel like a real recommender when the explanations were clear. If I kept building this project, I would add more song features, improve diversity in the top results, and give users more control over the weights.
