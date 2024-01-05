from mitmproxy import http, websocket
from mitmproxy.http import Headers
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box
from rich.panel import Panel
import json
import generateUserItemList
console = Console()

class Unlocker:
    def __init__(self):
        self.current_role = 10001
        self.current_skin = 0
        self.current_userEquip = {}
        self.current_userID = -1
        self.current_frame = 30000
        self.current_title = 0
        with open('setting.json', 'r') as f:
            setting = json.load(f)
            self.current_role = setting['role']
            self.current_skin = setting['skin']
            self.current_userEquip = setting['userEquip']
            self.current_title = setting['title']
            for item in self.current_userEquip['data']:
                if item['ItemType'] == 30:
                    self.current_frame = item['ItemID']
                    break


    def request(self, flow: http.HTTPFlow):
        assert flow.request
        if flow.request.method == "POST":
            if flow.request.path == "/users/updateRoleInfo":
                updateRoleInfo = json.loads(flow.request.content.decode("utf-8"))
                self.current_role = updateRoleInfo['roleID']
                self.current_skin = updateRoleInfo['skinID']
                with open('setting.json', 'r') as f:
                    setting = json.load(f)
                with open('setting.json', 'w') as f:
                    setting['role'] = self.current_role
                    setting['skin'] = self.current_skin
                    json.dump(setting, f)

                updateRoleInfo['roleID'] = 10001
                updateRoleInfo['skinID'] = 0
                dumpupdateRoleInfo = json.dumps(updateRoleInfo)
                flow.request.content = dumpupdateRoleInfo.encode("utf-8")

            if flow.request.path == "/backpack/equipItem":
                equipItem = json.loads(flow.request.content.decode("utf-8"))
                # Save the itemID to setting.json
                with open('setting.json', 'r') as f:
                    setting = json.load(f)
                with open('setting.json', 'w') as f:
                    for item in setting['userEquip']['data']:
                        if item['ItemType'] == equipItem['itemID']//1000:
                            item['ItemID'] = equipItem['itemID']
                            break
                    json.dump(setting, f)
                equipItem['itemID'] = 13001
                dumpEquipItem = json.dumps(equipItem)
                flow.request.content = dumpEquipItem.encode("utf-8")

            if flow.request.path == "/users/updateTitle":
                updateTitle = json.loads(flow.request.content.decode("utf-8"))
                self.current_title = updateTitle['titleID']
                with open('setting.json', 'r') as f:
                    setting = json.load(f)
                with open('setting.json', 'w') as f:
                    setting['title'] = self.current_title
                    json.dump(setting, f)
                updateTitle['titleID'] = 0
                dumpUpdateTitle = json.dumps(updateTitle)
                flow.request.content = dumpUpdateTitle.encode("utf-8")


    def response(self, flow: http.HTTPFlow):
        assert flow.response
        if flow.request.method == "POST":
            if flow.request.path == "/users/getRoleInfo":
                RoleInfo = json.loads(flow.response.content.decode("utf-8"))
                for role in RoleInfo['data']['roleList']:
                    role['isCanGet'] = True
                    role['isOwn'] = True
                    role['FeelValue'] = 10000
                    role['cultivateStatus'] = 5
                    role['exp'] = 99999
                    role['oathValue'] = 99999
                RoleInfo['data']['useRoleID'] = self.current_role
                RoleInfo['data']['useSkinID'] = self.current_skin
                dumpRoleInfo = json.dumps(RoleInfo)
                flow.response.content = dumpRoleInfo.encode("utf-8")

            if flow.request.path == "/users/getSkinInfo":
                SkinInfo = json.loads(flow.response.content.decode("utf-8"))
                for skin in SkinInfo['data']:
                    skin['expirationTime'] = 0
                    skin['isCanGet'] = True
                    skin['isOwn'] = True
                    skin['ownemoticon'] = True
                dumpSkinInfo = json.dumps(SkinInfo)
                flow.response.content = dumpSkinInfo.encode("utf-8")

            if flow.request.path == "/users/userBaseData":
                UserBaseData = json.loads(flow.response.content.decode("utf-8"))
                UserBaseData['data']['roleID'] = self.current_role
                UserBaseData['data']['skinID'] = self.current_skin
                UserBaseData['data']['titleID'] = self.current_title
                dumpUserBaseData = json.dumps(UserBaseData)
                flow.response.content = dumpUserBaseData.encode("utf-8")
        
            if flow.request.path == "/backpack/userItemList":
                UserItemList = json.loads(flow.response.content.decode("utf-8"))
                UserItemList = generateUserItemList.generateUserItemList(UserItemList)
                dumpUserItemList = json.dumps(UserItemList)
                flow.response.content = dumpUserItemList.encode("utf-8")

            if flow.request.path == "/backpack/userEquip":
                UserEquip = json.loads(flow.response.content.decode("utf-8"))
                UserEquip = self.current_userEquip
                dumpUserEquip = json.dumps(UserEquip)
                flow.response.content = dumpUserEquip.encode("utf-8")

            if flow.request.path == "/lobbys/enterFriendMatch":
                enterFriendMatch = json.loads(flow.response.content.decode("utf-8"))
                for player in enterFriendMatch['data']['players']:
                    if player['userID'] == self.current_userID:
                        player['roleId'] = self.current_role
                        player['skinId'] = self.current_skin
                        player['titleID'] = self.current_title

                        console.print(f"[bold green]Player {player['userID']} is you[/bold green]")
                dumpEnterFriendMatch = json.dumps(enterFriendMatch)
                flow.response.content = dumpEnterFriendMatch.encode("utf-8")
                    
            if flow.request.path == "/users/emailLogin":
                emailLogin = json.loads(flow.response.content.decode("utf-8"))
                self.current_userID = emailLogin['data']['user']['id']

            if flow.request.path == "/backpack/userProfileFrame":
                userProfileFrame = json.loads(flow.response.content.decode("utf-8"))
                for item in self.current_userEquip['data']:
                    if item['ItemType'] == 30:
                        self.current_frame = item['ItemID']
                        break
                for frame in userProfileFrame['data']:
                    frame['isCanEquip'] = True
                    frame['isEquip'] = frame['itemID'] == self.current_frame
                    frame['isLock'] = False
                    frame['num'] = 1
                dumpUserProfileFrame = json.dumps(userProfileFrame)
                flow.response.content = dumpUserProfileFrame.encode("utf-8")

            if flow.request.path == "/users/homeUserData":
                homeUserData = json.loads(flow.response.content.decode("utf-8"))
                homeUserData['data']['profileFrameID'] = self.current_frame
                homeUserData['data']['roleID'] = self.current_role
                homeUserData['data']['skinID'] = self.current_skin
                dumpHomeUserData = json.dumps(homeUserData)
                flow.response.content = dumpHomeUserData.encode("utf-8")

            if flow.request.path == "/users/getTitleList":
                getTitleList = json.loads(flow.response.content.decode("utf-8"))
                for title in getTitleList['data']:
                    title['createAt'] = 1610000000
                    title['expiredAt'] = 0
                    title['requireTimes'] = 0
                    title['titleState'] = 1

                dumpGetTitleList = json.dumps(getTitleList)
                flow.response.content = dumpGetTitleList.encode("utf-8")
            
            if flow.request.path == "/lobbys/getFriendMatchInfo":
                getFriendMatchInfo = json.loads(flow.response.content.decode("utf-8"))
                for player in getFriendMatchInfo['data']['players']:
                    if player['userID'] == self.current_userID:
                        player['roleId'] = self.current_role
                        player['skinId'] = self.current_skin
                        player['titleID'] = self.current_title
                        console.print(f"[bold green]Player {player['userID']} is you[/bold green]")

                dumpGetFriendMatchInfo = json.dumps(getFriendMatchInfo)
                flow.response.content = dumpGetFriendMatchInfo.encode("utf-8")

            # ========================================
                
            if flow.request.path == '/users/updateRoleInfo':
                updateRoleInfo = {
                    "code": 0,
                    "data": True,
                    "message": "ok"
                }
                dumpupdateRoleInfo = json.dumps(updateRoleInfo)
                flow.response.content = dumpupdateRoleInfo.encode("utf-8")

            if flow.request.path == '/users/roleWearSkin':
                roleWearSkin = {
                    "code": 0,
                    "message": "ok"
                }
                dumproleWearSkin = json.dumps(roleWearSkin)
                flow.response.content = dumproleWearSkin.encode("utf-8")

    # ============================================================================

    def websocket_start(self, flow: http.HTTPFlow):
        pass

    def websocket_message(self, flow: http.HTTPFlow):
        # Riichi City Websocket Format:
        #               Msg Lenth                       id  type start
        # 0000000000 | <Msg Lenth> 00 0f 00 01 00 00 00 4a 00 01 01 7b   ...|.......J...{
        # 0000000010 | 22 6c 61 6e 67 22 3a 22 7a 68 2d 68 6b 22 2c 22   "lang":"zh-hk","
        # 0000000020 | 75 ..........
        assert isinstance(flow.websocket, websocket.WebSocketData)
        message = flow.websocket.messages[-1]
        content = message.content
        msg_len = int.from_bytes(content[:4], byteorder='big')
        msg = content[15:msg_len]
        if msg_len > 15:
            msg = json.loads(msg.decode("utf-8"))
        else:
            return
        if message.from_client == False:
            # From Server
            if 'cmd' in msg:
                if msg['cmd'] == 'cmd_friend_match_action':
                    if msg['data']['userID'] == self.current_userID:
                        msg['data']['roleId'] = self.current_role
                        msg['data']['skinId'] = self.current_skin
                        msg['data']['titleID'] = self.current_title
                if msg['cmd'] == 'cmd_enter_room':
                    console.log(self.current_userID)
                    with open('setting.json', 'r') as f:
                        setting = json.load(f)
                        for item in setting['userEquip']['data']:
                            if item['ItemType'] == 13:
                                riichi_stick_id = item['ItemID']
                            elif item['ItemType'] == 14:
                                card_back_id = item['ItemID']
                            elif item['ItemType'] == 15:
                                tablecloth_id = item['ItemID']
                            elif item['ItemType'] == 16:
                                special_effect_id = item['ItemID']
                            elif item['ItemType'] == 17:
                                riichi_effect_id = item['ItemID']
                            elif item['ItemType'] == 19:
                                game_music_id = item['ItemID']
                                match_music_id = item['ItemID']
                            elif item['ItemType'] == 20:
                                riichi_music_id = item['ItemID']
                            elif item['ItemType'] == 26:
                                card_face_id = item['ItemID']
                            elif item['ItemType'] == 36:
                                table_frame_id = item['ItemID']
                    for player in msg['data']['players']:
                        if player['user']['user_id'] == self.current_userID:
                            player['user']['role_id'] = self.current_role
                            player['user']['skin_id'] = self.current_skin
                            player['user']['title_id'] = self.current_title
                            player['user']['riichi_stick_id'] = riichi_stick_id
                            player['user']['card_back_id'] = card_back_id
                            player['user']['tablecloth_id'] = tablecloth_id
                            player['user']['special_effect_id'] = special_effect_id
                            player['user']['riichi_effect_id'] = riichi_effect_id
                            player['user']['game_music_id'] = game_music_id
                            player['user']['match_music_id'] = match_music_id
                            player['user']['riichi_music_id'] = riichi_music_id
                            player['user']['card_face_id'] = card_face_id
                            player['user']['table_frame_id'] = table_frame_id
                            player['user']['profile_frame_id'] = self.current_frame
                    
        dumpMsg = json.dumps(msg)
        dumpMsgEncoded = dumpMsg.encode("utf-8")
        dumpMsgLength = len(dumpMsgEncoded) + 15
        dumpMsgLength = dumpMsgLength.to_bytes(4, byteorder='big')
        message.content = dumpMsgLength + content[4:15] + dumpMsgEncoded


        # console.log(msg)
        pass

    def websocket_end(self, flow: http.HTTPFlow):
        pass

sponsor_message = Table.grid(padding=1)
sponsor_message.add_column(style="green", justify="right")
sponsor_message.add_column(no_wrap=True)

sponsor_message.add_row(
    "MajsoulUnlocker",
    "[u blue link=https://github.com/shinkuan/MajsoulUnlocker]https://github.com/shinkuan/MajsoulUnlocker",
)
sponsor_message.add_row(
    "RiichiCityUnlocker",
    "[u blue link=https://github.com/shinkuan/RiichiCityUnlocker]https://github.com/shinkuan/RiichiCityUnlocker",
)

intro_message = Text.from_markup(
        """\
I hope you enjoy using the MajsoulUnlocker!

MajsoulUnlocker is made by [link=https://github.com/shinkuan]shinkuan[/]

[link=https://github.com/shinkuan/MajsoulUnlocker/issues]Open an issue[/] if you have any questions."""
    )

message = Table.grid(padding=2)
message.add_column()
message.add_column(no_wrap=True)
message.add_row(intro_message, sponsor_message)

console.print(
    Panel.fit(
        message,
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b cyan]Thanks for using MajsoulUnlocker!",
        border_style="bright_blue",
    ),
    justify="center",
)


addons = [
    Unlocker()
]