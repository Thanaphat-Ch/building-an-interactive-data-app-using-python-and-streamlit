import pandas as pd
import streamlit as st
import plotly.express as px

with st.sidebar:
    df = pd.read_csv("../datasets/1642645053.csv", encoding="tis-620")
    provinces = df["สถานที่เลี้ยงสัตว์ จังหวัด"].unique()
    # st.write(provinces)
    option = st.selectbox(
        "Which province?",
        provinces
    )

st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")

st.write(df[ df["สถานที่เลี้ยงสัตว์ จังหวัด"] == option])

provinces_df = pd.read_csv("https://raw.githubusercontent.com/dataengineercafe/thailand-province-latitude-longitude/refs/heads/main/provinces.csv")
joined = pd.merge(df, provinces_df, how="left", left_on="สถานที่เลี้ยงสัตว์ จังหวัด", right_on="province_name")

selected_df = joined[["สถานที่เลี้ยงสัตว์ จังหวัด", "province_lat", "province_lon", "โคเนื้อ พื้นเมือง เพศผู้ (ตัว)"]]
cleaned = selected_df.dropna()
cleaned["โคเนื้อ พื้นเมือง เพศผู้ (ตัว)"] = cleaned[cleaned["โคเนื้อ พื้นเมือง เพศผู้ (ตัว)"] != "1,480"]["โคเนื้อ พื้นเมือง เพศผู้ (ตัว)"].astype(int)

grouped_df = cleaned.groupby("สถานที่เลี้ยงสัตว์ จังหวัด")["โคเนื้อ พื้นเมือง เพศผู้ (ตัว)"].sum().reset_index()
joined_df = pd.merge(grouped_df, provinces_df, how="left", left_on="สถานที่เลี้ยงสัตว์ จังหวัด", right_on="province_name")
st.write(joined_df)

joined_df = joined_df.rename(columns={"โคเนื้อ พื้นเมือง เพศผู้ (ตัว)": "amount"})

st.map(joined_df, latitude="province_lat", longitude="province_lon", size="amount")











df = pd.read_csv("../datasets/1642645053.csv", encoding="tis-620")
df_grouped_by_species = df.groupby("สถานที่เลี้ยงสัตว์ จังหวัด")["รวมเกษตรกรผู้เลี้ยงสัตว์/ปลูกพืชอาหารสัตว์ (ราย)"].mean()
st.bar_chart(df_grouped_by_species)




# df = pd.read_csv("../datasets/panguin.csv", encoding="tis-620")
# st.write(df)

# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/car_crashes.csv"
# df = pd.read_csv(url)
# st.write(df)

# merged_df = pd.merge(df, df2, on='id', how='inner')
# st.write("Merged DataFrame (INNER JOIN):")
# st.write(merged_df)

df = pd.DataFrame(
    {
        "col1": [13.8175043],
        "col2": [100.514935],
        "col3": [13],
        "col4": ["#ffaa00"],
    }
)
st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")

# url = "https://raw.githubusercontent.com/dataengineercafe/thailand-province-latitude-longitude/refs/heads/main/provinces.csv"
# df = pd.read_csv(url)


# selected_lat = df[df["province_name"] == selected_province]["province_lat"].values[0]
# selected_lon = df[df["province_name"] == selected_province]["province_lon"].values[0]
# st.write(f"ละติจูด: {selected_lat}, ลองจิจูด: {selected_lon}")

# provinces = df["province_name"].unique()
# option = st.selectbox(
#     "Which province?",
#     provinces
# )
# st.write(df[ df["สถานที่เลี้ยงสัตว์ จังหวัด"] == option])

# map_df = pd.DataFrame({
#     "col1": [selected_lat],
#     "col2": [selected_lon],
#     "col3": [10],  # ขนาดของจุด
#     "col4": ["#ffaa00"]  # สีของจุด
# })
# st.map(map_df, latitude="col1", longitude="col2", size="col3", color="col4")