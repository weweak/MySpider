# coding=utf-8

import requests
import xlwt
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import HTTPError


class LGSpider(object):
    def __init__(self):
        self.target_city = [u"深圳", u"杭州", u"上海", u"北京"]  # 初始化待爬城市列表
        self.job_info = []                                          # 储存爬取招聘信息
        self.target_page = 30                                       # 设定该城市下爬取得招聘信息页面数

    # 爬虫主调度程序
    def craw(self):
        for city in self.target_city:
            flag = True
            page = 0
            while flag:
                company_ids_list, flag = self.get_company_ids(city, page)
                self.get_detail_info(company_ids_list)
                page += 1
                print u"正在获取%s第%s页招聘页面地址" % (city, page)
                if page == self.target_page:
                    break
            break
        self.out_puter()

    # 接受城市，页面序数参数，返回该城市python职位当前页面的招聘公司id的列表，以及是否有下一页
    def get_company_ids(self, city, page):
        date = {"first": "false", "pn": page, "kd": "python"}
        params = {"px": "default", "city": city}
        r = requests.post("http://www.lagou.com/jobs/positionAjax.json", data=date, params=params)
        cont = r.json()["content"]["result"]
        company_ids = []
        for i in cont:
            for k in i:
                if k == "positionId":
                    company_ids.append(i[k])

        return company_ids, r.json()["content"]["hasNextPage"]

    # 接受多个城市id的列表作为输入，补全地址，下载公司详情页，并分析内容，将每一条公司招聘详情信息储存
    def get_detail_info(self, com_ids):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}
        for com_id in com_ids:
            if not com_id:
                return
            else:
                try:
                    r = requests.get("http://www.lagou.com/jobs/" + str(com_id) + ".html", headers=headers)
                    bs_obj = BeautifulSoup(r.text, "html.parser")
                    this_com_info = {
                        "company_name": bs_obj.find("dl", attrs={"class": "job_company"}).find("img")["alt"],
                        "company_describe": bs_obj.find("dl", attrs={"class": "job_company"}).find("dd").get_text(),
                        "language": "Python",
                        "job_request": bs_obj.find("dd", attrs={"class": "job_request"}).get_text(),
                        "job_describe": bs_obj.find("dd", attrs={"class": "job_bt"}).get_text()}
                    self.job_info.append(this_com_info)
                except HTTPError, e:
                    print e

    # 用于将收集的招聘数据保存，接受一个招聘信息的列表，将信息储存在当前目录新建的一个excel文件中
    def out_puter(self):
        myfile = xlwt.Workbook()
        sheet = myfile.add_sheet("sheet1", cell_overwrite_ok=True)
        row = 0
        for com_info in self.job_info:
            sheet.write(row, 0, com_info["company_name"])
            sheet.write(row, 1, com_info["language"])
            sheet.write(row, 2, com_info["job_request"])
            sheet.write(row, 3, com_info["job_describe"])
            sheet.write(row, 4, com_info["company_describe"])
            print u"正在储存" + com_info["company_name"] + u"发布的招聘信息"
            row += 1
        myfile.save("lagou.xls")

if __name__ == "__main__":
    obj_spider = LGSpider()
    obj_spider.craw()
