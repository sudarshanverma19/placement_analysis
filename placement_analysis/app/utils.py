def get_total_cgpa_distribution(master_df):
	"""
	Returns a DataFrame with total student distribution by CGPA range from master data.
	"""
	master_df = master_df.copy()
	master_df["UG Mark"] = master_df["UG Mark"].replace({"": None, pd.NA: None})
	master_df["CGPA Range"] = master_df["UG Mark"].apply(categorize_cgpa)
	total_stats = master_df.groupby("CGPA Range").size().reset_index(name="Count")
	return total_stats
import pandas as pd

def load_master_data(path="data/student_cgpa.xlsx"):
	"""
	Loads the master Excel dataset containing student information.
	Returns a pandas DataFrame.
	"""
	df = pd.read_excel(path)
	# Ensure expected columns exist
	expected_cols = ["Registration Number", "Full Name", "UG Mark"]
	missing = [col for col in expected_cols if col not in df.columns]
	if missing:
		raise ValueError(f"Missing columns in master data: {missing}")
	return df

def categorize_cgpa(cgpa):
	"""
	Categorizes CGPA into buckets: '<8', '8-8.5', '8.5-9', '9+'.
	"""
	if cgpa is None or (isinstance(cgpa, float) and pd.isna(cgpa)):
		return "Missing"
	try:
		cgpa = float(cgpa)
	except (TypeError, ValueError):
		return "Missing"
	if cgpa < 8:
		return "<8"
	elif 8 <= cgpa < 8.5:
		return "8-8.5"
	elif 8.5 <= cgpa < 9:
		return "8.5-9"
	elif cgpa >= 9:
		return "9+"
	return "Missing"

def analyze_shortlist(master_df, shortlist_df):
	"""
	Analyzes shortlisting by CGPA range.
	Returns (shortlisted_stats, not_shortlisted_stats) DataFrames.
	"""
	# Add CGPA Range column
	master_df = master_df.copy()
	# Fill missing CGPA values with None for consistent handling
	master_df["UG Mark"] = master_df["UG Mark"].replace({"": None, pd.NA: None})
	master_df["CGPA Range"] = master_df["UG Mark"].apply(categorize_cgpa)

	# Standardize merge key
	master_df = master_df.rename(columns={"Registration Number": "regno"})
	shortlist_df = shortlist_df.rename(columns={"Registration Number": "regno"})

	# Find common regno (shortlisted) and not shortlisted
	common_regnos = set(master_df["regno"]).intersection(set(shortlist_df["regno"]))
	shortlisted = master_df[master_df["regno"].isin(common_regnos)]
	not_shortlisted = master_df[~master_df["regno"].isin(common_regnos)]

	shortlisted_stats = (
		shortlisted.groupby("CGPA Range").size().reset_index(name="Count")
	)
	not_shortlisted_stats = (
		not_shortlisted.groupby("CGPA Range").size().reset_index(name="Count")
	)

	return shortlisted_stats, not_shortlisted_stats
