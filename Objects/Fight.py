from Objects.Round import Round


class Fight:

    _rounds_per_fight = 10

    def __init__(self, fight_number, fighter_1, fighter_2):

        self.fight_number = fight_number
        self.fighter1 = fighter_1
        self.fighter2 = fighter_2

        _current_round = 0

        # start Rounds iteration
        while True:

            _current_round += 1

            # create Round
            r = Round(_current_round, self.fighter1, self.fighter2)

            # result of the round is captured in Fighters' scores

            if _current_round > self._rounds_per_fight:
                # last Round reached
                break
            elif self.fighter1.health <= 0:
                # Fighter 1 K.O.
                break
            elif self.fighter2.health <= 0:
                # Fighter 2 K.O.
                break

        # determine winner by consulting scores
        self._wins1 = 0
        self._wins2 = 0

        for v in self.fighter1.scores.values():
            if True in v:
                self._wins1 += 1

        for v in self.fighter2.scores.values():
            if True in v:
                self._wins2 += 1

        # dump scores to statistics file
        self.write_to_log("statistics.csv")

        # populate the number of achieved rounds from one of the Fighters' score card before clearing it
        self.number_of_rounds = len(self.fighter1.scores)

        # clear score card for fighters
        self.fighter1.scores.clear()
        self.fighter2.scores.clear()

    # region Properties

    @property
    def winner(self):
        if self._wins1 > self._wins2:
            return self.fighter1
        else:
            return self.fighter2

    @property
    def loser(self):
        if self._wins1 > self._wins2:
            return self.fighter2
        else:
            return self.fighter1

    @property
    def tie(self):
        if self._wins1 == self._wins2:
            return True
        else:
            return False

    @property
    def number_of_rounds(self):
        return self._number_of_rounds

    @number_of_rounds.setter
    def number_of_rounds(self, value):
        self._number_of_rounds = value

    # endregion

    # region Methods

    def write_to_log(self, file):
        file_handle = open(file, "a+")
        # go to beginning of the file
        file_handle.seek(0)

        # check if file is empty, if so, write headers
        first_char = file_handle.read(1)
        if not first_char:
            # file is empty, insert headers
            file_handle.write("fight_number,fight_round,fighter1_name,fighter1_strategy,fighter1_strategy_level,fighter1_characteristic_level,fighter1_health_in,fighter1_health_out,fighter1_score,fighter1_win,fighter2_name,fighter2_strategy,fighter2_strategy_level,fighter2_characteristic_level,fighter2_health_in,fighter2_health_out,fighter2_score,fighter2_win\n")

        # write data
        for number in range(len(self.fighter1.scores)-1):
            file_handle.write(str(self.fight_number)
                              + "," + str(number+1)
                              + "," + self.fighter1.name + ","
                              + ",".join([str(element) for element in self.fighter1.scores[number+1]])
                              + "," + self.fighter2.name + ","
                              + ",".join([str(element) for element in self.fighter2.scores[number+1]]) + "\n")

    # endregion
