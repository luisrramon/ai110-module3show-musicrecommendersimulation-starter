# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The biggest weakness I noticed is that the recommender can create a small filter bubble around genre and energy. Because genre has a large weight and energy is scored by closeness, users who want unusual combinations like high energy but sad mood may still get pushed toward upbeat songs that do not fully match their intent. The system can also over-recommend songs from genres that already have strong matches in the tiny catalog, while overlooking songs that are interesting but only match on mood or acousticness. Since the dataset is small and missing richer context like lyrics or listening history, the model may feel accurate for a narrow set of users but less flexible for more complex tastes.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a conflicting edge case with pop + sad + high energy. I looked for whether the top songs matched the intended vibe, and I compared how the ranking changed when the profile changed. The results mostly made sense: happy pop users got upbeat pop songs, lo-fi users got softer and more acoustic songs, and the intense rock user got the rock track first. What surprised me most was that the same song, “Gym Hero,” kept showing up near the top for more than one profile because it is a pop song with very high energy, so it scores well even when the mood does not fully match.

Profile comparisons:

- High-Energy Pop vs. Chill Lofi: the pop profile prefers bright, fast songs like “Sunrise City,” while the lofi profile shifts toward “Midnight Coding” and “Library Rain.” That makes sense because the lofi profile asks for lower energy and acoustic-friendly songs, so the scoring rule rewards those tracks more strongly.
- High-Energy Pop vs. Deep Intense Rock: both profiles like high energy, but the rock profile moves the top result to “Storm Runner” because genre and mood now match rock and intense instead of pop and happy. This shows that genre still matters, not just energy.
- Chill Lofi vs. Deep Intense Rock: these profiles pull in almost opposite directions. The lofi profile favors calm, acoustic songs, while the rock profile favors loud, intense songs, so the top results change a lot. That is a good sign because it means the scoring rule is reacting to the user’s preferences instead of returning the same songs every time.
- Conflicting Edge Case vs. High-Energy Pop: both profiles still keep “Sunrise City” or “Gym Hero” near the top, which shows that energy and genre can outweigh a mood mismatch. This makes sense with the current weights, but it also explains why a user who wants "sad but high-energy" may not get a truly sad song back.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
