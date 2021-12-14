import random


class Round:

    def __init__(self, round_number, fighter_1, fighter_2):

        self.fighter1 = fighter_1
        self.fighter2 = fighter_2
        self.round_number = round_number

        self._fighter1_score = 0
        self._fighter2_score = 0

        self._fighter1_health_initial = self.fighter1.health
        self._fighter2_health_initial = self.fighter2.health

        # coin flip on the strategy of each fighter: attack or defense?
        # heads for attack, tails for defense

        self._fighter1_strategy = "attack" if self.coin_flip() == "heads" else "defense"
        self._fighter2_strategy = "attack" if self.coin_flip() == "heads" else "defense"

        # coin flip on hi or low
        # value that reduces predictability even further and is part of the calculation
        # heads for hi, tails for lo

        _fighter1_hilo = "hi" if self.coin_flip() == "heads" else "lo"
        _fighter2_hilo = "hi" if self.coin_flip() == "heads" else "lo"

        # randomize strategy level
        # the value has to be within the fighter's profile range for the matching strategy
        # so if the fighter was assigned "attack" by coin flip, that level has to be within the
        # attack_range in the fighter's profile (on the object: Fighter.attack.min and Fighter.attack.max)

        self._fighter1_strategy_level = self.randomize_characteristic_level(self.fighter1, self._fighter1_strategy)
        self._fighter2_strategy_level = self.randomize_characteristic_level(self.fighter2, self._fighter2_strategy)

        # Knockout rule:
        # If any of the fighter hit the maximum of their strategy range, they completely deplete the health of
        # their opponent. The remaining calculations are superfluous.

        _knockout = False

        if self._fighter1_strategy == "attack":
            if self._fighter1_strategy_level == self.fighter1.attack.max:
                self.fighter2.health = 0
                _knockout = True
        else:
            if self._fighter1_strategy_level == self.fighter1.defense.max:
                self.fighter2.health = 0
                _knockout = True

        if self._fighter2_strategy == "attack":
            if self._fighter2_strategy_level == self.fighter2.attack.max:
                self.fighter1.health = 0
                _knockout = True
        else:
            if self._fighter2_strategy_level == self.fighter2.defense.max:
                self.fighter1.health = 0
                _knockout = True

        # only continue with the round if there is no knockout

        if not _knockout:
            # randomize the level of the associated characteristic
            # for attack, that characteristic is speed
            # for defend, that characteristic is stamina
            # that value is used as a multiplier in the next step

            self._fighter1_characteristic_level = 0
            self._fighter2_characteristic_level = 0

            if self._fighter1_strategy == "attack":
                self._fighter1_characteristic_level = self.randomize_characteristic_level(self.fighter1, "speed")
            else:
                self._fighter1_characteristic_level = self.randomize_characteristic_level(self.fighter1, "stamina")

            if self._fighter2_strategy == "attack":
                self._fighter2_characteristic_level = self.randomize_characteristic_level(self.fighter2, "speed")
            else:
                self._fighter2_characteristic_level = self.randomize_characteristic_level(self.fighter2, "stamina")

            # calculate base scores
            self._fighter1_score = \
                self._fighter1_strategy_level + self._fighter1_strategy_level * self._fighter1_characteristic_level / 100
            self._fighter2_score = \
                self._fighter2_strategy_level + self._fighter2_strategy_level * self._fighter2_characteristic_level / 100

            # adjust the base score according to match or mismatch of the two fighters
            # mismatched strategy means 25% adjustment
            # mismatched hi/lo means 25% adjustment

            _adjustment = 0

            if self._fighter1_strategy != self._fighter2_strategy:
                _adjustment += 25
            if _fighter1_hilo != _fighter2_hilo:
                _adjustment += 25

            self._fighter1_score -= self._fighter1_score * _adjustment / 100
            self._fighter2_score -= self._fighter2_score * _adjustment / 100

            # adjust health score for the loser
            # the loser is the fighter with the lowest score
            # his health score is reduced by the difference between the two scores in the Round

            _score_difference = abs(self._fighter1_score - self._fighter2_score)

            _loser = self.loser
            _loser.health -= round(_score_difference)

            # add scores to fighters' records
            # round number | strategy | strategy_level | characeristic_level | health_before | health_after | score | winner/loser

            self.fighter1.add_score(self.round_number,
                                    self._fighter1_strategy, self._fighter1_strategy_level,
                                    self._fighter1_characteristic_level,
                                    self._fighter1_health_initial, self.fighter1.health,
                                    self._fighter1_score, self.fighter1 == self.winner)

            self.fighter2.add_score(self.round_number,
                                    self._fighter2_strategy, self._fighter2_strategy_level,
                                    self._fighter2_characteristic_level,
                                    self._fighter2_health_initial, self.fighter2.health,
                                    self._fighter2_score, self.fighter2 == self.winner)

    # region Properties

    @property
    def winner(self):
        if self._fighter1_score > self._fighter2_score:
            return self.fighter1
        else:
            return self.fighter2

    @property
    def loser(self):
        if self._fighter1_score > self._fighter2_score:
            return self.fighter2
        else:
            return self.fighter1

    # endregion

    # region Functions

    # noinspection PyMethodMayBeStatic
    def coin_flip(self):
        heads_and_tails = ["heads", "tails"]
        return random.choice(heads_and_tails)

    # noinspection PyMethodMayBeStatic
    def randomize_characteristic_level(self, fighter, characteristic):
        # look up the appropriate profile range
        applicable_range = range(0, 0)
        if characteristic == "attack":
            applicable_range = range(fighter.attack.min, fighter.attack.max)
        elif characteristic == "defense":
            applicable_range = range(fighter.defense.min, fighter.defense.max)
        elif characteristic == "stamina":
            applicable_range = range(fighter.stamina.min, fighter.stamina.max)
        elif characteristic == "speed":
            applicable_range = range(fighter.speed.min, fighter.speed.max)

        return random.randint(min(applicable_range), max(applicable_range))

    # endregion
