from Objects.Base import RestrictedRange
import json


class Fighter:
    # set allowable ranges (range are INCLUSIVE, meaning they include the lower end but exclude the upper end)
    _attack_range = range(1, 101)
    _defense_range = range(1, 101)
    _stamina_range = range(1, 51)
    _speed_range = range(1, 51)
    _health_default = 50

    def __init__(self, name, attack, defense, stamina, speed):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.stamina = stamina
        self.speed = speed
        self.health = self._health_default
        self.scores = {}

    # region Representation

    def __repr__(self):
        obj = {"Fighter": {"name": self.name,
                           "attack": {"min": self.attack.min,
                                      "max": self.attack.max},
                           "defense": {"min": self.defense.min,
                                       "max": self.defense.max},
                           "stamina": {"min": self.stamina.min,
                                       "max": self.stamina.max},
                           "speed": {"min": self.speed.min,
                                     "max": self.speed.max}
                           }
               }
        return json.dumps(obj)

    def __str__(self):
        return "Fighter('%s', attack(%i-%i), defense(%i-%i), " \
               "stamina(%i-%i), speed(%i-%i))" % (self.name,
                                                  self.attack.min, self.attack.max,
                                                  self.defense.min, self.defense.max,
                                                  self.stamina.min, self.stamina.max,
                                                  self.speed.min, self.speed.max)

    # endregion

    # region Properties

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        __attack = RestrictedRange(min(Fighter._attack_range), max(Fighter._attack_range))

        if self.validate_range(value):
            __attack.min = value[0]
            __attack.max = value[1]
        else:
            raise ValueError(
                "The submitted 'attack' argument is not a list expressing a range. It should be [min, max].")

        self._attack = __attack

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        __defense = RestrictedRange(min(Fighter._defense_range), max(Fighter._defense_range))

        if self.validate_range(value):
            __defense.min = value[0]
            __defense.max = value[1]
        else:
            raise ValueError(
                "The submitted 'defense' argument is not a list expressing a range. It should be [min, max].")

        self._defense = __defense

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        __stamina = RestrictedRange(min(Fighter._stamina_range), max(Fighter._stamina_range))

        if self.validate_range(value):
            __stamina.min = value[0]
            __stamina.max = value[1]
        else:
            raise ValueError(
                "The submitted 'stamina' argument is not a list expressing a range. It should be [min, max].")

        self._stamina = __stamina

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        __speed = RestrictedRange(min(Fighter._speed_range), max(Fighter._speed_range))

        if self.validate_range(value):
            __speed.min = value[0]
            __speed.max = value[1]
        else:
            raise ValueError(
                "The submitted 'speed' argument is not a list expressing a range. It should be [min, max].")

        self._speed = __speed

    # endregion

    # region Functions

    # noinspection PyMethodMayBeStatic
    def validate_range(self, submitted_range):
        if type(submitted_range) is list:
            if len(submitted_range) != 2:
                return False
            else:
                if submitted_range[0] > submitted_range[1]:
                    submitted_range.reverse()
                return True
        else:
            return False

    # endregion

    # region Methods

    def add_score(self, round_number, strategy, strategy_level, characteristic_level, health_before, health_after,
                  score, winner):
        if round_number not in self.scores.keys():
            self.scores[round_number] = [strategy, strategy_level, characteristic_level, health_before, health_after,
                                         score, winner]
        else:
            raise ValueError("Round has already been accounted for.")

    # endregion
