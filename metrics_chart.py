import matplotlib.pyplot as plt

# Metrics
metrics = ["Latency (s)", "Accuracy (%)", "Usability (1–5)"]
values = [6.9141387939453125e-06, 100, 4.8]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(metrics, values, color=["blue", "green", "purple"])

# Labels and title
plt.title("System Performance Metrics Visualization")
plt.ylabel("Metric Values")
plt.xlabel("Metrics")

# Display values above bars
for i, v in enumerate(values):
    plt.text(i, v + (v * 0.05 if v != 0 else 0.000001), str(v), ha='center')

plt.tight_layout()
plt.show()
