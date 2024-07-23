import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 검색창 
character_name = st.text_input("캐릭터 이름을 입력하세요.")

# 입력된 이름이 ani_list에 있는지 확인
if character_name:
    if character_name in ani_list:
        index = ani_list.index(character_name)
        st.image(img_list[index], caption=character_name)
    else:
        st.write("해당 캐릭터를 찾을 수 없습니다.")
# 입력창에서 데이터를 받아서 
# 해당 문자열이 일치하는 이미지를 화면에 출력해 보세요.
