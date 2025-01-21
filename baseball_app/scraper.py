import requests
from bs4 import BeautifulSoup
from baseball_app.models import Player, BattingStats, PitchingStats

url = 'https://example.com/player-stats'  # スクレイピングするウェブサイトのURL

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# スクレイピング部分を関数化
def scrape_players():
    players_data = []
    for player in soup.find_all('div', class_='player-card'):  # HTML構造に応じて変更が必要
        player_name = player.find('h2').text
        team_name = player.find('span', class_='team').text
        position = player.find('span', class_='position').text
        jersey_number = player.find('span', class_='jersey').text
        birthplace = player.find('span', class_='birthplace').text
        birthday = player.find('span', class_='birthday').text
        height = player.find('span', class_='height').text
        weight = player.find('span', class_='weight').text

        players_data.append({
            'player_name': player_name,
            'team_name': team_name,
            'position': position,
            'jersey_number': jersey_number,
            'birthplace': birthplace,
            'birthday': birthday,
            'height': height,
            'weight': weight
        })
    
    return players_data

def save_data(data):
    for item in data:
        Player.objects.create(
            player_name=item['player_name'],
            team_name=item['team_name'],
            position=item['position'],
            jersey_number=item['jersey_number'],
            birthplace=item['birthplace'],
            birthday=item['birthday'],
            height=item['height'],
            weight=item['weight']
        )

if __name__ == '__main__':
    scraped_data = scrape_players()  # スクレイピングを実行
    save_data(scraped_data)  # データベースに保存
