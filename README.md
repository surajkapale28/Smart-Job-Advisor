# Smart-Job-Advisor
This GitHub project, titled "AI Resume Analyzer," is a comprehensive tool designed for analyzing resumes, providing predictions, recommendations, and insights. Here's a breakdown of the project's key components and features:

### About the Project
- **Description**: A tool that parses information from resumes using natural language processing (NLP) techniques to find keywords and cluster them into sectors based on their keywords.
- **Functionality**: It offers recommendations, predictions, analytics, and tips to the applicant/recruiter based on keyword matching.

### Scope
- **Usage**: Suitable for structuring resume data for analytics, providing recommendations to improve resumes, and gaining insights into applicant profiles.
- **Audience**: Applicable for individuals, recruiters, colleges (for student placements), and organizations seeking analytics on resume data and job roles.

### Tech Stack
- **Frontend**: Utilizes Streamlit, HTML, CSS, and JavaScript for the user interface.
- **Backend**: Employs Python with Streamlit for the application logic.
- **Database**: MySQL for storing user data.
- **Modules**: Includes pandas, pyresparser, pdfminer3, Plotly, NLTK, among others.

### Features
- **Client Side**: Offers resume analysis, skill recommendations, course recommendations, tips, overall scores, and video recommendations.
- **Admin Side**: Allows access to applicant data, resume downloads, feedback management, and analytics through charts.
- **Feedback System**: Provides a form for users to submit feedback and view past comments and ratings.

### Requirements
- **Setup**: Requires installation of Python, MySQL, Visual Studio Code, and Visual Studio build tools for C++.
- **Dependencies**: Relies on various Python libraries and modules, including spacy.

### Installation
- The setup and installation instructions for the "AI Resume Analyzer" project are provided below:

1. **Download the Code**:
   - You can manually download the code files or use Git to clone the repository:
     ```bash
     git clone https://github.com/deepakpadhi986/AI-Resume-Analyzer.git
     ```

2. **Create Virtual Environment**:
   - It's recommended to create a virtual environment for the project to manage dependencies.
   - Open your command prompt and navigate to the project directory "AI-Resume-Analyzer".
   - Run the following commands to create and activate the virtual environment (assuming you're using Python 3):
     ```bash
     python3 -m venv venvapp

     cd venvapp/Scripts

     activate
     ```

3. **Install Dependencies**:
   - Navigate to the "App" folder within the project directory.
   - Run the following command to install dependencies from the "requirements.txt" file:
     ```bash
     cd ../..

     cd App

     pip install -r requirements.txt

     python -m spacy download en_core_web_sm
     ```

4. **Database Setup**:
   - After installing dependencies, create a database named "cv".
   - Modify the user credentials inside the "App.py" file to connect to your database.
     You can find the relevant section to modify at [this link](https://github.com/deepakpadhi986/AI-Resume-Analyzer/blob/17e1cdb207fef62557dc394f4158bda515e541fd/App/App.py#L95).

5. **Replace File**:
   - Go to the "venvapp\Lib\site-packages\pyresparser" folder.
   - Replace the existing "resume_parser.py" file with the one provided by the project inside the "pyresparser" folder.

6. **Congratulations!**:
   - With the completion of the above steps, your setup and installation process is finished.

These instructions should guide you through setting up the project environment successfully. If you encounter any issues or have questions, feel free to ask for assistance.
### Known Errors and Issue Resolution
- Addresses common errors encountered during installation and provides solutions.

### Roadmap
- Outlines future enhancements such as adding more fields for other roles, individual user details view, and further analytics.

### Contribution Guidelines
- Welcomes contributions via pull requests and encourages contributors to discuss major changes beforehand.

### Acknowledgement
- Credits Dr. Bright for guidance, academic resources, and open-source projects that contributed to the development of the tool.

### Preview
- Offers screenshots of the user interface, including the main screen, resume analysis, skill recommendations, feedback form, admin dashboard, and analytical representations.

This project provides a valuable resource for individuals and organizations involved in resume analysis and recruitment processes. It offers an intuitive interface, robust functionality, and opportunities for further development and collaboration.
