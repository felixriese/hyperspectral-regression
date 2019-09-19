# import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# import subprocess
import matplotlib.pyplot as plt


def get_xy():
    # load dataframe
    path = "https://raw.githubusercontent.com/felixriese/hyperspectral-soilmoisture-dataset/master/soilmoisture_dataset.csv"
    df = pd.read_csv(path, index_col=0)

    # get features (= hyperspectral bands):
    features = [col for col in df.columns if col.isdigit()]
    # for col in df.columns:
    #     try:
    #         int(col)
    #     except Exception:
    #         continue
    #     features.append(col)

    X = df[features].values
    y = df["soil_moisture"].values

    return X, y


def get_xy_split(missing_rate=0.0):

    X, y = get_xy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=42, shuffle=True)

    if missing_rate == 0.0:
        return X_train, X_test, y_train, y_test

    # semi-supervised and active case
    else:
        rng = np.random.RandomState(42)
        random_unlabeled_points = rng.rand(len(y_train)) < missing_rate
        y_train_semi = np.copy(y_train)
        y_train_semi[random_unlabeled_points] = -1

        return X_train, X_test, y_train_semi, y_test, y_train


def get_xy_shifted(cut=35):
    X, y = get_xy()

    mask = y < cut
    X_train = X[mask]
    y_train = y[mask]
    X_test = X[~mask]
    y_test = y[~mask]

    return X_train, X_test, y_test, y_train


def write_results_to_latex_table(results, filename="results"):
    """Generate LaTeX table with results."""
    with open("results/"+filename+".tex", "w") as f:
        f.write("\documentclass{article}\n")
        f.write("\\usepackage{booktabs}\n")
        f.write("\\usepackage{multirow}\n")
        f.write("\\usepackage{siunitx}\n")
        f.write("\\begin{document}\n")
        f.write("\\begin{table}\n")
        f.write("\t\centering\n")
        f.write("\t\caption{Regression results for soil moisture.}\n")
        f.write("\t\\begin{tabular}{lSSSl}\n")
        f.write("\t\t\\toprule\n")
        f.write("\t\t Model &{$R^2$ in $\\%$} &{MAE} &{RMSE} & {Potential}\\\\\n")
        f.write("\t\t\midrule\n")
        for i in range(len(results["model"])):
            f.write("\t\t{model:10} & {r2:.1f} & {mae:.2f} & {rmse:.1f} & {potential}\\\\\n"
                    .format(model=results["model"][i],
                            r2=results["r2"][i]*100,
                            mae=results["mae"][i],
                            rmse=results["rmse"][i],
                            potential=results["potential"][i]))
        f.write("\t\t\\bottomrule\n")
        f.write("\t\end{tabular}\n")
        f.write("\t\label{tab:supervised_results}\n")
        f.write("\end{table}\n")
        f.write("\end{document}\n")
    # proc = subprocess.Popen(['pdflatex', '-output-directory', 'results',
    #                          "results/"+filename+".tex"])
    # proc.communicate()
    # try:
    #     os.remove("results/"+filename+".log")
    #     os.remove("results/"+filename+".aux")
    # except Exception:
    #     print("Warning: Not able to remove .log and .aux files!")


def plot_regression_results(truth, pred, model_name):
    _, ax = plt.subplots(1, 1, figsize=(5, 5))
    fontsize = 15

    # plot data
    plt.scatter(truth, pred, label="Datapoints", alpha=0.3)

    # set min and max
    pmin = np.min([np.min(truth), np.min(pred)]) - 1.
    pmax = np.max([np.max(truth), np.max(pred)]) + 1.
    plt.xlim(pmin, pmax)
    plt.ylim(pmin, pmax)

    # plot line
    plt.plot(np.linspace(pmin, pmax, 20), np.linspace(pmin, pmax, 20),
             linestyle="dashed", c="tab:red", label="Ideal estimation")

    plt.xlabel("Soil moisture (measured) in %", fontsize=fontsize)
    plt.ylabel("Soil moisture (estimated) in %", fontsize=fontsize)
    plt.legend(fontsize=fontsize*0.8)
    plt.title(model_name, fontsize=fontsize)
    for tick in ax.xaxis.get_major_ticks()[1::2]:
        tick.label.set_visible(False)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize)
    for tick in ax.yaxis.get_major_ticks()[1::2]:
        tick.label.set_visible(False)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize)
    plt.savefig("plots/truthestimation_"+model_name.replace(" ", "").lower()+".pdf",
                bbox_inches="tight")
