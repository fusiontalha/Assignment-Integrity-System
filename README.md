# Assignment-Integrity-System
Assignment Integrity System
The Assignment Integrity System is a web application developed using Django, aimed at facilitating the assignment submission process and ensuring academic integrity. It provides two panels, one for teachers and the other for students, enabling teachers to upload assignment questions and students to submit their answers. The application also includes a plagiarism detection feature that generates a plagiarism report.

Features
Teacher Panel:

Upload assignment questions: Teachers can easily upload assignment questions.
Manage assignments: Teachers can view and manage all the assignments they have uploaded.
Monitor submissions: Teachers can keep track of the submissions made by students and review their answers.
Student Panel:

Submit answers: Students can submit their answers to the assignment questions through the application.
Track submissions: Students can view the assignments they have submitted and their current status.
Receive feedback: Students can receive feedback and grades from their teachers on their submissions.
Plagiarism Detection:

Automatic plagiarism check: The system incorporates a powerful plagiarism detection algorithm to identify any instances of plagiarism in the students' submissions.
Plagiarism report: A detailed plagiarism report is generated, highlighting any matched content and providing a percentage indicating the level of similarity.
Installation
Clone the repository:

git clone (https://github.com/fusiontalha/Assignment-Integrity-System.git)
Change into the project directory:

cd assignment-integrity-system
Create a virtual environment (optional but recommended) and activate it:

python -m venv env
env/Scripts/activate.bat

Install the dependencies:
pip install -r requirements.txt

Set up the database:

python manage.py migrate
Create a superuser account (for accessing the admin panel):

python manage.py createsuperuser
Start the development server:

python manage.py runserver
Access the application in your web browser at http://localhost:8000.

Configuration
The application's configuration can be modified in the settings.py file located in the assignment_integrity_system directory. Here, you can adjust various settings such as database configuration, and file storage options.

Usage
As a teacher:

Log in to the teacher panel using your credentials.
Upload assignment questions.
Monitor student submissions and review their answers.
Provide feedback and grades for each submission.
As a student:

Log in to the student panel using your credentials.
View available assignments and their submission status.
Submit your answers to the assignment questions.
Check the feedback and grades provided by the teacher.
Contribution
Contributions to the Assignment Integrity System are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make the necessary changes and commit them.
Push your branch to your forked repository.
Submit a pull request describing your changes.
Please ensure that your contributions adhere to the code of conduct.

License
The Assignment Integrity System is open-source software licensed under the MIT License. Feel free to modify and distribute the application as per the terms of the license.
