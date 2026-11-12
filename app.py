import streamlit as st

st.set_page_config(
    page_title="와쳐스 WATCHERS",
    page_icon="🦅",
    layout="wide",
)

# 이 앱은 학교 과제용 시연 프로토타입입니다.
# 실제 정부 데이터, 회원가입, 투표 저장 기능은 연결되어 있지 않습니다.

st.markdown("""
<style>
    .stApp { background: #f4f8fc; }
    [data-testid="stSidebar"] { background: #e8f2fc; }
    .main-title { color: #1556a5; font-size: 2.25rem; font-weight: 800; }
    .sub-title { color: #52708f; font-size: 1rem; }
    .policy-card {
        background: white; border: 1px solid #dce8f4; border-radius: 14px;
        padding: 16px 18px; margin-bottom: 12px;
    }
    .tag { color: #1556a5; font-weight: 700; font-size: .85rem; }
    .muted { color: #6c7f91; font-size: .9rem; }
</style>
""", unsafe_allow_html=True)

POLICIES = [
    {
        "name": "청년 대중교통비 지원",
        "agency": "국토교통부",
        "related": "기획재정부, 지방자치단체",
        "budget": "예시 예산 120억 원",
        "deadline": "2026년 12월",
        "progress": 72,
        "company": "해당 없음(예시)",
        "private": "교통카드 운영사(예시)",
        "summary": "청년층의 대중교통비 부담을 줄이기 위한 지원 정책입니다.",
        "status": "진행 중",
        "score": 84,
        "category": "중앙부처",
    },
    {
        "name": "지역 공공도서관 확충",
        "agency": "문화체육관광부",
        "related": "지방자치단체, 교육청",
        "budget": "예시 예산 85억 원",
        "deadline": "2027년 6월",
        "progress": 45,
        "company": "해당 지자체 산하 시설관리공단(예시)",
        "private": "건설·설계 업체(예시)",
        "summary": "지역 주민의 독서·문화 접근성을 높이기 위한 시설 확충 사업입니다.",
        "status": "진행 중",
        "score": 67,
        "category": "지자체",
    },
    {
        "name": "노후 하수관로 정비 사업",
        "agency": "환경부",
        "related": "지방자치단체",
        "budget": "예시 예산 210억 원",
        "deadline": "2026년 10월",
        "progress": 28,
        "company": "지역 공기업(예시)",
        "private": "토목·정비 업체(예시)",
        "summary": "노후 하수관로를 정비해 침수와 누수 위험을 줄이기 위한 사업입니다.",
        "status": "점검 필요",
        "score": 42,
        "category": "중앙부처",
    },
]

def policy_card(p):
    st.markdown(f"""
    <div class="policy-card">
      <div class="tag">{p['category']} · {p['status']}</div>
      <h3 style="margin:6px 0;color:#183b60;">{p['name']}</h3>
      <div class="muted">담당: {p['agency']}　|　진행도: {p['progress']}%</div>
      <p style="margin-bottom:0;">{p['summary']}</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("## 🦅 WATCHERS")
st.sidebar.caption("정책을 살피고, 의견을 나누다")
page = st.sidebar.radio(
    "메뉴",
    ["홈", "중앙부처", "정책광장", "의견광장", "마이페이지"],
)
st.sidebar.divider()
st.sidebar.caption("학교 과제용 시연 앱 · 실제 서비스 아님")

st.markdown('<div class="main-title">🦅 와쳐스 WATCHERS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">국민의 시선으로 정책의 진행 과정을 살펴보는 정책 모니터링 서비스</div>', unsafe_allow_html=True)
st.write("")

if page == "홈":
    st.subheader("정책 한눈에 보기")
    st.info("🦅 와쳐스 안내: 정책 정보를 확인하고, 근거를 바탕으로 건전한 의견을 남겨보세요.")
    c1, c2, c3 = st.columns(3)
    c1.metric("등록 정책", "3개")
    c2.metric("평균 진행도", "48%")
    c3.metric("의견 참여", "128건")
    left, right = st.columns(2)
    with left:
        st.markdown("### 🏆 BEST 정책")
        policy_card(POLICIES[0])
    with right:
        st.markdown("### 🔎 점검이 필요한 정책")
        policy_card(POLICIES[2])
    st.markdown("### 전체 정책")
    for p in POLICIES:
        policy_card(p)

elif page == "중앙부처":
    st.subheader("중앙부처 정책")
    st.write("중앙행정기관이 담당하는 정책의 예시 목록입니다.")
    for p in [x for x in POLICIES if x["category"] == "중앙부처"]:
        policy_card(p)

elif page == "정책광장":
    st.subheader("정책광장")
    selected_name = st.selectbox("확인할 정책을 선택하세요", [p["name"] for p in POLICIES])
    p = next(x for x in POLICIES if x["name"] == selected_name)
    st.markdown(f"## {p['name']}")
    st.write(p["summary"])
    st.progress(p["progress"] / 100, text=f"정책 진행도 {p['progress']}%")
    a, b = st.columns(2)
    with a:
        st.markdown("#### 정책 기본 정보")
        st.write(f"**담당 부서:** {p['agency']}")
        st.write(f"**총책임자:** 담당 기관장(예시)")
        st.write(f"**관련 부서:** {p['related']}")
        st.write(f"**예산:** {p['budget']}")
        st.write(f"**목표 기한:** {p['deadline']}")
    with b:
        st.markdown("#### 참여 기관")
        st.write(f"**국유기업·공기업:** {p['company']}")
        st.write(f"**사유기업:** {p['private']}")
        st.write(f"**현재 상태:** {p['status']}")
    st.warning("표시된 기관·예산·일정·진행도는 화면 구성을 위한 가상 예시이며 실제 자료가 아닙니다.")
    st.markdown("#### 시민 반응 (시연용)")
    x, y = st.columns(2)
    x.metric("긍정 의견", "68%")
    y.metric("개선 의견", "32%")
    st.caption("실제 투표 결과가 아니며, 입력 내용도 저장되지 않습니다.")

elif page == "의견광장":
    st.subheader("의견광장")
    tab1, tab2 = st.tabs(["국민신문고", "의견알리미"])
    with tab1:
        st.markdown("### 📣 국민신문고")
        st.write("정책에 대한 건의나 개선 의견을 정리해 보는 공간입니다.")
        category = st.selectbox("의견 분야", ["정책 제안", "불편 사항", "예산·운영 관련", "기타"])
        title = st.text_input("제목")
        content = st.text_area("의견 내용", height=130, placeholder="확인한 사실과 개선 제안을 구체적으로 작성해 주세요.")
        if st.button("의견 등록 미리보기"):
            if title.strip() and content.strip():
                st.success("시연 미리보기입니다. 실제로 전송되거나 저장되지는 않습니다.")
                st.write(f"**[{category}] {title}**")
                st.write(content)
            else:
                st.error("제목과 의견 내용을 입력해 주세요.")
    with tab2:
        st.markdown("### 🔔 의견알리미")
        st.write("정책 관련 주요 소식과 토론 주제를 확인하는 공간입니다.")
        st.markdown('<div class="policy-card"><b>새 토론 주제</b><br>청년 대중교통비 지원의 신청 절차는 충분히 간편한가요?<p class="muted">예시 알림 · 10분 전</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="policy-card"><b>정책 진행 소식</b><br>지역 공공도서관 확충 사업의 중간 진행 상황이 등록되었습니다.<p class="muted">예시 알림 · 어제</p></div>', unsafe_allow_html=True)
        st.caption("알림은 모두 화면 시연을 위한 가상 내용입니다.")

elif page == "마이페이지":
    st.subheader("마이페이지")
    st.markdown("### 👤 방문자님")
    st.caption("비회원 시연 프로필")
    a, b, c = st.columns(3)
    a.metric("작성 의견", "2")
    b.metric("정책 공감", "5")
    c.metric("관심 정책", "3")
    st.markdown("### 활동 내역")
    st.markdown("""
    - 청년 대중교통비 지원 — 관심 정책으로 표시 (예시)
    - 지역 공공도서관 확충 — 개선 의견 작성 (예시)
    - 노후 하수관로 정비 사업 — 정책 확인 (예시)
    """)
    st.info("실제 회원가입, 개인 정보, 활동 기록 저장 기능은 구현되어 있지 않습니다.")

st.divider()
st.caption("ⓘ 본 화면은 학교 과제용 프로토타입입니다. 정책명과 수치, 기관 정보, 의견 및 통계는 모두 설명을 위한 가상 데이터입니다. 실제 정부 기관의 공식 서비스가 아닙니다.")
