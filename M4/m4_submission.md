<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Rohan Khanna (rk868)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 8:03:08 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/rk868" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.16.00image.png.webp?alt=media&token=ef0fac65-04c2-4c72-a3a6-86e0cb1d2c6d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logic of Addition when + operator is used in the equation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.16.17image.png.webp?alt=media&token=2f6a372e-9ec4-4ccb-a639-98b11d2b01ed"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logic of Subtraction when - operator is used in the equation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.16.33image.png.webp?alt=media&token=d41ed726-c082-42b6-aeb2-e67bd9805073"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logic of Mutiplication when * operator is used in the equation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T23.33.11image.png.webp?alt=media&token=3cc3ef06-44ae-4052-bb0e-213b3c964fe3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logic of Division  when / operator is used in the equation and<br>raises a Zero Division Error when it fails the division <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.23.40image.png.webp?alt=media&token=b99a270d-af01-4e93-a621-94e952aebe83"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>num-add-num 4 times. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.24.03image.png.webp?alt=media&token=294ebe24-ec77-4315-b8d2-02f32089f9b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.25.05image.png.webp?alt=media&token=819f6f39-5c65-486f-85bf-a76ea15bcad5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>ans-add-num 4 times. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.25.17image.png.webp?alt=media&token=b3c1e338-03a4-4eba-93e9-c313bbe631b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.25.35image.png.webp?alt=media&token=01b98609-4c6a-4646-ad2b-57a6837f8e55"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>num-sub-num 4 times. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.25.47image.png.webp?alt=media&token=5d34416b-cfea-4f71-8326-e6756af90126"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.47.34image.png.webp?alt=media&token=54b7009c-cdc1-4b0b-b484-a1e2c6d0cba2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>ans-sub-num 4 times. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.47.52image.png.webp?alt=media&token=30d81ac6-9c79-441a-8711-9c40f81750b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.51.02image.png.webp?alt=media&token=a4ce9a5b-573b-4ce3-91c8-4b7eb05b8cb6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>num-mul-num 4 times. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.51.15image.png.webp?alt=media&token=0426b756-81ab-4fd3-b572-b302502c5ddb"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.52.18image.png.webp?alt=media&token=e184d68f-71ea-42fb-b6eb-ed6f79f092a8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>ans-mul-num 4 times. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T22.51.39image.png.webp?alt=media&token=8e7363fa-c5ed-4999-beed-f26af299fc4a"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T23.33.50image.png.webp?alt=media&token=296d4959-6505-4126-8161-6afa184f7f6e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>num-div-num 3 times.  An additional test for 0 Division<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T23.34.04image.png.webp?alt=media&token=39b8f96e-3203-40d6-87bf-1e58baf9755e"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T23.34.21image.png.webp?alt=media&token=5eb1d175-3c53-4e9b-82c3-64bcb833964a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Used pytest.fixture to create my_calc class&#39;s instance and used parametrized decorator to test<br>ans-div-num 3 times.  An additional test for 0 Division<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-10-16T23.34.36image.png.webp?alt=media&token=803ee538-ef57-4381-ac30-25e7d79de5fd"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows all the test passed<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I got to know how to create a class&#39;s instance using fixture decorator<br>in pytest.<br>Also I got to know how to create multiple inputs for a<br>single test case function using the parametrized decorator in pytest.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <div>I defined a pytest fixture named my_calc_instance. In this case, the fixture returns<br>an instance of the MyCalc class<br><div style="color: rgb(204, 204, 204); background-color: rgb(31, 31,<br>31); font-family: Consolas, &quot;Courier New&quot;, monospace; line-height: 19px; white-space: pre;"><div><span style="color: #dcdcaa;">@</span><span style="color:<br>#4ec9b0;">pytest</span><span style="color: #dcdcaa;">.</span><span style="color: #dcdcaa;">fixture</span></div><div><span style="color: #569cd6;">def</span> <span style="color: #dcdcaa;">my_calc_instance</span>():</div><div>&nbsp; &nbsp; <span style="color:<br>#c586c0;">return</span> <span style="color: #4ec9b0;">MyCalc</span>()</div></div></div><div><br></div><div>I used the @pytest.mark.parametrize decorator to create a parameterized test<br>case. This allows the same test case to be executed with different sets<br>of inputs and expected outputs. The parameterized test case is for testing all<br>the operation.</div><div>Inside the test case function, I called the calc method of the<br>my_calc_instance object, passing number(a or ans and b accordingly) and assert the calculation<br>with the expected.<br>Eg:<br><div style="color: rgb(204, 204, 204); background-color: rgb(31, 31, 31); font-family: Consolas,<br>&quot;Courier New&quot;, monospace; line-height: 19px; white-space: pre;"><div><span style="color: #dcdcaa;">@</span><span style="color: #4ec9b0;">pytest</span><span style="color: #dcdcaa;">.</span><span<br>style="color: #9cdcfe;">mark</span><span style="color: #dcdcaa;">.</span><span style="color: #9cdcfe;">parametrize</span>(<span style="color: #ce9178;">"a, b, expected"</span>, [(<span style="color: #b5cea8;">11</span>,<br><span style="color: #b5cea8;">22</span>, <span style="color: #b5cea8;">33</span>), (<span style="color: #b5cea8;">0</span>, <span style="color: #b5cea8;">0</span>, <span<br>style="color: #b5cea8;">0</span>), (<span style="color: #d4d4d4;">-</span><span style="color: #b5cea8;">100</span>, <span style="color: #b5cea8;">100</span>, <span style="color: #b5cea8;">0</span>),<br>(<span style="color: #d4d4d4;">-</span><span style="color: #b5cea8;">55.5</span>, <span style="color: #b5cea8;">55.5</span>, <span style="color: #b5cea8;">0</span>)])</div><div><span style="color: #569cd6;">def</span><br><span style="color: #dcdcaa;">test_add</span>(<span style="color: #9cdcfe;">my_calc_instance</span>, <span style="color: #9cdcfe;">a</span>, <span style="color: #9cdcfe;">b</span>, <span style="color:<br>#9cdcfe;">expected</span>):</div><div>&nbsp; &nbsp; <span style="color: #9cdcfe;">result</span> <span style="color: #d4d4d4;">=</span> <span style="color: #9cdcfe;">my_calc_instance</span>.calc(<span style="color: #9cdcfe;">a</span>,<br><span style="color: #9cdcfe;">b</span>, <span style="color: #ce9178;">"+"</span>)</div><div>&nbsp; &nbsp; <span style="color: #c586c0;">assert</span> <span style="color: #9cdcfe;">result</span><br><span style="color: #d4d4d4;">==</span> <span style="color: #9cdcfe;">expected</span></div></div></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/14">https://github.com/ro-rok/rk868-is601-007/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/rk868" target="_blank">Grading</a></td></tr></table>