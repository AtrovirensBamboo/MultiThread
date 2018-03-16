# MultiThread
In this case,I get webpage information with multiple thread method.

The target website are kugou hot songs TOP500.Even though target web site cannot turn pages by clicking a button,I analyse the url's
details,and find we can have access to all the songs on TOP500.

And webcrawler need lots of time to wait for I/O to database,I create four threads to get information from these wensites.
But the webcrawler has an obvious shortcoming,it's seems like that I donot take measures to stop from ip forbidden,because 
the four thread use IP address of my computer.......
