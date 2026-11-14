# BUS 104: Finsimco Portfolio Management Simulation

Welcome to the **FinSimco** folder! Everything you need for the **Online Case Study (10% of your course grade)** is right here:

* **Rules, Deadlines & Grading Slides:** [`Portfolio_Simulation_Case_Study.pdf`](Portfolio_Simulation_Case_Study.pdf)
* **Ready-to-Run Python Starter Notebook:** [`Finsimco_Portfolio_Starter.ipynb`](Finsimco_Portfolio_Starter.ipynb)
* **One-Click Google Colab Link:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dxt48/BUS-104/blob/main/FinSimco/Finsimco_Portfolio_Starter.ipynb)

---

## Key Deadlines (At a Glance)
1. **Monday, Nov 23 (11:59 PM) — HARD PURCHASE CUTOFF:** Buy the Harvard Course Pack at `https://hbsp.harvard.edu/import/1456741` using your **exact UCR Canvas email and full name**. If you miss this deadline, you cannot be placed on a team and will receive **0%**.
2. **By Wednesday, Nov 25 — Teams Assigned:** Teams of 3 will be assigned from students who purchased the case by the Nov 23 cutoff.
3. **Monday, Nov 30 – Friday, Dec 4 — Play Window:** Teams of 3 complete Quarters 1–4 in Finsimco.
4. **Friday, Dec 4 (11:59 PM) — Individual Submission Due on Canvas:** Every student must individually submit their Team `#`, Finsimco Certificate, Optimization File (`.ipynb` or Excel), and brief summary on Canvas.

---

## Step-by-Step: How to Run the Python Notebook in Google Colab

You do **not** need to install Python on your computer. Google Colab runs everything for free in your web browser.

### 1. Download the Stock Data from Finsimco
1. Log into the Finsimco simulation and go to **Stage 2: Analysis & Quarter 1**.
2. Click the **History** tab at the top, then click **Download year historical data** (it downloads an Excel `.xlsx` file to your computer's `Downloads` folder).

### 2. Open the Starter Notebook in Google Colab
1. Click the blue **"Open In Colab"** badge above (or go to `https://colab.research.google.com/github/dxt48/BUS-104/blob/main/FinSimco/Finsimco_Portfolio_Starter.ipynb`).
2. Sign in with your **Google / UCR email** if asked.
3. *(Recommended)* Click **File $\to$ Save a copy in Drive** so your team's edits are saved to your Google Drive.

### 3. Run Each Cell from Top to Bottom
* Every code block has a **Play button (▶)** on the top-left corner. Click **▶** on **Step 1**, wait for it to finish, then click **▶** on **Step 2**, and so on.
* If Google Colab pops up a warning saying *"This notebook was not authored by Google"*, click **Run anyway**.
* **In Step 1**, a **"Choose Files"** button will appear under the cell. Click it and select the `.xlsx` historical data file you downloaded from Finsimco.
* **In Step 4**, run:
  * **Step 4A** if you are an **Odd Team (1, 3, 5, ... — Hedge Fund)**: maximizes your Sharpe Ratio.
  * **Step 4B** if you are an **Even Team (2, 4, 6, ... — Pension Fund)**: maximizes your Sharpe Ratio while keeping portfolio volatility below `VOL_CAP`.

### 4. Enter Your Trades in Finsimco
* The notebook prints a clean table with **Weight (%)** and **Dollar Allocation ($)** for each stock.
* **Important:** All 3 teammates share one portfolio in Finsimco. Pick **one teammate per quarter** to type the Buy/Sell orders into the **Trading** tab so you don't accidentally double-buy!

### 5. Download Your `.ipynb` for Canvas
* When you are done, click **File $\to$ Download $\to$ Download `.ipynb`** in Google Colab and upload that file to Canvas by **Friday, Dec 4 at 11:59 PM**.

---

## Option B: Using Finsimco's Built-In Excel Model (`PM Model`)
If your team prefers Excel over Python:
1. Inside Finsimco, click **PM Model** on the left-hand menu bar to download the built-in Excel template.
2. Watch the **6-minute Intro Video** on the Finsimco landing page (also available under **Overview** on the left menu)—it walks through how to use that Excel model step by step.
3. Upload your completed Excel file (`.xlsx`) to Canvas instead of a `.ipynb` notebook.

---

## Quick Troubleshooting FAQ
* **`NameError: name 'pd' is not defined` (or `'prices' is not defined`):** You skipped a cell! Always run cells **in order from Step 1 down to Step 4**.
* **My `Choose Files` button didn't appear in Step 1:** Make sure pop-ups/third-party cookies aren't blocking Colab's upload widget, or click the **Folder icon (📁)** on the left sidebar of Colab, drag-and-drop your `.xlsx` file there, and set `filename = "your_file_name.xlsx"` in Step 2.
* **Pension Fund optimization says "did not converge":** Increase `VOL_CAP` slightly (for example, from `0.16` to `0.18` or `0.20`) and re-run Step 4B.
