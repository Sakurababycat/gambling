from strategy import StrategyRegister, BaseStrategy
from random import choice, random


class Gambling:
    def __init__(self):
        self.strategyPool = {}
        for strategyClass in StrategyRegister.values():
            self.strategyPool.update(strategyClass.makeStrategy())

    def noise(self, lhr: bool, rhr: bool) -> tuple[bool, bool]:
        noiseRate = 0.01
        if random() < noiseRate:
            lhr = not lhr
        if random() < noiseRate:
            rhr = not rhr
        return lhr, rhr

    def singleRace(self, lh: BaseStrategy, rh: BaseStrategy) -> tuple[int, int]:
        lhrec, rhrec = [], []
        lhscore, rhscore = 0, 0
        for _ in range(200):
            lhr, rhr = lh.step(lhrec, rhrec), rh.step(rhrec, lhrec)
            score = self.getScore(lhr, rhr)
            lhscore += score[0]
            rhscore += score[1]
            lhr, rhr = self.noise(lhr, rhr)
            lhrec.append(lhr)
            rhrec.append(rhr)
        return lhscore, rhscore

    def getScore(self, lh: bool, rh: bool) -> tuple[int, int]:
        def __getScore(lh: bool, rh: bool) -> int:
            if lh:
                if rh:
                    return 3
                else:
                    return 0
            else:
                if rh:
                    return 5
                else:
                    return 1

        return __getScore(lh, rh), __getScore(rh, lh)

    def fullRace(self, raceWithSelf=False):
        strategyCnt = len(self.strategyPool)
        keys = list(self.strategyPool.keys())
        scores = dict(zip(keys, [0] * strategyCnt))
        for i in range(strategyCnt):
            lh = keys[i]
            for j in range(i + (not raceWithSelf), strategyCnt):
                rh = keys[j]
                score = self.singleRace(self.strategyPool[lh], self.strategyPool[rh])
                scores[lh] += score[0]
                scores[rh] += score[1]
                # print(lh, rh, score)
        return scores

    def randRace(self, raceWithSelf=False):
        strategyCnt = len(self.strategyPool)
        keys = list(self.strategyPool.keys())
        scores = dict(zip(keys, [0] * strategyCnt))
        for _ in range(1000):
            lh, rh = choice(keys), choice(keys)
            if raceWithSelf or lh != rh:
                score = self.singleRace(self.strategyPool[lh], self.strategyPool[rh])
                scores[lh] += score[0]
                scores[rh] += score[1]
        return scores


if __name__ == "__main__":
    res = Gambling().fullRace()
    res = sorted(res.items(), key=lambda item: item[1])
    print(res)
