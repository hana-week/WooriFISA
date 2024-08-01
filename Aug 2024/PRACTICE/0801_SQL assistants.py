import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine, text
import mysql.connector
import openai
from dotenv import load_dotenv
import os
from openai import OpenAI
import re

load_dotenv()  # .env 파일을 읽어서 환경변수로 설정
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWD = os.getenv("PASSWD")
PORT = os.getenv("PORT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

pymysql.install_as_MySQLdb()  # 파이썬 전용 데이터베이스 커넥터
engine = create_engine(f'mysql+pymysql://{USER}:{PASSWD}@{HOST}/wsid_second')  # 데이터베이스 연결 엔진
openai.api_key = OPENAI_API_KEY  # OpenAI API 키 설정   


def table_definition_prompt(dataframe: pd.DataFrame):
    
    prompt = """Given the following MySQL Query definition,
                write queries based on the request
                \n### MySQL Query, with its properties:
                
                #
                # df의 컬럼명({})
                #
                """.format(
        ",".join(str(x) for x in dataframe.columns)
    )

    return prompt
# 테이블 목록을 가져오는 쿼리
def get_tables(db_name: str) -> list:
   
    with engine.connect() as connection:
        connection.execute(text(f"USE {db_name}"))
        result = connection.execute(text("SHOW TABLES"))
        return [row[0] for row in result]

def main():

    st.title('여행지 숙소 검색기')

    #user_input = st.text_input('여행가는 지역, 원하는 부대시설을 자유롭게 입력해주세요')
    #user_input = "제주로 놀러가고 가격은 한 20만원 정도 보고있고, 피트니스센터랑 야외수영장이 있으면 좋겠어"
    user_input = st.text_input('여행가는 지역과 원하는 부대시설을 자유롭게 입력해주세요')
    sort_ = ' Just pick the top 3'
    
    if user_input:
        
        client = OpenAI()
        st.balloons()
        sql = f"SELECT * FROM wsid_second.wsid"
        df = pd.read_sql(sql, con = engine)
        db = 'wsid_second'
        table = get_tables(db) # -> pandas dataframe, 테이블을 Gpt한테 넘겨줌
        
        #유저가 입력받는 값 변수명 = user_input
        FULL_PROMPT = str(table_definition_prompt(df)) + str(user_input) + sort_

        #gpt한테 물어보고 응답받기
        RESPONSE = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {
                                    "role": "system",
                                    "content": f"You are an assistant that generates MySQL query \
                                        based on the given df definition and a natural language request.\
                                        The answer should contain only code, not any explanation or ``` for copy.\
                                        And you have to add the result of the answer query.\
                                        When you give a query statement, make sure to use the column name on the table.\
                                        The name of database is {db} and the name of table is {table}.\
                                        Statement 'FROM' must include {db}.{table}",
                                },
                                {
                                    "role": "user",
                                    "content": f"A query to answer: {FULL_PROMPT}",
                                },
                                
                                {
                                    "role": "assistant",
                                    "content": "Based on the provided table definition and the user's request,\
                                    I will generate a MySQL query to retrieve the required data. \
                                    If the region name has three characters,\
                                    only the first two characters will be used.\
                                    The query will not include square brackets or single quotes around the table name.\
                                    Additionally, use only the column names provided in the table definition and do not alter them in any way.",
                                },
                            ],
                            max_tokens=200,
                            temperature=1.0,
                            stop=None,
                        )
        
        answer = RESPONSE.choices[0].message.content
        answer = re.sub(r"[^\w\s,.*=']", '', answer)
        
        answer_df = pd.read_sql(answer, con = engine)
        #print(FULL_PROMPT)
        st.code(answer)
        st.write(answer_df)
        
        st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        justify-content: flex-end;
        margin: 20px;
    }
    .image-container img {
        width: 150px;  /* 원하는 너비로 조정 */
        height: auto;
    }
    </style>
    <div class="image-container">
        <img src="https://i.imgur.com/2LvOspG.gif" alt="My Image">
    </div>
    """,
    unsafe_allow_html=True
    )
        
if __name__ == "__main__":
    main()
