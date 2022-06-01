from scipy import stats

# raw solar data
class Solar:
    def __init__(self):
        self.data = [
        (0,	0,	0),
        (1,	0,	0),
        (2,	0,	0),
        (3,	0,	0.001548952),
        (4,	0,	0.017126799),
        (5,	0,	0.05556752),
        (6,	0.000103127,	0.13203421),
        (7,	0.00823918,	0.22293125),
        (8,	0.05180765,	0.31115308),
        (9,	0.11377241,	0.38261825),
        (10,	0.16397867,	0.42669293),
        (11,	0.1900904,	0.446001),
        (12,	0.18747252,	0.4401042),
        (13,	0.15443817,	0.40363738),
        (14,	0.09591667,	0.3424478),
        (15,	0.03456073,	0.26145884),
        (16,	0.004871739,	0.16952068),
        (17,	8.68E-06,	0.08330672),
        (18,	0,	0.026936987),
        (19,	0,	0.005260382),
        (20,	0,	0),
        (21,	0,	0),
        (22,	0,	0),
        (23,	0,	0)
        ]
        self.winter = list(map(lambda x : x[1], self.data))
        self.summer = list(map(lambda x : x[2], self.data))

    # generates the next solar rate
    def generate(self, season, hour):
        if season == "summer":
            factor = stats.norm.rvs(self.summer[hour % 24], self.summer[hour % 24]*0.15)
        else:
            factor = stats.norm.rvs(self.winter[hour % 24], self.winter[hour % 24]*0.15)
        return max(factor, 0)
