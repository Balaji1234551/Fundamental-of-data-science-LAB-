import pandas as pd
import string
import matplotlib.pyplot as plt
from collections import Counter

# 1. Load the CSV file
data = pd.read_csv(r"C:\Users\kurub\Downloads\data.csv")

# 2. Stop words
stop_words = {
    "the", "and", "is", "a", "an", "to", "of",
    "in", "for", "on", "with", "this", "that",
    "it", "was", "are", "very", "i", "we", "they"
}

# 3. Create an empty list for words
all_words = []

# 4. Preprocess each feedback
for feedback in data["feedback"]:
    
    # Convert to lowercase
    feedback = feedback.lower()
    
    # Remove punctuation
    feedback = feedback.translate(
        str.maketrans("", "", string.punctuation)
    )
    
    # Split into words
    words = feedback.split()
    
    # Remove stop words
    words = [
        word for word in words
        if word not in stop_words
    ]
    
    # Add words to the list
    all_words.extend(words)

# 5. Calculate word frequency
word_frequency = Counter(all_words)

# 6. Get N from user
N = int(input("Enter the number of top words (N): "))

# 7. Get top N words
top_words = word_frequency.most_common(N)

# 8. Display results
print("\nTop", N, "Most Frequent Words")
print("--------------------------------")

for word, frequency in top_words:
    print(word, ":", frequency)

# 9. Separate words and frequencies for plotting
words = [item[0] for item in top_words]
frequencies = [item[1] for item in top_words]

# 10. Create bar graph
plt.figure(figsize=(10, 5))
plt.bar(words, frequencies)

plt.title("Top Most Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
