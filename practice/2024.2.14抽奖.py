import random
import time
import os
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED,FIRST_COMPLETED, as_completed

# 最多加抽10次，失败和成功分别依次按照 100 80 60 40 20百分比递减和增加
money_set = {128,138,158,168,178,188,198,
             218,238,248,250,268,278,288,
             328,338,358,368,378,388,
             418,428,438,468,478,488,
             518,538,558,520,568,588,
             618,638,666,688,
             739,758,788,
             888,866,
             998}
# https://blog.51cto.com/u_16175468/6947026
# random_elements = random.sample(list(money_set), 1)
# random_elements = random.choice(list(money_set))

def random_choice(param):
    num_list = list(param[0])
    random_elements = -1
    while True:
        if param[1]:
            break
        random_elements = random.choice(num_list)
        print("\r%d ￥" % random_elements, end="")
        time.sleep(0.1) # 休眠，单位秒
    return random_elements

last_money = []
choice_money = []
compare_ret = []
ratio_ret = []
now_money = []
choice_times = 0
change_ratio = [1, 1, 0.8, 0.6, 0.4, 0.2, 0]
incr_times = 0
decr_times = 0
CHOICE_MAX_NUM = 10

def print_result():
    indentation = 8
    # def print_line():
    #     print("╔══════╦", end = "")
    #     for i in range(0, CHOICE_MAX_NUM):
    #         print("═════╦", end = "")
    #     print("═════╗", end = "")
    #     print("")
    # def print_times():
    #     print("║ 轮次 ║", end = "")
    #     for i in range(0, CHOICE_MAX_NUM+1):
    #         print(" %-3s ║" % i, end = "")
    #     print("")
    def print_header_line():
        print("%*s" % (indentation, ""), end = "")
        print("┏━━━━━━━━━━┳", end = "")
        for i in range(0, CHOICE_MAX_NUM):
            print("━━━━━┳", end = "")
        print("━━━━━┓", end = "")
        print("")
    def print_middle_line():
        print("%*s" % (indentation, ""), end = "")
        print("┣━━━━━━━━━━╋", end = "")
        for i in range(0, CHOICE_MAX_NUM):
            print("━━━━━╋", end = "")
        print("━━━━━┫", end = "")
        print("")
    def print_footer_line():
        print("%*s" % (indentation, ""), end = "")
        print("┗━━━━━━━━━━┻", end = "")
        for i in range(0, CHOICE_MAX_NUM):
            print("━━━━━┻", end = "")
        print("━━━━━┛", end = "")
        print("")
    def print_times():
        print("%*s" % (indentation, ""), end = "")
        print("┃   轮次   ┃", end = "")
        for i in range(0, CHOICE_MAX_NUM+1):
            print(" %-3s ┃" % i, end = "")
        print("")
    def print_now_money():
        print("%*s" % (indentation, ""), end = "")
        print("┃ 当前金额 ┃", end = "")
        for i in range(0, CHOICE_MAX_NUM+1):
            if i < len(last_money):
                print(" %-3s ┃" % last_money[i], end = "")
            else:
                print(" %-3s ┃" % "", end = "")
        print("")
    def print_choice_money():
        print("%*s" % (indentation, ""), end = "")
        print("┃ 抽取金额 ┃", end = "")
        for i in range(0, CHOICE_MAX_NUM+1):
            if i < len(choice_money):
                print(" %-3d ┃" % choice_money[i], end = "")
            else:
                print(" %-3s ┃" % "", end = "")
        print("")
    def print_compare_result():
        print("%*s" % (indentation, ""), end = "")
        print("┃ 对比结果 ┃", end = "")
        for i in range(0, CHOICE_MAX_NUM+1):
            if i < len(compare_ret):
                print(" %-3s ┃" % compare_ret[i], end = "")
            else:
                print(" %-3s ┃" % "", end = "")
        print("")
    def print_ratio_result():
        print("%*s" % (indentation, ""), end = "")
        print("┃ 改变比例 ┃", end = "")
        for i in range(0, CHOICE_MAX_NUM+1):
            if i < len(ratio_ret):
                print(" %-3s ┃" % ratio_ret[i], end = "")
            else:
                print(" %-3s ┃" % "", end = "")
        print("")
    def print_acquire_money():
        print("%*s" % (indentation, ""), end = "")
        print("┃ 获得金额 ┃", end = "")
        for i in range(0, CHOICE_MAX_NUM+1):
            if i < len(now_money):
                print(" %-3d ┃" % now_money[i], end = "")
            else:
                print(" %-3s ┃" % "", end = "")
        print("")
    print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
    print("                                         2024 小金金的抽奖之旅")
    print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
    print("规则：")
    print("1. 第一次抽奖，结果作为初始金额")
    print("2. 之后最多可以抽取10次，根据抽取金额和当前金额，按【比例】改变获得金额")
    print("\ta. 抽取金额的比例依次设置为[100%, 80%, 60%, 40%, 20%]")
    print("\tb. 若抽取金额比当前金额大，成为【递增抽取】，否则成为【递减抽取】")
    print("\tc.【递增抽取】和【递减抽取】分别统计次数，根据次数对应选择列表的比例进行计算")
    print("3. 例子：当前金额为a，抽取金额为b，：")
    print("\ta. 若b > a, 当前是第2次的【递增抽取】，对应比例为80%，则获得金额为 a*20%% + b*80%%")
    print("4. 【递增抽取】或【递减抽取】次数达到6次，则抽奖结束，当前抽奖结果丢弃，上轮的获得金额作为最终金额")
    print("\ta. 因此，最多可以抽取10次（不包括初始次数），即【递增抽取】和【递减抽取】分别5次")
    print("5. 重点！！！可以选择两种玩法：")
    print("\ta. 只进行【1】场次抽奖，玩家可以【中途选择终止】，将当年的获得金额带走")
    print("\tb. 进行【3】场次抽奖，玩家【不能中途终止】，直到场次结束。3场次中取最高金额作为最终金额")
    print("\n看好规则！！！抽奖就要开始啦！！！")
    print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
    print("")

    print_header_line()
    print_times()
    print_middle_line()
    print_now_money()
    print_middle_line()
    print_choice_money()
    print_middle_line()
    print_compare_result()
    print_middle_line()
    print_ratio_result()
    print_middle_line()
    print_acquire_money()
    print_footer_line()
    print("◎ 【递增抽取】次数: %d" % incr_times)
    print("◎ 【递减抽取】次数: %d" % decr_times)
    print("◎ 【总的抽取】次数: %d" % choice_times)
    print("◎ 【获得金额】    : %d" % (0 if len(now_money) == 0 else now_money[-1]))
    print("◎ 奖池剩余金额个数: %d" % len(money_set))


def cal_money(choice_ret):
    global choice_times, incr_times, decr_times
    if choice_times == 0:
        last_money.append("")
        choice_money.append(choice_ret)
        compare_ret.append("")
        ratio_ret.append("")
        now_money.append(choice_ret)
    else:
        last = now_money[-1]
        last_money.append(last)
        choice_money.append(choice_ret)
        ratio = 0
        if choice_ret > last:
            incr_times += 1
            ratio = change_ratio[incr_times]
            compare_ret.append(">")
        else:
            decr_times += 1
            ratio = change_ratio[decr_times]
            compare_ret.append("<")
        ratio_ret.append(ratio)
        now = int(last * (1 - ratio) + choice_ret * ratio)
        now_money.append(now)
    choice_times += 1

if __name__ == "__main__":
    pool= ThreadPoolExecutor(max_workers=1)
    param = [money_set, False]
    while True:
        os.system("clear")
        print_result()
        print("⊕ 抽取金额(按任意键停止...):")
        param[1] = False
        future_result = pool.submit(random_choice, param)
        input()
        param[1] = True
        choice_ret = future_result.result()
        print("抽取金额为: %d ￥" % choice_ret)
        money_set.remove(choice_ret)
        cal_money(choice_ret)
        if incr_times > CHOICE_MAX_NUM / 2 or decr_times > CHOICE_MAX_NUM / 2:
            break
    print_result()
    print("")
    print("⊕ 最终金额: %d ￥" % now_money[-1])
    print("恭喜小金金，获得大红包！！！")
    print("")
