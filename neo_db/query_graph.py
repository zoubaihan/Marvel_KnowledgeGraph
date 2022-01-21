from neo_db.config import graph, CA_LIST, similar_words
import base64
import sys
sys.path.append('..')
from spider.show_profile import get_profile
from KGQA.util.log_util import LogUtil
logutil = LogUtil()

def query(name):
    data = graph.run(
    "match(p )-[r]->(n:Person{Name:'%s'}) return  p.Name,r.relation,n.Name,p.cate,n.cate\
        Union all\
    match(p:Person {Name:'%s'}) -[r]->(n) return p.Name, r.relation, n.Name, p.cate, n.cate" % (name,name)
    )
    data = list(data)
    return get_json_data(data)

def get_json_data(data):
    json_data={'data':[],"links":[]}
    d = []
    
    
    for i in data:
        d.append(i['p.Name']+"_"+i['p.cate'])
        d.append(i['n.Name']+"_"+i['n.cate'])
        d = list(set(d))
    name_dict={}
    count = 0
    for j in d:
        j_array = j.split("_")
    
        data_item={}
        name_dict[j_array[0]]=count
        count += 1
        data_item['name']=j_array[0]
        data_item['category']=CA_LIST[j_array[1]]
        json_data['data'].append(data_item)
    for i in data:
   
        link_item = {}
        
        link_item['source'] = name_dict[i['p.Name']]
        
        link_item['target'] = name_dict[i['n.Name']]
        link_item['value'] = i['r.relation']
        json_data['links'].append(link_item)

    return json_data


def get_KGQA_answer(array):
    
    replace_dict={
     "女巫": "绯红女巫",
     "队长": "美国队长",
     "辣椒": "小辣椒",
     "博士": "奇异博士",
     "男爵": "斯特拉克男爵",
     "巨人": "绿巨人",
     "托尼": "钢铁侠",
     "托尼史塔克": "钢铁侠",
     "旺达": "绯红女巫",
     "浩克": "绿巨人"
     }
    for i in range(len(array)):
        if array[i] in replace_dict.keys():
            array[i] = replace_dict[array[i]]
    if(len(array) == 2):
        array.append(array[0])
        array[0], array[1] = array[1], array[0]
    last_num = 0
    all_num = 0
    data_array = []
    for i in range(len(array)-2):
        now_data = []
        if i == 0:
            name = array[0]
            cypher = "match(p)-[r:%s{relation: '%s'}]->(n:Person{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (
                similar_words[array[i + 1]], similar_words[array[i + 1]], name)
            log = "cypher语句是：" + cypher
            logutil.info(log)
            data = graph.run(cypher)
            data = list(data)
            now_data = data
            last_num = len(now_data)
            all_num = all_num + last_num
        else:
            for j in range(last_num):
                name = data_array[j]['p.Name']
                cypher = "match(p)-[r:%s{relation: '%s'}]->(n:Person{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (
                    similar_words[array[i + 1]], similar_words[array[i + 1]], name)
                log = "cypher语句是：" + cypher
                logutil.info(log)
                data = graph.run(cypher)
                data = list(data)
                now_data.extend(data)
            last_num = len(now_data)
            all_num = all_num + last_num
        data_array = now_data
    print("实体数目: ", len(data_array))
    with open("./spider/images/"+"%s.jpg" % (str(data_array[-1]['p.Name'])), "rb") as image:
            base64_data = base64.b64encode(image.read())
            b = str(base64_data)
    logutil.info(data_array)
    return [get_json_data(data_array), get_profile(str(data_array[-1]['p.Name'])), b.split("'")[1]]


def get_KGQA_answer_all(array):
    replace_dict = {
        "女巫": "绯红女巫",
        "队长": "美国队长",
        "辣椒": "小辣椒",
        "博士": "奇异博士",
        "男爵": "斯特拉克男爵",
        "巨人": "绿巨人",
        "托尼": "钢铁侠",
        "托尼史塔克": "钢铁侠",
        "旺达": "绯红女巫",
        "浩克": "绿巨人"
    }
    for i in range(len(array)):
        if array[i] in replace_dict.keys():
            array[i] = replace_dict[array[i]]
    if (len(array) == 2):
        array.append(array[0])
        array[0], array[1] = array[1], array[0]

    last_num = 0
    all_num = 0
    data_array = []
    final_array = []
    for i in range(len(array) - 2):
        now_data = []
        if i == 0:
            name = array[0]
            cypher = "match(p)-[r:%s{relation: '%s'}]->(n:Person{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (
                similar_words[array[i + 1]], similar_words[array[i + 1]], name)
            log = "cypher语句是：" + cypher
            logutil.info(log)
            data = graph.run(cypher)
            data = list(data)
            now_data = data
            last_num = len(now_data)
            all_num = all_num + last_num
        else:
            for j in range(last_num):
                name = data_array[j]['p.Name']
                cypher = "match(p)-[r:%s{relation: '%s'}]->(n:Person{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (
                    similar_words[array[i + 1]], similar_words[array[i + 1]], name)
                log = "cypher语句是：" + cypher
                logutil.info(log)
                data = graph.run(cypher)
                data = list(data)
                now_data.extend(data)
            last_num = len(now_data)
            all_num = all_num + last_num
        data_array = now_data
        final_array.extend(data_array)
    data_array = final_array
    print("实体数目: ", len(data_array))
    with open("./spider/images/" + "%s.jpg" % (str(data_array[-1]['p.Name'])), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)
    logutil.info(data_array)
    return [get_json_data(data_array), get_profile(str(data_array[-1]['p.Name'])), b.split("'")[1]]


def get_answer_profile(name):
    with open("./spider/images/"+"%s.jpg" % (str(name)), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)
    return [get_profile(str(name)), b.split("'")[1]]
        



