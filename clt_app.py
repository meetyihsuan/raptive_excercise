
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="CLT Visualizer", layout="wide")

st.title("The Central Limit Theorem (CLT) Machine")

st.markdown("""
The **Central Limit Theorem (CLT)** means that as long as you have a 
large enough sample size, the distribution of the **sample means** will be normally distributed, 
no matter what the original distribution it was.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Settings")
    dist_type = st.selectbox("1. Pick a population", 
                             ["Exponential (Skewed)", "Uniform (Flat)", "Bimodal (Two Humps)"])
    
    sample_size = st.slider("2. Sample Size (n)", 1, 100, 30, 
                            help="How many data points we average together to get ONE mean.")
    
    num_simulations = st.slider("3. Number of Simulations", 100, 10000, 2000, 
                                help="How many times we repeat the sampling process.")

# Generate the population based on selection
np.random.seed(42)
if dist_type == "Exponential (Highly Skewed)":
    pop = np.random.exponential(scale=2, size=10000)
elif dist_type == "Uniform (Flat)":
    pop = np.random.uniform(low=0, high=10, size=10000)
else:
    # Bimodal
    pop = np.concatenate([np.random.normal(2, 0.8, 5000), np.random.normal(8, 0.8, 5000)])

# Perform the simulation: Take samples and calculate their means
means = [np.mean(np.random.choice(pop, size=sample_size)) for _ in range(num_simulations)]

# Visualization
col1, col2 = st.columns(2)

with col1:
    st.subheader("The Parent Population")
    fig1, ax1 = plt.subplots()
    sns.histplot(pop, kde=True, color="orange", ax=ax1)
    ax1.set_title("Original Data Distribution")
    st.pyplot(fig1)

with col2:
    st.subheader("The Sampling Distribution")
    fig2, ax2 = plt.subplots()
    sns.histplot(means, kde=True, color="teal", ax=ax2)
    ax2.set_title(f"Distribution of Sample Means (n={sample_size})")
    st.pyplot(fig2)

