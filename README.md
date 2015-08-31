##Welcome to Questa Ebook Downloader!

I created this program because I was fed up with ITT's online ebook reader.
I couldn't get the merge pdf section to work out; for some reason it would join them out
of order. It should be noted that it is only tested and supported for Linux based OS.


#####To get started

From your console
    1. sudo chmod +x setup
    2. sudo ./setup
    3. python QEDownloader.py    

Configuring Cups-pdf to be your only printer is required for it to work
  1. sudo gpasswd -a username lpadmin
  2. visit http://localhost:631/
  3. go to Adding Printers and Classes
  4. Login with your username and password
  5. Add Printer
  6. CUPS-PDF (Virtual PDF Printer)
  7. Click Continue


#####What to expect on first run

- It will ask you for your ITT username and password. 
- It will automatically delete the username and password once used to login. 
- It will use the class row you entered to find your class. You find this out on the 
Distance-learning website. 
- It will configure a separate firefox profile to silently print to pdf.
- It will then open Firefox in an invisible browser.
- I will then get the page numbers from Amazon, and then finally start
- to print the pages off 10 at a time. 
- Feel free to do stuff while it does its thing. 