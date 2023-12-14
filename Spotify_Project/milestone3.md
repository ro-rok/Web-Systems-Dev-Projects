<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 API Project</td></tr>
<tr><td> <em>Student: </em> Rohan Khanna (rk868)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 6:56:57 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/rk868" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Data Association </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> How will this data relate to the User</td></tr>
<tr><td> <em>Response:</em> <p>The website allows users to create and manage a playlist of their favorite<br>songs, complete with album and artist information with a stylistic frontend to help<br>navigate users.<br><br><div>The user wants to discover new tracks, curate a personal collection as<br>their playlist, and revisit favorite mixes over time. Interacting with playlists enriches the<br>user&#39;s musical experience.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Data changes</td></tr>
<tr><td> <em>Response:</em> <div>If the user clicks on view, the backend will check whether the data's<br>information is complete. If it is not, the backend will fetch that particular<br>information from the API and add it to the table. Finally, it will<br>display the complete "more info" page with all the data from the SQL<br>database.<br><br></div><div>If the above edit occurs, the changes will not matter as all the<br>data association data is stored in a table with trac_id and user_id.<br>Although the<br>Admin can perform association changes to tracks and users through the help of<br>the "manage" endpoint.</div><div><br></div><div>&nbsp;The relationship is many-to-many for users to tracks, as many users<br>can choose many songs to add to their playlist.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how/where the user can associate the data with themselves</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.26.29image.png.webp?alt=media&token=28c5a4af-2170-408a-9052-60efa9acbdac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Track is the button to add it to the playlist, where the data<br>associate with user happens.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.29.58image.png.webp?alt=media&token=5fcc9a24-a2d8-459c-be24-f52f038669cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Backend code: Record: method to add the data in playlist, and Playlist: method<br>to show the playlist of a user<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> List Associated Entities to the logged in user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the page where a user can list related/associated entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.31.43image.png.webp?alt=media&token=52e11299-f412-4b0d-99d8-03232fbb1093"/></td></tr>
<tr><td> <em>Caption:</em> <p>Untrack is to remove the from the list, Total number of tracks in<br>the list is shown. User can filter using &quot;Track Name, Track Popularity, Is<br>Explicit, Album Name, Duration MS, Release Date&quot;. User can remove  all the<br>tracks from the playlist with Clear Playlist button.<br><br>Here the Limit check is done<br>at the backend, if limit is below 1 it will be or if<br>it is above 100 it will be 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.35.50image.png.webp?alt=media&token=1f802d64-0be1-46f7-8d37-5f9e69558613"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here all the tracks where album name has &#39;T&#39; in it and Is<br>Explicit with Duration MS in descending order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.37.24image.png.webp?alt=media&token=ad0e8b05-0b30-42bf-ae7e-0ccc26fe6e62"/></td></tr>
<tr><td> <em>Caption:</em> <p>All the tracks with 87 Popularity and track number in Asc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.38.23image.png.webp?alt=media&token=e1529299-ed72-43d9-b393-ec40570a5d66"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for clearing all the data in the playlist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/46">https://github.com/ro-rok/rk868-is601-007/pull/46</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List entities associated with users </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a page that lists entities that are associated with at least 1 user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.50.41image.png.webp?alt=media&token=46cfd201-5777-408d-ae09-482482a467f4"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a page for all the track entities which is not in<br> any user&#39;s playlist,<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.52.11image.png.webp?alt=media&token=cbf12b89-f0a4-403e-81e9-898e53474f2a"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the track association page where there is all the track which<br>are associated to users where, clicking on the username will redirect it to<br>their profile<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.52.58image.png.webp?alt=media&token=046ab5fc-e763-471d-ac8f-6d4c08b731c0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here the filter is where username = user and is explicit is true,<br>and sorted by release date in asc order<br><br>Here the Limit check is done<br>at the backend, if limit is below 1 it will be or if<br>it is above 100 it will be 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T22.56.51image.png.webp?alt=media&token=554df1a0-be6b-4dd4-ac9c-51c2f81e2348"/></td></tr>
<tr><td> <em>Caption:</em> <p>All the entities connected where track name has &quot;ca&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/46">https://github.com/ro-rok/rk868-is601-007/pull/46</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin Association Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Admin page to search for users and entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.24.50image.png.webp?alt=media&token=e2ae4698-6c5c-4a83-a4d8-0664901a5d2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>For username = user and track name = take<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.25.22image.png.webp?alt=media&token=8afe0096-b056-4d1c-81b2-7655a66a44a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash messages shows that the both the songs is added<br>It is just filled<br>with random tracks so the page will not look empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.25.46image.png.webp?alt=media&token=224fca48-4a67-4899-9e11-e634089f9d26"/></td></tr>
<tr><td> <em>Caption:</em> <p>Now to remove the same tracks added from the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.27.29image.png.webp?alt=media&token=1e504b8b-11fb-4ef0-a131-e2f1a2f0d1a6"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows 2 have been removed from the association of the user table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/46">https://github.com/ro-rok/rk868-is601-007/pull/46</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Project Related Screens not yet shown </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of other pages not yet shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.20.17image.png.webp?alt=media&token=2edfd945-a985-4b42-beb3-af03be8ef169"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Page, for searching arstist/songs/albums<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.13.51image.png.webp?alt=media&token=7153f1d6-fc30-41ad-aa99-f6f1f1f84b3a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Song Page for viewing more details,(not admin)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.14.02image.png.webp?alt=media&token=a91d2fbd-27f4-42ad-ab1a-41fa089d2e14"/></td></tr>
<tr><td> <em>Caption:</em> <p>Artist Page  for viewing more details (admin)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.23.37image.png.webp?alt=media&token=dbe7b2e8-60d8-4929-93e3-06b993ea9ae1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Album Page  for viewing more details  (no user logged in)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.14.49image.png.webp?alt=media&token=0c62f4b8-4d79-4e85-9a9e-7f711ee99ae2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index page, the first page to open up  (admin)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-14T23.15.27image.png.webp?alt=media&token=54854368-05e9-4714-8130-e7844fa5abe4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Landing_page after logged in, user is shown the tracks in their playlist <br>(admin)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain each screen shown above</td></tr>
<tr><td> <em>Response:</em> <div>1. Search Page: This page allows users to search for artists, songs, and<br>albums. The search query is passed through the API and the top result<br>is displayed in cards.<br></div><div><br></div><div>2. Song Page: This page displays all the available details<br>of a song or track from the SQL. Users can add the song<br>to their playlist, redirect to the respective artist/albums, and listen to a 30-second<br>preview using the Spotify embed. Users can also be redirected to Spotify on<br>browsers and desktops if they choose to.</div><div><br></div><div>3. Artist Page: This page displays all<br>the details of an artist. There is a Bootstrap accordion that allows users<br>to click on genres and albums by the artist. Users can also be<br>redirected to Spotify on browsers and desktops if they choose to. Since this<br>is an admin page, the admin can delete or edit the record.</div><div><br></div><div>4. Album<br>Page: This page displays all the details of an album. Clicking on the<br>total tracks will redirect users to the track list page for the tracks<br>of the song. Users can also be redirected to Spotify on browsers and<br>desktops if they choose to. The nav bar is different here since users<br>are not logged in.</div><div><br></div><div>5. Index Page: This is the first page to open<br>up. It features 3 Bootstrap carousels for artists, albums, and tracks, which are<br>shown randomly every time. Users can click on the black translucent to open<br>the view page for the specific card.</div><div><br></div><div>6. Landing Page: After logging in, users<br>are shown the tracks in their playlist. This page shows the tracks in<br>the user's playlist.<br><br>All of the website has animation when you first open the<br>page</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/46">https://github.com/ro-rok/rk868-is601-007/pull/46</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I utilized Bootstrap to develop the front end and tried to use it<br>as much as possible. It took me several hours to decide the appropriate<br>layout for the view pages. However, I faced some issues when trying to<br>create Jinja templates from the examples created by Bootstrap. I also added some<br>icons from the favicon.&nbsp;<div><br></div><div>During the process, I learned how to edit macros in<br>Jinja and utilize animated.css. I was able to create Bootstrap Accordion and Carousel.<br>With regards to SQL Queries with JOIN, it took some trial and error<br>to ensure that I get the necessary rows without creating a cross-product of<br>the entities.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/rk868" target="_blank">Grading</a></td></tr></table>