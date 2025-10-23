"""
String enumerations for Natro Macro
Equivalent to lib/enum/EnumStr.ahk
"""

class EnumStr:
    """String enumeration constants"""

    # Discord and communication settings
    webhook = 1
    bottoken = 2
    MainChannelID = 3
    ReportChannelID = 4
    discordUID = 5
    commandPrefix = 6
    MoveMethod = 7
    SprinklerType = 8
    ConvertBalloon = 9
    PrivServer = 10

    # Field settings (1-3 for different fields)
    FieldName1 = 11
    FieldName2 = 12
    FieldName3 = 13
    FieldPattern1 = 14
    FieldPattern2 = 15
    FieldPattern3 = 16
    FieldPatternSize1 = 17
    FieldPatternSize2 = 18
    FieldPatternSize3 = 19
    FieldReturnType1 = 20
    FieldReturnType2 = 21
    FieldReturnType3 = 22
    FieldSprinklerLoc1 = 23
    FieldSprinklerLoc2 = 24
    FieldSprinklerLoc3 = 25
    FieldRotateDirection1 = 26
    FieldRotateDirection2 = 27
    FieldRotateDirection3 = 28

    # Special actions
    MondoAction = 29
    AntPassAction = 30

    # Field boosters (1-3 for different fields)
    FieldBooster1 = 31
    FieldBooster2 = 32
    FieldBooster3 = 33

    # Hotbar while conditions
    HotbarWhile2 = 34
    HotbarWhile3 = 35
    HotbarWhile4 = 36
    HotbarWhile5 = 37
    HotbarWhile6 = 38
    HotbarWhile7 = 39

    # Quest and movement settings
    QuestGatherReturnBy = 40
    MoveSpeedNum = 41

    # Reconnect settings
    ReconnectInterval = 42
    ReconnectHour = 43
    ReconnectMin = 44
    FallbackServer1 = 45
    FallbackServer2 = 46
    FallbackServer3 = 47

    # Night announcements
    NightAnnouncementName = 48
    NightAnnouncementPingID = 49
    NightAnnouncementWebhook = 50

    # Monster health inputs
    SnailTime = 51
    ChickTime = 52
    InputSnailHealth = 53
    InputChickHealth = 54

    # Shrine settings
    ShrineItem1 = 55
    ShrineItem2 = 56
    ShrineIndex1 = 57
    ShrineIndex2 = 58

    # Blender settings
    BlenderIndex1 = 59
    BlenderIndex2 = 60
    BlenderIndex3 = 61
    BlenderItem1 = 62
    BlenderItem2 = 63
    BlenderItem3 = 64

    # Sticker settings
    StickerStackItem = 65
    StickerPrinterEgg = 66

    # Mondo loot
    MondoLootDirection = 67

    # Planter settings (1-3 for different planters)
    PlanterName1 = 68
    PlanterName2 = 69
    PlanterName3 = 70
    PlanterField1 = 71
    PlanterField2 = 72
    PlanterField3 = 73
    PlanterNectar1 = 74
    PlanterNectar2 = 75
    PlanterNectar3 = 76
    PlanterHarvestFull1 = 77
    PlanterHarvestFull2 = 78
    PlanterHarvestFull3 = 79

    # Array for backward compatibility
    arr = [
        "webhook", "bottoken", "MainChannelID", "ReportChannelID", "discordUID", "commandPrefix", "MoveMethod", "SprinklerType", "ConvertBalloon", "PrivServer",
        "FieldName1", "FieldName2", "FieldName3", "FieldPattern1", "FieldPattern2", "FieldPattern3", "FieldPatternSize1", "FieldPatternSize2", "FieldPatternSize3",
        "FieldReturnType1", "FieldReturnType2", "FieldReturnType3", "FieldSprinklerLoc1", "FieldSprinklerLoc2", "FieldSprinklerLoc3", "FieldRotateDirection1",
        "FieldRotateDirection2", "FieldRotateDirection3", "MondoAction", "AntPassAction", "FieldBooster1", "FieldBooster2", "FieldBooster3", "HotbarWhile2",
        "HotbarWhile3", "HotbarWhile4", "HotbarWhile5", "HotbarWhile6", "HotbarWhile7", "QuestGatherReturnBy", "MoveSpeedNum", "ReconnectInterval",
        "ReconnectHour", "ReconnectMin", "FallbackServer1", "FallbackServer2", "FallbackServer3", "NightAnnouncementName", "NightAnnouncementPingID",
        "NightAnnouncementWebhook", "SnailTime", "ChickTime", "InputSnailHealth", "InputChickHealth", "ShrineItem1", "ShrineItem2", "ShrineIndex1",
        "ShrineIndex2", "BlenderIndex1", "BlenderIndex2", "BlenderIndex3", "BlenderItem1", "BlenderItem2", "BlenderItem3", "StickerStackItem",
        "StickerPrinterEgg", "MondoLootDirection", "PlanterName1", "PlanterName2", "PlanterName3", "PlanterField1", "PlanterField2", "PlanterField3",
        "PlanterNectar1", "PlanterNectar2", "PlanterNectar3", "PlanterHarvestFull1", "PlanterHarvestFull2", "PlanterHarvestFull3"
    ]
