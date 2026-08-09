import matplotlib.pyplot as plt

# Usability metrics (Likert scale 1–5)
categories = ["Interface Clarity", "Ease of Navigation", "Readability of Outputs"]
scores = [5, 4.5, 4.8]  # Example values that average to 4.8

# Calculate average usability score
average_score = sum(scores) / len(scores)
print("Average Usability Score:", average_score)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, scores, color=["skyblue", "lightgreen", "violet"])

# Chart labels
plt.title("Usability Evaluation (Likert Scale 1–5)")
plt.ylabel("Score")
plt.ylim(0, 5)

# Display values above bars
for i, v in enumerate(scores):
    plt.text(i, v + 0.1, str(v), ha='center')

plt.tight_layout()
plt.show()
