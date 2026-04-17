"""
Fox-OMS 电力行业测试数据初始化脚本
生成面向电力行业（国家电网/南方电网/省级电力公司）的测试数据
输出 CSV 文件到当前目录
"""
import csv
import uuid
import random
from datetime import date, timedelta
from pathlib import Path

OUT = Path(__file__).parent
random.seed(42)

def uid():
    return str(uuid.uuid4())

def d(year, month, day):
    return date(year, month, day).isoformat()

def rdate(start='2018-01-01', end='2024-12-31'):
    s = date.fromisoformat(start)
    e = date.fromisoformat(end)
    return (s + timedelta(days=random.randint(0, (e - s).days))).isoformat()

def write_csv(name, rows):
    if not rows:
        return
    path = OUT / f'{name}.csv'
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    print(f'  {name}.csv  ({len(rows)} rows)')

# ── IDs ─────────────────────────────────────────────────────────────────────

dept_ids   = {k: uid() for k in ['sales', 'biz', 'tech', 'hr', 'finance', 'pm']}
emp_ids    = {k: uid() for k in [
    'zhang_wei', 'li_na', 'wang_fang', 'chen_hao', 'zhao_min',
    'liu_yang', 'sun_jing', 'zhou_tao', 'wu_xia', 'zheng_lei',
    'xu_peng', 'he_rong', 'lin_kai', 'guo_hui', 'ma_li',
]}
emp_list   = list(emp_ids.values())

cust_ids   = {k: uid() for k in [
    'sgcc', 'csg', 'huaneng', 'datang', 'huadian',
    'hebei_ep', 'shandong_ep', 'jiangsu_ep', 'guangdong_ep', 'sichuan_ep',
    'siemens', 'abb', 'nari', 'sifang', 'xuji',
]}
prod_ids   = {k: uid() for k in [
    'p_dms', 'p_scada', 'p_gis', 'p_ems', 'p_ami',
    'p_pms', 'p_oa', 'p_big',
]}
opp_ids    = [uid() for _ in range(12)]
bidreg_ids = [uid() for _ in range(10)]
bidsub_ids = [uid() for _ in range(8)]
ctr_ids    = [uid() for _ in range(8)]
proj_ids   = [uid() for _ in range(6)]
contact_ids = [uid() for _ in range(20)]

# ── DEPARTMENT ───────────────────────────────────────────────────────────────

departments = [
    {'id': dept_ids['sales'],   'name': '市场销售部', 'dept_code': 'D001', 'dept_type': 'functional',
     'parent_id': '', 'leader_id': emp_ids['zhang_wei'],
     'establish_date': d(2015,1,1), 'sort_order': 1, 'status': 'active',
     'responsibilities': '负责市场开发、客户维护与商机管理', 'remark': '', 'created_at': d(2015,1,1)},
    {'id': dept_ids['biz'],     'name': '商务合同部', 'dept_code': 'D002', 'dept_type': 'functional',
     'parent_id': '', 'leader_id': emp_ids['li_na'],
     'establish_date': d(2015,1,1), 'sort_order': 2, 'status': 'active',
     'responsibilities': '负责合同谈判、签署及合规管理', 'remark': '', 'created_at': d(2015,1,1)},
    {'id': dept_ids['tech'],    'name': '技术研发部', 'dept_code': 'D003', 'dept_type': 'business_unit',
     'parent_id': '', 'leader_id': emp_ids['wang_fang'],
     'establish_date': d(2015,1,1), 'sort_order': 3, 'status': 'active',
     'responsibilities': '负责产品研发与技术支持', 'remark': '', 'created_at': d(2015,1,1)},
    {'id': dept_ids['hr'],      'name': '人力资源部', 'dept_code': 'D004', 'dept_type': 'functional',
     'parent_id': '', 'leader_id': emp_ids['chen_hao'],
     'establish_date': d(2015,1,1), 'sort_order': 4, 'status': 'active',
     'responsibilities': '负责招聘、培训与员工关系管理', 'remark': '', 'created_at': d(2015,1,1)},
    {'id': dept_ids['finance'], 'name': '财务管理部', 'dept_code': 'D005', 'dept_type': 'functional',
     'parent_id': '', 'leader_id': emp_ids['zhao_min'],
     'establish_date': d(2015,1,1), 'sort_order': 5, 'status': 'active',
     'responsibilities': '负责财务核算、成本控制与资金管理', 'remark': '', 'created_at': d(2015,1,1)},
    {'id': dept_ids['pm'],      'name': '项目管理部', 'dept_code': 'D006', 'dept_type': 'functional',
     'parent_id': '', 'leader_id': emp_ids['liu_yang'],
     'establish_date': d(2016,3,1), 'sort_order': 6, 'status': 'active',
     'responsibilities': '负责项目全生命周期管理与质量把控', 'remark': '', 'created_at': d(2016,3,1)},
]
write_csv('department', departments)

# ── EMPLOYEE ─────────────────────────────────────────────────────────────────

emp_data = [
    ('zhang_wei', '张伟', 'male',   dept_ids['sales'],   '销售总监',   'P5', '2016-03-01'),
    ('li_na',     '李娜', 'female', dept_ids['biz'],     '商务经理',   'P4', '2017-06-01'),
    ('wang_fang', '王芳', 'female', dept_ids['tech'],    '技术总监',   'P5', '2015-09-01'),
    ('chen_hao',  '陈浩', 'male',   dept_ids['hr'],      'HR经理',     'P4', '2018-01-01'),
    ('zhao_min',  '赵敏', 'female', dept_ids['finance'], '财务总监',   'P5', '2016-01-01'),
    ('liu_yang',  '刘洋', 'male',   dept_ids['pm'],      '项目总监',   'P5', '2016-06-01'),
    ('sun_jing',  '孙静', 'female', dept_ids['sales'],   '大客户经理', 'P3', '2019-03-01'),
    ('zhou_tao',  '周涛', 'male',   dept_ids['tech'],    '高级工程师', 'P4', '2018-07-01'),
    ('wu_xia',    '吴霞', 'female', dept_ids['sales'],   '销售工程师', 'P2', '2021-04-01'),
    ('zheng_lei', '郑磊', 'male',   dept_ids['biz'],     '商务专员',   'P2', '2022-01-01'),
    ('xu_peng',   '徐鹏', 'male',   dept_ids['tech'],    '研发工程师', 'P3', '2020-05-01'),
    ('he_rong',   '何蓉', 'female', dept_ids['pm'],      '项目经理',   'P3', '2019-09-01'),
    ('lin_kai',   '林凯', 'male',   dept_ids['sales'],   '销售经理',   'P3', '2018-11-01'),
    ('guo_hui',   '郭慧', 'female', dept_ids['biz'],     '合同专员',   'P2', '2021-08-01'),
    ('ma_li',     '马丽', 'female', dept_ids['tech'],    '实施工程师', 'P2', '2022-03-01'),
]

employees = []
for key, name, gender, dept, pos, rank, hire in emp_data:
    hire_d = date.fromisoformat(hire)
    prob_end = (hire_d + timedelta(days=90)).isoformat()
    reg_d = (hire_d + timedelta(days=90)).isoformat()
    employees.append({
        'id': emp_ids[key], 'name': name, 'emp_number': f'EMP{len(employees)+1:03d}',
        'gender': gender, 'id_card_no': '', 'phone': f'138{random.randint(10000000,99999999)}',
        'email': f'{key.replace("_",".")}@foxtech.com', 'department_id': dept,
        'position': pos, 'rank': rank, 'employment_status': 'active',
        'hire_date': hire, 'probation_end_date': prob_end, 'regularization_date': reg_d,
        'contract_end_date': (date.fromisoformat(hire) + timedelta(days=3*365)).isoformat(),
        'resignation_date': '', 'emergency_contact': '', 'emergency_phone': '',
        'birthday': '', 'native_place': random.choice(['北京', '上海', '广州', '成都', '武汉']),
        'ethnicity': '汉族', 'political_status': random.choice(['党员', '群众', '共青团员']),
        'marital_status': random.choice(['已婚', '未婚']), 'blood_type': '',
        'zodiac': '', 'hobbies': '', 'specialties': '', 'remark': '', 'created_at': hire,
    })
write_csv('employee', employees)

# ── CUSTOMER ─────────────────────────────────────────────────────────────────

customer_data = [
    ('sgcc',        '国家电网有限公司',         'SGCC',   'energy', 'strategic', 'gt1000', 'customer', 'A', '北京市西城区金融街8号',     '91110000100013470B'),
    ('csg',         '南方电网有限责任公司',      'CSG',    'energy', 'strategic', 'gt1000', 'customer', 'A', '广东省广州市越秀区东风西路8号','911440000326781948'),
    ('huaneng',     '中国华能集团有限公司',      '华能',   'energy', 'key',       'gt1000', 'customer', 'A', '北京市朝阳区建国门外大街甲6号','91110000100005512X'),
    ('datang',      '中国大唐集团有限公司',      '大唐',   'energy', 'key',       'gt1000', 'customer', 'A', '北京市西城区太平桥大街23号',  '91110000100005514T'),
    ('huadian',     '中国华电集团有限公司',      '华电',   'energy', 'key',       'gt1000', 'customer', 'A', '北京市西城区太平桥大街33号',  '91110000100005516J'),
    ('hebei_ep',    '国网河北省电力有限公司',    '冀电',   'energy', 'key',       '500to1000', 'customer', 'A', '河北省石家庄市裕华区建设大街509号', '91130000714571028H'),
    ('shandong_ep', '国网山东省电力公司',        '鲁电',   'energy', 'key',       '500to1000', 'customer', 'A', '山东省济南市历下区经十路21668号',  '91370000101150003P'),
    ('jiangsu_ep',  '国网江苏省电力有限公司',    '苏电',   'energy', 'key',       '500to1000', 'customer', 'A', '江苏省南京市玄武区紫金路1号',      '9132000074924498XB'),
    ('guangdong_ep','南方电网广东电网有限责任公司','粤电', 'energy', 'key',       '500to1000', 'customer', 'B', '广东省广州市天河区天寿路6号',      '91440100717915891E'),
    ('sichuan_ep',  '国网四川省电力公司',        '川电',   'energy', 'normal',    '100to500',  'customer', 'B', '四川省成都市金牛区人民北路一段99号','91510000715100032E'),
    ('siemens',     '西门子（中国）有限公司',    '西门子', 'tech',   'normal',    'gt1000', 'supplier', 'A', '北京市朝阳区望京中环南路7号',     '91110000100000030B'),
    ('abb',         'ABB（中国）有限公司',       'ABB',    'tech',   'normal',    'gt1000', 'supplier', 'A', '上海市浦东新区康新公路4528号',    '91310115600180023F'),
    ('nari',        '南京南瑞集团公司',          '南瑞',   'tech',   'key',       '500to1000', 'partner', 'A', '江苏省南京市江宁区苏源大道19号',  '91320114718895855C'),
    ('sifang',      '北京四方继保工程技术有限公司','四方', 'tech',   'normal',    '100to500',  'partner', 'B', '北京市海淀区西三环北路甲28号',    '91110108618736684F'),
    ('xuji',        '许继集团有限公司',          '许继',   'tech',   'normal',    '100to500',  'partner', 'B', '河南省许昌市高新技术产业开发区',  '91411000154421025A'),
]

customers = []
for key, name, short, ind, tier, size, ctype, credit, addr, uscc in customer_data:
    customers.append({
        'id': cust_ids[key], 'name': name, 'industry': ind, 'website': f'http://www.{key.replace("_","")}.com.cn',
        'tier': tier, 'source': random.choice(['tender', 'referral', 'exhibition']),
        'short_name': short, 'type': ctype, 'tags': '电力行业',
        'size': size, 'address': addr, 'legal_person': random.choice(['王建国', '李志远', '张明华', '刘建平']),
        'registered_capital': random.choice([50000, 100000, 200000, 500000]),
        'established_date': random.choice([d(1994,1,1), d(1997,6,1), d(2002,3,1), d(2008,9,1)]),
        'credit_grade': credit, 'category_path': '能源/电力', 'parent_customer_id': '',
        'uscc': uscc, 'registration_status': 'active',
        'paid_in_capital': '', 'org_code': '', 'business_reg_no': '',
        'enterprise_type': '国有企业', 'business_term': '长期', 'taxpayer_qualification': '一般纳税人',
        'insured_count': random.randint(500, 50000), 'region': addr[:3],
        'registration_authority': '', 'english_name': '', 'former_names': '',
        'importance': 'high', 'credit_limit': random.choice([500, 1000, 2000, 5000]),
        'settlement_method': 'monthly_60', 'first_contact_date': rdate('2018-01-01','2020-12-31'),
        'first_cooperation_date': rdate('2019-01-01','2021-12-31'),
        'note': '', 'created_at': rdate('2018-01-01','2020-01-01'),
    })
write_csv('customer', customers)

# ── CONTACT ──────────────────────────────────────────────────────────────────

contact_names = [
    ('陈国栋', 'male',   'final',    '采购决策',    '总经理'),
    ('李晓梅', 'female', 'tech',     '技术规范制定', '信息化总监'),
    ('王志强', 'male',   'purchase', '采购执行',    '采购部经理'),
    ('张丽华', 'female', 'influencer','政策把关',   '法务总监'),
    ('刘建军', 'male',   'final',    '项目立项审批', '副总经理'),
    ('赵雪梅', 'female', 'tech',     '方案评审',    '技术部主任'),
    ('孙大明', 'male',   'purchase', '合同执行',    '合同管理部长'),
    ('周小燕', 'female', 'gatekeeper','信息筛选',   '办公室主任'),
    ('吴国庆', 'male',   'tech',     '系统验收',    '运维部主任'),
    ('郑美云', 'female', 'influencer','关系协调',   '对外合作部长'),
    ('徐建国', 'male',   'final',    '预算审批',    '财务总监'),
    ('何秀兰', 'female', 'tech',     '需求提出',    '调度中心主任'),
    ('林志远', 'male',   'purchase', '物资管控',    '物资部经理'),
    ('郭丽英', 'female', 'influencer','行业资源',   '战略合作部长'),
    ('马国强', 'male',   'tech',     '安全管控',    '安全总监'),
    ('朱晓红', 'female', 'final',    '最终决策',    '董事会秘书'),
    ('曹建华', 'male',   'purchase', '招标管理',    '招标部经理'),
    ('许小云', 'female', 'tech',     '信息安全',    '网络安全部长'),
    ('任建平', 'male',   'gatekeeper','资料接收',   '综合办主任'),
    ('谢美玲', 'female', 'influencer','业务推荐',   '业务发展部长'),
]

contacts = []
cust_keys = ['sgcc','csg','huaneng','datang','huadian','hebei_ep','shandong_ep','jiangsu_ep','guangdong_ep','sichuan_ep']
for i, (name, gender, role, scope, pos) in enumerate(contact_names):
    ckey = cust_keys[i % len(cust_keys)]
    contacts.append({
        'id': contact_ids[i], 'customer_id': cust_ids[ckey], 'name': name, 'gender': gender,
        'company': next(c['name'] for c in customers if c['id'] == cust_ids[ckey]),
        'department': random.choice(['信息化部', '采购部', '技术部', '办公室', '财务部']),
        'phone': f'01{random.randint(0,9)}-{random.randint(10000000,99999999)}',
        'mobile': f'138{random.randint(10000000,99999999)}',
        'wechat': f'wx_{name}', 'qq': '', 'email': f'{i:02d}@{ckey.replace("_","")}.com.cn',
        'address': '', 'position': pos, 'title': pos,
        'decision_role': role, 'influence_scope': scope,
        'priority': random.choice(['1','2','3']),
        'relationship_strength': random.choice(['acquaintance','familiar','deep']),
        'birthday': '', 'native_place': '',
        'party_member': random.choice(['yes','no']),
        'university': random.choice(['华北电力大学','西安交通大学','浙江大学','清华大学','上海交通大学']),
        'major': random.choice(['电气工程','计算机科学','软件工程','信息管理']),
        'hobbies': '', 'lifestyle': '', 'family_info': '',
        'attitude': random.choice(['supportive','neutral','supportive']),
        'preferred_contact_method': random.choice(['wechat','phone','email']),
        'prev_position': '', 'prev_department': '', 'position_changed_date': '',
        'honors': '', 'status': 'active', 'tags': '电力行业', 'note': '', 'created_at': rdate('2019-01-01','2021-01-01'),
    })
write_csv('contact', contacts)

# ── PRODUCT ──────────────────────────────────────────────────────────────────

products = [
    ('p_dms',  '配网自动化管理系统（DMS）',          'software', 280,  '实现配电网实时监控、故障隔离与供电恢复自动化'),
    ('p_scada','变电站综合自动化系统（SCADA）',       'solution', 450,  '集成保护、监控、通信于一体的变电站自动化平台'),
    ('p_gis',  '电力GIS地理信息系统',                'software', 180,  '基于GIS的电网设备台账管理与空间分析平台'),
    ('p_ems',  '能量管理系统（EMS）',                'solution', 600,  '电网调度自动化核心平台，支持AGC/AVC等高级应用'),
    ('p_ami',  '高级量测体系（AMI）',                'solution', 320,  '智能电表及用电信息采集系统整体解决方案'),
    ('p_pms',  '电力设备管理系统（PMS）',            'software', 150,  '输变配电设备全生命周期台账与检修管理'),
    ('p_oa',   '电力企业协同办公平台',               'software',  80,  '面向电力央企的定制化协同办公与流程审批系统'),
    ('p_big',  '电网大数据分析平台',                 'software', 220,  '汇聚多源电网数据，支持负荷预测、风险预警等分析场景'),
]

product_rows = []
for key, name, cat, price, desc in products:
    product_rows.append({
        'id': prod_ids[key], 'name': name, 'category': cat,
        'price': price, 'description': desc, 'created_at': d(2020,1,1),
    })
write_csv('product', product_rows)

# ── OPPORTUNITY ──────────────────────────────────────────────────────────────

opp_titles = [
    (cust_ids['sgcc'],        contact_ids[0],  '国家电网总部EMS系统升级项目',              1200, 'won',      'L1'),
    (cust_ids['csg'],         contact_ids[1],  '南方电网配网自动化建设项目',               850,  'won',      'L1'),
    (cust_ids['hebei_ep'],    contact_ids[5],  '国网河北电力GIS系统建设',                  320,  'won',      'L1'),
    (cust_ids['shandong_ep'], contact_ids[6],  '国网山东调度数据网升级改造',               480,  'won',      'L1'),
    (cust_ids['jiangsu_ep'],  contact_ids[7],  '国网江苏AMI智能量测体系建设',              650,  'won',      'L2'),
    (cust_ids['guangdong_ep'],contact_ids[8],  '南网广东电网大数据平台项目',               290,  'tracking', 'L3'),
    (cust_ids['sichuan_ep'],  contact_ids[9],  '国网四川PMS设备管理系统',                  180,  'tracking', 'L3'),
    (cust_ids['huaneng'],     contact_ids[2],  '华能集团协同办公平台升级',                 120,  'tracking', 'L4'),
    (cust_ids['datang'],      contact_ids[3],  '大唐集团变电站SCADA系统采购',              560,  'lost',     'L1'),
    (cust_ids['huadian'],     contact_ids[4],  '华电集团电网大数据分析系统',               350,  'lost',     'L1'),
    (cust_ids['sgcc'],        contact_ids[10], '国网总部PMS系统二期建设',                  750,  'tracking', 'L2'),
    (cust_ids['csg'],         contact_ids[11], '南网EMS系统扩容改造',                      420,  'hold',     'L3'),
]

opportunities = []
for i, (cid, ctid, title, amount, status, stage) in enumerate(opp_titles):
    disc = rdate('2021-01-01', '2023-06-01')
    opportunities.append({
        'id': opp_ids[i], 'customer_id': cid, 'contact_id': ctid,
        'sales_person_id': random.choice([emp_ids['zhang_wei'], emp_ids['sun_jing'], emp_ids['lin_kai']]),
        'handler_id': emp_ids['li_na'],
        'title': title, 'amount': amount, 'stage': stage, 'status': status,
        'win_prob': {'won': 100, 'lost': 0, 'tracking': random.choice([30,50,70]), 'hold': 20}.get(status, 50),
        'source': random.choice(['tender','referral','self_developed']),
        'priority': 'high' if amount > 500 else 'medium',
        'opp_type': '电网事业部', 'discovery_date': disc, 'second_customer_id': '',
        'client_relationship': random.choice(['familiar','deep','acquaintance']),
        'amount_currency_note': '', 'planned_sign_date': rdate('2022-01-01','2024-06-01'),
        'actual_sign_date': rdate('2022-06-01','2024-06-01') if status == 'won' else '',
        'competitors': random.choice(['南瑞科技,许继电气','西门子,ABB','南瑞,四方']),
        'gross_margin': random.randint(25, 45),
        'customer_requirements': '系统稳定可靠，满足电力行业相关标准，支持国产化适配',
        'lose_reason': '竞争对手报价更低，本地化服务不足' if status == 'lost' else '',
        'stage_note': '', 'description': f'面向{title[:6]}的信息化建设需求',
        'created_date': disc, 'status_changed_date': rdate('2022-01-01','2024-01-01'),
        'stage_changed_date': rdate('2022-01-01','2024-01-01'), 'created_at': disc,
    })
write_csv('opportunity', opportunities)

# ── FOLLOW_UP ────────────────────────────────────────────────────────────────

methods = ['visit', 'phone', 'wechat', 'video', 'email']
follow_ups = []
for i in range(30):
    opp_i = random.randint(0, len(opp_ids)-1)
    emp_k = random.choice(list(emp_ids.values()))
    ct_i  = random.randint(0, len(contact_ids)-1)
    follow_ups.append({
        'id': uid(), 'opportunity_id': opp_ids[opp_i],
        'customer_id': opportunities[opp_i]['customer_id'],
        'contact_id': contact_ids[ct_i],
        'method': random.choice(methods),
        'date': rdate('2022-01-01','2024-06-01'),
        'summary': random.choice([
            '与客户确认需求范围，重点讨论系统集成方案',
            '拜访采购部门，了解招标计划时间节点',
            '技术交流，演示系统功能，客户反馈积极',
            '商务洽谈，初步确认合同条款框架',
            '跟进项目进度，确认下一步行动计划',
            '参加客户组织的供应商说明会',
            '提交技术方案，等待客户评审意见',
        ]),
        'next_action': random.choice(['提交报价单', '安排技术演示', '等待客户反馈', '准备投标文件']),
        'next_date': rdate('2024-01-01','2024-12-31'),
        'recorded_by': random.choice(['张伟','李娜','孙静']),
        'created_at': rdate('2022-01-01','2024-06-01'),
    })
write_csv('follow_up', follow_ups)

# ── BID_REGISTRATION ─────────────────────────────────────────────────────────

won_opp_indices = [i for i, o in enumerate(opportunities) if o['status'] == 'won']
bid_opp_indices = won_opp_indices + [i for i, o in enumerate(opportunities) if o['status'] in ('tracking','lost')]
bid_opp_indices = bid_opp_indices[:10]

bid_registrations = []
for i, opp_i in enumerate(bid_opp_indices):
    opp = opportunities[opp_i]
    bid_registrations.append({
        'id': bidreg_ids[i],
        'project_name': opp['title'],
        'company_name': next(c['name'] for c in customers if c['id'] == opp['customer_id']),
        'applicant_name': random.choice(['张伟','李娜','孙静','林凯']),
        'our_role': 'main',
        'win_probability': opp['win_prob'],
        'status': 'formal' if opp['status'] in ('won','lost') else 'preparing',
        'estimated_amount': opp['amount'],
        'expected_bid_period': rdate('2022-06-01','2023-06-01'),
        'expected_batch': f'2023年第{random.randint(1,4)}批次',
        'bid_website': 'https://www.bidcenter.com.cn',
        'has_prior_research': 'yes',
        'prior_research_name': '', 'planned_dept': '市场销售部',
        'business_dept': '电网事业部',
        'our_contact': '张伟', 'biz_contact_position': '销售总监',
        'commerce_contact': '李娜', 'tech_providers': '王芳,徐鹏',
        'keywords': '电力自动化,智能电网,国产化',
        'main_bid_company': '', 'main_bid_contact': '', 'main_bid_time': '',
        'bid_reason_type': 'direct', 'transfer_type': '', 'transfer_reason': '',
        'purchaser_info': '', 'pass_points': '', 'pass_reason_type': '',
        'pass_notifier': '', 'promoted_to_tender': 'yes' if opp['status'] in ('won','lost') else 'no',
        'issuer_confirmed': 'yes', 'issuer_confirmation_time': rdate('2022-06-01','2023-01-01'),
        'issuer_our_contact': '张伟',
        'issuer_their_contact': next((c['name'] for c in contacts if c['customer_id'] == opp['customer_id']), ''),
        'remark': '', 'created_date': rdate('2022-01-01','2023-01-01'),
        'opportunity_id': opp['id'], 'created_at': rdate('2022-01-01','2023-01-01'),
    })
write_csv('bid_registration', bid_registrations)

# ── BID_SUBMISSION ───────────────────────────────────────────────────────────

bid_submissions = []
sub_indices = [i for i, br in enumerate(bid_registrations) if br['status'] == 'formal'][:8]
for i, br_i in enumerate(sub_indices):
    br   = bid_registrations[br_i]
    opp_i = bid_opp_indices[br_i]
    opp  = opportunities[opp_i]
    won  = opp['status'] == 'won'
    open_dt = rdate('2023-01-01','2024-01-01')
    bid_submissions.append({
        'id': bidsub_ids[i],
        'bid_registration_id': br['id'],
        'tender_section_name': br['project_name'],
        'company_name': br['company_name'],
        'project_name': br['project_name'],
        'planned_batch_no': f'2023-B{i+1:02d}',
        'planned_batch_name': br['expected_batch'],
        'sub_project_no': f'SP{i+1:03d}', 'sub_project_name': '',
        'package_no': f'PKG{i+1:02d}', 'bid_no': f'BID2023{i+1:03d}',
        'section_type': 'service',
        'bid_amount': opp['amount'],
        'handler_id': emp_ids['zhang_wei'],
        'commerce_contact_id': emp_ids['li_na'],
        'dept': '电网事业部',
        'internal_contact_id': emp_ids['wang_fang'],
        'doc_reviewer_id': emp_ids['zhou_tao'],
        'price_internal_contact_id': emp_ids['zhao_min'],
        'registration_deadline': rdate('2022-10-01','2023-01-01'),
        'official_deadline': rdate('2023-01-01','2023-06-01'),
        'internal_deadline': rdate('2023-01-01','2023-06-01'),
        'listing_date': rdate('2022-09-01','2022-12-01'),
        'open_date': open_dt,
        'doc_submit_time': rdate('2023-01-01','2023-04-01'),
        'award_notice_date': rdate('2023-02-01','2023-06-01') if won else '',
        'contract_date': rdate('2023-03-01','2023-08-01') if won else '',
        'price_strategy': 'comprehensive',
        'price_strategy_detail': '综合评分法，技术分40%商务分30%价格分30%',
        'price_score_method': '基准价法',
        'business_score_weight': 30, 'technical_score_weight': 40, 'price_score_weight': 30,
        'quote_method': 'discount_ratio',
        'bid_buyer': '张伟', 'bid_buy_time': rdate('2022-09-01','2022-11-01'),
        'bid_buy_method': 'online', 'bid_doc_fee': 0.5, 'bid_doc_no': f'BDOC2023{i+1:03d}',
        'bid_doc_downloaded': 'yes', 'checklist': '资质文件,业绩证明,技术方案,报价表',
        'bid_document_url': '', 'status': 'awarded' if won else 'lost',
        'result': 'won' if won else 'lost',
        'result_notify_date': rdate('2023-03-01','2023-07-01'),
        'result_notified_to': '销售部,商务部,技术部',
        'win_amount': opp['amount'] * 0.97 if won else '',
        'win_company': '本公司' if won else random.choice(['南瑞科技','许继电气','西门子中国']),
        'lose_reason': '' if won else '报价偏高，技术方案未充分体现国产化优势',
        'service_fee': '', 'service_fee_due_date': '', 'service_fee_invoice': '',
        'payment_recipient': '', 'payment_bank': '', 'payment_account': '', 'payment_notes': '',
        'remark': '', 'created_date': rdate('2022-09-01','2023-01-01'),
        'opportunity_id': opp['id'],
        'status_changed_at': rdate('2023-03-01','2023-08-01'), 'created_at': rdate('2022-09-01','2023-01-01'),
    })
write_csv('bid_submission', bid_submissions)

# ── BID_RESEARCH ─────────────────────────────────────────────────────────────

bid_researches = []
for i, br in enumerate(bid_registrations[:6]):
    bid_researches.append({
        'id': uid(), 'section_name': br['project_name'],
        'bid_registration_id': br['id'],
        'bid_unit_name': br['company_name'],
        'research_amount': br['estimated_amount'],
        'planned_dept': '信息化部',
        'is_private': 'no',
        'founded_date': random.choice([d(1994,1,1), d(2002,3,1)]),
        'reg_capital': random.choice([50000, 100000, 200000]),
        'paid_capital': random.choice([30000, 80000, 150000]),
        'insured_employees': random.randint(1000, 30000),
        'history_performance': '近三年在电力信息化领域采购规模持续增长',
        'recent_3yr_loss': 'none',
        'company_characteristics': '国有大型电力企业，采购流程规范，注重品牌与业绩',
        'service_scope': '电力系统信息化、自动化、智能化',
        'recent_5yr_performance': '实施多个省级电网信息化项目，业绩充分',
        'recommend_reason': '单位背景良好，需求明确，符合我司业务方向',
        'insufficient_note': '',
        'researcher_id': random.choice([emp_ids['zhang_wei'], emp_ids['lin_kai']]),
        'project_type': '政府采购/国企采购',
        'project_type_note': '国有企业内部采购，执行国资委相关规定',
        'version_year': '2023',
        'status': 'submitted',
        'submitted_at': rdate('2022-08-01','2023-01-01'),
        'remark': '', 'created_date': rdate('2022-07-01','2022-12-01'),
        'created_at': rdate('2022-07-01','2022-12-01'),
    })
write_csv('bid_research', bid_researches)

# ── BID_COMPANION ────────────────────────────────────────────────────────────

companion_companies = ['北京华电信息技术有限公司', '国网信通科技有限公司', '中电科信息技术有限公司']
bid_companions = []
for bs in bid_submissions[:5]:
    bid_companions.append({
        'id': uid(), 'bid_submission_id': bs['id'],
        'company_name': random.choice(companion_companies),
        'our_contact': '张伟', 'their_contact': random.choice(['王经理','李总监','陈主任']),
        'lifecycle_status': 'completed' if bs['result'] == 'won' else 'cancelled',
        'cancel_reason': '' if bs['result'] == 'won' else '投标作废',
        'remark': '满足最低投标人数要求', 'created_at': rdate('2022-10-01','2023-03-01'),
    })
write_csv('bid_companion', bid_companions)

# ── BID_COMPETITOR ───────────────────────────────────────────────────────────

bid_competitors = []
for bs in bid_submissions:
    competitors = [('南瑞科技股份有限公司','综合实力强，本地化服务好'), ('许继电气股份有限公司','价格竞争力强')]
    for comp_name, info in competitors[:random.randint(1,2)]:
        bid_competitors.append({
            'id': uid(), 'bid_submission_id': bs['id'],
            'company_name': comp_name, 'competitor_id': '',
            'contact_person': '', 'entry_info': info, 'remark': '',
            'created_at': rdate('2023-01-01','2023-06-01'),
        })
write_csv('bid_competitor', bid_competitors)

# ── BID_LOG ──────────────────────────────────────────────────────────────────

log_contents = [
    '提交投标报名申请，获得投标资格',
    '完成招标文件下载，组织技术研讨',
    '完成投标文件制作，内部审核通过',
    '成功递交投标文件',
    '参加开标会议',
    '收到中标通知书',
]
bid_logs = []
for bs in bid_submissions:
    for j, content in enumerate(log_contents[:random.randint(3,6)]):
        bid_logs.append({
            'id': uid(), 'bid_submission_id': bs['id'],
            'content': content,
            'logged_by_id': random.choice([emp_ids['zhang_wei'], emp_ids['li_na']]),
            'date': rdate('2022-10-01','2023-08-01'),
            'created_at': rdate('2022-10-01','2023-08-01'),
        })
write_csv('bid_log', bid_logs)

# ── BID_REVIEW ───────────────────────────────────────────────────────────────

bid_reviews = []
for bs in bid_submissions[:6]:
    bid_reviews.append({
        'id': uid(), 'bid_submission_id': bs['id'],
        'round_no': '第一轮',
        'target_type': 'main', 'accompany_company': '',
        'created_by': '张伟', 'role': 'first',
        'reviewer_id': emp_ids['zhou_tao'],
        'status': 'submitted', 'result': 'pass',
        'overall_remark': '技术方案完整，报价合理，资质齐全，建议提交',
        'checklist_detail': '营业执照√；资质证书√；业绩证明√；技术方案√；报价表√',
        'created_at': rdate('2023-01-01','2023-05-01'),
    })
write_csv('bid_review', bid_reviews)

# ── CONTRACT ─────────────────────────────────────────────────────────────────

won_subs = [bs for bs in bid_submissions if bs['result'] == 'won']
ctr_cust_map = [opp_ids.index(bs['opportunity_id']) for bs in won_subs]

contracts = []
for i, bs in enumerate(won_subs):
    opp_i_local = next((j for j, o in enumerate(opportunities) if o['id'] == bs['opportunity_id']), 0)
    opp = opportunities[opp_i_local]
    cid = opp['customer_id']
    sign = rdate('2023-04-01','2024-01-01')
    amount = float(bs['win_amount']) if bs['win_amount'] else opp['amount']
    contracts.append({
        'id': ctr_ids[i],
        'customer_id': cid,
        'party_a_contact_id': next((c['id'] for c in contacts if c['customer_id'] == cid), ''),
        'internal_contact_id': emp_ids['li_na'],
        'contract_no': f'HT2023{i+1:04d}',
        'name': f'{opp["title"]}合同',
        'nature': 'direct', 'contract_type': 'tech',
        'status': random.choice(['executing','completed']),
        'dept': '电网事业部', 'business_unit': '电力事业群',
        'party_a_name': next(c['name'] for c in customers if c['id'] == cid),
        'amount': round(amount, 2), 'tax_rate': 13,
        'sign_date': sign,
        'effective_date': sign,
        'end_date': (date.fromisoformat(sign) + timedelta(days=365)).isoformat(),
        'created_date': sign,
        'payment_method': random.choice(['milestone','installment']),
        'payment_terms': '项目验收后30天内付款',
        'second_customer_id': '', 'handler_id': emp_ids['li_na'],
        'transfer_from_contract_id': '', 'transfer_amount': '', 'transfer_status': '',
        'transfer_remark': '', 'remark': '',
        'opportunity_id': opp['id'], 'bid_submission_id': bs['id'],
        'status_changed_at': rdate('2023-05-01','2024-06-01'),
        'created_at': sign,
    })
write_csv('contract', contracts)

# ── SUB_CONTRACT ─────────────────────────────────────────────────────────────

sub_contracts = []
for ctr in contracts:
    for j, (spec, ratio) in enumerate([('软件开发与集成', 60), ('实施部署与培训', 40)]):
        sub_contracts.append({
            'id': uid(), 'contract_id': ctr['id'],
            'sub_name': f'{ctr["name"][:10]}{spec}子合同',
            'sub_no': f'{ctr["contract_no"]}-S{j+1:02d}',
            'sub_amount': round(ctr['amount'] * ratio / 100, 2),
            'sub_tax_rate': 13, 'specialty': spec, 'specialty_ratio': ratio,
            'handler_id': emp_ids['li_na'],
            'status': ctr['status'], 'remark': '', 'created_at': ctr['sign_date'],
        })
write_csv('sub_contract', sub_contracts)

# ── CONTRACT_PAYMENT_PLAN ────────────────────────────────────────────────────

payment_plans = []
for ctr in contracts:
    periods = [('第一期', 30, '合同签订后15天'), ('第二期', 40, '系统上线验收后'), ('第三期', 30, '终验后30天')]
    for no, (pname, ratio, cond) in enumerate(periods, 1):
        plan_d = (date.fromisoformat(ctr['sign_date']) + timedelta(days=no*120)).isoformat()
        payment_plans.append({
            'id': uid(), 'contract_id': ctr['id'],
            'period_no': str(no), 'plan_amount': round(ctr['amount'] * ratio / 100, 2),
            'plan_ratio': ratio, 'plan_date': plan_d, 'condition': cond,
            'sub_contract_id': '',
            'status': 'paid' if ctr['status'] == 'completed' else 'pending',
            'remark': '', 'created_at': ctr['sign_date'],
        })
write_csv('contract_payment_plan', payment_plans)

# ── CONTRACT_INVOICE ─────────────────────────────────────────────────────────

invoices = []
for ctr in contracts:
    inv_date = (date.fromisoformat(ctr['sign_date']) + timedelta(days=30)).isoformat()
    invoices.append({
        'id': uid(), 'contract_id': ctr['id'],
        'invoice_no': f'INV{ctr["contract_no"][2:]}',
        'invoice_type': 'special_vat',
        'invoice_amount': round(ctr['amount'] * 0.7, 2),
        'invoice_date': inv_date, 'tax_rate': 13,
        'sub_contract_id': '',
        'receiver_id': next((c['id'] for c in contacts if c['customer_id'] == ctr['customer_id']), ''),
        'status': 'confirmed', 'remark': '', 'created_at': inv_date,
    })
write_csv('contract_invoice', invoices)

# ── CONTRACT_PAYMENT ─────────────────────────────────────────────────────────

ctr_payments = []
for idx, ctr in enumerate(contracts):
    pay_date = (date.fromisoformat(ctr['sign_date']) + timedelta(days=60)).isoformat()
    plan_ids_for_ctr = [p for p in payment_plans if p['contract_id'] == ctr['id']]
    inv_for_ctr      = [v for v in invoices       if v['contract_id'] == ctr['id']]
    ctr_payments.append({
        'id': uid(), 'contract_id': ctr['id'],
        'invoice_id': inv_for_ctr[0]['id'] if inv_for_ctr else '',
        'payment_plan_id': plan_ids_for_ctr[0]['id'] if plan_ids_for_ctr else '',
        'payer_id': ctr['customer_id'],
        'amount': inv_for_ctr[0]['invoice_amount'] if inv_for_ctr else round(ctr['amount']*0.7,2),
        'payment_date': pay_date,
        'payment_method': ctr['payment_method'],
        'bank_account': '', 'transaction_no': f'TXN2023{idx+1:06d}',
        'remark': '首期款到账', 'created_at': pay_date,
    })
write_csv('contract_payment', ctr_payments)

# ── CONTRACT_LINE_ITEM ───────────────────────────────────────────────────────

line_items = []
prod_keys_list = list(prod_ids.keys())
for ctr in contracts:
    for j in range(random.randint(2,4)):
        pk = random.choice(prod_keys_list)
        pr = next(p for p in product_rows if p['id'] == prod_ids[pk])
        qty = random.randint(1,3)
        line_items.append({
            'id': uid(), 'contract_id': ctr['id'],
            'product_id': prod_ids[pk], 'product_name': pr['name'],
            'quantity': qty, 'unit': '套', 'unit_price': pr['price'],
            'discount': random.choice([1.0, 0.95, 0.9, 0.85]),
            'remark': '', 'created_at': ctr['sign_date'],
        })
write_csv('contract_line_item', line_items)

# ── CONTRACT_AMENDMENT ───────────────────────────────────────────────────────

amendments = []
for ctr in contracts[:3]:
    amendments.append({
        'id': uid(), 'contract_id': ctr['id'],
        'change_type': 'extension', 'change_no': f'AMD-{ctr["contract_no"]}-001',
        'change_date': (date.fromisoformat(ctr['end_date']) - timedelta(days=30)).isoformat(),
        'description': '因客户现场施工进度延迟，双方协商将合同履行期延长90天',
        'old_amount': ctr['amount'], 'new_amount': ctr['amount'],
        'old_end_date': ctr['end_date'],
        'new_end_date': (date.fromisoformat(ctr['end_date']) + timedelta(days=90)).isoformat(),
        'approved_by': '总经理', 'status': 'approved',
        'remark': '', 'created_at': (date.fromisoformat(ctr['end_date']) - timedelta(days=30)).isoformat(),
    })
write_csv('contract_amendment', amendments)

# ── PROJECT ──────────────────────────────────────────────────────────────────

projects = []
for i, ctr in enumerate(contracts[:6]):
    opp_match = next((o for o in opportunities if o['id'] == ctr['opportunity_id']), None)
    start = (date.fromisoformat(ctr['sign_date']) + timedelta(days=15)).isoformat()
    projects.append({
        'id': proj_ids[i], 'contract_id': ctr['id'],
        'customer_id': ctr['customer_id'],
        'opportunity_id': ctr['opportunity_id'],
        'name': ctr['name'].replace('合同', '项目'),
        'project_no': f'PRJ2023{i+1:04d}',
        'manager_id': emp_ids['liu_yang'],
        'status': random.choice(['executing','completed']),
        'start_date': start,
        'planned_end_date': ctr['end_date'],
        'actual_end_date': ctr['end_date'] if ctr['status'] == 'completed' else '',
        'budget': ctr['amount'],
        'description': f'基于{ctr["name"]}开展的信息化系统建设项目',
        'remark': '', 'created_at': start,
    })
write_csv('project', projects)

# ── PROJECT_MEMBER ───────────────────────────────────────────────────────────

member_roles = ['项目经理','技术负责人','商务负责人','实施工程师','测试工程师','运维工程师']
project_members = []
for proj in projects:
    members = [
        (emp_ids['liu_yang'],   '项目经理'),
        (emp_ids['wang_fang'],  '技术负责人'),
        (emp_ids['li_na'],      '商务负责人'),
        (emp_ids['xu_peng'],    '实施工程师'),
        (emp_ids['ma_li'],      '实施工程师'),
    ]
    for emp_id, role in members:
        project_members.append({
            'id': uid(), 'project_id': proj['id'], 'employee_id': emp_id,
            'customer_id': '',
            'role': role, 'join_date': proj['start_date'],
            'leave_date': proj['actual_end_date'],
            'allocation_ratio': 50 if role == '实施工程师' else 80,
            'remark': '', 'created_at': proj['start_date'],
        })
write_csv('project_member', project_members)

# ── PROJECT_COST ─────────────────────────────────────────────────────────────

cost_types = [
    ('labor',    '人力成本',  '项目组人员工资及绩效分摊'),
    ('purchase', '采购成本',  '服务器及网络设备采购'),
    ('outsource','外包成本',  '现场实施外包服务费'),
    ('travel',   '差旅成本',  '出差交通住宿费'),
]
project_costs = []
for proj in projects:
    for ctype, cname, cdesc in cost_types:
        project_costs.append({
            'id': uid(), 'project_id': proj['id'],
            'cost_type': ctype, 'cost_name': cname,
            'amount': round(proj['budget'] * random.uniform(0.05, 0.15), 2),
            'cost_date': rdate('2023-04-01','2024-06-01'),
            'purchase_order_id': '',
            'supplier_id': random.choice([cust_ids['siemens'], cust_ids['abb'], '']) if ctype == 'purchase' else '',
            'employee_id': emp_ids['liu_yang'],
            'description': cdesc, 'remark': '', 'created_at': rdate('2023-04-01','2024-06-01'),
        })
write_csv('project_cost', project_costs)

# ── PROJECT_REVIEW ───────────────────────────────────────────────────────────

project_reviews = []
for proj in projects:
    project_reviews.append({
        'id': uid(), 'project_id': proj['id'],
        'review_type': random.choice(['kickoff','milestone','acceptance']),
        'review_date': rdate('2023-05-01','2024-06-01'),
        'reviewer_names': '刘洋,王芳,李娜',
        'result': random.choice(['approved','approved','conditional']),
        'opinion': '项目整体推进顺利，技术方案落地良好，建议加强客户培训力度',
        'next_action': '完成系统割接上线，安排最终验收',
        'remark': '', 'created_at': rdate('2023-05-01','2024-06-01'),
    })
write_csv('project_review', project_reviews)

# ── PROJECT_LOG ──────────────────────────────────────────────────────────────

project_logs = []
milestones = [
    '项目启动会召开，完成团队组建',
    '完成需求调研与方案设计评审',
    '完成系统开发与联调测试',
    '现场实施部署完成，初步验收通过',
    '用户培训结束，系统正式上线',
]
for proj in projects:
    for j, ms in enumerate(milestones[:random.randint(3,5)]):
        project_logs.append({
            'id': uid(), 'project_id': proj['id'],
            'content': ms, 'completion': random.choice([80,90,100]),
            'milestone': ms[:10],
            'logged_by_id': random.choice([emp_ids['liu_yang'], emp_ids['he_rong']]),
            'date': rdate('2023-04-01','2024-06-01'),
            'remark': '', 'created_at': rdate('2023-04-01','2024-06-01'),
        })
write_csv('project_log', project_logs)

# ── PROJECT_ACCEPTANCE ───────────────────────────────────────────────────────

acceptances = []
for proj in projects:
    if proj['status'] == 'completed':
        acc_date = proj['actual_end_date'] or proj['planned_end_date']
        acceptances.append({
            'id': uid(), 'project_id': proj['id'], 'contract_id': proj['contract_id'],
            'acceptance_type': 'final',
            'acceptance_date': acc_date,
            'accepted_by_id': next((c['id'] for c in contacts if c['customer_id'] == proj['customer_id']), ''),
            'result': 'passed',
            'document_url': '', 'document_name': f'{proj["name"]}验收报告.pdf',
            'remark': '系统运行稳定，各项功能满足合同要求，客户确认验收通过',
            'created_at': acc_date,
        })
write_csv('project_acceptance', acceptances)

# ── PURCHASE_REQUEST ─────────────────────────────────────────────────────────

purchase_requests = []
pr_ids = []
for proj in projects:
    pr_id = uid()
    pr_ids.append(pr_id)
    purchase_requests.append({
        'id': pr_id, 'project_id': proj['id'],
        'title': f'{proj["name"]}服务器采购申请',
        'description': '项目部署所需服务器、存储设备及网络设备',
        'budget': round(proj['budget'] * 0.12, 2),
        'applicant_name': '刘洋',
        'apply_date': (date.fromisoformat(proj['start_date']) + timedelta(days=7)).isoformat(),
        'status': random.choice(['approved','executing','completed']),
        'approved_by': '张总',
        'approved_date': (date.fromisoformat(proj['start_date']) + timedelta(days=14)).isoformat(),
        'remark': '', 'created_at': proj['start_date'],
    })
write_csv('purchase_request', purchase_requests)

# ── PURCHASE_ORDER ───────────────────────────────────────────────────────────

purchase_orders = []
po_ids = []
for i, pr in enumerate(purchase_requests):
    po_id = uid()
    po_ids.append(po_id)
    proj = projects[i]
    purchase_orders.append({
        'id': po_id,
        'purchase_request_id': pr['id'],
        'project_id': proj['id'],
        'supplier_id': random.choice([cust_ids['siemens'], cust_ids['abb']]),
        'contract_id': proj['contract_id'],
        'po_no': f'PO2023{i+1:04d}',
        'name': pr['title'],
        'amount': pr['budget'],
        'payment_method': 'milestone',
        'order_date': pr['apply_date'],
        'expected_delivery': (date.fromisoformat(pr['apply_date']) + timedelta(days=30)).isoformat(),
        'actual_delivery': (date.fromisoformat(pr['apply_date']) + timedelta(days=35)).isoformat(),
        'status': random.choice(['delivered','completed']),
        'buyer_id': emp_ids['li_na'],
        'remark': '', 'created_at': pr['apply_date'],
    })
write_csv('purchase_order', purchase_orders)

# ── GOODS_RECEIPT ────────────────────────────────────────────────────────────

goods_receipts = []
for i, po in enumerate(purchase_orders):
    goods_receipts.append({
        'id': uid(), 'purchase_order_id': po['id'],
        'receipt_date': po['actual_delivery'],
        'quantity_description': '服务器2台，存储设备1套，交换机4台，全部验收合格',
        'inspector_name': '刘洋',
        'result': 'passed',
        'remark': '设备外观完好，配件齐全，与采购清单一致', 'created_at': po['actual_delivery'],
    })
write_csv('goods_receipt', goods_receipts)

# ── PURCHASE_PAYMENT ─────────────────────────────────────────────────────────

purchase_payments = []
for po in purchase_orders:
    purchase_payments.append({
        'id': uid(), 'purchase_order_id': po['id'],
        'amount': po['amount'],
        'payment_date': (date.fromisoformat(po['actual_delivery']) + timedelta(days=30)).isoformat(),
        'payment_method': 'lump_sum',
        'invoice_no': f'PINV{po["po_no"][2:]}',
        'invoice_amount': po['amount'],
        'invoice_date': po['actual_delivery'],
        'remark': '货到付款', 'created_at': po['actual_delivery'],
    })
write_csv('purchase_payment', purchase_payments)

# ── EMPLOYEE_EDUCATION ───────────────────────────────────────────────────────

educations = []
universities = ['华北电力大学','西安交通大学','浙江大学','清华大学','上海交通大学','北京邮电大学']
majors = ['电气工程及其自动化','计算机科学与技术','软件工程','信息管理与信息系统','电子信息工程']
for emp in employees:
    educations.append({
        'id': uid(), 'employee_id': emp['id'],
        'start_date': d(int(emp['hire_date'][:4])-4, 9, 1),
        'end_date': d(int(emp['hire_date'][:4]), 7, 1),
        'school': random.choice(universities), 'major': random.choice(majors),
        'study_mode': 'full_time', 'degree': 'bachelor', 'is_highest': 'yes',
        'remark': '', 'created_at': emp['hire_date'],
    })
write_csv('employee_education', educations)

# ── EMPLOYEE_WORK_HISTORY ────────────────────────────────────────────────────

work_histories = []
companies = ['中国电力科学研究院','国电南瑞科技股份有限公司','ABB（中国）有限公司','许继集团有限公司','南京南瑞集团']
for emp in employees[:8]:
    work_histories.append({
        'id': uid(), 'employee_id': emp['id'],
        'company_name': random.choice(companies),
        'position': random.choice(['软件工程师','项目工程师','售前工程师','商务专员']),
        'start_date': d(int(emp['hire_date'][:4])-3, 8, 1),
        'end_date': d(int(emp['hire_date'][:4]), 1, 1),
        'leave_reason': '寻求更好的发展机会',
        'remark': '', 'created_at': emp['hire_date'],
    })
write_csv('employee_work_history', work_histories)

# ── EMPLOYEE_QUALIFICATION ───────────────────────────────────────────────────

emp_qualifications = []
certs = [
    ('certificate', '软件工程师', 'CERT2023001'),
    ('certificate', 'PMP项目管理专业人士', 'PMP-CN-2023-12345'),
    ('certificate', '电力系统调度自动化工程师', 'PDAE2022001'),
    ('training',    'AWS云服务培训', ''),
    ('training',    '华为云计算认证', ''),
]
for emp in employees:
    cert = random.choice(certs)
    emp_qualifications.append({
        'id': uid(), 'employee_id': emp['id'],
        'qual_type': cert[0], 'qual_name': cert[1], 'cert_no': cert[2],
        'issue_date': rdate('2020-01-01','2023-12-01'),
        'expiry_date': rdate('2025-01-01','2028-12-01') if cert[0] == 'certificate' else '',
        'status': 'valid', 'remark': '', 'created_at': emp['hire_date'],
    })
write_csv('employee_qualification', emp_qualifications)

# ── EMPLOYEE_AWARD ───────────────────────────────────────────────────────────

awards = []
for emp in employees[:8]:
    awards.append({
        'id': uid(), 'employee_id': emp['id'],
        'record_type': 'award',
        'title': random.choice(['年度优秀员工','季度销售冠军','最佳项目奖','优秀技术贡献奖']),
        'description': '因工作表现突出，对公司业绩增长贡献显著',
        'award_date': rdate('2021-01-01','2023-12-01'),
        'reward': random.choice([3000, 5000, 10000]),
        'remark': '', 'created_at': emp['hire_date'],
    })
write_csv('employee_award', awards)

# ── EMPLOYEE_SALARY_HISTORY ──────────────────────────────────────────────────

salaries = []
for emp in employees:
    salaries.append({
        'id': uid(), 'employee_id': emp['id'],
        'effective_date': emp['regularization_date'],
        'base_salary': random.choice([8000, 10000, 12000, 15000, 20000, 25000]),
        'performance_coefficient': random.choice([1.0, 1.1, 1.2, 1.5]),
        'allowance': random.choice([500, 1000, 1500, 2000]),
        'change_reason': random.choice(['转正调薪','年度调薪','晋升调薪']),
        'approved_by': '陈浩',
        'remark': '', 'created_at': emp['regularization_date'],
    })
write_csv('employee_salary_history', salaries)

# ── EMPLOYEE_CONTRACT ────────────────────────────────────────────────────────

emp_contracts = []
for emp in employees:
    emp_contracts.append({
        'id': uid(), 'employee_id': emp['id'],
        'contract_type': random.choice(['fixed','fixed','open_ended']),
        'start_date': emp['hire_date'],
        'end_date': emp['contract_end_date'],
        'signing_entity': '本公司',
        'termination_reason': '',
        'remark': '', 'created_at': emp['hire_date'],
    })
write_csv('employee_contract', emp_contracts)

# ── EMPLOYEE_TRANSFER ────────────────────────────────────────────────────────

transfers = []
for emp in employees[:5]:
    transfers.append({
        'id': uid(), 'employee_id': emp['id'],
        'change_type': 'regularize',
        'change_date': emp['regularization_date'],
        'old_department_id': emp['department_id'], 'new_department_id': emp['department_id'],
        'old_position': emp['position'], 'new_position': emp['position'],
        'old_rank': emp['rank'], 'new_rank': emp['rank'],
        'reason': '试用期满转正',
        'approved_by': '陈浩',
        'remark': '', 'created_at': emp['regularization_date'],
    })
write_csv('employee_transfer', transfers)

# ── IP_ASSET ─────────────────────────────────────────────────────────────────

ip_assets = []
ip_ids = [uid() for _ in range(6)]
ip_data = [
    ('patent',    '一种配电网故障自愈方法及系统',          'authorized', 'ZL202310001234.X'),
    ('patent',    '基于机器学习的电力负荷预测方法',          'authorized', 'ZL202210056789.0'),
    ('software',  '配网自动化管理系统V2.0',                 'authorized', '2023SR0123456'),
    ('software',  '电力GIS空间信息管理平台V1.5',            'authorized', '2022SR0654321'),
    ('software',  '智能电网大数据分析平台V1.0',             'applying',   ''),
    ('trademark', 'FoxPower 电力智能化品牌商标',             'applying',   ''),
]
for i, (ip_type, name, status, cert_no) in enumerate(ip_data):
    proj_id = proj_ids[i % len(proj_ids)] if projects else ''
    ctr_id  = ctr_ids[i % len(ctr_ids)] if contracts else ''
    ip_assets.append({
        'id': ip_ids[i], 'ip_type': ip_type, 'name': name,
        'cert_no': cert_no, 'status': status,
        'application_date': rdate('2021-01-01','2023-06-01'),
        'authorized_date': rdate('2022-01-01','2024-01-01') if status == 'authorized' else '',
        'expiry_date': rdate('2030-01-01','2043-01-01') if status == 'authorized' else '',
        'project_id': proj_id, 'contract_id': ctr_id,
        'purchase_order_id': '',
        'manager_id': emp_ids['wang_fang'],
        'owner_name': '本公司', 'applicant_name': '王芳',
        'remark': '', 'created_at': rdate('2021-01-01','2023-06-01'),
    })
write_csv('ip_asset', ip_assets)

# ── IP_AUTHOR ────────────────────────────────────────────────────────────────

ip_authors = []
for i, ip in enumerate(ip_assets):
    for emp_key in (['wang_fang','xu_peng'] if ip['ip_type'] in ('patent','software') else ['wang_fang']):
        ip_authors.append({
            'id': uid(), 'ip_asset_id': ip['id'],
            'employee_id': emp_ids[emp_key],
            'name': next(e['name'] for e in employees if e['id'] == emp_ids[emp_key]),
            'role': random.choice(['inventor','co_inventor','author']),
            'phone': '', 'address': '',
            'created_at': ip['application_date'],
        })
write_csv('ip_author', ip_authors)

# ── COMPETITOR ───────────────────────────────────────────────────────────────

competitors = []
comp_data = [
    ('南瑞科技股份有限公司', '产品线完整，行业背书强，电力央企信任度高', '价格偏高，定制化能力弱', 0.92, 45),
    ('许继电气股份有限公司', '保护装置领域强，成本低，本地服务快',       '软件集成能力不足',       0.88, 15),
    ('四方继保工程技术有限公司','继保设备口碑好，价格灵活',               '整体解决方案能力弱',     0.85, 20),
    ('西门子（中国）有限公司', '品牌知名，技术先进，国际合规',            '价格昂贵，国产化适配难', 0.80, 0),
    ('ABB（中国）有限公司',   '自动化领域权威，系统稳定',               '本地化服务响应慢',       0.82, 0),
]
for name, strengths, weaknesses, win_rate, discount in comp_data:
    competitors.append({
        'id': uid(), 'name': name, 'short_name': name[:4],
        'industry': 'energy', 'strengths': strengths, 'weaknesses': weaknesses,
        'typical_discount': discount, 'win_rate_against_us': win_rate,
        'remark': '', 'created_at': d(2020,1,1),
    })
write_csv('competitor', competitors)

# ── CUSTOMER_BILLING_INFO ────────────────────────────────────────────────────

billing_infos = []
for cust in customers[:10]:
    billing_infos.append({
        'id': uid(), 'customer_id': cust['id'],
        'company_name': cust['name'],
        'tax_no': cust['uscc'],
        'bank_name': random.choice(['工商银行','建设银行','中国银行','农业银行']),
        'bank_account': f'10{random.randint(10000000000000000, 99999999999999999)}',
        'bank_branch': f'{cust["address"][:5]}支行',
        'address': cust['address'],
        'phone': f'010-{random.randint(10000000,99999999)}',
        'is_current': 'yes', 'remark': '', 'created_at': cust['created_at'],
    })
write_csv('customer_billing_info', billing_infos)

# ── TENDER_NOTICE ────────────────────────────────────────────────────────────

tender_notices = []
for i, opp in enumerate(opportunities[:8]):
    tender_notices.append({
        'id': uid(), 'customer_id': opp['customer_id'],
        'title': f'{opp["title"]}招标公告',
        'budget': opp['amount'],
        'publish_date': rdate('2022-06-01','2023-06-01'),
        'deadline': rdate('2023-01-01','2023-08-01'),
        'platform': random.choice(['中国电力招标投标平台','国家电网网上购物平台','政府采购云平台']),
        'notice_no': f'NOTICE2023{i+1:04d}',
        'project_description': f'{opp["title"]}，要求具备相关电力行业资质及成功实施案例',
        'qualification_requirement': '具备信息系统集成商三级及以上资质',
        'status': random.choice(['open','closed','awarded']),
        'remark': '', 'created_at': rdate('2022-06-01','2023-06-01'),
    })
write_csv('tender_notice', tender_notices)

# ── SALES_EXPENSE ────────────────────────────────────────────────────────────

expense_types = ['travel', 'entertainment', 'gift', 'marketing', 'other']
sales_expenses = []
for opp in opportunities[:8]:
    for _ in range(random.randint(2, 4)):
        etype = random.choice(expense_types)
        sales_expenses.append({
            'id': uid(), 'opportunity_id': opp['id'],
            'expense_type': etype,
            'amount': round(random.uniform(0.2, 5.0), 2),
            'expense_date': rdate('2022-01-01','2024-06-01'),
            'description': {
                'travel': '出差拜访客户交通住宿费',
                'entertainment': '客户接待餐饮费',
                'gift': '客户关系维护礼品费',
                'marketing': '行业展会参展费用',
                'other': '其他销售费用',
            }[etype],
            'employee_id': random.choice([emp_ids['zhang_wei'], emp_ids['sun_jing']]),
            'status': random.choice(['approved','paid']),
            'remark': '', 'created_at': rdate('2022-01-01','2024-06-01'),
        })
write_csv('sales_expense', sales_expenses)

# ── SALES_TASK ───────────────────────────────────────────────────────────────

task_titles = [
    '安排技术演示，准备演示环境',
    '提交资质文件清单给客户',
    '跟进合同审批进度',
    '组织内部投标策略会议',
    '拜访客户采购部门负责人',
]
sales_tasks = []
for opp in opportunities[:8]:
    for _ in range(random.randint(1, 3)):
        sales_tasks.append({
            'id': uid(), 'opportunity_id': opp['id'],
            'title': random.choice(task_titles),
            'description': '按照销售计划推进商机',
            'assignee_id': random.choice([emp_ids['zhang_wei'], emp_ids['sun_jing'], emp_ids['lin_kai']]),
            'due_date': rdate('2023-01-01','2024-12-31'),
            'priority': random.choice(['high','medium','low']),
            'status': random.choice(['pending','done','overdue']),
            'remark': '', 'created_at': rdate('2022-01-01','2024-01-01'),
        })
write_csv('sales_task', sales_tasks)

# ── CUSTOMER_DEPARTMENT ──────────────────────────────────────────────────────

cust_departments = []
dept_structures = [
    ('信息化部', None), ('采购部', None), ('技术部', None),
    ('调度中心', None), ('运维部', '技术部'), ('系统室', '信息化部'),
]
for cust in customers[:5]:
    parent_map = {}
    for dname, parent in dept_structures:
        did = uid()
        parent_map[dname] = did
        cust_departments.append({
            'id': did, 'customer_id': cust['id'],
            'name': dname,
            'parent_id': parent_map.get(parent, '') if parent else '',
            'head_name': random.choice(['王总监','李部长','陈经理','张主任']),
            'remark': '', 'created_at': cust['created_at'],
        })
write_csv('customer_department', cust_departments)

# ── RFM_SCORE ────────────────────────────────────────────────────────────────

rfm_scores = []
for cust in customers[:10]:
    r = random.randint(1, 5); f = random.randint(1, 5); m = random.randint(1, 5)
    rfm_scores.append({
        'id': uid(), 'customer_id': cust['id'],
        'calculated_date': d(2024,1,1),
        'last_follow_date': rdate('2023-06-01','2024-01-01'),
        'follow_count': random.randint(5, 30),
        'total_amount': random.randint(200, 5000),
        'r_score': r, 'f_score': f, 'm_score': m,
        'total_score': r + f + m,
        'level': random.choice(['high_value','active','potential']),
        'created_at': d(2024,1,1),
    })
write_csv('rfm_score', rfm_scores)

# ── CUSTOMER_PARTNERSHIP ─────────────────────────────────────────────────────

partnerships = []
for cust in [c for c in customers if c['type'] == 'partner']:
    partnerships.append({
        'id': uid(), 'customer_id': cust['id'],
        'partnership_tier': random.choice(['gold','silver','bronze']),
        'can_accompany_bid': random.choice(['yes','no']),
        'cooperation_scope': '电力自动化系统联合投标',
        'contract_url': '',
        'start_date': rdate('2019-01-01','2022-01-01'),
        'expiry_date': rdate('2025-01-01','2027-01-01'),
        'remark': '', 'created_at': rdate('2019-01-01','2022-01-01'),
    })
write_csv('customer_partnership', partnerships)

# ── PARTNER_QUALIFICATION ────────────────────────────────────────────────────

pq_list = []
for cust in [c for c in customers if c['type'] == 'partner']:
    pq_list.append({
        'id': uid(), 'customer_id': cust['id'],
        'qual_type': 'business',
        'qual_name': '信息系统集成及服务资质（二级）',
        'cert_no': f'ISCCC{random.randint(10000,99999)}',
        'person_count': random.randint(5, 50),
        'issue_date': rdate('2020-01-01','2022-01-01'),
        'expiry_date': rdate('2024-01-01','2026-01-01'),
        'status': 'valid', 'remark': '', 'created_at': rdate('2020-01-01','2022-01-01'),
    })
write_csv('partner_qualification', pq_list)

# ── BID_PLATFORM_ACCOUNT ─────────────────────────────────────────────────────

bp_accounts = []
for cust in customers[:8]:
    bp_accounts.append({
        'id': uid(), 'customer_id': cust['id'],
        'platform_name': random.choice(['中国电力招标投标平台','国家电网电子商务平台','政府采购云平台']),
        'account': f'USER_{cust["short_name"]}_{random.randint(1000,9999)}',
        'owner_type': 'customer',
        'expiry_date': rdate('2025-01-01','2027-01-01'),
        'status': 'active', 'remark': '', 'created_at': cust['created_at'],
    })
write_csv('bid_platform_account', bp_accounts)

# ── CUSTOMER_CHANGE_LOG ──────────────────────────────────────────────────────

change_logs = []
for cust in customers[:5]:
    change_logs.append({
        'id': uid(), 'customer_id': cust['id'],
        'field_name': 'tier',
        'old_value': 'normal', 'new_value': 'key',
        'info_source': '销售拜访确认',
        'recorded_by': '张伟',
        'changed_date': rdate('2022-01-01','2023-12-01'),
        'created_at': rdate('2022-01-01','2023-12-01'),
    })
write_csv('customer_change_log', change_logs)

# ── CONTACT_RELATIONSHIP ─────────────────────────────────────────────────────

cr_list = []
for i in range(0, min(10, len(contact_ids)-1), 2):
    cr_list.append({
        'id': uid(),
        'contact_id': contact_ids[i],
        'related_contact_id': contact_ids[i+1],
        'relation_type': random.choice(['colleague','friend','subordinate']),
        'note': '',
        'created_at': rdate('2021-01-01','2023-01-01'),
    })
write_csv('contact_relationship', cr_list)

print('\n电力行业测试数据生成完成。')
print(f'输出目录: {OUT}')
