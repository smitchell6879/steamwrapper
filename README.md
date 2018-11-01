# stmpy
API wrapper for Steam written in Python.

# example.py
```
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
```

# Player
```
import stm

stmw = stm.stm('key')
player = stmw.player(steamid=76561198348243540) # Get player by steamid
# all
player.steamid
player.communityvisibilitystate
player.profilestate
player.personaname
player.lastlogoff
player.commentpermission
player.avatar
player.avatarmedium
player.avatarfull
player.personastate
player.realname
player.primaryclanid
player.timecreated
player.personastateflags
player.loccountrycode
player.locstatecode
```

# Friends List
```
import stm

stmw = stm.stm('key')

friendslist = stmw.friendslist(steamid=76561198348243540)
print('Friend Steamid')
print(f'Friend 0 Steamid {friendslist.list[0].steamid}')
# all
friendslist.list
# all 2
friendlist.list[0].steamid
friendlist.list[0].relationship
friendlist.list[0].friend_since
```

# Game Stats
```
import stm

stmw = stm.stm('key')

stats = stmw.stats(steamid=76561198348243540, appid=730)

# all
stats.game
stats.appid
stats.stats
```

# Games List
```
import stm

stmw = stm.stm('key')

gameslist = stmw.gameslist(steamid=76561198348243540)
if 730 in gameslist.list:
    print('730 Appid exists in list')

# all
gameslist.games_count
gameslist.list
```

# Recently Played
```
import stm

stmw = stm.stm('key')

rplayed = stmw.recentlyplayed(steamid=76561198348243540)
print('Recently Played')
print(f'Appid: {rplayed.appid}\nIcon URL: {rplayed.icon_url}')

# all
rplayed.appid
rplayed.name
rplayed.playtimetwoweeks
rplayed.playtime
rplayed.icon_url
rplayed.logo_url
```

# Ban Check
```
import stm

stmw = stm.stm('key')

banstatus = stmw.checkban(steamid=76561198348243540)
print('Ban Status')
print(f'Community Ban: {banstatus.communityban}\nVac Ban: {banstatus.vacban}')

# all
banstatus.communityban
banstatus.vacban
banstatus.total_vacs
banstatus.dayssincelastban
banstatus.total_game_bans
banstatus.economyban
```
