import time
import sys
import itertools
import random

# Setting (Don't edit it, edit it if you change something.)
EFFECTS = {
    "bold": "\033[1m",
    "underline": "\033[4m",
    "blink": "\033[5m",
}
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m",
}
# 
def text_color(text, color="white"):
    color_code = COLORS.get(color.lower(), COLORS["white"])
    print(color_code + text + COLORS["reset"])

def typing_effect(text, delay=0.05, color="white"):
    color_code = COLORS.get(color.lower(), COLORS["white"])
    sys.stdout.write(color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(COLORS["reset"])

def print_banner(text, border="*"):
    length = len(text) + 4
    print(border * length)
    print(f"{border} {text} {border}")
    print(border * length)

def typing(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

def rainbow_text(text):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }
    
    color_list = ["red", "green", "yellow", "blue", "purple", "cyan"]
    
    result = "".join(f"{colors[color_list[i % len(color_list)]]}{char}" for i, char in enumerate(text))
    
    sys.stdout.write(result + colors["reset"] + "\n")  # In tất cả trên một dòng và reset màu
    sys.stdout.flush()

def wave_text(text, delay=0.1, repeat=3):
    """Hiệu ứng sóng chữ (di chuyển qua lại mượt mà, không lỗi)."""
    width = len(text) + 10
    for _ in range(repeat):
        for i in range(width):
            sys.stdout.write("\r" + " " * i + text + " " * (width - i))
            sys.stdout.flush()
            time.sleep(delay)
        for i in range(width, 0, -1):
            sys.stdout.write("\r" + " " * i + text + " " * (width - i))
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\r" + " " * (width + len(text)) + "\r")
    sys.stdout.flush()

def fancy_text(text, style=0):
    styles = [
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"),
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"),
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"),
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"),
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"),
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"),
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"),
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉")
    ]

    if 0 <= style < len(styles):
        return text.translate(styles[style])
    else:
        return text  # Nếu style không hợp lệ, trả về text bình thường

def vertical_text_with_bars(text):
    """ Hiển thị chữ theo dạng cột dọc với ký tự | ở hai bên """
    lines = [list(word) for word in text.split()]
    max_len = max(len(word) for word in lines)

    # Làm cho tất cả từ có cùng độ dài bằng cách thêm khoảng trắng
    for word in lines:
        while len(word) < max_len:
            word.append(" ")

    # Xoay chữ thành cột dọc và thêm dấu |
    result = "\n".join("| " + " ".join(row) + " |" for row in zip(*lines))

    return result
def programe_bar_effect(text='Test', max_length=10):
    for lenght in range(max_length+1):
        sys.stdout.write('\r'+f'{text}'+': '+'['+'0'*lenght + ' '*(max_length-lenght) + ']')
        sys.stdout.flush()
        time.sleep(random.randint(0, 5))
    print(f'{text}'+': '+'Success')