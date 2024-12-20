class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Not:
    def __init__(self,value):
        self._value = value
    def test(self,player):
        if self._value.test(player):
            return False
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self,value,attr):
        self._value = value
        self._attr = attr
    
    def test(self, player):
        player_value = getattr(player,self._attr)
        return player_value < self._value

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self,player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False

class QueryBuilder:
    def __init__(self, query = All()):
        self._query = query

    def plays_in(self,team):
        return QueryBuilder(And(self._query,PlaysIn(team)))

    def has_at_least(self,num,attr):
        return QueryBuilder(And(self._query,HasAtLeast(num,attr)))
    
    def has_fewer_than(self,num,attr):
        return QueryBuilder(And(self._query,HasFewerThan(num,attr)))

    def one_of(self,first_matcher, second_matcher):
        return QueryBuilder(Or(first_matcher, second_matcher))

    def build(self):
        return self._query
