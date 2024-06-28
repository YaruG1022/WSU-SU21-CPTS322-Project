# Sprint 2 Report (6/01/24 - 6/28/2024)

## What's New (User Facing)
 * Added a Report Generating System: Users can now export inventory, donation, and order data as a CSV or XLSX file. It also allows users to view the inventory, donation, and order data tables by selecting and sorting by name, quantity, category, date, or status.
 * Added an Inventory Management System: This system allows users to add, update, or delete items in the database and view item information. It supports real-time updates of inventory item data and includes a view for the comprehensive item list mentioned above.
 * Added a Donation Management System: Users can add donations to the database with details such as name, date, quantity, and image. Users can also search existing items by name or ID.
 * Added a Log-In and Sign-Up System: This system features login and signup modals. Users need to sign up if they don't have an account and log in to use other features of the website. It also includes a "remember me" feature to store user information.
 * Added a User Center: Once logged in, users can access this page. On this page, users can edit their information, including avatar, name, email, and ID.
 * Implemented Transport Layer Security (TLS) Encryption: Passwords are now stored as encrypted code in the application's database file.
 * Implemented Two-Factor Authentication (2FA): Users can set up 2FA in the user center. Once it is set up, users will need to verify their identity via QR code at login time.
 * Improved UI Design: Enhanced the visual design of all pages, adding features such as a slideshow and a clickable menu on the homepage for a better visual experience.
 

## Work Summary (Developer Facing)
During this sprint, I developed a complete static HTML template, including the frontend of login modal, user center, and other related pages. I also created the backend for a report generating system and an inventory management system. Additionally, I added various interactive features to the templates and made overall UI improvements, enhancing the visual design and usability of the HTML pages.

My team member developed the basic framework of our application, as well as the backend system for the user center. He also added the login and sign-up system, TLS encryption, and 2FA system. Additionally, he developed a donation management system and the basic features of the inventory management system.

## Unfinished Work
In this sprint, we were unable to fully complete the overall improvements to the user interface and the design of some pages, such as the stylesheet for the donation management page. The stylesheet for this page needs to be redone to match the new updates made by my team member. Additionally, several interactive features, including the homepage slideshow, were not finished due to time constraints. These features, along with other planned enhancements, were given lower priority compared to major functionalities. These improvements are set as goals for our next sprint. It is also likely that the recipient order backend system will remain unfinished due to time constraints.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * [Develop a complete HTML interface](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/2)
 * [Develop login and signup system](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/8)
 * [Add TLS encryption to server communication](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/11)
 * [Implement 2FA on backend](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/12)
 * [Integrate inventory management with the main interface](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/13)
 * [Implement report generating system](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/15)
 * [Implement inventory management system](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/16)
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 We set this issue as the final task to be completed at the end of the project
 * [TODO: Implement Frontend and Backend Systems](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/3) <<We designated this issue as the final task to be completed at the end of the project, completing this issue means that our project is completed.>>
 * [Overall User Interface Improvement](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/7) <<We think this issue has lower priority comparing to the major-functionality-related issues so we postponed this issue to the next sprint.>>
 * [Improve the usability, conveniency and efficiency of the application of our inventory management system](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/issues/17) <<We set this issue as the goal of the next sprint.>>

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [main/src](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/tree/dc74c128ea521ddb33a990efe9fc965d6ed99237/src)
 * [Backend/src](https://github.com/YaruG1022/WSU-SU21-CPTS322-Project/tree/ccd3fc07a882a14aa88f8ce73783aed0cf34ec80/src)
 
## Retrospective Summary
In this sprint, we have essentially completed all foundational functionalities of our website and integrated the frontend and backend systems by connecting HTML to flask application. Although the basic functionalities have been achieved, we aim to improve them. We intend to enhance other aspects of our application to meet the goals stated in the initial proposal.

Here's what went well:
  * Completed most of the vital implementations of the management system for the application.
  * Tested and ensured that all the implemented functionalities work well.
 
Here's what we'd like to improve:
   * Improve usability and reliability of the application.
   * Enhance efficiency and convenience of the management system.
   * Improve UI design quality, making the website more visually appealing.

Here are changes we plan to implement in the next sprint:
   * Add more advanced functionalities to the management system for inventory, donation, and order for better convenience, such as the ability to select the desired number of items to export and support for adding or editing user-defined categories of items.
   * Enhance the security of our application, requiring users to be certified as staff to manage inventory items.
   * Add more interactive features to the HTML pages for decorative purposes.

