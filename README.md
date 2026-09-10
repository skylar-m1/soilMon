# soilMon
A soil monitoring system that tracks hiking and biking trail conditions.

Created by Skylar McDermott

## Motivation

Over the summer of 2022, I spent alot of time outdoors hiking and (most of all) mountain biking the trails of the Knoxville Urban Wilderness.

*However,*

What I soon came to learn is that when it would rain, my favorite riding location would be unusable days after all of the other locations would be ready to ride. So why not build something to keep me updated on the wetness of the trails! Enter, soilMon.

Okay so *maybe* I could just remember the last time it rained and plan a visit a few days in advance. But where's the fun in that?
## Project status

*Early development phase (active)*


## Installation

Use git clone: 
```bash
git clone "https://github.com/skylar-m1/soilMon/"
chmod +x soilMon/*
```
With virtual environment:
```bash
python3 -m venv env
source env/bin/activate
pip3 install requirements.txt
```
Without:
```bash
pip3 install -r requirements.txt
```
## Setup

A waterproof box will house the raspberry pi, connected to the soil moisture sensor. A USB 4G dongle will be connected to the pi as well. Using ngrok, I will host the front end webserver for access anywhere in the world (mars support coming soon).

One possible flaw of this, however, is speed. I do not know how latent the 4G connection will be in the woods. In my use case, the speed may not be unusably slow, due to the location being centered just outside a city, but this is a shot in the dark

## Usage

*With hardware connected, on rpi run*
```bash
cd soilMon
# if venv is activated, otherwise run source env/bin/activate
./start
```

# Specifications

The project has two main components. The "backend" and the "frontend". The backend retrieves all of the data (soil conditions, weather, etc.) and creates a save file every hour. The frontend uses this save file, and displays the data in a pretty user-friendly format (graphs, colored, easy to read).

The backend schedule will be managed via a cron job on the raspberry pi.
