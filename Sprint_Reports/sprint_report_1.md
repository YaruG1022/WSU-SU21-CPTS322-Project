# Sprint 1 Report (5/17/24 - 5/31/2024)

## What's New (User Facing)
 * User Interface Update: Developed HTML-based web pages including homepage, inventory management page, and donation page. 
 * User Interface Update: Enchanced the design of homepage and inventory page and added new features including log-in area, inventory list, inventory management buttons, report generating button.
 * Backend Update: Added package structure, dependency installation, SQLAlchemy backend, basic test pages, and the Flask app.

## Work Summary (Developer Facing)
In this sprint, I used fundamental HTML knowledge to create the web template. To enhance the site, I expanded my skills in HTML and explored basic JavaScript to add dynamic elements to our web pages. My team member worked on learning Flask, overcoming the challenge of setting up a server that interacts with our database and renders templates. We also established a general package structure to simplify the process of installing dependencies. 

## Unfinished Work
In this sprint, due to time constraints, we were unable to fully complete the development of our HTML UI website as the scope of this task is more extensive than we anticipated. Additionally, interactive UI elements, user account functionalities and comprehensive database design remain underdeveloped. We have decided to implement these features in the upcoming sprints.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * [Set up SQLAlchemy database engine and flask backend](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/4)
 
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 We set this issue as the final task to be completed at the end of the project
 * [TODO: Implement Frontend and Backend Systems](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/3) <<We designated this issue as the final task to be completed at the end of the project,.>>
 * [Develop a complete HTML interface](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/2) <<We found that providing a complete UI for the whole project was a much bigger task than expected, which could not be completed by the deadline of Sprint 1.>>

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [main/src](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/tree/dc74c128ea521ddb33a990efe9fc965d6ed99237/src)
 * [interface/src/template](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/tree/2ade5d95e441eb082bc0703f712d611479a3f86c/src/template)
 
## Retrospective Summary
In this sprint, we made significant progress by building a multi-page website and setting up a basic operational backend. We also identified areas for enhancement, particularly in making our website more interactive and functional. Going forward, we aim to integrate our frontend and backend components, implement authentication processes, and extend our database to store various types of information.

Here's what went well:
  * Successfully created a multi-page web template featuring a descent design.
  * Established and tested a foundational database and basic operational functionality.
 
Here's what we'd like to improve:
   * Refine HTML architecture and enhance data structures for increased usability. Implementing reusable components, such as navigation bars and login forms, in a single JavaScript file will allow for global integration across all HTML pages, facilitating easier updates and maintenance.
   * Integrate more JavaScript functionalities, enriching UI features and reduce the redundancy of code across web pages.
   * Refactor HTML code to be more organized and streamlined. 

Here are changes we plan to implement in the next sprint:
   * Integrate Flask to bridge the backend functionality with the frontend, enhancing the application's functionality beyond static displays to interactive, operational features.
   * Implement modal pop-up windows for user authentication, enabling login and registration functionalities that interact with backend processes.
   * Expand SQL database architecture to include diverse data types such as user account details, inventory, donations, and transaction records
   * Develop and refine the login system, and establish a backup system for data integrity and recovery.
   * Develop a security system by implementing two-factor authentication (2FA) and Transport Layer Security (TLS) protocols.

