import random
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱", layout="centered")

# 2. 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애를 해결해 드립니다! 아래 버튼을 눌러 오늘의 메뉴를 확인해 보세요.")

# 3. 메뉴 리스트 (카테고리별 구성)
menu_dict = {
    "한식": [
        "김치찌개",
        "된장찌개",
        "제육볶음",
        "비빔밥",
        "순대국밥",
        "칼국수",
        "불고기백반",
    ],
    "중식": ["짜장면", "짬뽕", "탕수육 세트", "마라탕", "볶음밥"],
    "일식": ["돈가스", "초밥", "라멘", "우동", "규동(소고기덮밥)"],
    "양식": ["파스타", "햄버거", "피자", "리조또", "샌드위치"],
    "분식/기타": ["떡볶이 & 튀김", "김밥 & 라면", "쌀국수", "타코", "샐러드"],
}

# 4. 카테고리 선택 옵션
category = st.selectbox(
    "원하는 음식 종류를 선택하세요 (전체 선택 가능):",
    ["전체"] + list(menu_dict.keys()),
)

# 5. 버튼 클릭 시 랜덤 추천 실행
if st.button("🎲 메뉴 추천받기!", type="primary", use_container_width=True):
  if category == "전체":
    # 모든 카테고리의 메뉴를 하나로 합침
    all_menus = [menu for menus in menu_dict.values() for menu in menus]
    selected_menu = random.choice(all_menus)
  else:
    # 선택한 카테고리의 메뉴 중에서 선택
    selected_menu = random.choice(menu_dict[category])

  # 결과 출력 및 축하 효과
  st.balloons()
  st.success(f"오늘의 추천 점심 메뉴는 **'{selected_menu}'** 입니다! 맛있게 드세요! 😋")
