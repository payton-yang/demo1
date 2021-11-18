import re
import os
import sys
import time
import urllib.parse
from requests_html import HTMLSession

session = HTMLSession()


def likes_200():
    resp = session.get('https://tieba.baidu.com/mo/q/newmoindex', headers=header)
    if resp.status_code == 200:
        data = resp.json()
        likes = data['data']['like_forum']
        likes_filter = list(filter(lambda x: x['is_sign'] == 0, likes))
        return [x['forum_name'] for x in likes_filter]
    return []


def likes_last():
    t = int(round(time.time() * 1000))
    url = 'http://tieba.baidu.com/f/like/mylike'
    resp = session.get(url, params={'v': t}, headers=header)
    if resp.status_code == 200:
        _as = resp.html.xpath('//*[@id="j_pagebar"]/div/a/@href')
        last_page = int(_as[-1].split('=')[1])
        likes = []
        if last_page > 10:
            for i in range(11, last_page + 1):
                params = {
                    'v': t,
                    'pn': i
                }
                resp = session.get(url, params=params, headers=header)
                if resp.status_code == 200:
                    spans = resp.html.xpath('/html/body/div[1]/div[1]/table/tr/td/span')
                    for x in spans:
                        name = urllib.parse.unquote(x.attrs['balvname'], encoding='gbk')
                        likes.append(name)
        return likes


def all_likes():
    likes = likes_200()
    last_likes = likes_last()
    likes.extend(last_likes)
    return likes


def get_tbs(kw):
    """
    Args:
        kw: 吧名

    Returns: tbs是每一个页面的随机值
    """
    url = f'https://tieba.baidu.com/f?kw={kw}'
    resp = session.get(url, headers=header)
    re_result = re.findall('tbs(.*)};', resp.text)
    regex = r'"(.*)"'
    tbs = re.findall(regex, re_result[0])[0]
    return tbs


def sign(kw, tbs):
    url = 'https://tieba.baidu.com/sign/add'
    data = {
        'ie': 'utf-8',
        'kw': kw,
        'tbs': tbs
    }
    resp = session.post(url, data=data, headers=header)
    if resp.status_code == 200:
        data = resp.json()
        if data['error']:
            return False
        if data['data'].get('errmsg', '') == 'success':
            return True
    return False


def get_header():
    stoken = os.getenv('STOKEN')
    bduss = os.getenv('BDUSS')
    header = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Host": "tieba.baidu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Cookie": f"BDUSS={bduss}; STOKEN={stoken}"
    }
    return header


if __name__ == '__main__':
    header = get_header()
    try:
        kws = all_likes()
    except Exception as e:
        print(e.__repr__())
        print('get likes tieba failed')
        sys.exit()
    sign_failure = []
    n = 0
    for kw in kws:
        n += 1
        if (n % 6) == 0:
            time.sleep(0.05)
        try:
            tbs = get_tbs(kw)
            flag = sign(kw, tbs)
            if flag:
                print(kw)
        except Exception as e:
            sign_failure.append(kw)
            continue
    for kw in sign_failure:
        try:
            tbs = get_tbs(kw)
            flag = sign(kw, tbs)
            if flag:
                print(kw)
                continue
            print(f'sign failure: {kw}')
        except Exception as e:
            print(e.__repr__())
            continue
