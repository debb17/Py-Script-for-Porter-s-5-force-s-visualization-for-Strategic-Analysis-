import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 1: Define the framework ---
forces = ["Threat of New Entrants", 
          "Bargaining Power of Suppliers", 
          "Bargaining Power of Buyers", 
          "Threat of Substitutes", 
          "Industry Rivalry"]

# --- STEP 2: Collect user input ---
print("Rate each force from 1 (Low impact) to 5 (High impact).")
ratings = []
for force in forces:
    while True:
        try:
            score = int(input(f"{force}: "))
            if 1 <= score <= 5:
                ratings.append(score)
                break
            else:
                print("Enter a value between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer.")

# --- STEP 3: Store results ---
df = pd.DataFrame({
    "Force": forces,
    "Rating": ratings
})

# --- STEP 4: Visualize (Radar Chart) ---
def plot_radar(values, labels):
    N = len(labels)
    angles = [n / float(N) * 2 * 3.14159 for n in range(N)]
    values += values[:1]  # repeat first value to close the loop
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticks(range(1, 6))
    ax.set_yticklabels([str(i) for i in range(1, 6)])
    plt.title("Porter’s 5 Forces Analysis", size=15, weight="bold")
    plt.show()

plot_radar(ratings, forces)

# --- STEP 5: Quick interpretation ---
avg_score = sum(ratings) / len(ratings)
print("\n--- Strategic Insight ---")
if avg_score <= 2:
    print("Industry appears attractive with low competitive pressures.")
elif 2 < avg_score <= 3.5:
    print("Industry has moderate competition. Need selective positioning.")
else:
    print("Industry is highly competitive. Strong differentiation required.")
