# steamwrapper
API wrapper for Steam written in Python.

# Git Clone
```
git clone https://github.com/truedl/steamwrapper/
```

# example.py
```
import steamwrapper

stmw = steamwrapper.wrapper('key')
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

Output:
```
C:\stmpy>py example.py
Player Avatar
https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/b7/b79e7adace1c659404920f78e0598a15f9c5073b.jpg

Friend Steamid
76561198017254602

Stats for ValveTestApp260 [ID: 730]
Total Kills: 19690
Total Deaths: 18005
730 Appid exists in list

Recently Played
Appid: 560380
Icon URL: https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/560380/cb5162531011571b4028a06818a7be9154aa3458.jpg

Ban Status
Community Ban: False
Vac Ban: False
```

# Player
```
import steamwrapper

stmw = steamwrapper.wrapper('key')
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
import steamwrapper

stmw = steamwrapper.wrapper('key')

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
import steamwrapper

stmw = steamwrapper.wrapper('key')

stats = stmw.stats(steamid=76561198348243540, appid=730)

# all
stats.game
stats.appid
stats.stats
```

# Games List
```
import steamwrapper

stmw = steamwrapper.wrapper('key')

gameslist = stmw.gameslist(steamid=76561198348243540)
if 730 in gameslist.list:
    print('730 Appid exists in list')

# all
gameslist.games_count
gameslist.list
```

# Recently Played
```
import steamwrapper

stmw = steamwrapper.wrapper('key')

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
import steamwrapper

stmw = steamwrapper.wrapper('key')

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
