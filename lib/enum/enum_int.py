"""
Integer enumerations for Natro Macro
Equivalent to lib/enum/EnumInt.ahk
"""

class EnumInt:
    """Integer enumeration constants"""

    # Discord and communication settings
    discordMode = 1
    discordCheck = 2
    MainChannelCheck = 3
    ReportChannelCheck = 4
    WebhookEasterEgg = 5
    ssCheck = 6
    ssDebugging = 7

    # Critical screenshots and checks
    CriticalSSCheck = 8
    AmuletSSCheck = 9
    MachineSSCheck = 10
    BalloonSSCheck = 11
    ViciousSSCheck = 12
    DeathSSCheck = 13
    PlanterSSCheck = 14
    HoneySSCheck = 15
    criticalCheck = 16
    CriticalErrorPingCheck = 17
    DisconnectPingCheck = 18
    GameFrozenPingCheck = 19
    PhantomPingCheck = 20
    UnexpectedDeathPingCheck = 21
    EmergencyBalloonPingCheck = 22

    # Macro state and planters
    MacroState = 23
    PlanterMode = 24
    MaxAllowedPlanters = 25
    HarvestInterval = 26
    AutomaticHarvestInterval = 27
    HarvestFullGrown = 28
    GotoPlanterField = 29
    GatherFieldSipping = 30
    ConvertFullBagHarvest = 31
    GatherPlanterLoot = 32

    # Planter types
    PlasticPlanterCheck = 33
    CandyPlanterCheck = 34
    BlueClayPlanterCheck = 35
    RedClayPlanterCheck = 36
    TackyPlanterCheck = 37
    PesticidePlanterCheck = 38
    HeatTreatedPlanterCheck = 39
    HydroponicPlanterCheck = 40
    PetalPlanterCheck = 41
    PaperPlanterCheck = 42
    TicketPlanterCheck = 43
    PlanterOfPlentyCheck = 44

    # Field checks
    BambooFieldCheck = 45
    BlueFlowerFieldCheck = 46
    CactusFieldCheck = 47
    CloverFieldCheck = 48
    CoconutFieldCheck = 49
    DandelionFieldCheck = 50
    MountainTopFieldCheck = 51
    MushroomFieldCheck = 52
    PepperFieldCheck = 53
    PineTreeFieldCheck = 54
    PineappleFieldCheck = 55
    PumpkinFieldCheck = 56
    RoseFieldCheck = 57
    SpiderFieldCheck = 58
    StrawberryFieldCheck = 59
    StumpFieldCheck = 60
    SunflowerFieldCheck = 61

    # Various settings
    MultiReset = 62
    ConvertMins = 63
    LastConvertBalloon = 64
    DisableToolUse = 65
    AnnounceGuidingStar = 66
    NewWalk = 67
    HiveSlot = 68
    HiveBees = 69
    ConvertDelay = 70
    ReconnectMessage = 71
    PublicFallback = 72
    KeyDelay = 73

    # Field pattern settings (1-3 for different fields)
    FieldPatternReps1 = 74
    FieldPatternReps2 = 75
    FieldPatternReps3 = 76
    FieldPatternShift1 = 77
    FieldPatternShift2 = 78
    FieldPatternShift3 = 79
    FieldPatternInvertFB1 = 80
    FieldPatternInvertFB2 = 81
    FieldPatternInvertFB3 = 82
    FieldPatternInvertLR1 = 83
    FieldPatternInvertLR2 = 84
    FieldPatternInvertLR3 = 85
    FieldUntilMins1 = 86
    FieldUntilMins2 = 87
    FieldUntilMins3 = 88
    FieldUntilPack1 = 89
    FieldUntilPack2 = 90
    FieldUntilPack3 = 91
    FieldSprinklerDist1 = 92
    FieldSprinklerDist2 = 93
    FieldSprinklerDist3 = 94
    FieldRotateTimes1 = 95
    FieldRotateTimes2 = 96
    FieldRotateTimes3 = 97
    FieldDriftCheck1 = 98
    FieldDriftCheck2 = 99
    FieldDriftCheck3 = 100

    # Time-based events
    ClockCheck = 101
    LastClock = 102
    MondoBuffCheck = 103
    LastMondoBuff = 104
    AntPassCheck = 105
    LastAntPass = 106
    RoboPassCheck = 107
    LastRoboPass = 108

    # Dispensers
    HoneyDisCheck = 109
    LastHoneyDis = 110
    TreatDisCheck = 111
    LastTreatDis = 112
    BlueberryDisCheck = 113
    LastBlueberryDis = 114
    StrawberryDisCheck = 115
    LastStrawberryDis = 116
    CoconutDisCheck = 117
    LastCoconutDis = 118
    RoyalJellyDisCheck = 119
    LastRoyalJellyDis = 120
    GlueDisCheck = 121
    LastGlueDis = 122

    # Boosters
    BlueBoostCheck = 123
    LastBlueBoost = 124
    RedBoostCheck = 125
    LastRedBoost = 126
    MountainBoostCheck = 127
    LastMountainBoost = 128

    # Beesmas events
    BeesmasGatherInterruptCheck = 129
    StockingsCheck = 130
    LastStockings = 131
    WreathCheck = 132
    LastWreath = 133
    FeastCheck = 134
    LastFeast = 135
    GingerbreadCheck = 136
    LastGingerbread = 137

    # Machines and special events
    SnowMachineCheck = 138
    LastSnowMachine = 139
    CandlesCheck = 140
    LastCandles = 141
    SamovarCheck = 142
    LastSamovar = 143
    LidArtCheck = 144
    LastLidArt = 145
    GummyBeaconCheck = 146
    LastGummyBeacon = 147
    MonsterRespawnTime = 148

    # Bugrun events
    BugrunInterruptCheck = 149
    BugrunLadybugsCheck = 150
    BugrunLadybugsLoot = 151
    LastBugrunLadybugs = 152
    BugrunRhinoBeetlesCheck = 153
    BugrunRhinoBeetlesLoot = 154
    LastBugrunRhinoBeetles = 155
    BugrunSpiderCheck = 156
    BugrunSpiderLoot = 157
    LastBugrunSpider = 158
    BugrunMantisCheck = 159
    BugrunMantisLoot = 160
    LastBugrunMantis = 161
    BugrunScorpionsCheck = 162
    BugrunScorpionsLoot = 163
    LastBugrunScorpions = 164
    BugrunWerewolfCheck = 165
    BugrunWerewolfLoot = 166
    LastBugrunWerewolf = 167

    # Monsters
    TunnelBearCheck = 168
    TunnelBearBabyCheck = 169
    LastTunnelBear = 170
    KingBeetleCheck = 171
    KingBeetleBabyCheck = 172
    LastKingBeetle = 173
    StumpSnailCheck = 174
    LastStumpSnail = 175
    CommandoCheck = 176
    LastCommando = 177
    CocoCrabCheck = 178
    LastCocoCrab = 179

    # Stingers
    StingerCheck = 180
    StingerPepperCheck = 181
    StingerMountainTopCheck = 182
    StingerRoseCheck = 183
    StingerCactusCheck = 184
    StingerSpiderCheck = 185
    StingerCloverCheck = 186

    # Boost chaser and field settings
    BoostChaserCheck = 187
    FieldBoosterMins = 188

    # Hotbar timing
    HotbarTime2 = 189
    HotbarTime3 = 190
    HotbarTime4 = 191
    HotbarTime5 = 192
    HotbarTime6 = 193
    HotbarTime7 = 194
    LastHotkey2 = 195
    LastHotkey3 = 196
    LastHotkey4 = 197
    LastHotkey5 = 198
    LastHotkey6 = 199
    LastHotkey7 = 200

    # Special items and events
    LastWhirligig = 201
    LastEnzymes = 202
    LastGlitter = 203
    LastSnowflake = 204
    LastWindShrine = 205
    LastMicroConverter = 206

    # Quests
    QuestGatherMins = 207
    PolarQuestCheck = 208
    PolarQuestGatherInterruptCheck = 209
    HoneyQuestCheck = 210
    BlackQuestCheck = 211
    LastBlackQuest = 212
    BuckoQuestCheck = 213
    BuckoQuestGatherInterruptCheck = 214
    RileyQuestCheck = 215
    RileyQuestGatherInterruptCheck = 216

    # Amulets
    KingBeetleAmuletMode = 217
    ShellAmuletMode = 218

    # Announcements and status
    NightAnnouncementCheck = 219
    PublicJoined = 220
    DebugLogEnabled = 221
    StingerDailyBonusCheck = 222
    GatherDoubleReset = 223

    # Honeystorm and other events
    HoneystormCheck = 224
    LastHoneystorm = 225
    RBPDelevelCheck = 226
    LastRBPDelevel = 227

    # Shrine and blender
    ShrineCheck = 228
    BlenderCheck = 229
    ShrineAmount1 = 230
    ShrineAmount2 = 231
    BlenderAmount1 = 232
    BlenderAmount2 = 233
    BlenderAmount3 = 234
    BlenderRot = 235
    TimerInterval = 236
    LastBlenderRot = 237
    BlenderTime1 = 238
    BlenderTime2 = 239
    BlenderTime3 = 240

    # Mondo settings
    MondoSecs = 241
    MPlanterGatherA = 242
    MPlanterGather1 = 243
    MPlanterGather2 = 244
    MPlanterGather3 = 245
    MPuffModeA = 246
    MPuffMode1 = 247
    MPuffMode2 = 248
    MPuffMode3 = 249

    # Field boosters
    BlueFlowerBoosterCheck = 250
    BambooBoosterCheck = 251
    PineTreeBoosterCheck = 252
    DandelionBoosterCheck = 253
    SunflowerBoosterCheck = 254
    CloverBoosterCheck = 255
    SpiderBoosterCheck = 256
    PineappleBoosterCheck = 257
    CactusBoosterCheck = 258
    PumpkinBoosterCheck = 259
    MushroomBoosterCheck = 260
    StrawberryBoosterCheck = 261
    RoseBoosterCheck = 262

    # Planter management
    MPlanterHold1 = 263
    MPlanterHold2 = 264
    MPlanterHold3 = 265

    # Additional quests and events
    BrownQuestCheck = 266
    LastBrownQuest = 267
    StickerStackCheck = 268
    LastStickerStack = 269
    StickerStackMode = 270
    StickerStackTimer = 271
    StickerPrinterCheck = 272
    LastStickerPrinter = 273
    AntPassBuyCheck = 274
    StickerStackHive = 275
    StickerStackCub = 276
    QuestBoostCheck = 277
    MConvertFullBagHarvest = 278

    # More planter settings
    MPlanterGatherA = 279  # Duplicate from 242
    MPlanterGather1 = 280  # Duplicate from 243
    MPlanterGather2 = 281  # Duplicate from 244
    MPlanterGather3 = 282  # Duplicate from 245
    MPlanterSmoking1 = 283
    MPlanterSmoking2 = 284
    MPlanterSmoking3 = 285
    MPuffModeA = 286  # Duplicate from 246
    MPuffMode1 = 287  # Duplicate from 247
    MPuffMode2 = 288  # Duplicate from 248
    MPuffMode3 = 289  # Duplicate from 249

    # Planter automation
    PlanterHarvestNow1 = 290
    PlanterHarvestNow2 = 291
    PlanterHarvestNow3 = 292
    PlanterSS1 = 293
    PlanterSS2 = 294
    PlanterSS3 = 295
    PlanterHarvestTime1 = 296
    PlanterHarvestTime2 = 297
    PlanterHarvestTime3 = 298
    PlanterEstPercent1 = 299
    PlanterEstPercent2 = 300
    PlanterEstPercent3 = 301
    PlanterGlitter1 = 302
    PlanterGlitter2 = 303
    PlanterGlitter3 = 304
    PlanterGlitterC1 = 305
    PlanterGlitterC2 = 306
    PlanterGlitterC3 = 307
    PlanterManualCycle1 = 308
    PlanterManualCycle2 = 309
    PlanterManualCycle3 = 310

    # Memory matches
    NormalMemoryMatchCheck = 311
    LastNormalMemoryMatch = 312
    MegaMemoryMatchCheck = 313
    LastMegaMemoryMatch = 314
    ExtremeMemoryMatchCheck = 315
    LastExtremeMemoryMatch = 316
    NightMemoryMatchCheck = 317
    LastNightMemoryMatch = 318
    WinterMemoryMatchCheck = 319
    LastWinterMemoryMatch = 320
    MemoryMatchInterruptCheck = 321

    # Memory match ignores (many items)
    MicroConverterMatchIgnore = 322
    SunflowerSeedMatchIgnore = 323
    JellyBeanMatchIgnore = 324
    RoyalJellyMatchIgnore = 325
    TicketMatchIgnore = 326
    CyanTrimMatchIgnore = 327
    OilMatchIgnore = 328
    StrawberryMatchIgnore = 329
    CoconutMatchIgnore = 330
    TropicalDrinkMatchIgnore = 331
    RedExtractMatchIgnore = 332
    MagicBeanMatchIgnore = 333
    PineappleMatchIgnore = 334
    StarJellyMatchIgnore = 335
    EnzymeMatchIgnore = 336
    BlueExtractMatchIgnore = 337
    GumdropMatchIgnore = 338
    FieldDiceMatchIgnore = 339
    MoonCharmMatchIgnore = 340
    BlueberryMatchIgnore = 341
    GlitterMatchIgnore = 342
    StingerMatchIgnore = 343
    TreatMatchIgnore = 344
    GlueMatchIgnore = 345
    CloudVialMatchIgnore = 346
    SoftWaxMatchIgnore = 347
    HardWaxMatchIgnore = 348
    SwirledWaxMatchIgnore = 349
    NightBellMatchIgnore = 350
    HoneysuckleMatchIgnore = 351
    SuperSmoothieMatchIgnore = 352
    SmoothDiceMatchIgnore = 353
    NeonberryMatchIgnore = 354
    GingerbreadMatchIgnore = 355
    SilverEggMatchIgnore = 356
    GoldEggMatchIgnore = 357
    DiamondEggMatchIgnore = 358

    # Additional boosters
    CoconutBoosterCheck = 359
    StumpBoosterCheck = 360
    PepperBoosterCheck = 361

    # Final settings
    HoneyUpdateSSCheck = 362
    StickerStackVoucher = 363
    MGatherPlanterLoot = 364
    prioritylistnumeric = 365

    # Array for backward compatibility
    arr = [
        "discordMode", "discordCheck", "MainChannelCheck", "ReportChannelCheck", "WebhookEasterEgg", "ssCheck", "ssDebugging",
        "CriticalSSCheck", "AmuletSSCheck", "MachineSSCheck", "BalloonSSCheck", "ViciousSSCheck", "DeathSSCheck", "PlanterSSCheck", "HoneySSCheck",
        "criticalCheck", "CriticalErrorPingCheck", "DisconnectPingCheck", "GameFrozenPingCheck", "PhantomPingCheck", "UnexpectedDeathPingCheck", "EmergencyBalloonPingCheck",
        "MacroState", "PlanterMode", "MaxAllowedPlanters", "HarvestInterval", "AutomaticHarvestInterval", "HarvestFullGrown", "GotoPlanterField", "GatherFieldSipping",
        "ConvertFullBagHarvest", "GatherPlanterLoot", "PlasticPlanterCheck", "CandyPlanterCheck", "BlueClayPlanterCheck", "RedClayPlanterCheck", "TackyPlanterCheck",
        "PesticidePlanterCheck", "HeatTreatedPlanterCheck", "HydroponicPlanterCheck", "PetalPlanterCheck", "PaperPlanterCheck", "TicketPlanterCheck", "PlanterOfPlentyCheck",
        "BambooFieldCheck", "BlueFlowerFieldCheck", "CactusFieldCheck", "CloverFieldCheck", "CoconutFieldCheck", "DandelionFieldCheck", "MountainTopFieldCheck",
        "MushroomFieldCheck", "PepperFieldCheck", "PineTreeFieldCheck", "PineappleFieldCheck", "PumpkinFieldCheck", "RoseFieldCheck", "SpiderFieldCheck",
        "StrawberryFieldCheck", "StumpFieldCheck", "SunflowerFieldCheck", "MultiReset", "ConvertMins", "LastConvertBalloon", "DisableToolUse", "AnnounceGuidingStar",
        "NewWalk", "HiveSlot", "HiveBees", "ConvertDelay", "ReconnectMessage", "PublicFallback", "KeyDelay", "FieldPatternReps1", "FieldPatternReps2", "FieldPatternReps3",
        "FieldPatternShift1", "FieldPatternShift2", "FieldPatternShift3", "FieldPatternInvertFB1", "FieldPatternInvertFB2", "FieldPatternInvertFB3",
        "FieldPatternInvertLR1", "FieldPatternInvertLR2", "FieldPatternInvertLR3", "FieldUntilMins1", "FieldUntilMins2", "FieldUntilMins3",
        "FieldUntilPack1", "FieldUntilPack2", "FieldUntilPack3", "FieldSprinklerDist1", "FieldSprinklerDist2", "FieldSprinklerDist3",
        "FieldRotateTimes1", "FieldRotateTimes2", "FieldRotateTimes3", "FieldDriftCheck1", "FieldDriftCheck2", "FieldDriftCheck3",
        "ClockCheck", "LastClock", "MondoBuffCheck", "LastMondoBuff", "AntPassCheck", "LastAntPass", "RoboPassCheck", "LastRoboPass",
        "HoneyDisCheck", "LastHoneyDis", "TreatDisCheck", "LastTreatDis", "BlueberryDisCheck", "LastBlueberryDis", "StrawberryDisCheck", "LastStrawberryDis",
        "CoconutDisCheck", "LastCoconutDis", "RoyalJellyDisCheck", "LastRoyalJellyDis", "GlueDisCheck", "LastGlueDis", "BlueBoostCheck", "LastBlueBoost",
        "RedBoostCheck", "LastRedBoost", "MountainBoostCheck", "LastMountainBoost", "BeesmasGatherInterruptCheck", "StockingsCheck", "LastStockings",
        "WreathCheck", "LastWreath", "FeastCheck", "LastFeast", "GingerbreadCheck", "LastGingerbread", "SnowMachineCheck", "LastSnowMachine",
        "CandlesCheck", "LastCandles", "SamovarCheck", "LastSamovar", "LidArtCheck", "LastLidArt", "GummyBeaconCheck", "LastGummyBeacon", "MonsterRespawnTime",
        "BugrunInterruptCheck", "BugrunLadybugsCheck", "BugrunLadybugsLoot", "LastBugrunLadybugs", "BugrunRhinoBeetlesCheck", "BugrunRhinoBeetlesLoot", "LastBugrunRhinoBeetles",
        "BugrunSpiderCheck", "BugrunSpiderLoot", "LastBugrunSpider", "BugrunMantisCheck", "BugrunMantisLoot", "LastBugrunMantis", "BugrunScorpionsCheck", "BugrunScorpionsLoot", "LastBugrunScorpions",
        "BugrunWerewolfCheck", "BugrunWerewolfLoot", "LastBugrunWerewolf", "TunnelBearCheck", "TunnelBearBabyCheck", "LastTunnelBear", "KingBeetleCheck", "KingBeetleBabyCheck", "LastKingBeetle",
        "StumpSnailCheck", "LastStumpSnail", "CommandoCheck", "LastCommando", "CocoCrabCheck", "LastCocoCrab", "StingerCheck", "StingerPepperCheck", "StingerMountainTopCheck",
        "StingerRoseCheck", "StingerCactusCheck", "StingerSpiderCheck", "StingerCloverCheck", "BoostChaserCheck", "FieldBoosterMins", "HotbarTime2", "HotbarTime3", "HotbarTime4",
        "HotbarTime5", "HotbarTime6", "HotbarTime7", "LastHotkey2", "LastHotkey3", "LastHotkey4", "LastHotkey5", "LastHotkey6", "LastHotkey7", "LastHotkey7",
        "LastWhirligig", "LastEnzymes", "LastGlitter", "LastSnowflake", "LastWindShrine", "LastMicroConverter", "QuestGatherMins", "PolarQuestCheck",
        "PolarQuestGatherInterruptCheck", "HoneyQuestCheck", "BlackQuestCheck", "LastBlackQuest", "BuckoQuestCheck", "BuckoQuestGatherInterruptCheck",
        "RileyQuestCheck", "RileyQuestGatherInterruptCheck", "KingBeetleAmuletMode", "ShellAmuletMode", "NightAnnouncementCheck", "PublicJoined",
        "DebugLogEnabled", "StingerDailyBonusCheck", "GatherDoubleReset", "HoneystormCheck", "LastHoneystorm", "RBPDelevelCheck", "LastRBPDelevel",
        "ShrineCheck", "BlenderCheck", "ShrineAmount1", "ShrineAmount2", "BlenderAmount1", "BlenderAmount2", "BlenderAmount3", "BlenderRot",
        "TimerInterval", "LastBlenderRot", "BlenderTime1", "BlenderTime2", "BlenderTime3", "MondoSecs", "MPlanterGatherA", "MPlanterGather1",
        "MPlanterGather2", "MPlanterGather3", "MPuffModeA", "MPuffMode1", "MPuffMode2", "MPuffMode3", "BlueFlowerBoosterCheck", "BambooBoosterCheck",
        "PineTreeBoosterCheck", "DandelionBoosterCheck", "SunflowerBoosterCheck", "CloverBoosterCheck", "SpiderBoosterCheck", "PineappleBoosterCheck",
        "CactusBoosterCheck", "PumpkinBoosterCheck", "MushroomBoosterCheck", "StrawberryBoosterCheck", "RoseBoosterCheck", "MPlanterHold1", "MPlanterHold2", "MPlanterHold3",
        "BrownQuestCheck", "LastBrownQuest", "StickerStackCheck", "LastStickerStack", "StickerStackMode", "StickerStackTimer", "StickerPrinterCheck",
        "LastStickerPrinter", "AntPassBuyCheck", "StickerStackHive", "StickerStackCub", "QuestBoostCheck", "MConvertFullBagHarvest", "MPlanterGatherA",
        "MPlanterGather1", "MPlanterGather2", "MPlanterGather3", "MPlanterSmoking1", "MPlanterSmoking2", "MPlanterSmoking3", "MPuffModeA", "MPuffMode1",
        "MPuffMode2", "MPuffMode3", "PlanterHarvestNow1", "PlanterHarvestNow2", "PlanterHarvestNow3", "PlanterSS1", "PlanterSS2", "PlanterSS3",
        "PlanterHarvestTime1", "PlanterHarvestTime2", "PlanterHarvestTime3", "PlanterEstPercent1", "PlanterEstPercent2", "PlanterEstPercent3",
        "PlanterGlitter1", "PlanterGlitter2", "PlanterGlitter3", "PlanterGlitterC1", "PlanterGlitterC2", "PlanterGlitterC3", "PlanterManualCycle1",
        "PlanterManualCycle2", "PlanterManualCycle3", "NormalMemoryMatchCheck", "LastNormalMemoryMatch", "MegaMemoryMatchCheck", "LastMegaMemoryMatch",
        "ExtremeMemoryMatchCheck", "LastExtremeMemoryMatch", "NightMemoryMatchCheck", "LastNightMemoryMatch", "WinterMemoryMatchCheck", "LastWinterMemoryMatch",
        "MemoryMatchInterruptCheck", "MicroConverterMatchIgnore", "SunflowerSeedMatchIgnore", "JellyBeanMatchIgnore", "RoyalJellyMatchIgnore", "TicketMatchIgnore",
        "CyanTrimMatchIgnore", "OilMatchIgnore", "StrawberryMatchIgnore", "CoconutMatchIgnore", "TropicalDrinkMatchIgnore", "RedExtractMatchIgnore",
        "MagicBeanMatchIgnore", "PineappleMatchIgnore", "StarJellyMatchIgnore", "EnzymeMatchIgnore", "BlueExtractMatchIgnore", "GumdropMatchIgnore",
        "FieldDiceMatchIgnore", "MoonCharmMatchIgnore", "BlueberryMatchIgnore", "GlitterMatchIgnore", "StingerMatchIgnore", "TreatMatchIgnore",
        "GlueMatchIgnore", "CloudVialMatchIgnore", "SoftWaxMatchIgnore", "HardWaxMatchIgnore", "SwirledWaxMatchIgnore", "NightBellMatchIgnore",
        "HoneysuckleMatchIgnore", "SuperSmoothieMatchIgnore", "SmoothDiceMatchIgnore", "NeonberryMatchIgnore", "GingerbreadMatchIgnore", "SilverEggMatchIgnore",
        "GoldEggMatchIgnore", "DiamondEggMatchIgnore", "CoconutBoosterCheck", "StumpBoosterCheck", "PepperBoosterCheck", "HoneyUpdateSSCheck",
        "StickerStackVoucher", "MGatherPlanterLoot", "prioritylistnumeric"
    ]
