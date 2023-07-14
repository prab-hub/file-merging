# file-merging

Couple of years ago, I came across the problem where I had many posts from WSPB website in HTML format. Since they were in HTML, all the posts had meta data in header and social media links in footer, making it harder to read actual content from posts. 

Since there were 400+ posts, manually cleaning all the files and converting them to PDF was time consuming process. 

So I created a pythong script that would iterate all the files saved in computer disk, remove header & footer, and copy post body to one master file. 

For this RegEx was used to only copy the relevant text. 

Master HTML file was then converted to PDF manaually using online tool. 

Here's the link to file: https://drive.google.com/file/d/1uNqCGRAV0gOMRazRcyk1ACjlTfVwTp_H/view?usp=sharing
