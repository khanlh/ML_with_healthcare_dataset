import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_gender_distribution(data):
    plt.figure(figsize=(6, 5))
    ax = sns.countplot(x="Gender", data=data, palette="Set2")
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    fontsize=12, color='black',
                    xytext=(0, 9), textcoords='offset points')
    plt.title("Gender Distribution")
    plt.show()

def plot_age_distribution(data):
    plt.figure(figsize=(8, 5))
    sns.histplot(data["Age"], bins=30, kde=True, color="green")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()

def plot_billing_amount(data):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=data["Billing Amount"], color="lightblue")
    plt.title("Billing Amount Spread")
    plt.show()

def plot_age_wise_admission_type(data):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=data, x='Admission Type', y='Age')
    plt.title('Age-wise Admission Type', fontweight='bold')
    plt.xlabel('Admission Type', size=13)
    plt.ylabel('Age Distribution', size=13)
    plt.show()