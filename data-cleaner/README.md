A simple and intuitive web app built with Streamlit that allows users to upload, clean, and convert their CSV and Excel files effortlessly.

🚀 Features
Upload CSV and Excel files.

Clean Data by filling missing values in numeric columns with the mean.

Remove Duplicate Rows to ensure clean data.

Column Selection allows users to keep only selected columns.

Data Visualization shows bar charts for numeric columns.

Convert Formats between CSV and Excel.

Download the cleaned and converted files with just one click.

🛠️ Technologies Used
Streamlit - For building the web app interface.

Pandas - For data manipulation and cleaning.

BytesIO - For handling file download functionality.

📥 Installation & Setup
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/file-converter-cleaner.git
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv .venv
Activate the virtual environment:

On Windows:

bash
Copy
Edit
.\.venv\Scripts\activate
On Mac/Linux:

bash
Copy
Edit
source .venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run main.py
Open the link displayed in your terminal to use the app locally.

⚙️ Configuration
The app is configured to accept multiple file uploads.

Users can choose to clean data by filling missing values or removing duplicate rows.

Users can convert files between CSV and Excel formats.

📜 Usage
Upload your CSV or Excel file.

Preview the data and clean it by filling missing values or removing duplicates.

Choose the columns you want to keep.

Visualize the data with bar charts (optional).

Select the desired format (CSV or Excel) for conversion.

Click the download button to save your cleaned and converted file.

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

Additional Sections You Might Want to Add:
Contributing: If others want to contribute to your project, include instructions here (e.g., fork the repo, make changes, and create a pull request).

FAQ: If you receive common questions or need to explain some aspects of the app, add a FAQ section.

Example:
markdown
Copy
Edit
## 🤔 FAQ

**Q: How do I use the bar chart feature?**
A: You can choose columns with numeric data and visualize them in a bar chart format by clicking the "📊 Show Chart" checkbox.

**Q: Can I convert files to other formats apart from CSV and Excel?**
A: Currently, the app supports only CSV and Excel conversions. Future updates may include additional formats.