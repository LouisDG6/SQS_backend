"""SqsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Sqs import Sqs

class SqsTableSeeder(Seeder):
    def run(self):
        Sqs.create({"borough": "Manhattan", "name": "Boxers", "section": "Chelsea", "description": "bar", "address": "37 West 20th Street, New York, NY 10011", "image": "https://lh3.googleusercontent.com/proxy/HKvqvrvQr8JMGQuY4ilHJQhfNZHXP70hbR46l4bfYL7IUpFH_LYt-Klq3KKFxDkDGmAtYWm4srLDroJyq5jZZKOkuD3E"})
        Sqs.create({"borough": "Bronx", "name": "Identity", "section": "Mount Vernon", "description": "bar", "address": "119 East 233rd Street, Bronx, NY 10470", "image": "https://scontent-lga3-2.xx.fbcdn.net/v/t1.6435-9/199926641_103156185343013_5715550545018902176_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=973b4a&_nc_ohc=h_Yc405UhogAX9_7kC-&_nc_ht=scontent-lga3-2.xx&oh=ea6a5deb1c076455e92ff9eebdf50553&oe=61D4AEE6"})
        Sqs.create({"borough": "Queens", "name": "Friend's Tavern", "section": "Jackson Heights", "description": "bar", "address": "78-11 Roosevelt Ave, Jackson Heights, NY 11372", "image": "https://media.timeout.com/images/100715931/1372/772/image.jpg"})
        Sqs.create({"borough": "Brooklyn", "name": "Metropolitan", "section": "East Williamsburg", "description": "bar", "address": "559 Lorimer Street, Brooklyn, NY 11211", "image": "https://www.nycgo.com/images/venues/3103/metropolitan_bar_williamsburg_brooklyn_shelli_weiler_mg_3757_copy.jpg"})
        Sqs.create({"borough": "Staten Island", "name": "Liedy's Shore Inn", "section": "Shore Side", "description": "bar", "address": "748 Richmond Terrace, Staten Island, NY 10301", "image": "https://pbs.twimg.com/media/CDSYcy1WMAACB3H.png"})
