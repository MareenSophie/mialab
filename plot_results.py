import matplotlib.pyplot as plt
import numpy as np
import os
import csv

def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    # in a boxplot
    results_file = "mia-result/2025-10-30-22-50-05/results.csv"  # path to your results.csv
    if not os.path.exists(results_file):
        raise FileNotFoundError(f"{results_file} not found.")

    # Prepare empty lists for each label
    labels = ['GreyMatter', 'WhiteMatter', 'Hippocampus', 'Amygdala', 'Thalamus']
    dice_per_label = {label: [] for label in labels}

    # Read CSV line by line
    with open(results_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            subject = row['SUBJECT']
            # Skip post-processed results if desired
            #if subject.endswith('-PP'):
                #continue
            label = row['LABEL']
            dice = float(row['DICE'])
            if label in dice_per_label:
                dice_per_label[label].append(dice)

    # Prepare data for boxplot in the correct label order
    data = [dice_per_label[label] for label in labels]

    # Plot boxplot
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, tick_labels=labels)
    plt.ylabel("Dice Coefficient")
    plt.title("Dice Coefficients per Brain Label")
    plt.ylim(0, 1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')


if __name__ == '__main__':
    main()
