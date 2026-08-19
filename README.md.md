# CodeAlpha Secure Coding Review



## &#x20;CodeAlpha Cyber Security Internship - Task 3



### &#x20;  Project Description



This project is a secure coding review of a small Python Flask login application.



The project demonstrates how security vulnerabilities can be identified through source-code review and how the identified issues can be remediated in a secure version of the application.



#### &#x20;Application



\*\*Language:\*\* Python



\*\*Framework:\*\* Flask



\*\*Environment:\*\* Kali Linux



\### Files Reviewed



\- `vulnerable\_app.py` - Original application containing intentional security weaknesses.

\- `secure\_app.py` - Remediated version with security improvements.

\- `security\_review.md` - Security review report documenting the findings and recommendations.



\## Security Vulnerabilities Identified



The following security weaknesses were identified in the original application:



1\. Hardcoded secret key

2\. Hardcoded credentials

3\. Plaintext password handling

4\. Debug mode enabled



\## Security Improvements



The secure version addresses these issues by:



\- Loading the Flask secret key from an environment variable.

\- Avoiding hardcoded application secrets.

\- Using password hashing and secure password verification.

\- Adding basic input validation.

\- Disabling Flask debug mode.



\## Security Review Process



The review process consisted of:



1\. Creating and running the original application.

2\. Inspecting the source code manually.

3\. Identifying security weaknesses.

4\. Documenting the vulnerabilities and their risks.

5\. Applying remediation techniques.

6\. Creating and testing the secure version.



\## Evidence



Screenshots demonstrating the original vulnerable source code and the security review process are stored in the `screenshots` directory.



\## Project Structure



```text

CodeAlpha\_SecureCodeingReview/

│

├── vulnerable\_app.py

├── secure\_app.py

├── security\_review.md

├── README.md

│

└── screenshots/

&#x20;   ├── vulnerable\_code\_1.png

&#x20;   └── vulnerable\_code\_2.png

