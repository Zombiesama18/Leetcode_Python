"""
468. 验证IP地址
给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；
如果不是上述类型的 IP 地址，返回 "Neither" 。
有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中 0 <= xi <= 255 且 xi 不能包含 前导零。
例如: “192.168.1.1” 、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “192.168@1.1” 为无效IPv4地址。
一个有效的IPv6地址 是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中:
1 <= xi.length <= 4
xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。
在 xi 中允许前导零。
例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7334" 是有效的 IPv6 地址，
而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 是无效的 IPv6 地址。
"""


def validIPAddress(queryIP: str) -> str:
    if '.' in queryIP:
        groups = queryIP.split('.')
        if len(groups) != 4:
            return 'Neither'
        for group in groups:
            if not (1 <= len(group) <= 3):
                return 'Neither'
            thisNumber = 0
            for char in group:
                if not char.isdigit():
                    return 'Neither'
                thisNumber = thisNumber * 10 + int(char)
            if not (0 <= thisNumber <= 255) or len(str(thisNumber)) != len(group):
                return 'Neither'
        return 'IPv4'
    if ':' in queryIP:
        groups = queryIP.split(':')
        if len(groups) != 8:
            return 'Neither'
        for group in groups:
            if not (1 <= len(group) <= 4):
                return 'Neither'
            for char in group:
                if not ('0' <= char <= '9' or 'a' <= char <= 'f' or 'A' <= char <= 'F'):
                    return 'Neither'
        return 'IPv6'
    return 'Neither'


