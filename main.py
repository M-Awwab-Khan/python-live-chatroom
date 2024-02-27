from flask import Flask
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase