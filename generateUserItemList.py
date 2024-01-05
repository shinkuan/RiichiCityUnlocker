import os
import re
import json

userEquip = {}
with open('setting.json', 'r') as f:
    setting = json.load(f)
    userEquip = setting['userEquip']

# 立直棒
def find_itemType13(directory):
    pattern = r'room_(\d+)'  # Regular expression to match the pattern 'roleimg_<roleID>_<model>'
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 13:
            equipID = item['ItemID']
    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            itemID = match.groups()
            result.append({
                "expiredAt": 0,
                "feelValue": 0,
                "giftContent": [],
                "isCanEquip": True,
                "isEquip": equipID == int(itemID[0]), # Check if the item is equipped
                "isExpired": False,
                "isLock": False,
                "itemID": int(itemID[0]),
                "itemType": 13,
                "label": 0,
                "num": 1,
                "recycleNum": 0,
                "source": 0
            })

    return result

# 牌背
def find_itemType14(directory):
    pattern = r'tiletexture_majinagzi_heap_(\d+)'
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 14:
            equipID = item['ItemID']
    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            itemID = match.groups()
            result.append({
                "expiredAt": 0,
                "feelValue": 0,
                "giftContent": [],
                "isCanEquip": True,
                "isEquip": equipID == int(itemID[0]), # Check if the item is equipped
                "isExpired": False,
                "isLock": False,
                "itemID": int(itemID[0]),
                "itemType": 14,
                "label": 0,
                "num": 1,
                "recycleNum": 0,
                "source": 0
            })

    return result

def find_itemType15(directory):
    pattern = r'desktexture_(\d+)'
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 15:
            equipID = item['ItemID']

    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            itemID = match.groups()
            result.append({
                "expiredAt": 0,
                "feelValue": 0,
                "giftContent": [],
                "isCanEquip": True,
                "isEquip": equipID == int(itemID[0]),
                "isExpired": False,
                "isLock": False,
                "itemID": int(itemID[0]),
                "itemType": 15,
                "label": 0,
                "num": 1,
                "recycleNum": 0,
                "source": 0
            }) 

    return result

def find_itemType16(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 16:
            equipID = item['ItemID']

    for i in range(1, 18):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+16000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+16000,
            "itemType": 16,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType17(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 17:
            equipID = item['ItemID']

    for i in range(1, 7):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+17000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+17000,
            "itemType": 17,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType18(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 18:
            equipID = item['ItemID']

    for i in range(1, 6):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+18000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+18000,
            "itemType": 18,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType19(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 19:
            equipID = item['ItemID']

    for i in range(1, 5):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+19000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+19000,
            "itemType": 19,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType20(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 20:
            equipID = item['ItemID']

    for i in range(1, 5):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+20000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+20000,
            "itemType": 20,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType22(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 22:
            equipID = item['ItemID']

    for i in range(1, 2):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+22000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+22000,
            "itemType": 22,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType24(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 24:
            equipID = item['ItemID']

    for i in range(1, 5):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+24000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+24000,
            "itemType": 24,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType25(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 25:
            equipID = item['ItemID']

    for i in range(1, 5):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": True,
            "isEquip": equipID == int(i+25000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+25000,
            "itemType": 25,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType26(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 26:
            equipID = item['ItemID']

    for i in range(1, 4):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": False,
            "isEquip": equipID == int(i+26000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+26000,
            "itemType": 26,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType27(directory):
    pattern = None # I don't know the pattern for this one
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 27:
            equipID = item['ItemID']

    for i in range(1, 4):
        result.append({
            "expiredAt": 0,
            "feelValue": 0,
            "giftContent": [],
            "isCanEquip": False,
            "isEquip": equipID == int(i+27000),
            "isExpired": False,
            "isLock": False,
            "itemID": i+27000,
            "itemType": 27,
            "label": 0,
            "num": 1,
            "recycleNum": 0,
            "source": 0
        })

    return result

def find_itemType30(directory):
    pattern = r'avatarframe_(\d+)'
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 30:
            equipID = item['ItemID']

    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            itemID = match.groups()
            result.append({
                "expiredAt": 0,
                "feelValue": 0,
                "giftContent": [],
                "isCanEquip": True,
                "isEquip": equipID == int(itemID[0]),
                "isExpired": False,
                "isLock": False,
                "itemID": int(itemID[0]),
                "itemType": 30,
                "label": 0,
                "num": 1,
                "recycleNum": 0,
                "source": 0
            })

    return result

def find_itemType36(directory):
    pattern = r'deskedge_(\d+)'
    result = []
    equipID = 0
    for item in userEquip['data']:
        if item['ItemType'] == 36:
            equipID = item['ItemID']

    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            itemID = match.groups()
            result.append({
                "expiredAt": 0,
                "feelValue": 0,
                "giftContent": [],
                "isCanEquip": True,
                "isEquip": equipID == int(itemID[0]),
                "isExpired": False,
                "isLock": False,
                "itemID": int(itemID[0]),
                "itemType": 36,
                "label": 0,
                "num": 1,
                "recycleNum": 0,
                "source": 0
            })

    return result

def generateUserItemList(OriginalUserItemList):
    userItemList = {
        "code": 0,
        "data": [],
        "message": "ok"
    }

    for item in OriginalUserItemList['data']:
        if item['itemType'] in [13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 27, 30, 36]:
            OriginalUserItemList['data'].remove(item)
    userItemList['data'] = OriginalUserItemList['data']

    directory="D:\Riichi_City\Mahjong-JP_Data\StreamingAssets"
    item13 = find_itemType13(directory)
    userItemList['data'] += item13
    item15 = find_itemType15(directory)
    userItemList['data'] += item15
    item14 = find_itemType14(directory)
    userItemList['data'] += item14
    item16 = find_itemType16(directory)
    userItemList['data'] += item16
    item17 = find_itemType17(directory)
    userItemList['data'] += item17
    item18 = find_itemType18(directory)
    userItemList['data'] += item18
    item19 = find_itemType19(directory)
    userItemList['data'] += item19
    item20 = find_itemType20(directory)
    userItemList['data'] += item20
    item22 = find_itemType22(directory)
    userItemList['data'] += item22
    item24 = find_itemType24(directory)
    userItemList['data'] += item24
    item25 = find_itemType25(directory)
    userItemList['data'] += item25
    item26 = find_itemType26(directory)
    userItemList['data'] += item26
    item27 = find_itemType27(directory)
    userItemList['data'] += item27
    item30 = find_itemType30(directory)
    userItemList['data'] += item30
    item36 = find_itemType36(directory)
    userItemList['data'] += item36

    return userItemList