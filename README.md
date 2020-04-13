<h1>Wholefoods Slot finder service</h1>	

Tired of logging into wholefoods every 30 minutes only to find that all delivery slots have been taken? Let your computer do the work for you and email you when there's a slot.

<h2>How to use it</h2>  

1. Clone this repository
2. Make sure you have docker installed (https://docs.docker.com/get-docker/)  
3. Enter all the information needed in utils/secrets.py (you will need to create a mailgun API key)  
4. Build the docker image `docker build -t wholefoods .`
5. Run the image `docker run wholefoods`

<h2>Additional notes</h2>  

1. The docker image should take care of getting compatible versions of chrome (81.x) and chromedriver.
2. It also takes care of using the right Python interpreter (3.7) and installing the right dependencies
3. Running the script every so often might be a hassle so you could run it as a cron job (https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/).
4. Since this script relies on Selenium accessing Amazon's website, it is prone to breaking if the amazon.com DOM changes.  
5. I will do my best to keep this updated but no promises. If you run into problems, please drop an issue on this and I'd be glad to help out. Thanks!
