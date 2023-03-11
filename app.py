import requests, json
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

roleid = ROLEID # This is the role of the id you want the user to receive after verified
guildid = GULDID # This is the server where the verification will be needed.
token = "YOUR DISCORD BOT TOKEN"

@app.route("/verify/<userid>")
def verify(userid):
    r = json.loads(requests.get(f"https://discord.com/api/v10/guilds/{guildid}/members/{userid}", headers = {"Authorization":f"Bot {token}"}).text)

    try:
        user = r["user"]["username"]
        discrim = r["user"]["discriminator"]
        return render_template("verify.html", user = user, discrim = discrim, guildid = guildid, userid = userid)
    except:
        return render_template("not_in_guild.html")

@app.route("/verifying/<userid>/<user>/<discrim>")
def verifying(userid,user, discrim):
    r = requests.put(f"https://discord.com/api/v10/guilds/{guildid}/members/{userid}/roles/{roleid}", headers = {"Authorization":f"Bot {token}"}).text
    if r == "":
        return render_template("success.html", user = user, discrim = discrim)
    else:
        return render_template("unsuccessful.html", user = user, discrim = discrim)
@app.route("/")
def home():
    return "<h1>Please use the link provided by the bot in the server, thanks!</h1>"

