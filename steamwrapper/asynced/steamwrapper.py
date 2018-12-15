import aiohttp

class wrapper:
    def __init__(self, key):
        self.key = key
        self.last = [None, None]

    async def fetch(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def SteamIdByCustom(self, custom=None):
        """ Get Steam ID By Steam Custom, Returned: SteamID """

        if self.last[0] == custom:
            return self.last[1]
        else:
            self.last = [custom, await self.fetch(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={self.key}&vanityurl={custom}')['response']['steamid']]
            return self.last[1]

    async def player(self, steamid=None, custom=None):
        """ Get information about steam user by steamid or custom, Returned: SteamPlayer Class """

        if not steamid:
            steamid = await self.SteamIdByCustom(custom=custom)
        data = await self.fetch(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.key}&steamids={steamid}')['response']['players'][0]
        required = ['steamid', 'communityvisibilitystate', 'profilestate', 'personaname', 'lastlogoff', 'commentpermission', 'avatar', 'avatarmedium', 'avatarfull'
                    'personastate', 'realname', 'primaryclanid', 'timecreated', 'personastateflags', 'loccountrycode', 'locstatecode']
        for x in data:
            try:
                required.remove(x)
            except:
                pass
        for x in required:
            data[x] = None
        return SteamPlayer(data['steamid'], data['communityvisibilitystate'], data['profilestate'], data['personaname'], data['lastlogoff'],
                           data['commentpermission'], data['avatar'], data['avatarmedium'], data['avatarfull'], data['personastate'],
                           data['realname'], data['primaryclanid'], data['timecreated'], data['personastateflags'], data['loccountrycode'],
                           data['locstatecode'])

    async def friendslist(self, steamid=None, custom=None, friends=[]):
        """ Get user friendlist by steamid or custom, Returned: SteamFriendsList Class """

        if not steamid:
            steamid = await self.SteamIdByCustom(custom=custom)
        data = await self.fetch(f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.key}&steamid={steamid}&relationship=friend')['friendslist']['friends']
        for x in data:
            friends.append(SteamFriend(x['steamid'], x['relationship'], x['friend_since']))
        return SteamFriendsList(friends)

    async def stats(self, steamid=None, custom=None, appid=None, stats={}, gn=None):
        """ Get user stats by appid and steamid/custom, Returned: SteamGameStats Class """

        if not steamid:
            steamid = await self.SteamIdByCustom(custom=custom)
        data = await self.fetch(f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={self.key}&steamid={steamid}')['playerstats']
        gn = data['gameName']
        for x in data['stats']:
            stats[x['name']] = x['value']
        return SteamGameStats(gn, appid, stats)

    async def gameslist(self, steamid=None, custom=None, list=[], total=None):
        """ Get user gameslist by steamid or custom, Returned: SteamGamesList Class """

        if not steamid:
            steamid = await self.SteamIdByCustom(custom=custom)
        data = await self.fetch(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.key}&steamid={steamid}&format=json')['response']
        total = data['game_count']
        for x in data['games']:
            list.append(x['appid'])
        return SteamGamesList(total, list)

    async def recentlyplayed(self, steamid=None, custom=None):
        """ Get user recently game played by steamid or custom, Returned: SteamRecentlyPlayed Class """

        if not steamid:
            steamid = await self.SteamIdByCustom(custom=custom)
        data = await self.fetch(f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={self.key}&steamid={steamid}&format=json')['response']['games'][0]
        return SteamRecentlyPlayed(data['appid'], data['name'], data['playtime_2weeks'], data['playtime_forever'], data['img_icon_url'], data['img_logo_url'])

    async def checkban(self, steamid=None, custom=None):
        """ Get user ban's information by steamid or custom, Returned: SteamBanStatus Class """

        if not steamid:
            steamid = await self.SteamIdByCustom(custom=custom)
        data = await self.fetch(f'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={self.key}&steamids={steamid}')['players'][0]
        return SteamBanStatus(data['CommunityBanned'], data['VACBanned'], data['NumberOfVACBans'], data['DaysSinceLastBan'], data['NumberOfGameBans'], data['EconomyBan'])

class SteamBanStatus:
    def __init__(self, communityban, vacban, total_vacs, dayssincelastban, total_game_bans, economyban):
        self.communityban = communityban
        self.vacban = vacban
        self.total_vacs = total_vacs
        self.dayssincelastban = dayssincelastban
        self.total_game_bans = total_game_bans
        self.economyban = economyban

class SteamPlayer:
    def __init__(self, steamid, communityvisibilitystate, profilestate, personaname, lastlogoff, commentpermission, avatar, avatarmedium, avatarfull, personastate, realname, primaryclanid, timecreated, personastateflags, loccountrycode, locstatecode):
        self.steamid = steamid
        self.communityvisibilitystate = communityvisibilitystate
        self.profilestate = profilestate
        self.personaname = personaname
        self.lastlogoff = lastlogoff
        self.commentpermission = commentpermission
        self.avatar = avatar
        self.avatarmedium = avatarmedium
        self.avatarfull = avatarfull
        self.personastate = personastate
        self.realname = realname
        self.primaryclanid = primaryclanid
        self.timecreated = timecreated
        self.personastateflags = personastateflags
        self.loccountrycode = loccountrycode
        self.locstatecode = locstatecode

class SteamFriendsList:
    def __init__(self, list):
        self.list = list

class SteamFriend:
    def __init__(self, steamid, relationship, friend_since):
        self.steamid = steamid
        self.relationship = relationship
        self.friend_since = friend_since

class SteamGameStats:
    def __init__(self, game, appid, stats):
        self.game = game
        self.appid = appid
        self.stats = stats

class SteamGamesList:
    def __init__(self, tg, list):
        self.games_count = tg
        self.list = list

class SteamRecentlyPlayed:
    def __init__(self, appid, name, playtimetwoweeks, playtime, icon_url, logo_url):
        self.appid = appid
        self.name = name
        self.playtimetwoweeks = playtimetwoweeks
        self.playtime = playtime
        self.icon_url = f'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/{appid}/{icon_url}.jpg'
        self.logo_url = f'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/{appid}/{logo_url}.jpg'
