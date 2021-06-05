from .database import PLAYERS


class CardFactory:

    def create_card(self, text):
        items = text[0].description.split('\n')
        number = self.get_number(items)
        year = self.get_year(items)
        name, team = self.get_player(number, year)
        return number, year, name, team

    def get_number(self, items):
        for item in items:
            if "no." in item.lower():
                return item.strip().lower().removeprefix('no.').strip()

    def get_player(self, number, year):
        for player in PLAYERS:
            if player["number"] == number:
                return player["name"], player["team"]

    def get_year(self, items):
        for item in items:
            if "PANINI" in item:
                panini_section = item.split(' ')
                for item in panini_section:
                    if item.isnumeric():
                        return item
