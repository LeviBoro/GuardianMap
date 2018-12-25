# GuardianMap
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A python bot that scrapes through all *The Guardian* articles in a given time frame and then generates a *topic landscape*.

Below you can see the outcome of scanning the last 12 months:


![Map](https://i.imgur.com/G78nbZH.jpg)[https://i.imgur.com/G78nbZH.jpg]

#### What is going on in the landscape
Each article on The Guardian has a list of topics at the very bottom of the page like this:


![Topics](https://i.imgur.com/WB2Rhkt.png)

The bot collects all these tags in a database. The graph is created by setting each topic to be one node and two nodes are joint by an edge if they are covered simultaniously in an article - edge weight corresponds to how often articles are covered together.

Graph visualisation is done in Gephi 0.92. 

Node size corresponds to the amount of articles covering the topic, two nodes are closer the more often they are covered by the same articles.

