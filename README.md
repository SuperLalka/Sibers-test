# Sibers-test

Installing dependencies, building and running
============

For the project to work, you need to install docker & docker-compose

https://docs.docker.com/engine/install/ubuntu/

https://docs.docker.com/compose/install/

Variables for work are already filled in and are in files .environment & .environment.db 

Next, you need to build and run:

    docker-compose -f docker-compose.yml build
    docker-compose -f docker-compose.yml up -d

Filling the database with objects
============

Added to the project fixtures with sample news, which are added to the database with the command:

    docker-compose exec web python manage.py loaddata fixtures/data.json

Alternatively, you can run the news generation script:

    docker-compose exec web python manage.py fill_db

--------------------------------------
link to the project's github https://github.com/SuperLalka/Sibers-test