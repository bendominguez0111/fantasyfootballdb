from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Player(Base):
    __tablename__ = 'player_'
    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    position = Column(String)
    team = Column(String)
    games_played = Column(Integer)
    int = Column(Integer)
    fumbles_lost = Column(Integer)
    passing_att = Column(Integer)
    passing_cmp = Column(Integer)
    passing_td = Column(Integer)
    passing_yds = Column(Integer)
    receptions = Column(Integer)
    receiving_yds = Column(Integer)
    receiving_td = Column(Integer)
    rushing_att = Column(Integer)
    rushing_td = Column(Integer)
    rushing_yds = Column(Integer)
    targets = Column(Integer)

    def fantasy_points(self, ppr=True):
        fant_points = (
        self.passing_yds/25 + self.passing_td*4 + self.receiving_yds/10 + self.receiving_td*6 \
        + self.rushing_td*6 + self.rushing_yds/10 - self.fumbles_lost*2 - self.int*2
        )

        if ppr:
            fant_points += self.receptions

        return fant_points

    def __repr__(self):
        return f'<Player {self.player_name}>'
