CGPA Analytics

A Python project to analyze and visualize CGPA data from Excel using **Pandas, Plotly, and Matplotlib**.  
This project helps you quickly generate insights and interactive plots for student CGPA trends.


⚙️ Setup Instructions

 1️⃣ Clone the Repository (if using GitHub)
```bash
git clone https://github.com/sudarshanverma19/CGPA-Analytics.git
cd CGPA-Analytics
2️⃣ Create a Virtual Environment

# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
3️⃣ Activate the Virtual Environment

# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
4️⃣ Install Dependencies

pip install -r requirements.txt
📂 Adding Your Data
Place your CGPA Excel file inside the data/ folder.

Example: data/cgpa.xlsx

Make sure the file has a proper header (e.g., Name, RollNo, CGPA).

▶️ Running the Project

python src/main.py
🔄 Updating the Environment Later
If you install new packages during development, update requirements.txt with:


pip freeze > requirements.txt
Then others (or future you) can install the updated list with:


pip install -r requirements.txt
📊 Libraries Used
pandas → Data manipulation

plotly → Interactive visualizations

matplotlib → Static plots

🛑 Exiting the Environment
To deactivate the virtual environment:


deactivate
(No worries if you forget—just restart your terminal.)

other commands that will help you .
cd file name
cd .. 
streamlit run app/main.py
touch file name
mkdir folder name
cp ~/Downloads/cgpa.xlsx data/
rm data/cgpa.xlsx

** Note : Sorry i can not provide you cgpa data of the students of my college if you have it in your mail that is fine.