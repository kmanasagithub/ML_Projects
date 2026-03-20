import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

# ---------- Page Config ----------
st.set_page_config(
    page_title="WhatsApp Analyzer",
    page_icon="💬",
    layout="wide"
)

st.markdown("<h1 style='text-align:center;'>💬 WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------- Sidebar ----------
st.sidebar.header("📂 Upload Chat File")
uploaded_file = st.sidebar.file_uploader("Choose WhatsApp exported file")

if uploaded_file is not None:

    data = uploaded_file.getvalue().decode("utf-8")
    df = preprocessor.preprocess(data)

    # User selection
    user_list = df["user"].unique().tolist()
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Analysis Scope", user_list)

    if st.sidebar.button("🚀 Analyze Chat"):

        # ================= Top Stats =================
        num_messages, words, num_media, num_links = helper.fetch_stats(selected_user, df)

        st.subheader("📊 Chat Statistics")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("💬 Messages", num_messages)
        c2.metric("📝 Words", words)
        c3.metric("🖼️ Media", num_media)
        c4.metric("🔗 Links", num_links)

        st.divider()

        # ================= Timeline =================
        st.subheader("📅 Message Timeline")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Monthly Trend**")
            timeline = helper.monthly_timeline(selected_user, df)
            fig, ax = plt.subplots(figsize=(6,4))
            ax.plot(timeline["time"], timeline["message"], color="#2ecc71", linewidth=2)
            plt.xticks(rotation=60)
            st.pyplot(fig)

        with col2:
            st.markdown("**Daily Trend**")
            daily = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots(figsize=(6,4))
            ax.plot(daily["only_date"], daily["message"], color="#34495e")
            plt.xticks(rotation=60)
            st.pyplot(fig)

        st.divider()

        # ================= Activity Map =================
        st.subheader("🗓️ Activity Insights")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Most Active Day**")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(5,4))
            ax.bar(busy_day.index, busy_day.values, color="#3498db")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:
            st.markdown("**Most Active Month**")
            busy_month = helper.monthly_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(5,4))
            ax.bar(busy_month.index, busy_month.values, color="#e67e22")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        st.divider()

        # ================= Most Busy Users =================
        if selected_user == "Overall":
            st.subheader("🏆 Most Active Users")

            x, percent_df = helper.most_busy_users(df)
            col1, col2 = st.columns([2,1])

            with col1:
                fig, ax = plt.subplots(figsize=(6,4))
                ax.bar(x.index, x.values, color="#e74c3c")
                plt.xticks(rotation=45)
                st.pyplot(fig)

            with col2:
                st.dataframe(percent_df, hide_index=True, use_container_width=True)

            st.divider()

        # ================= WordCloud =================
        st.subheader("☁️ Frequent Words")

        wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots(figsize=(8,4))
        ax.imshow(wc)
        ax.axis("off")
        st.pyplot(fig)

        st.divider()

        # ================= Common Words =================
        st.subheader("📝 Most Common Words")

        common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(common_df[0], common_df[1], color="#9b59b6")
        plt.xticks(rotation=60)
        st.pyplot(fig)

        st.divider()

        # ================= Emoji Analysis =================
        st.subheader("😄 Emoji Usage")

        emoji_df = helper.emoji_helper(selected_user, df)

        col1, col2 = st.columns(2,gap="medium")

        with col1:
            st.markdown("**Top Emojis**")
            st.dataframe(
                emoji_df.head(5),
                hide_index=True,
                use_container_width=True
            )

        with col2:
            st.markdown("**Emoji Share**")
            fig, ax = plt.subplots(figsize=(3,3))
            top = emoji_df.head(5)
            ax.pie(top["COUNT"], labels=top["EMOJI"], autopct="%.1f%%", startangle=140,textprops={"fontsize":10})
            ax.axis("equal")
            st.pyplot(fig)
