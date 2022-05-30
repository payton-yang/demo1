import asyncio

import aiotieba as tb


async def main2():
    # 使用键名"default"对应的BDUSS创建客户端
    async with tb.Client("default") as brow:
        # 同时请求用户个人信息和asoul吧首页前30帖
        # asyncio.gather会为两个协程brow.get_self_info和brow.get_threads自动创建任务然后“合并”为一个协程
        # await释放当前协程持有的CPU资源并等待协程asyncio.gather执行完毕
        # 参考https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.gather
        user, threads = await asyncio.gather(brow.get_self_info(), brow.get_threads('asoul'))

    # 将获取的信息打印到日志
    tb.log.info(f"当前用户信息: {user}")
    for thread in threads:
        tb.log.info(f"tid: {thread.tid} 最后回复时间戳: {thread.last_time} 标题: {thread.title}")


"""
1. 获取所有关注的吧
2. 签到未签到的吧
"""


async def sign_all():
    async with tb.Client("default") as brow:
        ret = []
        pn = 2
        has_more = True
        while has_more:
            res_list, has_more = await brow.get_self_forum_list(pn)
            ret.extend(res_list)
            pn += 1
        print(f'关注贴吧数量：{len(ret)}')
        for x in ret:
            fname = x[0]
            flag = await brow.sign_forum(fname)
            if not flag:
                print(f'{fname}----{flag}')


async def main():
    await sign_all()


# 执行协程main
# 参考https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.run
asyncio.run(main())
