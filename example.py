import stm

stmw = stm.stm('key')
player = stmw.player(steamid=76561198348243540)
print('Player Avatar')
print(player.avatar)

friendslist = stmw.friendslist(steamid=76561198348243540)
print('\nFriend Steamid')
print(friendslist.list[10].steamid)

stats = stmw.stats(steamid=76561198348243540, appid=730)
print(f'\nStats for {stats.game} [ID: {stats.appid}]')
print(f'Total Kills: {stats.stats["total_kills"]}')
print(f'Total Deaths: {stats.stats["total_deaths"]}')

gameslist = stmw.gameslist(steamid=76561198348243540)
if 730 in gameslist.list:
    print('730 Appid exists in list')

rplayed = stmw.recentlyplayed(steamid=76561198348243540)
print('\nRecently Played')
print(f'Appid: {rplayed.appid}\nIcon URL: {rplayed.icon_url}')

banstatus = stmw.checkban(steamid=76561198348243540)
print('\nBan Status')
print(f'Community Ban: {banstatus.communityban}\nVac Ban: {banstatus.vacban}')
