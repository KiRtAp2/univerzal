import discord


import settings as stg


client = discord.Client()
with open("SECRET") as f:
    SECRET = f.readline().strip()


if __name__ == "__main__":
    pass
