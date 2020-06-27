from new_session import new_session
from models import Player
from sqlalchemy import desc

session = new_session()

def get_all_players():
    players = session.query(Player).all()
    return players

def get_top_n_fantasy_players(n=5):
    players = get_all_players()

    sorted_players = []
    for player in players:
        player = (player, player.fantasy_points())
        sorted_players.append(player)

    sorted_players = sorted(sorted_players, reverse=True, key=lambda x:x[1])

    return sorted_players[:n]

def get_top_n_rushers(n=5):
    top_rushers = []
    for row in session.query(Player).order_by(desc(Player.rushing_yds)):
        top_rushers.append(row)

    return [(p.rushing_yds, p) for p in top_rushers[:n]]

def get_top_n_receivers(n=5):
    top_receivers = []
    for row in session.query(Player).order_by(desc(Player.receiving_yds)):
        top_receivers.append(row)

    return [(p.receiving_yds, p) for p in top_receivers[:n]]

def get_top_n_passers(n=5):
    top_passers = []
    for row in session.query(Player).order_by(desc(Player.passing_yds)):
        top_passers.append(row)

    return [(p.passing_yds, p) for p in top_passers[:n]]

def get_top_n_rushing_tds(n=5):
    top_tds = []
    for row in session.query(Player).order_by(desc(Player.rushing_td)):
        top_tds.append(row)

    return [(p.rushing_td, p) for p in top_tds[:n]]

print(
    get_top_n_rushing_tds(10)
)
