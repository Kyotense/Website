#Description

#Authors
Alan Singleton and Chase Carthen

#Dependencies

* Django 
* MySQL
* Venv
* pip

#Setup and Getting Started

There are a few steps we need to take to get this website up and running.

The first thing that needs to happen is the installition of the dependencies of the project. This project makes use of Virtual Env.
``` bash
  virtualenv VirtualEnvironment
  source VirtualEnvironemnt/bin/activate
  
  # now to install the python dependencies
  pip install -r requirements.txt
```

Everytime you want to use the server you must activate the environment.

Now lets get the database setup for the website and generate some fake data. Here is how data is generated:
```bash
  # this is loading the fixture.json from /djangosite/shop/fixtures/fixture.sjon
  python3 manage.py loaddata fixture.json
```

In fixtures.json you will notice some json that prepopulates the models of this website:
```json
[
{
 "model": "shop.company",
 "pk": 1,
 "fields": {
  "company_name": "chase",
  "image": "./clouds_back.jpg"
 }
},
{
 "model": "shop.product",
 "pk": 1,
 "fields": {
  "company": 1,
  "description": "Apple man",
  "pub_date": "2016-07-19T07:06:02Z",
  "name": "Appleness",
  "price": 11.1
 }
},
{
 "model": "shop.product",
 "pk": 2,
 "fields": {
  "company": 1,
  "description": "The apple of my eye.",
  "pub_date": "2016-07-20T17:49:25Z",
  "name": "The Kraken",
  "price": 100.0
 }
},
{
 "model": "shop.productimage",
 "pk": 3,
 "fields": {
  "product": 1,
  "image": "shop/clouds_right.jpg"
 }
},
{
 "model": "shop.productimage",
 "pk": 4,
 "fields": {
  "product": 2,
  "image": "shop/posz.jpg"
 }
}
]
```

This json has been included as a way to populate data for this website. The image fields in the json are stored in the media directory and new entries should be done this way as well.

However, it is not the only way to add data to the website, but the admin page of this website can be used to add data as well.

