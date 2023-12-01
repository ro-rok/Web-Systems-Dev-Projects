<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Rohan Khanna (rk868)</td></tr>
<tr><td> <em>Generated: </em> 12/1/2023 12:21:58 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/rk868" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.34.18image.png.webp?alt=media&token=8320e075-40e5-4063-aada-9d5ee3e46aae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index with my name and ucid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.35.07image.png.webp?alt=media&token=61b9f724-01f6-4899-bf6f-c26fac7fa9d2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for base html<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.42.19image.png.webp?alt=media&token=20ab057b-2ad7-4f6d-ae62-652b32d8faa0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Nav bar with changed ucid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.43.09image.png.webp?alt=media&token=02ad7d3f-d689-4c15-98dd-1d6018587dac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for nav.html<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.44.06image.png.webp?alt=media&token=7b94bf75-864d-423e-a1b7-2f080c9f30b3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check for .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.45.01image.png.webp?alt=media&token=d40ddc5c-1b9a-4dee-8048-25542963e954"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for csv2,3,4, reading the csv and extracting organization and donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.46.08image.png.webp?alt=media&token=63992d6c-beb1-4036-aa6e-7cb0947ed2de"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for csv5,6,7,8: performing multiple checks and corresponding flash messages<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.55.29image.png.webp?alt=media&token=c5766260-a3d6-4169-8180-5251b79e653c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add And Edit Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T18.57.12image.png.webp?alt=media&token=5f878ccb-3fd7-4fd6-95df-f78e04f803c9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit View<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.06.08image.png.webp?alt=media&token=0e8586d9-270d-49aa-8b53-a3b738aafd93"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add View<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.10.33image.png.webp?alt=media&token=85816fd8-70c6-4d8d-a485-01544337d5e6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unfiltered Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.12.05image.png.webp?alt=media&token=a4894a1b-93a4-40b7-898c-abe6bbbe7fe2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filtering of Code with Item Name in desc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.17.12image.png.webp?alt=media&token=afcfe53d-5e86-4377-9160-2031f4c032c9"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML Code of manage donation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.18.06image.png.webp?alt=media&token=3213e6d6-dc22-4350-ac73-a8de245668da"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for search-1: retrieve donation details using LEFT JOIN; search-2 gets args; search-3-6<br>append like filters for firstname, lastname, email, item_name; search-7 appends equality filter for<br>organization_id; search-8 appends sorting if args present and valid.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.24.09image.png.webp?alt=media&token=24cf9556-23da-43e2-8e9f-55bd2b3b7536"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for search-9: append limit (default 10) or limit between 1 and 100;<br>search-10: provide proper error message for invalid limit; search-11: make error message user-friendly;<br>search-12: set organization_name variable to correct name if organization identifier is in request<br>args.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.25.02image.png.webp?alt=media&token=50c53b0e-4b8e-462e-93a8-8d92f1fb4a11"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for add-1: retrieve form data for donor details; add-2 to add-8 specify<br>required fields and format validations, flashing proper error messages for missing or incorrect<br>data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.26.28image.png.webp?alt=media&token=928f0d81-a67e-4d54-a552-1df919540024"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for add-9: ensure donation_date is required and within the past 30 days;<br>add-10: specify comments as optional; add-11: add query and arguments; add-7: enhance user-friendly<br>error messages for better understanding.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.28.03image.png.webp?alt=media&token=8f6fa11f-ed3f-4322-9094-43f9caa6e051"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for edit-1: ensure request args id is required, flashing a proper error<br>message; add-2: retrieve form data for donor details; add-3 to add-8: specify required<br>fields and format validations, flashing proper error messages for missing or incorrect data;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.28.24image.png.webp?alt=media&token=d6201fd2-5c40-4a3f-b3f8-4930dc08dc07"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for add-9: ensure item_quantity is required and more than 0, flashing proper<br>error message; add-10: ensure donation_date is required and within the past 30 days;<br>add-11: specify comments as optional; edit-12: fill in proper update query; edit-13: enhance<br>user-friendly messages; edit-14: fetch updated data; edit-15: improve user-friendly error messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.35.36image.png.webp?alt=media&token=f8d5ec53-3aef-4371-9449-59ce38e9e61f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for delete-1: flash a necessary message and redirect to search if id<br>is missing; delete-2: delete donation by id from the request; delete-3: ensure a<br>flash message shows for successful delete; delete-4: pass all arguments except id to<br>this route; delete-5: redirect to donation search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.36.03image.png.webp?alt=media&token=206c2c23-ae0e-460b-bb3d-0bd4c33a2b53"/></td></tr>
<tr><td> <em>Caption:</em> <p>SS of Successful  deletion<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.39.26image.png.webp?alt=media&token=bbfb259e-b76e-4a5c-9c61-fc5847c816cd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for edit view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.40.08image.png.webp?alt=media&token=821657e0-c0de-47ae-91bf-b6828f8e158d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for create vie<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.43.37image.png.webp?alt=media&token=78608dc5-9467-4074-b8b7-c43ff11c8d35"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add And Edit Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.39.02image.png.webp?alt=media&token=31327bcf-cf9c-4cb1-8816-b9ecaeeb61db"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page loaded with No organization filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.47.23image.png.webp?alt=media&token=51ce706a-0039-444f-aa8a-c39a4dcdeb27"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page Loaded with state sorted in desc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.46.14image.png.webp?alt=media&token=13c1a890-946f-48e3-8067-9d08a43c261b"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML code for manage_organization<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-01T05.16.41image.png.webp?alt=media&token=d1a8576f-d964-4e03-8cba-b41b16b0101d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for search-1: retrieve organization details with donation count; search-2 gets name, country,<br>state, column, order, limit from args; search-3 appends LIKE filter for name if<br>provided; search-4 appends equality filter for country if provided; search-5 appends equality filter<br>for state if provided; search-6 appends sorting if args valid.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.50.05image.png.webp?alt=media&token=b4be895e-bd1e-47cb-926b-4c78b90bc648"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for search-7: append limit (default 10) or limit between 1 and 100;<br>search-8: provide error message if limit isn&#39;t a valid number or out of<br>bounds; search-9: create user-friendly error message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.52.01image.png.webp?alt=media&token=af2f4b31-2c95-4093-b83b-f9701db3a88e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for add-1: retrieve form data for name, address, city, state, country, zip,<br>website, description; add-2 to add-7: validate and flash proper error messages for required<br>fields; add-5a: ensure state is a valid state mentioned in pycountry for the<br>selected country.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T19.52.33image.png.webp?alt=media&token=38d704dc-4775-4548-9899-2f056a4b6abb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code For add-8: validate and flash proper error message for required variable &quot;zipcode&quot;;<br>add-9: description is not required; add-10: add query and arguments; add-11: create user-friendly<br>error messages for validation.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.02.32image.png.webp?alt=media&token=69b3f464-5a8f-4d3e-a20c-3d762aeed37c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for edit-1: validate and flash proper error message for the required &quot;id&quot;<br>in request args; edit-2: retrieve form data for name, address, city, state, country,<br>zip, website; edit-3 to edit-7a: validate and flash proper error messages for required<br>fields, ensuring states and countries are valid as per pycountry.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.03.23image.png.webp?alt=media&token=c4327649-b12b-4da6-aaed-bdd6662a7343"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for edit-8: website is not required; edit-9: validate and flash proper error<br>message for required variable &quot;zipcode,&quot; rename variable to &quot;zip_code&quot; to avoid conflicts with<br>the built-in zip function; edit-10: fill in proper update query; edit-11: create user-friendly<br>error messages for update; edit-12: fetch the updated data; edit-13: create user-friendly error<br>messages for select.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.16.28image.png.webp?alt=media&token=476f528e-d5da-4c49-b534-3b858738c302"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for delete-1: if id is missing, flash necessary message, and redirect to<br>search; delete-2: delete organization by id (consider deleting related donations first due to<br>foreign key constraints); delete-3: ensure a flash message shows for a successful delete;<br>delete-4: pass all arguments except id to this route; delete-5: redirect to organization<br>search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.14.06image.png.webp?alt=media&token=3ecf112d-3a6f-4d99-ba95-57f6c4a2404e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Deletion of an Organization<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.21.55image.png.webp?alt=media&token=8c68c3ae-5bb1-4125-946f-6b6c9cd9cc2a"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test case passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.23.43image.png.webp?alt=media&token=9665d269-0cdc-4514-816c-a0aa64c16b29"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test case passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.23.59image.png.webp?alt=media&token=7dc0f21a-695d-47e4-b121-236c5fa373a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test case passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-11-27T20.18.49image.png.webp?alt=media&token=f08b08aa-39b4-4cd4-8ad1-a3c9077f567e"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test case passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>All the test cases are passing<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/37">https://github.com/ro-rok/rk868-is601-007/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-01T05.12.08image.png.webp?alt=media&token=4e3fab57-6a7f-4928-956f-404ce46d94bf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Currently there is a total of 19 commits <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-01T05.06.19image.png.webp?alt=media&token=0fdaa034-8885-4f9f-a849-875942ce9b44"/></td></tr>
<tr><td> <em>Caption:</em> <p>17 hours spent on this project<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk868-td-bfd8751fbd51.herokuapp.com/">https://is601-rk868-td-bfd8751fbd51.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/rk868" target="_blank">Grading</a></td></tr></table>