# soiled
A soil monitoring framework that tracks hiking and biking trail conditions.

Created by Skylar McDermott

## Motivation

Over the summer of 2022, I spent alot of time outdoors hiking and (most of all) mountain biking the trails of the Knoxville Urban Wilderness.

*However,*

What I soon came to learn is that when it would rain, my favorite riding location would be unusable days after all of the other locations would be ready to ride. So why not build something to keep me updated on the wetness of the trails! Enter, ```soiled```.

Okay so *maybe* I could just remember the last time it rained and plan a visit a few days in advance. But where's the fun in that?
## Project status

*Early development phase (active)*


## Installation

Use git clone: 
```bash
git clone "https://github.com/skylar-m1/soiled/"
chmod +x soiled/*
```
With virtual environment:
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
Without:
```bash
pip3 install -r requirements.txt
```
## Usage

*With hardware connected, on rpi*
```bash
cd soiled
./start
```