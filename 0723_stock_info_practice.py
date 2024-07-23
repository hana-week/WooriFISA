import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import plotly.graph_objects as go
from io import BytesIO

# 한글 지원을 위한 설정
st.set_page_config(page_title="주식 데이터 분석", layout="wide")

# 캐시된 함수로 KRX 주식 정보 가져오기
@st.cache_data
def get_stock_info():
    base_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    url = f"{base_url}?method={method}"
    df = pd.read_html(url, header=0)[0]
    df['종목코드'] = df['종목코드'].apply(lambda x: f"{x:06d}")
    df = df[['회사명', '종목코드']]
    return df

def get_ticker_symbol(company_name):
    df = get_stock_info()
    code = df[df['회사명'] == company_name]['종목코드'].values
    ticker_symbol = code[0]
    return ticker_symbol

# 앱 제목 및 설명
st.title("주식 데이터 분석 애플리케이션")

# 주식 종목 이름 입력
stock_name = st.text_input("주식 종목 이름을 입력하세요:", value='삼성전자')

# 날짜 범위 선택
date_range = st.date_input("날짜 범위를 선택하세요:", [datetime.date(2020, 1, 1), datetime.date.today()])

if stock_name and date_range:
    ticker_symbol = get_ticker_symbol(stock_name)
    start_p = date_range[0]
    end_p = date_range[1] + datetime.timedelta(days=1)
    
    df = fdr.DataReader(f'KRX:{ticker_symbol}', start_p, end_p)
    df.index = df.index.date
    
    st.subheader(f"[{stock_name}] 주가 데이터")
    st.dataframe(df.tail(7))
    
    # 종가 그래프
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='종가'))
    fig.update_layout(title=f"{stock_name} 종가 그래프", xaxis_title='날짜', yaxis_title='종가')
    st.plotly_chart(fig)

    # 엑셀 파일로 다운로드
    excel_data = BytesIO()
    df.to_excel(excel_data)
    excel_data.seek(0)
    
    st.download_button("엑셀 파일 다운로드", excel_data, file_name='stock_data.xlsx', mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
