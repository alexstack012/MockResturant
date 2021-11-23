from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask import jsonify
from flask_app import app


# ======================================================= #
# ==== BASE =========#
# ======================================================= #

@app.route("/")
def enter():
    return render_template('index.html')


# ======================================================= #
# ==== directions =========#
# ======================================================= #

@app.route("/directions")
def directions():
    return render_template('directions.html')


# ======================================================= #
# ==== menu =========#
# ======================================================= #


@app.route("/menu")
def menu():
    return render_template('menu.html')
