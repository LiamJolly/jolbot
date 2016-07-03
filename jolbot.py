import rg


class Robot:

    def act(self, game):
        # if we're in the center blow up!
        if self.location == rg.CENTER_POINT:
            return ['suicide']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        return self.makeSafeMove(game)

    def makeSafeMove(self, game):
        potentialLocations = rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))

        for location in potentialLocations:
            if not self.isPotentialCollision(game, location):
                return ['move', location]
        #no safe move so guard
        return ['guard']

    def isPotentialCollision(self, game, moveLocation):
        locationsToCheck = self.getLocationsAroundPoint(game, moveLocation)
        for locationToCheck in locationsToCheck:
            if (locationToCheck != self.location):
                if (locationToCheck in game.robots):
                    return True
        return False

    def getLocationsAroundPoint(self, game, point):
        locations = []
        locations.append((point[0] - 1, point[1]))
        locations.append((point[0] + 1, point[1]))
        locations.append((point[0], point[1] - 1))
        locations.append((point[0], point[1] + 1))
        return locations