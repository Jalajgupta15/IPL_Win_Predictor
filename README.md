# IPL Win Predictor

## Overview
The **IPL Win Predictor** is an interactive web application designed to estimate the winning probabilities of Indian Premier League (IPL) teams based on match conditions and historical data. It provides an engaging way for cricket enthusiasts to analyze potential match outcomes using statistical insights and real-time inputs.

---

## Features

- **Team Selection:** Choose any two IPL teams from a list of historical IPL franchises.
- **Dynamic Inputs:**
  - Target runs
  - Current runs scored
  - Overs completed
  - Wickets lost
  - Match venue
- **Win Probability Calculation:**
  - Utilizes historical statistics combined with live match conditions.
- **Visualization:**
  - Displays winning probabilities as a clear and intuitive bar chart.
- **Prediction:**
  - Provides an insightful prediction of the likely winner or a possible tie.
- **Custom IPL Styling:**
  - Engages users with a visually appealing IPL-themed interface.

---

## How It Works
1. Load the match data from the provided `matches.csv` file.
2. Input the current match conditions (runs, overs, wickets, etc.).
3. Select the competing teams and venue.
4. The app computes win probabilities using:
   - Historical home/away win percentages.
   - Current match progress.
5. Visualize the probabilities and view the predicted winner in real-time.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for building the interactive web app.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Visualizing the win probabilities.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ipl-win-predictor.git
   cd ipl-win-predictor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open the provided URL in your browser to use the app.

---

## Data
The application uses historical IPL match data stored in `matches.csv`. Ensure the file is present in the same directory as the app script.

---

## Usage

1. Select the two teams competing in the match.
2. Enter the current match conditions (e.g., target runs, runs scored, overs completed, wickets lost).
3. Select the match venue.
4. View the predicted win probabilities and results.

---

## Project Structure

```
ipl-win-predictor/
|-- matches.csv             # IPL match data file
|-- app.py                  # Main application script
|-- requirements.txt        # List of required Python packages
|-- README.md               # Project README file
```

---

## Screenshot

![image](https://github.com/user-attachments/assets/91d764a8-9746-45c5-b39b-8ea4a09e1486)
![image](https://github.com/user-attachments/assets/af61089f-2053-4419-b19d-88af2c3d8275)


---

## Contribution

Contributions are welcome! Feel free to submit issues or pull requests for enhancements, bug fixes, or additional features.

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---
