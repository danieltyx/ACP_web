#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:07:12 2021

@author: andreases
"""

import streamlit as st;
import pandas as pd
import numpy as np
from PIL import Image

title_image = Image.open("./titlepage.jpg")
st.image(title_image)
st.title('ACP Recommendation')
st.write("  ")
st.write("  ")

st.write("#1. 您是否了解什么是临终关怀？")
quest1 = st.selectbox("选择1",("是","否"))
if (quest1=="否"):
    st.write("什么是临终关怀：当你的至亲患有重疾时，病情如果持续恶化，临终关怀（palliative care) 不失为一种相较于医院治疗更好的选择。它是为末期病患者减轻痛苦，提高他们在生命最后一段时间中生活质量的人性化服务。临终关怀并不勉强抢救病人的生命，而是将死亡视作一个自然的过程，在关怀的过程中关注病人的心理与精神，尊重病人的价值观和需求，帮助他们安乐地活着，让他们在余下的日子里过得舒适、过得有尊严。")

    st.write("#2. 您是否有意向接受临终关怀？（请谨慎考虑）")
quest2 = st.selectbox("选择2",("是","否"))
st.write("  ")

if (quest2 == "否"):
    st.write("谢谢您的支持")
    st.stop()
else:
    with st.form(key='my_form'):
        st.write("请输入您的相关信息")
        patient_gender = st.selectbox("选择您的生理性别",("男","女"))
        patient_age = st.number_input("输入您的年龄",min_value=30,max_value=110,step=1)
        patient_job = st.selectbox('选择您目前工作领域',["农业、林业、畜牧业、渔业","建设类",
        "文化、体育、娱乐","教育","金融中介","卫生、社会保障和社会福利 ","酒店及餐饮服务",
         "信息传输、计算机服务和软件","租赁和商业服务","水利环境管理","制造业","矿业",
         "电力、煤气和水的生产和分配","公共管理和社会组织","房地产","科学研究、技术服务和地质勘查",
         "家庭服务和其他服务","交通、运输、仓储、邮政","批发零售业","退休","自由职业",'学生','其他'])
        patient_cost = st.number_input("请输入您目前每月支出的医疗费用")
        patient_disease = st.selectbox("请选择您被诊断出的疾病种类",["左肺小细胞癌（局限期）3周期化疗后","肺癌","肺恶性肿瘤","右肺非小细胞癌","肺部感染","右肺上叶占位","肺占位性病变","右肺小细胞癌（广泛期）化疗后","左肺小细胞癌（广泛期）三周期化疗后","非小细胞肺癌伴全身多处及骨骼转移","右肺非小细胞肺癌伴肾上腺、骨骼转移","左肺非小细胞癌肝、骨转移化疗后","右肺上叶小细胞肺癌伴纵膈","右肺门淋巴结","左肺小细胞肺癌广泛期","右肺小细胞肺癌四周期化疗后放疗后"])
        patient_family = st.selectbox("您家庭中子女的数量",[1,2,3,4,5,'5+'])
        patient_marriage = st.selectbox("您的婚姻状况",['已婚','未婚','离丧'])
        st.write("  ")
        patient_pain = st.select_slider('根据您当前身体与心理的不适程度，输入一个0-10的数值，0为舒适，10为非常痛苦。',options=[0,1,2,3,4,5,6,7,8,9,10])
        submit_button = st.form_submit_button(label='确认')
    if st.button('下一步'):
                        
                
# ——————————————————————————————————————————————
#把网页的选择转换成可以process的数据
        
        class patients_out2in:
        
            gender = '女'
            gender_in = 0
            marriage = '已婚'
            marriage_in = 0
            job = '建设类'
            job_in = 0
          
            def __init__(self,gender,job,marriage):
                #gender input
                if (gender =='女'):
                    gender_in = 0
                else:
                    gender_in = 1
        
                #marriage input
                if (marriage=='未婚'):
                    marriage_in = 0
                elif(marriage=='已婚'):
                    marriage_in=1
                else:
                    marriage_in=2
        
                #job input
                if (job == '建设类','制造业','矿业','电力、煤气和水的生产和分配','交通、运输、仓储、邮政'):
                    job_in =0
                elif(job == '农业、林业、畜牧业、渔业'):
                    job_in = 1
                elif(job == '退休'):
                    job_in=2
                elif(job == '学生' ):
                    job_in=3
                elif(job =='文化、体育、娱乐','教育','金融中介','卫生、社会保障和社会福利','租赁和商业服务','家庭服务和其他服务'):
                    job_in=4
                elif(job =='批发零售业','公共管理和社会组织','房地产'):
                    job_in=5
                elif(job=='信息传输、计算机服务和软件','水利环境管理','科学研究、技术服务和地质勘查'):
                    job_in=6
                elif(job=='自由职业'):
                    job_in=7
                else:
                    job_in=9
            
        
            def get_gender(self):
                return self.gender_in
        
            def get_marriage(self):
                return self.marriage_in
                
            def get_job(self):
                return self.job_in
        
        # ——————————————————————————————————————————————
        #K算法
        
        # ——————————————————————————————————————————————
        #从K算法那里提取数据
        
        class patients_in2out:
          gender = 0
          gender_out = "女"
          marriage = 0
          marriage_out ="未婚"
          job = 0
          job_out = "Testing"
          def __init__(self,gender,marriage,job):
            if gender == 0:
              gender_out = "女"
            else:
              gender_out = "男"
        
            if marriage == 0:
              marriage_out = "未婚"
            elif marriage == 1:
              marriage_out = "已婚"
            elif marriage == 2:
              marriage_out =="离异"
            
          def get_job(self):
            return self.job_out
            
          def get_marriage(self):
            return self.marriage_out
        
          def get_gender(self):
           return self.gender_out
            
        
        sample_patients = []
        sample_patients.append(patients_in2out(0,0,324))
                
# ——————————————————————————————————————————————
#获取数据之后呈现K个Sample供选择
#if submit_button = True:    这里需要做一个点了submit之后就弹出下面被生成之后的form
        
        st.write("请选择你是否满意对基于以下患者的情况，若比较满意，请选择“是”，若不满意，请选择“否”")
        
            
        with st.form(key='my_form1'):
            for i in range(len(sample_patients)):
                 st.write("性别：",sample_patients[i].get_gender())
                 #st.write("工作：",P1.job)
                 st.write("婚姻情况:",sample_patients[i].get_marriage())
                 st.write("工作:",sample_patients[i].get_job())
                 result = st.selectbox("请选择您对这位患者Profile的感觉",["满意","不满意"])
            submit_button2 = st.form_submit_button(label='确认')
            
            
# ——————————————————————————————————————————————
#把选择“是”，“否”之后的output转换成新算法的input

# ——————————————————————————————————————————————
#把新算法的output转换成finalgraph和选择推荐

st.header("Your Personalized Results")

col1, col2, col3, col4, col5 = st.beta_columns(5)

with col1:
    st.subheader("ACP")
    st.image("./22.jpg")
    
with col2:
    st.subheader("ACP2")
    st.image("./21.jpg")
    
with col3:
    st.subheader("Middle")
    st.image("./15.jpg")
    
with col4:
    st.subheader("Hospital Care")
    st.image("./18.jpg")
    
with col5:
    st.subheader("Hospital Care")
    st.image("./17.jpg")
    






    
