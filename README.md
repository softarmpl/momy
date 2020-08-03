## How to start this project

You need to have running Splash server in Docker: 

docker run -it -p 8050:8050 --rm scrapinghub/splash


Set SPLASH_URL in Scrapy project settings - `settings.py` to your Dockerized splash server.