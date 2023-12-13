<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Rohan Khanna (rk868)</td></tr>
<tr><td> <em>Generated: </em> 12/12/2023 7:30:46 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/rk868" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <p>Spotify API by Glavier&nbsp;<br><a href="https://rapidapi.com/Glavier/api/spotify23">https://rapidapi.com/Glavier/api/spotify23</a><div>It is based on : <a href="https://developer.spotify.com/documentation/web-api/reference/get-track">https://developer.spotify.com/documentation/web-api/reference/get-track</a></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <p>Search<div>Tracks/GetTrack<br><div>Artist/GetArtist</div></div><div>Albums/GetAlbum</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <div><span style="color: rgba(255, 255, 255, 0.87); font-family: Lato, sans-serif; white-space: pre; background-color: rgb(29,<br>29, 32);">The following is the response of the Get Track Endpoint.<br>This is the<br>information about the single tracking spanning through the Artists to Album in which<br>I will be storing the following fields:<br>Album Name: To help group a bunch<br>of songs into one Side.</span></div><div><span style="color: rgba(255, 255, 255, 0.87); font-family: Lato, sans-serif;<br>white-space: pre; background-color: rgb(29, 29, 32);">Artist: And its subsquesnts fields to store in<br>artitst table</span></div><div><span style="color: rgba(255, 255, 255, 0.87); font-family: Lato, sans-serif; white-space: pre; background-color:<br>rgb(29, 29, 32);">Information of Songs which i am not storing as it doesnt<br>have any purpose for the end user to see it:<br></span><span style="color: rgba(255, 255,<br>255, 0.87); font-family: Lato, sans-serif; white-space: pre; background-color: rgb(29, 29, 32);">"id": "4WNcduiCmDNfmTEz7JvmLv",<br> <br>    "is_local": false,<br>      "is_playable": true,<br><br>     "track_number": 1,<br>      "type":<br>"track",</span><span style="color: rgba(255, 255, 255, 0.87); font-family: Lato, sans-serif; white-space: pre; background-color: rgb(29,<br>29, 32);">"release_date_precision": "day",<br>        "total_tracks": 1,</span></div><div><span style="color:<br>rgba(255, 255, 255, 0.87); font-family: Lato, sans-serif; white-space: pre; background-color: rgb(29, 29, 32);"><br>{<br><br> "tracks": [<br>    {<br>      "album":<br>{<br>        "album_type": "single",<br>   <br>    "artists": [<br>       <br>  {<br>          <br> "external_urls": {<br>          <br>   "spotify": "https://open.spotify.com/artist/3t8WiyalpvnB9AObcMufiE"<br>        <br>   },<br>         <br>  "id": "3t8WiyalpvnB9AObcMufiE",<br>         <br>  "name": "Mahmut Orhan",<br>        <br>   "type": "artist",<br>        <br>   "uri": "spotify:artist:3t8WiyalpvnB9AObcMufiE"<br>        <br> },<br>          {<br> <br>          "external_urls": {<br> <br>            "spotify":<br>"https://open.spotify.com/artist/40Hr91B6wn9pO83Gj0JMrP"<br>            },<br><br>           "id": "40Hr91B6wn9pO83Gj0JMrP",<br><br>           "name": "Ali<br>Arutan",<br>            "type":<br>"artist",<br>            "uri":<br>"spotify:artist:40Hr91B6wn9pO83Gj0JMrP"<br>          },<br>  <br>       {<br>     <br>      "external_urls": {<br>     <br>        "spotify": "https://open.spotify.com/artist/5xkqotsRPu6KQ4PiWjSGQf"<br>   <br>        },<br>    <br>       "id": "5xkqotsRPu6KQ4PiWjSGQf",<br>    <br>       "name": "Selin",<br>    <br>       "type": "artist",<br>    <br>       "uri": "spotify:artist:5xkqotsRPu6KQ4PiWjSGQf"<br>    <br>     }<br>       <br>],<br>        "external_urls": {<br>   <br>      "spotify": "https://open.spotify.com/album/1B68g8b4wpedNDvvQLAoCe"<br>     <br>  },<br>        "id": "1B68g8b4wpedNDvvQLAoCe",<br> <br>      "images": [<br>     <br>    {<br>        <br>   "height": 640,<br>        <br>   "url": "https://i.scdn.co/image/ab67616d0000b273fa258529452f4ed34cc961b1",<br>        <br>   "width": 640<br>        <br> },<br>          {<br> <br>          "height": 300,<br> <br>          "url": "https://i.scdn.co/image/ab67616d00001e02fa258529452f4ed34cc961b1",<br> <br>          "width": 300<br> <br>        },<br>    <br>     {<br>       <br>    "height": 64,<br>       <br>    "url": "https://i.scdn.co/image/ab67616d00004851fa258529452f4ed34cc961b1",<br>       <br>    "width": 64<br>       <br>  }<br>        ],<br>  <br>     "name": "In Control (feat. Selin)",<br>   <br>    "release_date": "2020-10-30",<br>       <br>"release_date_precision": "day",<br>        "total_tracks": 1,<br>  <br>     "type": "album",<br>      <br> "uri": "spotify:album:1B68g8b4wpedNDvvQLAoCe"<br>      },<br>    <br> "artists": [<br>        {<br>  <br>       "external_urls": {<br>    <br>       "spotify": "https://open.spotify.com/artist/3t8WiyalpvnB9AObcMufiE"<br>    <br>     },<br>       <br>  "id": "3t8WiyalpvnB9AObcMufiE",<br>         <br>"name": "Mahmut Orhan",<br>          "type":<br>"artist",<br>          "uri": "spotify:artist:3t8WiyalpvnB9AObcMufiE"<br> <br>      },<br>      <br> {<br>          "external_urls": {<br><br>           "spotify": "https://open.spotify.com/artist/40Hr91B6wn9pO83Gj0JMrP"<br><br>         },<br>   <br>      "id": "40Hr91B6wn9pO83Gj0JMrP",<br>     <br>    "name": "Ali Arutan",<br>      <br>   "type": "artist",<br>        <br> "uri": "spotify:artist:40Hr91B6wn9pO83Gj0JMrP"<br>        },<br>  <br>     {<br>       <br>  "external_urls": {<br>         <br>  "spotify": "https://open.spotify.com/artist/5xkqotsRPu6KQ4PiWjSGQf"<br>         <br>},<br>          "id": "5xkqotsRPu6KQ4PiWjSGQf",<br> <br>        "name": "Selin",<br>   <br>      "type": "artist",<br>     <br>    "uri": "spotify:artist:5xkqotsRPu6KQ4PiWjSGQf"<br>       <br>}<br>      ],<br>      "disc_number":<br>1,<br>      "duration_ms": 179232,<br>     <br>"explicit": false,<br>      "external_ids": {<br>    <br>   "isrc": "USUS12000579"<br>      },<br>  <br>   "external_urls": {<br>        "spotify":<br>"https://open.spotify.com/track/4WNcduiCmDNfmTEz7JvmLv"<br>      },<br>      "id":<br>"4WNcduiCmDNfmTEz7JvmLv",<br>      "is_local": false,<br>     <br>"is_playable": true,<br>      "name": "In Control (feat. Selin)",<br> <br>    "popularity": 57,<br>      "preview_url": "https://p.scdn.co/mp3-preview/315b151078df729934712ed1cc21e11506c64017?cid=f6a40776580943a7bc5173125a1e8832",<br><br>     "track_number": 1,<br>      "type":<br>"track",<br>      "uri": "spotify:track:4WNcduiCmDNfmTEz7JvmLv"<br>    }<br> <br>]<br>}</span><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <p>I will create a Page for the song that will showcase the song<br>information that I will get from the Songs table that will get populated<br>by the GetTracks Endpoint.<br>The song will have a foreign ID on the album.<br>Then the album and artist will have many to many tables. Albums and<br>artists will have the same features.<br>Here, Genre to Artist will have many-to-many. and<br>Finally Featuring artist to song will have many-to-many relationship<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.04.03image.png.webp?alt=media&token=a214f2f2-a9cd-428d-83c0-914619e62ef7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create Track Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.05.10image.png.webp?alt=media&token=a2c0b7f0-2be2-460e-8b3b-21daf17f5b4f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation for Track ID which is a spotify ID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.06.02image.png.webp?alt=media&token=42063b9a-6683-464a-a89a-3674d4f8fbe8"/></td></tr>
<tr><td> <em>Caption:</em> <p>On Duplicate, it will update the old keys<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.08.09image.png.webp?alt=media&token=480e0225-7cc0-4116-9b3c-c8abd59b392b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success of Test Song<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.11.04image.png.webp?alt=media&token=1e5bba25-28dd-4e38-829b-0d09c2667750"/></td></tr>
<tr><td> <em>Caption:</em> <p>ID = 281 is the test song <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/40">https://github.com/ro-rok/rk868-is601-007/pull/40</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.23.03image.png.webp?alt=media&token=99d2a608-12e5-45e4-b6d4-6b71add15bad"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows No Results when track popularity is 101<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.31.08image.png.webp?alt=media&token=139b7ec5-8a7a-4adc-8c03-8386044aca6f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search of Track Name= &#39;te&#39; , and sorted with desc Orders of Duration<br>There<br>is a mix of API and created tracks<br>It has View, Add, List<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.32.15image.png.webp?alt=media&token=9589a3bc-febf-4d37-ad87-deac9a245514"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limit if it is more than 100, it will be turned to 100<br>and if less than 1, it will be 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/40">https://github.com/ro-rok/rk868-is601-007/pull/40</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.43.52image.png.webp?alt=media&token=f17940bd-e8d6-442e-9c83-e53e134792fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Page for A track<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.45.12image.png.webp?alt=media&token=c3b58854-a5b5-43ec-8dbe-7772310bec79"/></td></tr>
<tr><td> <em>Caption:</em> <p>It will redirect to List if the id is not in the SQLDB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/40">https://github.com/ro-rok/rk868-is601-007/pull/40</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-12T23.57.35image.png.webp?alt=media&token=69b25e2c-5e01-4980-87cb-3f71644b871d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Track Name is required, it was prefill with data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.00.38image.png.webp?alt=media&token=924d1820-4502-4db8-a6ae-8bbd636630f9"/></td></tr>
<tr><td> <em>Caption:</em> <p>It is the backend of the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.03.00image.png.webp?alt=media&token=73644a43-9741-4dcd-b42a-3fd3fe02980b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Track Popularity updated of track &quot;Take Care&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.03.52Screenshot%202023-12-12%20185534.png.webp?alt=media&token=f8b04fd3-de6e-4cc6-814d-4ad59def2633"/></td></tr>
<tr><td> <em>Caption:</em> <p>Wrong ID<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.02.46image.png.webp?alt=media&token=4ee9ebe3-8d0a-4421-96f2-119436d8790d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before here the track Take care has popularity of 22<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.04.38image.png.webp?alt=media&token=2adfb1fe-da19-44f3-a169-5728a72c947a"/></td></tr>
<tr><td> <em>Caption:</em> <p>It is changed to 88 now<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/40">https://github.com/ro-rok/rk868-is601-007/pull/40</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.13.24image.png.webp?alt=media&token=4581f43d-7ded-4773-802e-3f7db64efa82"/></td></tr>
<tr><td> <em>Caption:</em> <p>It is successful deleted ad redirected to list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.16.24image.png.webp?alt=media&token=66fd99e7-dab6-4067-b242-7bb18b186699"/></td></tr>
<tr><td> <em>Caption:</em> <p>Backend of the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.17.29image.png.webp?alt=media&token=b2d9ca3e-4df7-4dbf-a2d0-c6ea487398d9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash  message when invalid/missing id<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.13.53image.png.webp?alt=media&token=3f738051-3603-4330-a658-a6abab96fd73"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Track with id = 1 is present<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.14.03image.png.webp?alt=media&token=00da6142-a10e-4186-8ca1-8243c38f6fea"/></td></tr>
<tr><td> <em>Caption:</em> <p>Song with ID = 1 is deleted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/40">https://github.com/ro-rok/rk868-is601-007/pull/40</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.22.32image.png.webp?alt=media&token=bffccda6-64cb-464a-b47c-c5f183979ede"/></td></tr>
<tr><td> <em>Caption:</em> <p>Front end for fetch for an admin and user can use the search<br>bar for fetching<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.23.30image.png.webp?alt=media&token=442535e6-da7e-4270-ad98-1e04dbc09076"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is Sportify API fetch call<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.23.52image.png.webp?alt=media&token=e7b7c530-ffa1-4cb8-bd68-05e7b25c4a84"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the transformation of data for SQL<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.24.16image.png.webp?alt=media&token=04777cae-3480-45fb-9d6d-1975cb1d17df"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is taking transformed data to and adding it to DB. Here the<br>if track is loaded or artist is loaded or album is loaded, then<br>it will update the existing data on duplicate otherwise it will ignore as<br>api gives half the data will other fetch calls<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <p>Admin can trigger Fetch directly from the Fetch endpoint created for artist, album<br>and tracks using their respective spoitfy ids<div>The user can fetch if the user<br>searches for the track,&nbsp; artist, album etc, and tries to view it, the<br>app will first check if the data is there, if not it will<br>first fetch the data and load it to the database and then showcase<br>it to the user.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ro-rok/rk868-is601-007/pull/40">https://github.com/ro-rok/rk868-is601-007/pull/40</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>The learning i got is how to be patient with the project<br>On Web<br>development related: I learnt make many-to-many table and schema and how much trial<br>and error goes into it. And I how to use Bootstrap and Jinja2<br>even further&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk868-prod-45f317a15212.herokuapp.com/login">https://is601-rk868-prod-45f317a15212.herokuapp.com/login</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frk868%2F2023-12-13T00.29.04image.png.webp?alt=media&token=1a9fad02-95f0-420c-a6da-377bd29d4552"/></td></tr>
<tr><td> <em>Caption:</em> <p>33 hrs 13 mins Total time<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/rk868" target="_blank">Grading</a></td></tr></table>